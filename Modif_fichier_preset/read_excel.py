import pandas as pd
def recuperer_pan_tilt_par_id(chemin_fichier,sheetName):
    # Lire les données à partir du fichier Excel
    donnees_excel = pd.read_excel(chemin_fichier, sheet_name=sheetName)

    # Créer un dictionnaire pour stocker les valeurs de Pan et Tilt pour chaque ID
    valeurs_pan_tilt_par_id = {}

    # Parcourir tous les ID uniques
    for id_unique in donnees_excel['ID'].unique():
        # Filtrer les lignes correspondant à cet ID
        lignes_id = donnees_excel[donnees_excel['ID'] == id_unique]
        # Récupérer les valeurs de Pan et Tilt pour cet ID
        valeurs_pan = list(lignes_id['Pan'])
        valeurs_tilt = list(lignes_id['Tilt'])
        # Stocker les valeurs dans le dictionnaire
        valeurs_pan_tilt_par_id[id_unique] = {'Pan': valeurs_pan, 'Tilt': valeurs_tilt}

    return valeurs_pan_tilt_par_id



# Enregistrer les données filtrées dans un fichier de votre choix
#donnees_filtrees.to_csv('chemin/vers/votre/fichier_de_sortie.csv', index=False)


def trouver_et_modifier_ligne_et_suivante(chemin_fichier, mot_cle1, mot_cle2, nouveau_num):
    lignes_modifiees = []
    with open(chemin_fichier, 'r',encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            # Si la ligne contient le premier mot-clé
            if mot_cle1 in lines[i]:
                # Vérifier si la ligne suivante contient le deuxième mot-clé
                if mot_cle2 in lines[i + 1]:
                    # Modifier le numéro dans la deuxième ligne
                    parts = lines[i + 1].split('"')
                    parts[3] = str(nouveau_num)
                    lines[i + 1] = '"'.join(parts)
                    lignes_modifiees.append((lines[i + 1], lines[i + 1]))
    # Réécrire les lignes modifiées dans le fichier
    with open(chemin_fichier, 'w',encoding='utf-8') as file:
        file.writelines(lines)
    return lignes_modifiees

def modifier_xml(path, id, type, valeur):
    # Exemple d'utilisation
    chemin_fichier = path  # Remplacer par le chemin de votre fichier
    mot_cle1 = f'ID="{id}"'
    mot_cle2 = type

    lignes_modifiees = trouver_et_modifier_ligne_et_suivante(chemin_fichier, mot_cle1, mot_cle2, valeur)
    if lignes_modifiees:
        print("Ligne avec le numéro modifié : ")
        for ligne in lignes_modifiees:
            print(ligne)
    else:
        print("Aucune ligne contenant les mots-clés n'a été trouvée.")

def obtenir_noms_feuilles(chemin_fichier):
    xl = pd.ExcelFile(chemin_fichier)
    return xl.sheet_names

noms_feuilles = obtenir_noms_feuilles('./Presets1.xlsx')
for nom_feuille in noms_feuilles:
    valeurs_pan_tilt_par_id = recuperer_pan_tilt_par_id('./Presets1.xlsx',nom_feuille)
    for id_unique, valeurs in valeurs_pan_tilt_par_id.items():
        print(f"ID: {id_unique}, Pan: {valeurs['Pan']}, Tilt: {valeurs['Tilt']}")
        modifier_xml(f'./{nom_feuille}',id_unique,'Pan',valeurs['Pan'][0])
        modifier_xml(f'./{nom_feuille}',id_unique,'Tilt',valeurs['Tilt'][0])


