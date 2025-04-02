# people_list_project
# People List Project

This is a simple Django web application for managing and displaying a list of people. The application retrieves entries from a database and renders them on a web page using Django’s template engine.

## Features

- View a list of people with their name, age, and email
- Rendered using Django views and templates
- Clean project structure following Django best practices
- Easily extendable for add/edit/delete functionality

## Tech Stack

- Python 3
- Django
- SQLite (default development database)

## Project Structure


people_list_project/
├── app/                     # Django app with models, views, templates, and URLs
│   ├── templates/app/       # HTML templates
│   └── migrations/          # Django migrations
├── view_project/            # Project-level settings and URLs
├── db.sqlite3               # SQLite database
├── manage.py                # Django’s command-line utility
└── requirements.txt         # Python dependencies

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/starksimaging/people_list_project.git
cd people_list_project