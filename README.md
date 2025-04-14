# JubileeJive - Event Planning Optimization Platform

A professional event planning optimization platform that uses linear programming to help users make data-driven decisions for their events.

## Features

- Event planning optimization using linear programming
- Graphical method visualization
- Budget allocation optimization
- Minimum requirements for guests and entertainment
- Modern, responsive UI
- Professional design with indigo and cyan theme

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/JubileeJive.git
cd JubileeJive
```

2. Create and activate a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Deployment

### Prerequisites
- Python 3.8+
- PostgreSQL (recommended for production)
- Gunicorn
- WhiteNoise

### Steps

1. Set up your production environment variables:
```bash
DEBUG=False
DJANGO_SECRET_KEY=your-secure-secret-key
ALLOWED_HOSTS=your-domain.com
```

2. Collect static files:
```bash
python manage.py collectstatic
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the production server:
```bash
gunicorn core.wsgi
```

### Using Docker

1. Build the Docker image:
```bash
docker build -t jubileejive .
```

2. Run the container:
```bash
docker run -p 8000:8000 jubileejive
```

## Project Structure

```
JubileeJive/
├── core/                 # Django project settings
├── events/              # Main application
├── static/              # Static files
├── templates/           # HTML templates
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

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