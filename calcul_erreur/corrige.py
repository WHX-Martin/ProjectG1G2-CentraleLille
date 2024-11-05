from change_angle import change_angle
from resolution_moindre_carre_ProjetG1G2 import fonction_finale

import pandas as pd
import numpy as np
import os
import openpyxl


def tilt_theo_to_real(tilt):
    tilt_real = 0.8277 * tilt + 2.8336
    return tilt_real


def tilt_real_to_theo(tilt):
    tilt_theo = 1.2082 * tilt - 3.4236
    return tilt_theo


def corrigePreset(
    file_path, file_path_change, positions_bouteilles, position_theorique_projecteur
):
    # load excel
    # file_path = 'Modif_fichier_preset/test4.xlsx'

    # read all sheetnames
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names

    # load each sheet
    sheets_data = {
        sheet: pd.read_excel(file_path, sheet_name=sheet) for sheet in sheet_names
    }

    # get all IDs
    # we assume that all tables have the same IDs
    id_list = sheets_data[sheet_names[0]]["ID"].tolist()

    # fonction to get Pan and Tilt
    def get_pan_tilt_for_id(id, sheet_data):
        row = sheet_data[sheet_data["ID"] == id]
        pan = row["Pan"].values[0]
        tilt = row["Tilt"].values[0]
        # corrige of tilt theoretic to tilt real
        tilt = tilt_theo_to_real(tilt)
        return [pan, tilt]

    # get all Pans and Tilts
    result = {}
    for id in id_list:
        result[id] = []
        for sheet in sheet_names:
            result[id].append(get_pan_tilt_for_id(id, sheets_data[sheet]))

    error_results = {}
    error_radians = {}
    for id, values in result.items():
        print(f"ID: {id}, Pan/Tilt values: {values}")
        error_results[id] = fonction_finale(
            values, positions_bouteilles, position_theorique_projecteur
        )
        # print("error_results: ",error_results[id])
        print(error_results[id][0])
        print(f"error-{id} alpha:", error_results[id][0][3])
        print(f"error-{id} beta:", error_results[id][0][4])
        print(f"error-{id} alpha-angle:", np.degrees(error_results[id][0][3]))
        print(f"error-{id} beta-angle:", np.degrees(error_results[id][0][4]))
        error_radians[id] = [error_results[id][0][3], error_results[id][0][4]]

    print("error_radians:", error_radians)

    # change preset data
    # load excel (which contains the preset data that we want to change)
    # file_path_change = 'Modif_fichier_preset/test5.xlsx'

    xls = pd.ExcelFile(file_path_change)
    sheet_names = xls.sheet_names

    sheets_data = {
        sheet: pd.read_excel(file_path_change, sheet_name=sheet)
        for sheet in sheet_names
    }

    id_list = sheets_data[sheet_names[0]]["ID"].tolist()

    result_change = {}
    for id in id_list:
        result_change[id] = []
        for sheet in sheet_names:
            result_change[id].append(get_pan_tilt_for_id(id, sheets_data[sheet]))

    print("result_change:", result_change)
    deta_corrige = {}
    for id, values in error_radians.items():
        id_change = []
        values1 = result_change[id]
        for angles in values1:
            # corrige tilt real to tilt theoretic
            angle_theo = change_angle(values[0], values[1], angles[0], angles[1])
            angle_theo[1] = tilt_real_to_theo(angle_theo[1])
            id_change.append(angle_theo)
        deta_corrige[id] = id_change

    print("deta_corrige: ", deta_corrige)

    # add deta_Pan and deta_Tilt to the Pans/Tilts theoretic
    angle_final = {}
    for key in result_change:
        if key in deta_corrige:
            angle_final[key] = []
            for i in range(len(result_change[key])):
                combined_list = [
                    round(result_change[key][i][j] + deta_corrige[key][i][j], 2)
                    for j in range(len(result_change[key][i]))
                ]
                angle_final[key].append(combined_list)

    print("angle_final：", angle_final)

    # create a new excel
    original_file = file_path_change

    # get filename
    base_name = os.path.basename(original_file)  # 'test5.xlsx'
    name, extension = os.path.splitext(base_name)  # 'test5', '.xlsx'

    # new excel name
    new_file_name = f"{name}_change{extension}"  # 'test5_change.xlsx'
    new_file_path = os.path.join(os.path.dirname(original_file), new_file_name)

    # write the new excel
    wb = openpyxl.load_workbook(file_path_change)

    for sheet_index, sheet_name in enumerate(wb.sheetnames):
        ws = wb[sheet_name]

        for row in ws.iter_rows(min_row=2):
            id_value = int(row[0].value)
            if id_value in angle_final:
                row[1].value = angle_final[id_value][sheet_index][0]  # Pan
                row[2].value = angle_final[id_value][sheet_index][1]  # Tilt

    wb.save(new_file_path)

    print(f"Succeed in creating the new excel: {new_file_path}")


if __name__ == "__main__":
    positions_bouteilles = [
        [1,6.29,-1.7],[3.42,4.5,-1.3],[3.42,1,-1.2]
    ]  # postion x_B1,y_B1,z_B1 de la première bouteille, puis de la deuxième etc...
    position_theorique_projecteur = [
        0,0,-0.29
    ]  # postion théorique du projecteur dans l'espace
    file_path = "Modif_fichier_preset/test4.xlsx"
    file_path_change = "Modif_fichier_preset/test5.xlsx"
    corrigePreset(
        file_path, file_path_change, positions_bouteilles, position_theorique_projecteur
    )
