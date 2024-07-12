# Music App API

This is a music app API that allows users to authenticate and manage their songs. It is built using FastAPI and PostgreSQL. This backend is for the frontend available [here](https://github.com/BiAksoy/music-app-client).

## Getting Started

### Requirements

- Python 3.8 or higher
- PostgreSQL
- [Cloudinary](https://cloudinary.com) account

### Installation

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add the following environment variables:

   ```bash
   DATABASE_URL=postgresql://user:password@localhost/dbname
   JWT_SECRET_KEY=secret
   CLOUDINARY_CLOUD_NAME=cloud_name
   CLOUDINARY_API_KEY=api_key
   CLOUDINARY_API_SECRET=api_secret
   ```

4. Ensure PostgreSQL is running.

5. Start the server:

   ```bash
   fastapi dev main.py
   ```

## API Documentation

### User Endpoints

#### POST /auth/signup

- **Description:** Register a new user.
- **Body Parameters:**
  - `name` (string, required): The user's full name.
  - `email` (string, required): The user's email address.
  - `password` (string, required): The user's password.

#### POST /auth/login

- **Description:** Login a user.
- **Body Parameters:**
  - `email` (string, required): The user's email address.
  - `password` (string, required): The user's password.

#### GET /auth/

- **Description:** Get the current user profile.
- **Headers:**
  - `Authorization`: Bearer `<token>`

### Song Endpoints

#### POST /song/upload

- **Description:** Upload a new song.
- **Headers:**
  - `Authorization`: Bearer `<token>`
- **Form Parameters:**
  - `song` (file, required): The audio file of the song.
  - `thumbnail` (file, required): The thumbnail image for the song.
  - `artist` (string, required): The artist's name.
  - `song_name` (string, required): The name of the song.
  - `hex_code` (string, required): Color code associated with the song.

#### GET /song/list

- **Description:** Get a list of all songs.
- **Headers:**
  - `Authorization`: Bearer `<token>`

#### POST /song/favorite

- **Description:** Favorite or unfavorite a song.
- **Headers:**
  - `Authorization`: Bearer `<token>`
- **Body Parameters:**
  - `song_id` (string, required): The ID of the song to favorite/unfavorite.

#### GET /song/list/favorites

- **Description:** Get the list of favorite songs for the current user.
- **Headers:**
  - `Authorization`: Bearer `<token>`
