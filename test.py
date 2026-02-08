import Track_actions
from pathlib import Path

#call the data from the csv file:
path_Baby_trackerDB = Path.home() / "Documents" / "bosstek" / "Perso_projects" / "Baby_Tracker" / "Baby_tracker_db.csv"

with open(path_Baby_trackerDB, "r") as file: 

    last_line = 1

    #iterate through the lines
    lines = []
    lines = file.read().replace(" ","").split("\n")

    #traite 1ère ligne pour que le programme utilise les noms entrés dans cette première ligne pour définir les colonnes des lignes suivantes
    column_name = lines[0].split(",")

    #boucle pour chaque ligne pour retrouver les colonnes
    for line in lines[1:]:
        line = line.split(",")
        
        if len(line) != 0:
            ID = last_line + 1
    
            
print(last_line)
print(ID)