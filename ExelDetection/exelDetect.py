import pandas as pd

# Chemin vers votre fichier Excel
fichier_excel = 'suspect.xlsx'

# Lire le fichier Excel
df = pd.read_excel(fichier_excel)

# Afficher les noms des colonnes pour vérifier
print("Column names in the Excel file:")
print(df.columns)

# Nom de la colonne contenant les noms (mettez à jour avec le nom correct)
column_name = 'Name'

# Calculer le nombre total de noms différents
unique_names_count = df[column_name].nunique()

# Calculer la fréquence de chaque nom
name_counts = df[column_name].value_counts()

# Compter le nombre de noms répétés (fréquence > 1)
repeated_names_count = (name_counts > 1).sum()

# Obtenir les noms répétés et leur fréquence
repeated_names = name_counts[name_counts > 1]

# Afficher les résultats
print(f"There are {unique_names_count-1} different names in the column '{column_name}'.")
print(f"There are {repeated_names_count} names that are repeated in the column '{column_name}'.")

# Afficher les noms répétés et leur fréquence
if not repeated_names.empty:
    print("\nRepeated names and their frequencies:")
    for name, count in repeated_names.items():
        print(f"'{name}' is repeated {count} times.")
else:
    print("There are no repeated names.")
