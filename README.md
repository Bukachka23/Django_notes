# Django Notes Application
This is a simple yet powerful note-taking application built with Django and the Django Ninja REST framework. It allows users to create, read, update, and delete notes. Notes can be grouped by categories for better organization.

## Features
- Create, read, update, and delete notes
- Organize notes by categories
- RESTful API for managing notes and categories
- Getting Started
- These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- Django Ninja 0.9 or higher

### Installing
- Clone the repository to your local machine:

- git clone https://github.com/yourusername/django-notes.git
- Change into the project directory:

- cd django-notes

### Set up a Python virtual environment and activate it:

- python3 -m venv venv
- source venv/bin/activate

### Install the required dependencies:

- pip install -r requirements.txt
- Running the Application

### To run the application locally:

- python manage.py runserver
- The application will be available at http://localhost:8000/.

## Running the Tests
- To run the tests for the application:

- python manage.py test

## Usage
- Visit http://localhost:8000/ to view the note-taking application. Notes can be created, viewed, updated, and deleted. They can be organized by categories.

- The RESTful API is available at http://localhost:8000/api/. It provides endpoints for managing notes and categories.

## Contributing
- If you want to contribute to this project and make it better, your help is very welcome. Please open an issue first to discuss what you would like to change.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.
