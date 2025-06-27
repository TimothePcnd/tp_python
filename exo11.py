
# Lecture CSV
import csv


import sqlite3
con = sqlite3.connect("departement.db")
cur = con.cursor()




with open('departements-france.csv', encoding='UTF-8') as csvfile:
    # ligne pour créer la table dans la bdd
    # cur.execute("CREATE TABLE depart(code_departement, nom_departement, code_region, nom_region)")
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        cur.execute("""INSERT INTO depart VALUES (01, 'Ain', 84, 'Auvergne-Rhône-Alpes'), (02, 'Aisne', 32, 'Hauts-de-France')""")
        print(row[0:2])