import zipfile
import xml.etree.ElementTree as ET
import os
import re
from openpyxl import load_workbook


def extract_mvr(mvr_path, extract_to="mvr_extracted"):
    """decompress MVR"""
    mvr_dir_path = os.path.dirname(mvr_path)
    mvr_name, mvr_ext = os.path.splitext(os.path.basename(mvr_path))
    extract_to = mvr_dir_path + "/" + mvr_name + "_" + extract_to
    with zipfile.ZipFile(mvr_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"MVR decompressed to : {extract_to}")
    return extract_to


def parse_mvr_projectors(xml_path):
    """read GeneralSceneDescription.xml and get infos"""
    tree = ET.parse(xml_path)
    root = tree.getroot()

    projectors = []

    for fixture in root.findall(".//Fixture"):
        fixture_id = fixture.find("FixtureID").text
        matrix_text = fixture.find("Matrix").text

        matrix_values = re.findall(r"{(.*?)}", matrix_text)

        # position
        translation = list(map(float, matrix_values[-1].split(",")))

        # rotation matrix
        rotation_matrix = [list(map(float, m.split(","))) for m in matrix_values[:-1]]

        projectors.append(
            {
                "id": fixture_id,
                "position": {
                    "x": translation[0] / 1000,
                    "y": translation[1] / 1000,
                    "z": translation[2] / 1000,
                },
                "rotation_matrix": rotation_matrix,
            }
        )

    return projectors


def append_to_excel(projector_data, excel_path):

    try:
        wb = load_workbook(excel_path)

        if "Spotlights" not in wb.sheetnames:
            raise ValueError("Error: Table Spotlights is not exist!")

        ws = wb["Spotlights"]

        # find start row
        start_row = 3  #

        # find last non null row
        max_row = ws.max_row
        while max_row > 0 and all(cell.value is None for cell in ws[max_row]):
            max_row -= 1
        insert_row = max_row + 1 if max_row >= start_row else start_row

        column_order = [
            "ID",
            "Theoretical Position(m):x",
            "Theoretical Position(m):y",
            "Theoretical Position(m):z",
            "Axis(pan0,tilt90)",
            "Rotation",
            "Orientation pan",
        ]

        for idx, projector in enumerate(projector_data, start=1):
            row_data = [
                projector["id"],
                projector["position"]["x"],
                projector["position"]["y"],
                projector["position"]["z"],
                "x",  # default axis
                str(projector["rotation_matrix"]),
                0,  # default rotation
            ]

            # write
            for col_idx, value in enumerate(row_data, start=1):
                ws.cell(row=insert_row, column=col_idx, value=value)

            insert_row += 1

        # save
        wb.save(excel_path)
        print(f"Successful add {len(projector_data)} data to{excel_path}")

    except Exception as e:
        print(f"Error: {str(e)}")
        if "wb" in locals():
            wb.close()


def add_mvr_data(mvr_file_path, excel_path):

    output_folder = extract_mvr(mvr_file_path)

    # read GeneralSceneDescription.xml
    xml_file_path = os.path.join(output_folder, "GeneralSceneDescription.xml")
    projector_data = parse_mvr_projectors(xml_file_path)

    # output spotlights' infos
    for projector in projector_data:
        print(f"spotlight ID: {projector['id']}")
        print(
            f"position: x={projector['position']['x']}, y={projector['position']['y']}, z={projector['position']['z']}"
        )
        print(f"rotation_matrix: {projector['rotation_matrix']}\n")

    # write into Excel
    append_to_excel(projector_data, excel_path)


if __name__ == "__main__":
    mvr_file_path = "Modif_fichier_preset/Re PresetCorrection- Dénomination programme/TiltInvert.mvr"  # 你的 MVR 文件路径
    output_folder = extract_mvr(mvr_file_path)

    xml_file_path = os.path.join(output_folder, "GeneralSceneDescription.xml")
    projector_data = parse_mvr_projectors(xml_file_path)

    for projector in projector_data:
        print(f"spotlight ID: {projector['id']}")
        print(
            f"position: x={projector['position']['x']}, y={projector['position']['y']}, z={projector['position']['z']}"
        )
        print(f"rotation_matrix: {projector['rotation_matrix']}\n")

    append_to_excel(projector_data, "config-3.0.0-auto.xlsx")
