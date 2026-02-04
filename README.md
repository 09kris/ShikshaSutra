# ShikshaSutra - College Management System

A comprehensive web-based College Management System built with Django and Python.

## Features

- **Student Management**: Add, update, view, and manage student records
- **Faculty Management**: Manage teacher profiles and assignments
- **Course Management**: Handle courses, subjects, and academic structure
- **Attendance Tracking**: Digital attendance marking and reporting
- **Results Management**: Exam creation, result entry, and grade calculation
- **Role-based Access**: Admin, Teacher, and Student login with appropriate permissions
- **Responsive Design**: Mobile-friendly interface using Bootstrap

## Installation

1. **Clone or download the project**
   ```
   cd "sisa sutra"
   ```

2. **Create virtual environment**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```
   python manage.py runserver
   ```

7. **Access the application**
   - Open browser and go to: http://127.0.0.1:8000
   - Admin panel: http://127.0.0.1:8000/admin

## Default Login Credentials

After creating sample data:
- **Admin**: Use superuser credentials
- **Students**: Password is 'student123'
- **Faculty**: Password is 'faculty123'

## Project Structure

```
shiksha_sutra/
├── shiksha_sutra/
│   ├── apps/
│   │   ├── accounts/     # User authentication
│   │   ├── students/     # Student management
│   │   ├── faculty/      # Faculty management
│   │   ├── courses/      # Course management
│   │   ├── attendance/   # Attendance tracking
│   │   └── results/      # Results management
│   ├── settings.py
│   └── urls.py
├── templates/            # HTML templates
├── static/              # CSS, JS, images
├── media/               # User uploads
└── manage.py
```

## Usage

1. **Admin Functions**:
   - Add departments, courses, and subjects
   - Register students and faculty
   - View reports and analytics

2. **Faculty Functions**:
   - Mark attendance
   - Enter exam results
   - View student performance

3. **Student Functions**:
   - View personal profile
   - Check attendance records
   - View exam results

## Technologies Used

- **Backend**: Django 4.2, Python
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (default), can be changed to PostgreSQL/MySQL
- **Authentication**: Django's built-in authentication system

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes.