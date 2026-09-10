import pandas as pd


def readConfig(file_path):

    # read table Sensors from second ligne
    sensors_data = pd.read_excel(file_path, sheet_name="Sensors", header=1)

    # rename
    sensors_data.columns = ["Name", "x", "y", "z"]

    # delete vid ligne(only ID,x,y,z are all non null)
    sensors_data = sensors_data.dropna(subset=["Name", "x", "y", "z"])

    # to dict:key - ID,value - list [x, y, z]
    sensors_dict = sensors_data.set_index("Name")[["x", "y", "z"]].T.to_dict(
        orient="list"
    )

    # read table Spotlights from second ligne
    spotlights_data = pd.read_excel(
        file_path, sheet_name="Spotlights", header=1, usecols="A:G"
    )

    # rename
    spotlights_data.columns = ["ID", "x", "y", "z", "axis", "Rotation", "Orientation"]

    # delete vid ligne(only ID, x, y, z, Orientation are all non null)
    spotlights_data = spotlights_data.dropna(
        subset=["ID", "x", "y", "z", "axis", "Rotation", "Orientation"]
    )

    # to dict:key - ID,value - list [x, y, z]
    spotlights_dict = spotlights_data.set_index("ID")[
        ["x", "y", "z", "axis", "Rotation", "Orientation"]
    ].T.to_dict(orient="list")
    return sensors_dict, spotlights_dict


if __name__ == "__main__":
    file_path = "Modif_fichier_preset/config-3.0.0.xlsx"
    # output
    sensors_dict, spotlight_dict = readConfig(file_path)
    print("Capteurs Dictionary:")
    print(sensors_dict)
    print("Projecteurs Dictionary:")
    print(spotlight_dict)
