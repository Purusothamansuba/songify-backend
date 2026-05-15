# Songify Backend

A scalable Django REST API backend for the **Songify** music streaming platform.  
This backend manages songs, playlists, likes, listening history, and Supabase integration for storage and database services.

---

## Features

- REST API built with Django REST Framework
- Song management system
- Playlist creation and management
- Like system
- Listening history tracking
- Supabase integration
- Django Admin panel
- Production-ready deployment configuration
- Static files support
- Modular Django app structure

---

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework

### Database & Storage
- Supabase

### Deployment
- Gunicorn
- Procfile support
- Runtime configuration

---

## Project Structure

```bash
songify/
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── songify/                 # Main Django project
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── songs/                   # Songs application
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── supabase_client.py
│   └── migrations/
│
└── staticfiles/             # Collected static files
