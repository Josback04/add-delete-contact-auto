import pandas as pd
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Fichier des credentials Google
CLIENT_SECRETS_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/contacts"]

def authenticate_google():
    """Authentifie l'utilisateur via OAuth 2.0"""
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials

def import_contacts(filepath):
    """Lit un fichier Excel et ajoute les contacts à Google Contacts"""
    credentials = authenticate_google()
    service = build("people", "v1", credentials=credentials)

    df = pd.read_excel(filepath)

    for _, row in df.iterrows():
        contact_data = {
            "names": [{"givenName": str(row["Nom"])}],
            "phoneNumbers": [{"value": str(row["Téléphone"])}]
        }

        service.people().createContact(body=contact_data).execute()
        print(f"✅ Contact ajouté : {row['Nom']} ")

if __name__ == "__main__":
    import_contacts("'/Users/josback/Downloads/CONTACTS 18.03.13H.xlsx'")
