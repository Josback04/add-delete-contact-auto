from flask import Flask, request, redirect, url_for, session, render_template, flash
import os
import pandas as pd
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json

# Configuration Flask
app = Flask(__name__)
app.secret_key = "secret_key"

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
# Configuration OAuth Google
CLIENT_SECRETS_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/contacts"]
REDIRECT_URI = "http://localhost:5000/callback"

flow = Flow.from_client_secrets_file(
    CLIENT_SECRETS_FILE,
    scopes=SCOPES,
    redirect_uri=REDIRECT_URI
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url(access_type="offline", include_granted_scopes="true", prompt="consent")
    session["state"] = state
    return redirect(authorization_url)

@app.route("/callback")
def callback():
    """Gère la réponse OAuth et stocke les identifiants."""
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    session["credentials"] = credentials.to_json()
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    """Page d'accueil après connexion."""
    return render_template("dashboard.html")

@app.route("/upload", methods=["POST"])
def upload():
    """Gère l'upload du fichier Excel."""
    if "file" not in request.files:
        flash("Aucun fichier sélectionné")
        return redirect(url_for("dashboard"))

    file = request.files["file"]
    if file.filename == "":
        flash("Nom de fichier vide")
        return redirect(url_for("dashboard"))

    if file:
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)
        flash("Fichier importé avec succès")
        import_contacts(filepath)
        return redirect(url_for("dashboard"))

def import_contacts(filepath):
    """Lit un fichier Excel et ajoute les contacts dans Google Contacts."""
    if "credentials" not in session:
        return redirect(url_for("login"))

    credentials = Credentials.from_authorized_user_info(json.loads(session["credentials"]))
    service = build("people", "v1", credentials=credentials)

    df = pd.read_excel(filepath)
    
    for _, row in df.iterrows():
        contact_data = {
            "names": [{"givenName": row["Nom"]}],
            "phoneNumbers": [{"value": str(row["Téléphone"])}]
        }
        service.people().createContact(body=contact_data).execute()

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True, host="0.0.0.0", port=5000)
