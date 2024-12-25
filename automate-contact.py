from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path

# Scopes pour l'accès à Google Contacts
SCOPES = ['https://www.googleapis.com/auth/contacts']

def authenticate():
    """Authentifie l'utilisateur avec OAuth2."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_contact(service, contact):
    """Crée un contact dans Google Contacts."""
    service.people().createContact(body={
        "names": [{"givenName": contact['firstname']}],
        "phoneNumbers": [{"value": contact['phone']}],
    }).execute()

def main():
    """Programme principal."""
    creds = authenticate()
    service = build('people', 'v1', credentials=creds)

    # Exemple de liste de contacts
 

    contacts = [
     
        {"firstname": "3", "phone": "+243898242448"},
        {"firstname": "4", "phone": "+243972912083"},
        {"firstname": "3", "phone": "+243990491286"},
        {"firstname": "3", "phone": "+243849433451"},
        {"firstname": "3", "phone": "+243897369836"},
        {"firstname": "3", "phone": "+243997486039"},
        {"firstname": "3", "phone": "+243895511485"},
        {"firstname": "3", "phone": "+243819799393"},
        {"firstname": "3", "phone": "+243992700262"},
        {"firstname": "3", "phone": "+243975362746"},
        {"firstname": "3", "phone": "+243853033065"},
        {"firstname": "3", "phone": "+243823092678"},
        {"firstname": "3", "phone": "+243820098480"},
        {"firstname": "3", "phone": "+243993133729"},
        {"firstname": "3", "phone": "+243830351770"},
        {"firstname": "3", "phone": "+243830973386"},
        {"firstname": "3", "phone": "+243834759063"},
        {"firstname": "3", "phone": "+243992834624"},
        {"firstname": "3", "phone": "+243857084688"},
        {"firstname": "3", "phone": "+243890607615"},
        {"firstname": "3", "phone": "+243850358760"},
        {"firstname": "3", "phone": "+243831999739"},
        {"firstname": "3", "phone": "+243901058311"},
        {"firstname": "3", "phone": "+243995477266"},
        {"firstname": "3", "phone": "+243814731569"},
        {"firstname": "3", "phone": "+243904488368"},
        {"firstname": "3", "phone": "+243985569156"},
        {"firstname": "3", "phone": "+243850050326"},
        {"firstname": "3", "phone": "+243995496511"},
        {"firstname": "3", "phone": "+243890607615"},
        {"firstname": "3", "phone": "+243811162894"},
        {"firstname": "3", "phone": "+243972848956"},
        {"firstname": "3", "phone": "+243813241614"},
        {"firstname": "3", "phone": "+243837903056"},
        {"firstname": "3", "phone": "+243858238304"},
        {"firstname": "3", "phone": "+243978423821"},
        {"firstname": "3", "phone": "+243897278460"},
        {"firstname": "3", "phone": "+243974894679"},
        {"firstname": "3", "phone": "+243843001854"},
        {"firstname": "3", "phone": "+243985166362"},
        {"firstname": "3", "phone": "+243851456965"},
        {"firstname": "3", "phone": "+243894015273"},
        {"firstname": "3", "phone": "+243894015273"},
        {"firstname": "3", "phone": "+243823538309"},
        {"firstname": "3", "phone": "+243818356994"},
        {"firstname": "3", "phone": "+243972124024"},
        {"firstname": "3", "phone": "+243823538309"},
        {"firstname": "3", "phone": "+243976598149"},
        {"firstname": "3", "phone": "+243823538309"},
        {"firstname": "3", "phone": "+243990175228"},
        {"firstname": "3", "phone": "+243978978621"},
        {"firstname": "3", "phone": "+243981891953"},
        {"firstname": "3", "phone": "+243821922778"},
        {"firstname": "3", "phone": "+243981891953"},

       
    ]

    for contact in contacts:
        create_contact(service, contact)
        print(f"Contact ajouté : {contact['firstname']} ")

if __name__ == '__main__':
    main()
