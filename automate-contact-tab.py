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
            flow = InstalledAppFlow.from_client_secrets_file('credentials_script.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_contact(service, contact):
    """Crée un contact dans Google Contacts."""
    service.people().createContact(body={
        "names": [{"givenName": contact['firstname']}],
"emailAddresses": [{"value": contact['email']}],        "phoneNumbers": [{"value": contact['phone']}],
    }).execute()

# def updata_contact(service, firstname, new_phone):
#     results=service.people().connections().list(
#         ressourceName="people/me"
#         personFields="names,phoneNumbers"
#     ).execute()

#     contacts=results.get('connections', [])

#     for contact in contacts:
#         names=contact.get('names', [])
#         phoneNumbers= contact.get('phoneNumbers', [])

#         if names:
#             contact_name=names[0].get("displayName", "")
           

#             if contact_name == firstname:
#                 contact_id=contact["resourceName"]

#                 #mise a jour

#                 updated_contact= {

#                     "phoneNumbers": [{"value":new_phone}]
#                 }

#                 service.people().updateContact(
#                     ressourceName=contact_id,updatePersonFields="phoneNumbers",body=update_body).execute()
                
#                 print(f"Numéro mis à jour pour : {firstname} -> {new_phone}")
#                 return
#     print(f"contact {firstname} non trouvé")

def main():
    """Programme principal."""
    creds = authenticate()
    service = build('people', 'v1', credentials=creds)

    # Exemple de liste de contacts
 

    contacts = [
        


    {"firstname": "400. Bvnd", "email": "bonandombasi@gmail.com", "phone": "0819639862"},




]

    for contact in contacts:
        create_contact(service, contact)
        print(f"Contact ajouté : {contact['firstname']} ")

if __name__ == '__main__':
    main()
