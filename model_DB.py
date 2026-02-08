from pathlib import Path

from Baby_tracker_current import baby_name, feed_logs, sleep_logs, poop_logs, cry_logs

path_Baby_trackerDB = Path.home() / "Documents" / "bosstek" / "Perso_projects" / "Baby_Tracker" / "Baby_tracker_db.csv"

with open(path_Baby_trackerDB, "r") as file: 

    #iterate through the lines
    lines = []
    lines = file.read().replace(" ","").split("\n")
    
    #traite 1ère ligne pour que le programme utilise les noms entrés dans cette première ligne pour définir les colonnes des lignes suivantes
    column_name = lines[0].split(",")

    #boucle pour chaque ligne pour retrouver les colonnes
    for line in lines[1:]:
        line = line.split(",")

        #print(line[column_name.index("Activity")]) >> check que le programme retrouve bien la colonne correspondante

        if line[column_name.index("BabyName")] == baby_name: 
        #pas de while parce que déjà for loop et le pgm doit prendre les infos directement, au fur et à mesure qu'il va de ligne en ligne, SI le Baby Name == nom du bébé donné par l'utilisateur


            def load_feed():
                if line[column_name.index("Activity")] == "feed":
                    new_feed_log = {"feed time" : line[column_name.index("StartingTime")], "feed duration" : line[column_name.index("Duration")]}
                    feed_logs.append(new_feed_log) #.write si ajouter dans un fichier externe, .append si ajouter dans la liste du programme


            def load_sleep():
                if line[column_name.index("Activity")] == "sleep":
                    new_sleep_log = {"sleep time" : line[column_name.index("StartingTime")], "sleep duration" : line[column_name.index("Duration")]}
                    sleep_logs.append(new_sleep_log)

            def load_poop():
                if line[column_name.index("Activity")] == "poop":
                    new_poop_log = {"poop time" : line[column_name.index("StartingTime")]}
                    poop_logs.append(new_poop_log)

            def load_cry():
                if line[column_name.index("Activity")] == "cry":
                    new_cry_log = {"cry time" : line[column_name.index("StartingTime")], "cry duration" : line[column_name.index("Duration")]}
                    cry_logs.append(new_cry_log)
