# Event Registration System

## Overview
An Event Registration System is a software solution designed to facilitate the process of managing registrations for various events, activities, or gatherings. It provides a centralized platform for both event organizers and participants, streamlining the registration process, managing attendee information, and ensuring a smooth and organized experience for all involved.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Configuration](#configuration)

## Features
- User Registration and Authentication
- Event creation only for superuser
- Event Registration, Event Unregister, Own Event show, Event slot etc For authenticate user
- Event Filtering
- Admin Can change create Event from Django Admin

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Python (3.8) installed on your system.
- Virtual environment set up with python 3.8


## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/amirhamjacse/event_registration_system
   cd event_registration_system
   python -m venv venv
   source venv/bin/activate  
   # On Windows, use 'venv\Scripts\activate'

Install project dependencies:
- pip install -r requirements.txt
- Create a PostgreSQL database and configure the project's .env file. You can use the provided .env.example as a template, You have to copy .env.example and remove .example.

Apply database migrations:
- python manage.py migrate

Create a superuser for admin access (optional):
- python manage.py createsuperuser

Load the fixture (sample data):
- Go to this Location event_manager/fixtures/event_register_fixture.json
- all user password is '@Event123'
- admin email after load fixture admin@example.com, password: '@123adminxyz
- python manage.py loaddata Event_register_fixture

Run the development server:
- python manage.py runserver

- Access the application in your web browser at http://localhost:8000/.


## Usage
- Register a new user account or log in with existing credentials.
- Manage your Regitered Event through the user dashboard.
- Use the filter options to organize your Event efficiently.
- Log out when you're done.

## API
Run the development server:
- python manage.py runserver
- API Documentation Link: http://localhost:8000/swagger/

## Configuration
Customize project settings in settings.py, such as email settings, and more.