**Healthcare Management System**
A comprehensive healthcare management system built with Flask and MySQL for managing patient records, appointments, prescriptions, and medical history with a user-friendly web interface.

🚀 Features 

👨‍⚕️ Doctor Management

View all doctors

Search doctors by ID

Filter doctors by specialization

Complete doctor profiles with contact information


👥 Patient Management

Search patients by ID

Find patients by last name

Comprehensive patient profiles with medical information

Emergency contact details and allergy tracking


📋 Medical History

Complete patient medical history tracking

Visit records with detailed diagnosis and symptoms

Vital signs storage (JSON format)

Treatment and medication tracking

Doctor-patient visit relationships


💊 Prescription Management

Patient-specific prescription tracking

Medication details with dosage and frequency

Prescription status monitoring (Active/Completed/Discontinued)

Refill tracking and instructions

📅 Appointment System

Patient appointment scheduling

Appointment status tracking (Scheduled/Completed/Cancelled/No-Show)

Date-based appointment viewing

Doctor-patient appointment relationships

🛠️ Tech Stack

Backend: Python Flask

Database: MySQL

Frontend: HTML, CSS, JavaScript

Database Connector: mysql-connector-python


📋 Prerequisites

Python 3.7+

MySQL Server

pip (Python package installer)

🔧 Installation

1.Clone the repository

bashgit clone https://github.com/yourusername/healthcare-management-system.git

cd healthcare-management-system

2.Install required packages

bashpip install flask mysql-connector-python

3.Set up MySQL Database

sqlCREATE DATABASE healthcare_management;

4.Run the database schema

Execute the SQL commands from database_schema.sql to create tables

Optionally, run sample_data.sql to populate with test data


4.Configure Database Connection

Open app.py

Update the DB_CONFIG section with your MySQL credentials:

pythonDB_CONFIG = {

    'host': 'localhost',
    
    'database': 'healthcare_management',
    
    'user': 'your_username',
    
    'password': 'your_password',
    
    'port': 3306
    
}


5.Run the application

python app.py

6.Access the application

Open your browser and navigate to: http://localhost:5000

🖥️ Usage

Web Interface

Navigate to http://localhost:5000 for the main dashboard

Use the intuitive interface to search and manage healthcare data

Each section provides specific functionality for different data types


API Endpoints

Doctors
GET /api/doctors - Get all doctors
GET /api/doctors/{id} - Get doctor by ID
GET /api/doctors/specialization/{specialization} - Get doctors by specialization

Patients
GET /api/patients/{id} - Get patient by ID
GET /api/patients/search/{name} - Search patients by last name

Medical History
GET /api/medical-history/patient/{patient_id} - Get patient's medical history
GET /api/medical-history/doctor/{doctor_id} - Get medical history by doctor

Prescriptions
GET /api/prescriptions/patient/{patient_id} - Get patient's prescriptions
GET /api/prescriptions/status/{status} - Get prescriptions by status

Appointments
GET /api/appointments/patient/{patient_id} - Get patient's appointments
GET /api/appointments/date/{date} - Get appointments by date
GET /api/appointments/status/{status} - Get appointments by status

The system uses the following main tables:
1.doctors - Doctor information and specializations
2.patients - Patient demographics and medical info
3.medical_history - Visit records and diagnoses
4.prescriptions - Medication prescriptions and tracking
5.appointments - Appointment scheduling and status


🤝 Contributing
1.Fork the repository
2.Create a feature branch (git checkout -b feature/AmazingFeature)
3.Commit your changes (git commit -m 'Add some AmazingFeature')
4.Push to the branch (git push origin feature/AmazingFeature)
5.Open a Pull Request

👨‍💻 Author
Harshit Singh
GitHub:Megaultron19 
Email:harshitkatiyar2003@gmail.com

Acknowledgments
Flask documentation and community
MySQL documentation
Healthcare industry standards and practices

📞 Support
If you encounter any issues or have questions:
1.Create a new issue with detailed information
2.Contact the maintainer
