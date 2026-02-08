feed_emo = "\U0001F37C"

feed_logs = [] 

def get_start_time():
    while True:
        time_str = input("What time did it start? (HH:MM, e.g. 14:45)\n ").strip()

        if len(time_str) != 5 or time_str[2] != ":":
            print("❌ Invalid format. Please use HH:MM (e.g. 09:30).")

        hours, minutes = time_str.split(":")

        if not (hours.isdigit() and minutes.isdigit()):
            print("❌ Time must contain numbers only.")

        hours = int(hours)
        minutes = int(minutes)

        if not (0 <= hours <= 23 and 0 <= minutes <= 59):
            print("❌ Time must be between 00:00 and 23:59.")

        hours = str(hours)
        minutes = str(minutes)

        return time_str

def get_duration():
    while True:
        duration_str = input("How long did it last? (in minutes, e.g. 15)\n ").strip()

        if not duration_str.isdigit():
            print("❌ Please enter a number only (e.g. 45).")

        duration = int(duration_str)

        if duration <= 0:
            print("❌ Duration must be greater than 0.")

        duration = str(duration)

        return duration


def feed_actions():
    print("\U0001F37C Feed Tracker activated!\n")
    
    #ask for user input
    feed_time = get_start_time()
    feed_duration = get_duration()

    #store feed logs
    new_log_feed = {"feeding time" : feed_time, "feed duration" : feed_duration}
    feed_logs.append(new_log_feed)

    #display confirmation text
    print(f"Your baby enjoyed your milk at " + feed_time + " for " + feed_duration + " min.\n" 
          "The information \U0001F37C has been saved, hope your baby had a nice feed!\n")
