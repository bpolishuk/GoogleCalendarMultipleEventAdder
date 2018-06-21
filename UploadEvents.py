"""
I don't know how to code so I'm hacking Google's
quickstart to put multiple dates on a calendar
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
f = open('calendar_log.txt', 'r')
summary = f.readline()
start_time = f.readline()
end_time = f.readline()
for line in f: 
    event = {
            'summary' : summary.rstrip(),
            'start' : {
                'dateTime' : line.rstrip() + 'T' + start_time.rstrip(),
                'timeZone': 'America/New_York',
                },
            'end' : {
                'dateTime' : line.rstrip() + 'T' + end_time.rstrip(),
                'timeZone': 'America/New_York',
                }
            }
    print(event)
    events_result = service.events().insert(calendarId='primary', body=event).execute()
