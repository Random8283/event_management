# Event Management System

A Django-based event management system that allows users to create, manage, and register for events.

## Features

- User authentication and authorization
- Event creation and management
- Event registration and deregistration
- Event categories and filtering
- Admin dashboard for event management
- User registration management

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repo-url>
cd event-management
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```
6. Load dummy events
We’ve included sample events for testing!
```bash
python manage.py loaddata fixtures/dummy_events.json


7. Run the development server:
```bash
python manage.py runserver
```

8. Access the application at `http://127.0.0.1:8000/`

## Project Structure

- `events/` - Main application directory
  - `models.py` - Database models
  - `views.py` - View functions and classes
  - `urls.py` - URL routing
  - `forms.py` - Form definitions
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, JS, images)
  - `templatetags/` - Custom template tags

- Any user who signs up can view ALL events.
- Any user can register for ANY event, regardless of organizer.
- Admin users (staff=True) can create, update, delete events.


## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

📝 Notes
Dummy events’ organizer is set to user ID 1 (first superuser created)

You can see loaded events in Django admin → Events section

Static files collected in /staticfiles/ (run python manage.py collectstatic if needed for deployment)




## License

This project is licensed under the MIT License - see the LICENSE file for details. 