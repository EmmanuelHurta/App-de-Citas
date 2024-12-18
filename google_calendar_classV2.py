import os.path
import datetime as dt
import datetime as datetime


from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

class GoogleCalendarManager:
    def __init__(self):
        self.service = self._authenticate()

    def _authenticate(self):
        creds = None

        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("client_secret_app_escritorio_oauth.json", SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        return build("calendar", "v3", credentials=creds)

    def list_upcoming_events(self, max_results=10):
        now = dt.datetime.utcnow().isoformat() + "Z"
        tomorrow = (dt.datetime.now() + dt.timedelta(days=5)).replace(hour=23, minute=59, second=0, microsecond=0).isoformat() + "Z"

        events_result = self.service.events().list(
            calendarId='primary', timeMin=now, timeMax=tomorrow,
            maxResults=max_results, singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        else:
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print (f"{start, event['summary']},ID:{event['id']}")
        
        return events

    def create_event(self, summary, start_time, end_time, timezone, attendees=None):
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time,
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_time,
                'timeZone': timezone,
            }
        }

        if attendees:
            event["attendees"] = [{"email": email} for email in attendees]

        try:
            event = self.service.events().insert(calendarId="primary", body=event).execute()
            print(f"Event created: {event.get('htmlLink')}")
        except HttpError as error:
            print(f"An error has occurred: {error}")

    def update_event(self, event_id, summary=None, start_time=None, end_time=None):
        event = self.service.events().get(calendarId='primary', eventId=event_id).execute()

        if summary:
            event['summary'] = summary

    
        if start_time:
            try:
                start_time = dt.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
                event['start']['dateTime'] = start_time.strftime('%Y-%m-%dT%H:%M:%S')
            except ValueError:
                print(f"Error: El formato de la fecha de inicio no es válido: {start_time}")
                return

        if end_time:
            try:
                end_time = dt.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S")
                event['end']['dateTime'] = end_time.strftime('%Y-%m-%dT%H:%M:%S')
            except ValueError:
                print(f"Error: El formato de la fecha de fin no es válido: {end_time}")
                return

        updated_event = self.service.events().update(
            calendarId='primary', eventId=event_id, body=event).execute()
        return updated_event

    def delete_event(self, event_id):
        self.service.events().delete(calendarId='primary', eventId=event_id).execute()
        return True
    

calendar_manager = GoogleCalendarManager()

#calendar_manager.create_event("Hola youtube","2024-12-08T16:30:00+02:00","2024-12-08T17:30:00+02:00","Europe/Madrid",["antonio@gmail.com","pedro@gmail.com"])


#calendar_manager.list_upcoming_events()



#calendar.update_event('up6ch1kapa8gtndkiboj5ilng4', "Hola emanuel Trujillo", "2024-12-08T16:30:00+02:00", "2024-12-08T18:30:00+02:00")
                        
#ID: up6ch1kapa8gtndkiboj5ilng4

#calendar.create_event("Hola youtube","2024-12-08T16:30:00+02:00","2024-12-08T17:30:00+02:00","Europe/Madrid",["antonio@gmail.com","pedro@gmail.com"])

#calendar.update_event('up6ch1kapa8gtndkiboj5ilng4',"Hola emanuel","2024-12-08T15:30:00+02:00","2024-12-08T17:30:00+02:00","Europe/Madrid",["antonio@gmail.com","pedro@gmail.com"])

#Borrar evento
#calendar.delete_event(event_id='6bdpt73hvg1rlf50djcv1kf7vk')
#calendar.delete_event(event_id='m5pkc2gvog8oeos9f9bbp7paao')


#modificar evento
#calendar.update_event("Hola Twich","2024-08-08T16:30:00+02:00","2024-08-08T17:30:00+02:00","Europe/Madrid",["antonio@gmail.com","pedro@gmail.com"])


#crear evento
#calendar.create_event("Hola youtube","2024-08-08T16:30:00+02:00","2024-08-08T17:30:00+02:00","Europe/Madrid",["antonio@gmail.com","pedro@gmail.com"])
#client_secret_app_escritorio_oauth.json
