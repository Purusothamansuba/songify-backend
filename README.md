# Songify Backend

A scalable Django REST API backend for the **Songify** music streaming platform.  
This backend manages songs, playlists, likes, listening history, and Supabase integration for cloud storage and database services.

---

# Live API

```bash
https://songify-backend-3nly.onrender.com/api/songs/
```

---

# Features

- Django REST API backend
- Song management system
- Playlist support
- Like system
- Listening history tracking
- Supabase integration
- Production-ready deployment
- RESTful API architecture
- Django Admin support
- Static file handling

---

# Tech Stack

## Backend
- Python
- Django
- Django REST Framework

## Database & Storage
- Supabase

## Deployment
- Vercel
- Render
- Gunicorn

---

# Deployment Architecture

| Service | Usage |
|---|---|
| Vercel | Frontend Hosting |
| Render | Django Backend Hosting |
| Supabase | Database & File Storage |

---

# Project Structure

```bash
songify/
├── Procfile
├── manage.py
├── requirements.txt
├── runtime.txt
│
├── songify/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── songs/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── supabase_client.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
└── staticfiles/
```

---

# API Functionalities

## Songs
- Add songs
- Fetch songs
- Update songs
- Delete songs

## Playlists
- Create playlists
- Add/remove songs
- Retrieve playlist data

## Likes
- Like songs
- Store liked songs

## History
- Track listening history
- Retrieve recently played songs

---

# API Endpoint

## Get All Songs

```http
GET /api/songs/
```

Example:

```bash
https://songify-backend-3nly.onrender.com/api/songs/
```

---

# Example Song Object

```json
{
  "title": "Blinding Lights",
  "artist": "The Weeknd",
  "image_url": "https://example.com/image.jpg",
  "audio_url": "https://example.com/audio.mp3"
}
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Purusothamansuba/songify-backend.git
cd songify-backend
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Environment

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SECRET_KEY=your_django_secret_key
DEBUG=True
```

---

# Database Migration

```bash
python manage.py migrate
```

---

# Run Development Server

```bash
python manage.py runserver
```

Server:

```bash
http://127.0.0.1:8000/
```

---

# Django Admin

## Create Superuser

```bash
python manage.py createsuperuser
```

## Admin Panel

```bash
http://127.0.0.1:8000/admin/
```

---

# Production Deployment

## Render Deployment

Backend deployed using Render with:

- Gunicorn
- Procfile
- Static file collection
- Runtime configuration

Run manually:

```bash
gunicorn songify.wsgi
```

---

# Future Improvements

- JWT Authentication
- AI-based music recommendations
- Audio streaming optimization
- Search and filtering
- User authentication
- Recommendation engine
- Real-time analytics
- User following system
- Playlist collaboration

---

# Author

## Purushothaman

- Computer Science Engineering Student
- AI & Robotics Enthusiast
- Backend Developer
- Systems Programming Enthusiast

---

# License

This project is licensed under the MIT License.
