import pandas as pd

# Charger les fichiers Excel
file1 = 'רגילים 1.xlsx'
file2 = 'רגילים 2.xlsx'

df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# On considère que la première ligne contient les titres
columns = df1.columns

# Initialiser les nouveaux DataFrames avec seulement la colonne 'Serie'
new_file1 = pd.DataFrame(df1['Serie'])
new_file2 = pd.DataFrame(df1['Serie'])

# Fonction pour diviser une colonne en deux moitiés équitables
def split_column(column):
    half1 = column[:len(column) // 2].reset_index(drop=True)
    half2 = column[len(column) // 2:].reset_index(drop=True)
    return half1, half2

# Traiter chaque colonne (sauf 'Serie')
for column in columns:
    if column == 'Serie':
        continue

    # Diviser les colonnes de chaque fichier en deux moitiés
    col1_half1, col1_half2 = split_column(df1[column])
    col2_half1, col2_half2 = split_column(df2[column])

    # Mélanger les moitiés de chaque colonne pour les nouveaux fichiers
    new_file1[column] = pd.concat([col1_half1, col2_half1]).reset_index(drop=True)
    new_file2[column] = pd.concat([col1_half2, col2_half2]).reset_index(drop=True)

# Ajouter les colonnes restantes des fichiers originaux
for column in columns:
    if column == 'Serie':
        new_file1[column] = df2['Serie']
        new_file2[column] = df1['Serie']

# Enregistrer les nouveaux fichiers Excel
new_file1.to_excel('new_file1.xlsx', index=False)
new_file2.to_excel('new_file2.xlsx', index=False)
