**Healthcare Management System**

A comprehensive healthcare management system built with Flask and MySQL for managing patient records, appointments, prescriptions, and medical history with a user-friendly web interface.

🚀 Features 

👨‍⚕️ Doctor Management

1.View all doctors

2.Search doctors by ID

3.Filter doctors by specialization

4.Complete doctor profiles with contact information


👥 Patient Management

1.Search patients by ID

2.Find patients by last name

3.Comprehensive patient profiles with medical information

4.Emergency contact details and allergy tracking


📋 Medical History

1.Complete patient medical history tracking

2.Visit records with detailed diagnosis and symptoms

3.Vital signs storage (JSON format)

4.Treatment and medication tracking

5.Doctor-patient visit relationships


💊 Prescription Management

1.Patient-specific prescription tracking

2.Medication details with dosage and frequency

3.Prescription status monitoring (Active/Completed/Discontinued)

4.Refill tracking and instructions

📅 Appointment System

1.Patient appointment scheduling

2.Appointment status tracking (Scheduled/Completed/Cancelled/No-Show)

3.Date-based appointment viewing

4.Doctor-patient appointment relationships

🛠️ Tech Stack

1.Backend: Python Flask

2.Database: MySQL

3.Frontend: HTML, CSS, JavaScript

4.Database Connector: mysql-connector-python


📋 Prerequisites

Python 3.7+

MySQL Server

pip (Python package installer)

🔧 Installation

1.Clone the repository

a) bashgit clone https://github.com/Megaultron19/healthcare-management-system.git

b) cd healthcare-management-system

2.Install required packages

a) bashpip install flask mysql-connector-python

3.Set up MySQL Database

a) sqlCREATE DATABASE healthcare_management;

4.Run the database schema

a) Execute the SQL commands from database_schema.sql to create tables

b) Optionally, run sample_data.sql to populate with test data


4.Configure Database Connection

a) Open app.py

b) Update the DB_CONFIG section with your MySQL credentials:

c) pythonDB_CONFIG = {

    'host': 'localhost',
    
    'database': 'healthcare_management',
    
    'user': 'your_username',
    
    'password': 'your_password',
    
    'port': 3306
    
}


5.Run the application

a) python app.py

6.Access the application

a) Open your browser and navigate to: http://localhost:5000

🖥️ Usage

a) Web Interface

b) Navigate to http://localhost:5000 for the main dashboard

c) Use the intuitive interface to search and manage healthcare data

d) Each section provides specific functionality for different data types


API Endpoints

1. Doctors
   
a)GET /api/doctors - Get all doctors

b)GET /api/doctors/{id} - Get doctor by ID

c)GET /api/doctors/specialization/{specialization} - Get doctors by specialization


2. Patients

a)GET /api/patients/{id} - Get patient by ID

b)GET /api/patients/search/{name} - Search patients by last name


3. Medical History

a)GET /api/medical-history/patient/{patient_id} - Get patient's medical history

b)GET /api/medical-history/doctor/{doctor_id} - Get medical history by doctor


4. Prescriptions
   
a)GET /api/prescriptions/patient/{patient_id} - Get patient's prescriptions

b)GET /api/prescriptions/status/{status} - Get prescriptions by status


5. Appointments
   
a)GET /api/appointments/patient/{patient_id} - Get patient's appointments

b)GET /api/appointments/date/{date} - Get appointments by date

c)GET /api/appointments/status/{status} - Get appointments by status


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

## ⚠️ Security Notice

This repository contains SAMPLE DATA ONLY for development purposes.

- All patient information is fictional
  
- Do not use in production without proper security review


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

