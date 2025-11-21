@echo off
echo Installation de l'environnement pour l'atelier IA Agentique...

:: Créer l'environnement virtuel
python -m venv myenv
call myenv\Scripts\activate

:: Installer les packages nécessaires
pip -q install openai requests jupyter notebook tqdm flask load_dotenv google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client  python-dotenv
echo Installation terminée!
echo Pour activer l'environnement: myvenv\Scripts\activate