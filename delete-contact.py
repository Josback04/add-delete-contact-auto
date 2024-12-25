from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path

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

def list_contacts(service):
    """Liste tous les contacts."""
    results = service.people().connections().list(
        resourceName='people/me',
        personFields='names,emailAddresses,phoneNumbers',
        pageSize=2000 
    ).execute()
    connections = results.get('connections', [])
    return connections

def delete_contact(service, contact_id):
    """Supprime un contact en utilisant son ID."""
    service.people().deleteContact(
        resourceName=contact_id
    ).execute()
    print(f"Contact avec ID {contact_id} supprimé.")

def main():
    """Programme principal."""
    creds = authenticate()
    service = build('people', 'v1', credentials=creds)

    contacts = list_contacts(service)
    
    if not contacts:
        print("Aucun contact trouvé.")
    else:
        contacts.reverse()
        
        for contact in contacts[:50]:
            contact_id = contact['resourceName']
            delete_contact(service, contact_id)

if __name__ == '__main__':
    main()
