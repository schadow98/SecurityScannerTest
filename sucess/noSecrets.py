import os
from dotenv import load_dotenv

# Lade die Umgebungsvariablen aus der .env Datei
load_dotenv()

# Zugriff auf die Secrets
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')

class SecretManager:
    def __init__(self):
        self.database_url = os.getenv('DATABASE_URL')
        self.api_key = os.getenv('API_KEY')
        self.secret_key = os.getenv('SECRET_KEY')

    def connect_to_database(self):
        print(f"Connecting to database at {self.database_url}")

    def use_api_key(self):
        print(f"Using API key: {self.api_key}")

    def display_secret_key(self):
        print(f"Secret key: {self.secret_key}")

def main():
    secret_manager = SecretManager()
    secret_manager.connect_to_database()
    secret_manager.use_api_key()
    secret_manager.display_secret_key()

if __name__ == "__main__":
    main()
