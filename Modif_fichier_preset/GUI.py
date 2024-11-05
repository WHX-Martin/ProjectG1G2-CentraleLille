import tkinter as tk
import os
import shutil
import read_excel as cpre
import read_preset as rpre
from tkinter import filedialog

def select_folder(selection_entry):
    # create a window to select folder
    folder_path = filedialog.askdirectory()
    if folder_path:  # if folder selected
        # show the folder in the entry
        selection_entry.delete(0,tk.END)
        selection_entry.insert(0,f"{folder_path}")

def select_file(selection_entry):
    filepath = filedialog.askopenfilename(
        title="Select Excel",  # window title
        filetypes=(("Excel files", "*.xlsx;*.xls"),)  # file type
    )
    if filepath:  # if user choose a file
        print("Select file path：", filepath)
        selection_entry.delete(0,tk.END)
        selection_entry.insert(0,f"{filepath}")

# create the main window
root = tk.Tk()
root.title("Preset Operation")  # set window title
root.geometry("500x300")  # set window size (width x height)

#Read Preset
readPresetLabel = tk.Label(text="Read Presets(xml file):")
readPresetLabel.pack()
# create a parent Frame，set it in the middle of the window
parent_frame = tk.Frame(root)
parent_frame.pack(fill=tk.X)

# create two blocks in the frame
selection_label = tk.Label(parent_frame,text="         Presets Folder:")
selection_label.pack(side=tk.LEFT)
# an entry to show the path
selection_entry = tk.Entry(parent_frame)
selection_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
selection_entry.config(bg="white")

# a button to start the selection for the folder
select_button = tk.Button(parent_frame, text="Select Folder", command=lambda:select_folder(selection_entry))
select_button.pack(side=tk.LEFT)


cExcel_frame = tk.Frame(root)
cExcel_frame.pack(fill=tk.X)


cExcel_label = tk.Label(cExcel_frame,text="Export Excel Folder:")
cExcel_label.pack(side=tk.LEFT)

cExcel_entry = tk.Entry(cExcel_frame)
cExcel_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
cExcel_entry.config(bg="white")


cExcel_button = tk.Button(cExcel_frame, text="Select Folder", command=lambda:select_folder(cExcel_entry))
cExcel_button.pack(side=tk.LEFT)

cExcelName_frame = tk.Frame(root)
cExcelName_frame.pack(fill=tk.X)
cExcelName_label = tk.Label(cExcelName_frame,text="              Excel Name:")
cExcelName_label.pack(side=tk.LEFT)
cExcelName_entry = tk.Entry(cExcelName_frame)
cExcelName_entry.pack(side=tk.LEFT)

def readPreset(xml_folder_path,excel_folder_path,excel_name):
    if xml_folder_path and excel_folder_path and excel_name:
        # Get all the xml files in the folder 
        xml_files = rpre.get_xml_files(xml_folder_path)
        print("xml file in the folder：", xml_files)
        for file in xml_files:
            data = rpre.readXml(file)
            rpre.writeExcel(data,excel_folder_path+'/'+excel_name+'.xlsx')

rPreset_button = tk.Button(root, text="Read Presets", command=lambda:readPreset(selection_entry.get(),cExcel_entry.get(),cExcelName_entry.get()))
# change button color
rPreset_button.config(bg="#ADD8E6", fg="black")
rPreset_button.pack(fill=tk.X)

#Change Preset
changePresetLabel = tk.Label(text="Change Presets(xml file):")
changePresetLabel.pack()

# change presets Excel

changePresetExcel_frame = tk.Frame(root)
changePresetExcel_frame.pack(fill=tk.X)


changePresetExcel_label = tk.Label(changePresetExcel_frame,text="        Excel Path:")
changePresetExcel_label.pack(side=tk.LEFT)

changePresetExcel_entry = tk.Entry(changePresetExcel_frame)
changePresetExcel_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
changePresetExcel_entry.config(bg="white")


changePresetExcel_button = tk.Button(changePresetExcel_frame, text="Select Excel File", command=lambda:select_file(changePresetExcel_entry))
changePresetExcel_button.pack(side=tk.LEFT)

# change presets folder

changePresetFolder_frame = tk.Frame(root)
changePresetFolder_frame.pack(fill=tk.X)


changePresetFolder_label = tk.Label(changePresetFolder_frame,text="Presets Folder:")
changePresetFolder_label.pack(side=tk.LEFT)

changePresetFolder_entry = tk.Entry(changePresetFolder_frame)
changePresetFolder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
changePresetFolder_entry.config(bg="white")


changePresetFolder_button = tk.Button(changePresetFolder_frame, text="Select Folder", command=lambda:select_folder(changePresetFolder_entry))
changePresetFolder_button.pack(side=tk.LEFT)

def changePreset(xml_folder_path,excel_path):
    # create a new folder
    new_folder_path = os.path.join(xml_folder_path, 'presets_change')

    # create folder if not exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Create folder: {new_folder_path}")

    # walk through xml_folder_path and copy xml files to the new folder
    for filename in os.listdir(xml_folder_path):
        # check if xml
        if filename.endswith('.xml'):
            src_file_path = os.path.join(xml_folder_path, filename)
            dst_file_path = os.path.join(new_folder_path, filename)
            shutil.copy2(src_file_path, dst_file_path)
            print(f"Copy: {src_file_path} -> {dst_file_path}")

    print("all XML files are copyed into folder presets_change")
    if xml_folder_path and excel_path:
        noms_feuilles = cpre.obtenir_noms_feuilles(excel_path)
        for nom_feuille in noms_feuilles:
            valeurs_pan_tilt_par_id = cpre.recuperer_pan_tilt_par_id(excel_path,nom_feuille)
            for id_unique, valeurs in valeurs_pan_tilt_par_id.items():
                print(f"ID: {id_unique}, Pan: {valeurs['Pan']}, Tilt: {valeurs['Tilt']}")
                cpre.modifier_xml(new_folder_path+f'/{nom_feuille}',id_unique,'Pan',valeurs['Pan'][0])
                cpre.modifier_xml(new_folder_path+f'/{nom_feuille}',id_unique,'Tilt',valeurs['Tilt'][0])

# button to change the presets
cPreset_button = tk.Button(root, text="Change Presets", command=lambda:changePreset(changePresetFolder_entry.get(),changePresetExcel_entry.get()))
# change button color
cPreset_button.config(bg="#ADD8E6", fg="black")
cPreset_button.pack(fill=tk.X)





root.mainloop()
