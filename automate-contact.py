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


     
        {"firstname": "3", "phone": "+243849433451"},
        {"firstname": "4", "phone": "+243992700262"},
        {"firstname": "3", "phone": "+243981660546"},
        {"firstname": "3", "phone": "+243990175228"},
        {"firstname": "3", "phone": "+243818356994"},
        {"firstname": "3", "phone": "+243985166362"},
        {"firstname": "3", "phone": "+243837903056"},
        {"firstname": "3", "phone": "+243972848956"},
        {"firstname": "3", "phone": "+243814731569"},
        {"firstname": "3", "phone": "+243830351770"},

       
    ]

    for contact in contacts:
        create_contact(service, contact)
        print(f"Contact ajouté : {contact['firstname']} ")

if __name__ == '__main__':
    main()
