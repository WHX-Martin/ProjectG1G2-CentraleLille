import os


def is_excel_file_open(file_path):
    """
    Checks if an Excel file is open by attempting to rename it.

    Args:
        file_path: The path to the Excel file.

    Returns:
        True if the file is open, False otherwise.
    """
    if not os.path.exists(file_path):
        return False  # File doesn't exist

    try:
        # Try to rename the file by appending a temporary suffix
        temp_file_path = file_path + "_temp"
        os.rename(file_path, temp_file_path)
        os.rename(temp_file_path, file_path)  # Rename it back
        return False
    except OSError:
        return True


if __name__ == "__main__":
    filepath = "E:/大学/双学位/学习/ProjetG1G2/ProjectG1G2-CentraleLille/Modif_fichier_preset/PresetTest.xlsx"
    print(is_excel_file_open(filepath))
