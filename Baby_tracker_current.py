#expected outputs: 1/ current/last entry tracking; 2/ history (horaires? stats?); 3/ graphs (with times, number of feeds p.day); 4/ AI personalized schedule maker
#évolution possible:
    #comportement 1: note heure de début + lance un timer
    #comportement 2: note heure de début + lance un timer
    #comportement 3: note heure (+type de poop?+ pipi? + vomi?)
    #comportement 4: note heure de début + lance un timer
#**Génère un qr code pour pouvoir visualiser les overviews?
#**prévois une overview croisée des différentes activités 
#(ajoute option switch baby pour pouvoir changer de bébé sans interrompre le programme)

#tests unitaires
#classes
#API (the Bump)
#serveur (scaling?)
#librairies externes (date du jour)



#rajoute une option dans le menu "oh nooooon! >> mais c'est pour ça qu'il faut toujours préparer du modulable!"
#pour charger mon fichier dans mes tableaux (sans duplicata, afin que le programme puisse se souvenir des précédents logs même s'il a été arrêté)
# > faire appel au contenu du fichier au lancement du programme mais après baby_name de manière à pas surchager la RAM avec des infos inutiles


#next TODO: check dans option 3 pour ne pas réécrire dans le csv les données déjà présentes + attribution ID >> pb de loop/identations??

#tous les imports sont précisés au début du code
import Track_actions
#import model_DB
from pathlib import Path

baby_name = input("What's the name of your baby? \U0001F476\n")


#emojis
feed_emo = "\U0001F37C"
sleep_emo = "\U0001F634"
poop_emo = "\U0001F4A9"
cry_emo = "\U0001F4AA"

#
feed = "feed"
sleep = "sleep"
poop = "poop"
cry = "cry"

feed_logs = [] 
sleep_logs = []
poop_logs =  []
cry_logs = []


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


