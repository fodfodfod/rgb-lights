import json
import datetime
import main

file = open("Schedule.json", "r")
schedule_string = file.read()
schedule = json.loads(schedule_string)
file.close()

for event in schedule:
            # print(event["start"])
            if("Schedule" in event["summary"] or "schedule" in event["summary"]):
                if(event["start"]["date"] == str(datetime.date.today())):
                    print("there is school")
                    main.run_display()