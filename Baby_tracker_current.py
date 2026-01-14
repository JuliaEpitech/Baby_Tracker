#expected outputs: 1/ current/last entry tracking; 2/ history (horaires? stats?); 3/ graphs (with times, number of feeds p.day); 4/ AI personalized schedule maker
#évolution possible:
    #comportement 1: note heure de début + lance un timer
    #comportement 2: note heure de début + lance un timer
    #comportement 3: note heure (+type de poop?+ pipi? + vomi?)
    #comportement 4: note heure de début + lance un timer
#**Génère un qr code pour pouvoir visualiser les overviews?
#**prévois une overview croisée des différentes activités 

#où placer la création de liste pour sauvegarder chacune des entrées sauvegardées selon l'identité du bébé? >>DB
#librairies externes (date du jour)
#ma propre base de données

baby_name = input("What's the name of your baby? \U0001F476\n")

#tous les imports sont précisés au début du code
import Track_actions
from pathlib import Path

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

activity_type = []        

#main menu
while True:

    activity_choice = input(
        "What would you like to do? \n"
        "\U0001F4DD Log an activity (feed, sleep, poop, cry): 1 \n"
        "\U0001F4CA View an activity overview: 2 \n"
        "\U0001F6AA Exit: 3\n"
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
                    feed_logs.append(new_feed_log)


                #SLEEP     
                elif activity in ["2", "sleep"]:                
                    new_sleep_log = Track_actions.sleep_actions(baby_name)
                    sleep_logs.append(new_sleep_log)


                #POOP
                elif activity in ["3", "poop"]:
                    new_poop_log = Track_actions.poop_actions(baby_name)
                    poop_logs.append(new_poop_log)


                #CRY
                elif activity in ["4", "cry"]:
                    new_cry_log = Track_actions.cry_actions(baby_name)
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


    # option 3: Exit
    elif activity_choice in ["3", "exit"]:
        
        
        path_Baby_trackerDB = Path.home() / "Documents" / "bosstek" / "Perso_projects" / "Baby_tracker.db"
        
        #with open(path_Baby_trackerDB, "r") as file:
            #print(file.read())


        #with open(path_Baby_trackerDB, "a") as file: 
            #file.write(f"{baby_name}, {activity}, new, info\n")   #comme pour printf

            #fichier .csv >> check d'abord la structure:
            #ligne 1 == name, activity, logs/data specificities >> Nina, feed, starting time, duration
            #formate données: élément 1 == nom bébé (==baby_name), élément 2 == activity (==activity), élément 3 == starting time (==feed_time or sleep-time or poop_time or cry_time), élément 4 == duration (==feed_duration or sleep_duration or poop_duration or cry_duration)
            #"write" ajoute a la fin si ouvre en append, add line by line of the list, virgules entre les éléments
            # dictionary's blabla_time + blabla_duration == 3rd +4th elements in the csv 
            #




        with open(path_Baby_trackerDB, "r") as file:
            print(file.read())



            pass

        print("Thanks for using the app! See you soon! \U0001F44B")
        quit()

    
    #user input incorrect
    else: 
        print("I don't understand the activity you'd like to log.\n")
