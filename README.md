# JubileeJive - Event Planning Extravaganza

A Django-based application that helps event organizers optimize their event planning using the graphical method of linear programming.

## Features

- Interactive budget and cost parameter input
- Capacity limit settings
- Multiple objective selection options
- Visual representation of constraints and optimal solutions
- Detailed numerical results

## Setup Instructions

1. Clone the repository
```bash
git clone <repository-url>
cd JubileeJive
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

Visit http://localhost:8000 to access the application.

## Project Structure

- `core/`: Main Django project configuration
- `events/`: Main application module
  - `templates/`: HTML templates
  - `static/`: CSS, JavaScript, and other static files
  - `models.py`: Data models
  - `views.py`: View logic
  - `forms.py`: Form definitions
  - `utils.py`: Utility functions for calculations

## Usage

1. Enter your event budget
2. Specify cost parameters for guests and entertainment
3. Set capacity limits
4. Choose your optimization objective
5. View the graphical solution and recommendations

## Technologies Used

- Django 5.0.2
- NumPy
- Matplotlib
- Bootstrap 5
- Crispy Forms 