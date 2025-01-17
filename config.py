import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='configs/.env')

sheet_id = os.getenv('SHEET_ID')
folder_name = os.getenv('FOLDER_NAME')
drive_id = os.getenv('DRIVE_ID')
