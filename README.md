# Lab Tech Project

Lab Tech is a Django-based web application that allows users to book appointments for various hospital-related services.
It streamlines the process of scheduling lab tests and hospital visits, making healthcare more accessible and organized.

## 🔧 Technologies Used

- Backend: Python, Django
- Frontend: HTML, CSS, Bootstrap (if applicable)
- Database: SQLite (default), easily configurable to PostgreSQL or MySQL
- Tools: Git, Django Admin

## 💡 Features

-  View available hospital services
-  Book appointments for lab tests and consultations
-  Secure login/logout functionality
-  Admin dashboard to manage users, services, and appointments
-  Unit testing for key features

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (recommended)

### Installation
```bash
# Clone the repository
git clone https://github.com/SaroJamdr/Lab_Tech_Project.git
cd Lab_Tech_Project

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
