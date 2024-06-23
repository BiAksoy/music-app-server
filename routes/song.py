import uuid
import cloudinary.uploader
from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session
from config import CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET, CLOUDINARY_CLOUD_NAME
from database import get_db
from middleware.auth_middleware import auth_middleware
import cloudinary
from cloudinary.uploader import upload

from models.song import Song

router = APIRouter()

cloudinary.config( 
    cloud_name = CLOUDINARY_CLOUD_NAME,
    api_key = CLOUDINARY_API_KEY,
    api_secret = CLOUDINARY_API_SECRET,
    secure=True
)

@router.post('/upload', status_code=201)
def upload_song(song: UploadFile=File(...),
                thumbnail: UploadFile=File(...),
                artist: str=Form(...),
                song_name: str=Form(...),
                hex_code: str=Form(...),
                db: Session=Depends(get_db),
                auth_dict=Depends(auth_middleware)):
    
    song_id = str(uuid.uuid4())
    song_res = cloudinary.uploader.upload(song.file, resource_type='auto', folder=f'songs/{song_id}')
    thumbnail_res = cloudinary.uploader.upload(thumbnail.file, resource_type='image', folder=f'songs/{song_id}')

    new_song = Song(
        id=song_id,
        artist=artist,
        song_name=song_name,
        hex_code=hex_code,
        song_url=song_res['url'],
        thumbnail_url=thumbnail_res['url'],
    )

    db.add(new_song)
    db.commit()
    db.refresh(new_song)

    return new_song
