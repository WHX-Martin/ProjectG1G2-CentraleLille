import sys, os, ast


from calcul_erreur.change_angle import change_angle, rotation_matrix

# from resolution_moindre_carre_ProjetG1G2 import fonction_finale

# from calcul_erreur.resolution_moindre_carre_ProjetG1G2_4_bouteille import (
#     fonction_finale4B,
# )
# from calcul_erreur.resolution_moindre_carre_ProjetG1G2_5_bouteille import (
#     fonction_finale5B,
# )
from calcul_erreur.resolution import fonction_finale

sys.path.append(os.getcwd())
from Modif_fichier_preset.readConfig import readConfig

import pandas as pd
import numpy as np
import openpyxl


def tilt_theo_to_real(a, b, c, d, tilt_theo):
    # tilt_real = 0.8277 * tilt + 2.8336
    # tilt_real = 0.857 * tilt
    if tilt_theo >= 0:
        tilt_real = a * tilt_theo + b
    else:
        tilt_real = c * tilt_theo + d
    return tilt_real


def tilt_real_to_theo(a, b, c, d, tilt_real):
    # tilt_theo = 1.2082 * tilt - 3.4236
    # tilt_theo = (1 / 0.857) * tilt
    if tilt_real >= b:
        tilt_theo = 1 / a * tilt_real - b / a
    else:
        tilt_theo = 1 / c * tilt_real - d / c
    return tilt_theo


def rotation_init(axis, rotation_theo):
    angle_z = 0
    if axis == "x":
        angle_z = 0
    elif axis == "y":
        angle_z = 90
    elif axis == "-x":
        angle_z = 180
    elif axis == "-y":
        angle_z == -90
    else:
        print(
            f"Error: fault definition on spotlights' axis! \nChoice:(x/y/-x/-y)\nDefined:{axis}"
        )
        return
    Rz = rotation_matrix([0, 0, 1], np.radians(angle_z))

    # change str to list
    nested_list = ast.literal_eval(rotation_theo)

    R_theo = np.array(nested_list)
    # print(Rz @ R_theo)
    return Rz @ R_theo


def corrigePreset(
    file_path,
    file_path_change,
    positions_bouteilles,
    position_theorique_projecteur,
    a,
    b,
    c,
    d,
    num_capteur,
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
        tilt = tilt_theo_to_real(a, b, c, d, tilt)
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
        # if num_capteur == 4:
        #     error_results[id] = fonction_finale4B(
        #         values, positions_bouteilles, position_theorique_projecteur[id]
        #     )
        # elif num_capteur == 5:
        #     error_results[id] = fonction_finale5B(
        #         values, positions_bouteilles, position_theorique_projecteur[id]
        #     )
        if position_theorique_projecteur[id][5] == 1:
            # if orientation is clockwise, invert the sign of pan
            for value in values:
                value[0] = -value[0]
        rotation_matrix_theo = rotation_init(
            position_theorique_projecteur[id][3], position_theorique_projecteur[id][4]
        )
        # print(f"inv R:{np.linalg.inv(rotation_matrix_theo)}")
        error_results[id] = fonction_finale(
            values,
            positions_bouteilles,
            position_theorique_projecteur[id][0:3],
            rotation_matrix_theo,
        )
        # print("error_results: ",error_results[id])
        print(f"Error calculated: {error_results[id][0]}")
        print(f"error-{id} alpha:", error_results[id][0][3])
        print(f"error-{id} beta:", error_results[id][0][4])
        print(f"error-{id} gamma:", error_results[id][0][5])
        print(f"error-{id} alpha-angle:", np.degrees(error_results[id][0][3]))
        print(f"error-{id} beta-angle:", np.degrees(error_results[id][0][4]))
        print(f"error-{id} gamma-angle:", np.degrees(error_results[id][0][5]))
        error_radians[id] = [
            error_results[id][0][3],
            error_results[id][0][4],
            error_results[id][0][5],
        ]

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

    data_to_change = {}
    for id in id_list:
        data_to_change[id] = []
        for sheet in sheet_names:
            data_to_change[id].append(get_pan_tilt_for_id(id, sheets_data[sheet]))

    print("data_to_change:", data_to_change)
    deta_corrige = {}
    for id, values in error_radians.items():
        id_change = []
        values1 = data_to_change[id]
        for angles in values1:
            # corrige tilt real to tilt theoretic
            angle_theo = change_angle(
                values[0],
                values[1],
                values[2],
                angles[0],
                angles[1],
                int(position_theorique_projecteur[id][5]),
            )
            # angle_theo[1] = tilt_real_to_theo(a, b, c, d, angle_theo[1])
            id_change.append(angle_theo)
        deta_corrige[id] = id_change

    print("deta_corrige: ", deta_corrige)

    # add deta_Pan and deta_Tilt to the Pans/Tilts theoretic
    angle_final = {}
    for key in data_to_change:
        if key in deta_corrige:
            angle_final[key] = []
            for i in range(len(data_to_change[key])):
                combined_list = []
                for j in range(len(data_to_change[key][i])):
                    angle = 0
                    if j == 0:
                        angle = round(
                            data_to_change[key][i][j] + deta_corrige[key][i][j], 2
                        )
                        # adapt to GrandMA3
                        if angle <= -270:
                            angle += 360
                        if angle >= 270:
                            angle -= 360
                    else:
                        angle = tilt_real_to_theo(
                            a,
                            b,
                            c,
                            d,
                            round(
                                data_to_change[key][i][j] + deta_corrige[key][i][j], 2
                            ),
                        )
                        if angle > 135:
                            angle = 135
                        if angle < -135:
                            angle = -135
                    combined_list.append(angle)

                angle_final[key].append(combined_list)

    print("angle_final：", angle_final)

    # create a new excel
    original_file = file_path_change

    # get filename
    base_name = os.path.basename(original_file)  # 'test5.xlsx'
    name, extension = os.path.splitext(base_name)  # 'test5', '.xlsx'

    # new excel name
    new_file_name = f"{name}_final{extension}"  # 'test5_final.xlsx'
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
    # positions_bouteilles = [
    #     [1, 6.29, -1.7],
    #     [3.42, 4.5, -1.3],
    #     [3.42, 1, -1.2],
    # ]  # postion x_B1,y_B1,z_B1 de la première bouteille, puis de la deuxième etc...
    # position_theorique_projecteur = [
    #     0,
    #     0,
    #     -0.29,
    # ]  # postion théorique du projecteur dans l'espace
    config_path = "Modif_fichier_preset/config.xlsx"
    sensors_dict, spotlight_dict = readConfig(config_path)
    position_sensors = []
    for key, values in sensors_dict.items():
        position_sensors.append(values)
    file_path = "Modif_fichier_preset/test4.xlsx"
    file_path_change = "Modif_fichier_preset/test5.xlsx"
    corrigePreset(file_path, file_path_change, position_sensors, spotlight_dict)
