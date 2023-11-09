from __future__ import print_function

import datetime
import os.path
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



import json
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_events():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds:
        print("no creds")

    #if not creds.valid:
     #   print("no creds valid")
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='kim6n4bbnpecd1cm165mmej9e10hkdju@import.calendar.google.com', timeMin=now,
                                               singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])


        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        print(len(events))
        for event in events:
            # print(event["start"])
            if("Schedule" in event["summary"]):
                if(event["start"]["date"] == str(datetime.date.today())):
                    print("there is school")
                # else:
                    # print("there is not school today, todays date: " + str(datetime.date.today()) + " the events date "+ event["start"]["date"])
            # start = event['start'].get('dateTime', event['start'].get('date'))
            # print(start, event['summary'])

        return events
        # calendar = service.calendars().get(calendarId='kim6n4bbnpecd1cm165mmej9e10hkdju@import.calendar.google.com').execute()

        # print(calendar)
    except HttpError as error:
        print(f'An error occurred: {error}')

file = open("Schedule.json", "w")
file.write(json.dumps(get_events()))
file.close()