#Baby Tracker Programme
#main menu
while True:

    activity_choice = input(
        "What would you like to do? \n"
        "\U0001F4DD Log an activity (feed, sleep, poop, cry): 1 \n"
        "\U0001F4CA View an activity overview: 2 \n"
        "\U0001F4E5 Load from Database: 3 \n"
        "\U0001F6AA Exit: 4\n"
        ).strip().lower()

    #option 1: Activities tracker
    if activity_choice in ["1", "log", "log an activity"]:


            print("\U0001F4DD Let's log an activity!\n")

            #sub-menu activity selection < activity tracker
            while True: 
                #ask for user's choice
                activity = input(
                    "Which activity would you like to track?\n"
                    "\U0001F37C feed: 1\n" 
                    "\U0001F634 sleep:2\n" 
                    "\U0001F4A9 poop:3\n"
                    "\U0001F62D cry: 4\n"
                     "\U0001F519 back: 5\n"
                     ).strip().lower()


                #FEED
                if activity in ["1", "feed"]:
                    #activity_type.append(activity)
                    new_feed_log = Track_actions.feed_actions(baby_name)
                    if new_feed_log != -1:
                        feed_logs.append(new_feed_log) #check if new log != none or -1 then >> add it


                #SLEEP     
                elif activity in ["2", "sleep"]:                
                    new_sleep_log = Track_actions.sleep_actions(baby_name)
                    if new_sleep_log != -1:
                        sleep_logs.append(new_sleep_log)


                #POOP
                elif activity in ["3", "poop"]:
                    new_poop_log = Track_actions.poop_actions(baby_name)
                    if new_poop_log != -1:
                        poop_logs.append(new_poop_log)


                #CRY
                elif activity in ["4", "cry"]:
                    new_cry_log = Track_actions.cry_actions(baby_name)
                    if new_cry_log != -1:
                        cry_logs.append(new_cry_log)
                        
            
                #Back to main menu
                elif activity in ["5", "back"]:
                    print("Back to the main menu! \U0001F519\n")
                    break


                #user input incorrect
                else: 
                    print("I don't understand the activity you'd like to log.\n")
                


    # option 2: Activities overview
    elif activity_choice in ["2", "overview"]:
        print("\U0001F4CA Let's review your activity!\n")

        #sub-menu activity selection < activities overview
        review = input(
            "Which activity would you like to review?\n"
            + feed_emo +" feed: 1 \n" 
            + sleep_emo + " sleep: 2 \n" 
            + poop_emo + " poop: 3 \n" 
            + cry_emo +" cry: 4 \n"
            "\U0001F4CA all activities: 5 \n"
            "\U0001F519 back: 6\n"
            ).strip().lower()

        #display feed logs
        if review in ["1", "feed"]:
            Track_actions.overview_actions(feed_logs, feed_emo, feed)

        #display sleep logs
        elif review in ["2", "sleep"]:
            Track_actions.overview_actions(sleep_logs, sleep_emo, sleep)

        #display poop logs
        elif review in ["3", "poop"]:
            Track_actions.overview_actions(poop_logs, poop_emo, poop)

        #display cry logs
        elif review in ["4", "cry"]:
            Track_actions.overview_actions(cry_logs, cry_emo, cry)

        
        #display the logs for all activities 
        elif review in ["5", "all activities"]:
            print("\U0001F4CA Here is your logs review for all activities:\n")
            print("Feed activities:")
            Track_actions.overview_actions(feed_logs, feed_emo, feed)
            print("Sleep activities:")
            Track_actions.overview_actions(sleep_logs, sleep_emo, sleep)  
            print("Poop activities:")
            Track_actions.overview_actions(poop_logs, poop_emo, poop)
            print("Cry activities:")
            Track_actions.overview_actions(cry_logs, cry_emo, cry)

        elif review in ["6", "back"]:
            print("\U0001F519 Back to the main menu!\n")
            pass


    # option 3: Load from Database
    elif activity_choice in ["3", "load", "database"]:
        print("\U0001F4E5 Your baby’s data is ready\n")

        #call the data from the csv file:
        path_Baby_trackerDB = Path.home() / "Documents" / "bosstek" / "Perso_projects" / "Baby_Tracker" / "Baby_tracker_db.csv"

        with open(path_Baby_trackerDB, "r") as file: 

            #iterate through the lines
            lines = []
            lines = file.read().replace(" ","").split("\n")

            #boucle pour chaque ligne pour retrouver les colonnes
            for line in lines[1:]:
                line = line.split(",")

                last_line = 0

            #count lines to define the last_line & ID
                if len(line) != 0:
                    ID = last_line + 1

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

                    load_feed()
                    load_sleep()
                    load_poop()
                    load_cry()
#check pour ne pas que les données soient importées et donc apparaissent une autre fois dans le csv

        print(feed_logs, sleep_logs, poop_logs, cry_logs)    

    
    
    
    # option 4: Exit
    elif activity_choice in ["4", "exit"]:
        
        #store the data in an external csv file:
        path_Baby_trackerDB = Path.home() / "Documents" / "bosstek" / "Perso_projects" / "Baby_Tracker" / "Baby_tracker_db.csv"
        
        with open(path_Baby_trackerDB, "r") as file:
            print(file.read())

        #store data ONLY if it's not there already!!
        with open(path_Baby_trackerDB, "a") as file:

            if ID > last_line:

                if feed_logs != "":
                    print(feed_logs)
                    for log in feed_logs:
                        file.write(f"{ID}, on, {baby_name},feed,{log["feed time"]},{log["feed duration"]}\n")

                if sleep_logs != "":
                    for log in sleep_logs:
                        file.write(f"{ID}, on, {baby_name},sleep,{log["sleep time"]},{log["sleep duration"]}\n")

                if poop_logs != "":
                    for log in poop_logs:
                        file.write(f"{ID}, on, {baby_name},poop,{log["poop time"]}\n")

                if cry_logs != "":
                    for log in cry_logs:
                        file.write(f"{ID}, on, {baby_name},cry,{log["cry time"]},{log["cry duration"]}\n")   
 

        print("Thanks for using the app! See you soon! \U0001F44B")
        quit()

    
    #user input incorrect
    else: 
        print("I don't understand the activity you'd like to log.\n")