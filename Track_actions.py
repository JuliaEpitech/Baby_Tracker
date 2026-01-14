#comment importer ce fichier action dans le fichier principal
    #from [nom du fichier .py où les fonctions sont définies] import [nom du ou des fichiers]
    #si toutes les ou beaucoup de fonctions du fichier: "import [nom du fichier]"" puis quand on utilise les fonctions "[nom du fichier .py où les fonctions sont définies].[nom de la fonction qu'on veut utiliser]


from pathlib import Path


def confirm_action():
    selection_mistake = input(
        "Is it really what you want to log?\n"
        "yes (Y)? no (N)?\n"
        ).strip().lower() 
    #.strip() retire tous les potentiels espaces ajoutés par l'utilisateur et .lower() formate tout en minuscule pour uniformiser le texte rentré par l'utilisateur

    if selection_mistake in ["n", "no"]:
    # à la place de devoir écrire selection_mistake == "n" or selection_mistake == "no": 
        print("\U0001F519 Back to the main menu!\n")
        return(-1)
        

def feed_actions(baby_name):
    print("\U0001F37C Feed Tracker activated!\n")

    #offer to go back if that wasn't the right choice
    if confirm_action() == -1:
        return
    
    #ask for user input
    feed_time = input(" What time did " + baby_name + " start eating? (HH:MM, e.g. 14:45)\n ")
    feed_duration = input(" How long did " + baby_name + " eat? (in minutes, e.g. 15)\n ")
    
    #store feed logs in corresponding list
    new_feed_log = {"feeding time" : feed_time, "feed duration" : feed_duration}
    #feed_logs.append(new_feed_log)

    #store dans DB
    path_Baby_trackerDB = Path.home() / "Documents" / "bosstek" / "Perso_projects" / "Baby_tracker.db"
    with open(path_Baby_trackerDB, "a") as file: 
            file.write(f"{baby_name}, feed, {feed_time}, {feed_duration}\n")

    #display confirmation text
    print(baby_name + " enjoyed your milk at " + feed_time + " for " + feed_duration + " min.\n" 
          "The information \U0001F37C has been saved, hope " + baby_name + " had a nice feed!\n")
    
    return new_feed_log


def sleep_actions(baby_name):
    print("\U0001F634 Sleep Tracker activated!\n")

    #offer to go back if that wasn't the right choice
    if confirm_action() == -1:
        return

    #ask for user input
    sleep_time = input(" At what time did " + baby_name + " fall asleep? (HH:MM, e.g. 14:45)\n ")
    sleep_duration = input(" How long did " + baby_name + " sleep? (in minutes, e.g. 15)\n ")

    #store sleep logs in corresponding list
    new_sleep_log = {"sleeping time" : sleep_time, "sleep duration" : sleep_duration} 
    #sleep_logs.append(new_sleep_log)

    #store dans DB
    path_Baby_trackerDB = Path.home() / "Documents" / "bosstek" / "Perso_projects" / "Baby_tracker.db"
    with open(path_Baby_trackerDB, "a") as file: 
            file.write(f"{baby_name}, sleep, {sleep_time}, {sleep_duration}\n")

    #display confirmation text
    print(baby_name + " fell asleep at " + sleep_time + " for " + sleep_duration + " min.\n"
          "The information has been saved, hope " + baby_name + " had a nice sleep! \U0001F634\n")
    
    return new_sleep_log


def poop_actions(baby_name):
    print("\U0001F4A9 Poop Tracker activated!\n")

    #offer to go back if that wasn't the right choice
    if confirm_action() == -1:
        return

    #ask for user input
    poop_time = input(" At what time did " + baby_name + " poop? (HH:MM, e.g. 14:45)\n ")
    #poop_color = input(" How did it look like?\n green? yellow? orange? brown?\n ")
    
    #store poop logs in corresponding list
    new_poop_log = {"poop time" : poop_time}
    #poop_logs.append(new_poop_log)
    
    #store dans DB
    path_Baby_trackerDB = Path.home() / "Documents" / "bosstek" / "Perso_projects" / "Baby_tracker.db"
    with open(path_Baby_trackerDB, "a") as file: 
            file.write(f"{baby_name}, poop, {poop_time}\n")

    #display confirmation text
    print(baby_name + " pooped at " + poop_time + ".\n"
        "The information has been saved, well done " + baby_name + "! \U0001F4A9\U0001F4A9\n")
    
    return new_poop_log


def cry_actions(baby_name):
    print("\U0001F62D Cry Tracker activated!\n")

    #offer to go back if that wasn't the right choice
    if confirm_action() == -1:
        return

    #ask for user input
    cry_time = input(" At what time did " + baby_name + " start crying? (HH:MM, e.g. 14:45)\n ")
    cry_duration = input(" " \
    "How long did " + baby_name + " cry? (in minutes, e.g. 15)\n ")

    #store cry logs in corresponding list
    new_cry_log = {"crying time" : cry_time, "crying duration" : cry_duration}
    #cry_logs.append(new_cry_log)

    #store dans DB
    path_Baby_trackerDB = Path.home() / "Documents" / "bosstek" / "Perso_projects" / "Baby_tracker.db"
    with open(path_Baby_trackerDB, "a") as file: 
            file.write(f"{baby_name}, cry, {cry_time}, {cry_duration}\n")

    #display confirmation text
    print(baby_name + " started her pleasant singing at " + cry_time + " for " + cry_duration + " min.\n"
        "You are strong and you love " + baby_name + " very much! you can endure it \U0001F4AA\n")
    
    return new_cry_log


def overview_actions(logs, emoji, activity):
    if not logs:
        print("No activity recorded yet. Start logging to see data here!\n ")

    else:      
        print(f"{emoji} Here is your {activity} logs review:")       
        for log in logs:
            print(log)
        print("")


#def store_activity(logs, activity):
    #if not logs:
        #pass

    #else:
        #return activity