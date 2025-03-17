from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path
import pandas as pd

# Scopes pour l'accès à Google Contacts
SCOPES = ['https://www.googleapis.com/auth/contacts']

def authenticate():
    """Authentifie l'utilisateur avec OAuth2 et gère le token."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials_script.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_contact(service, contact):
    """Ajoute un contact dans Google Contacts."""
    service.people().createContact(body={
        "names": [{"givenName": contact['firstname']}],
        "phoneNumbers": [{"value": contact['phone']}],
        # "emailAddresses": [{"value": contact['email']}],
    }).execute()

def import_contacts_from_excel(filepath):
    """Lit un fichier Excel et ajoute les contacts avec numérotation."""
    creds = authenticate()
    service = build('people', 'v1', credentials=creds)

    df = pd.read_excel(filepath)
    print("Colonnes du fichier Excel :", df.columns)


    contacts = []
    for _, row in df.iterrows():
        contacts.append({
            "firstname": str(row['Nom']),
            "phone": str(row["Téléphone"]),
            # "email": str(row["E-mail"]),
        })

    for contact in contacts:
        create_contact(service, contact)
        print(f"Contact ajouté : {contact['firstname']}")

if __name__ == '__main__':
    import_contacts_from_excel("'/Users/josback/Downloads/CONTACTS 18.03.13H.xlsx'")
