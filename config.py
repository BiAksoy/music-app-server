from dotenv import load_dotenv
import os

load_dotenv()

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET')
