from flask import Flask, request, jsonify, render_template_string
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, timedelta
import json
from decimal import Decimal
app = Flask(__name__)
DB_CONFIG = {
    'host': 'localhost',
    'database': 'healthcare_management',
    'user': '', 
    'password': '',  
    'port': 3306
}
def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def serialize_datetime(obj):
    """JSON serializer for datetime objects"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, timedelta):
        total_seconds = int(obj.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Healthcare Management System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        .section { margin: 20px 0; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
        .form-group { margin: 10px 0; }
        input, select, button { padding: 8px; margin: 5px; }
        button { background-color: #007bff; color: white; border: none; border-radius: 3px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 20px; padding: 10px; background-color: #f8f9fa; border-radius: 3px; }
        pre { white-space: pre-wrap; word-wrap: break-word; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Healthcare Management System</h1>
        
        <!-- Doctors Section -->
        <div class="section">
            <h2>Doctors</h2>
            <div class="form-group">
                <button onclick="getAllDoctors()">Get All Doctors</button>
                <input type="number" id="doctorId" placeholder="Doctor ID">
                <button onclick="getDoctorById()">Get Doctor by ID</button>
            </div>
            <div class="form-group">
                <input type="text" id="doctorSpecialization" placeholder="Specialization">
                <button onclick="getDoctorsBySpecialization()">Get by Specialization</button>
            </div>
            <div id="doctorResult" class="result" style="display:none;"></div>
        </div>

        <!-- Patients Section -->
        <div class="section">
            <h2>Patients</h2>
            <div class="form-group">
                <input type="number" id="patientId" placeholder="Patient ID">
                <button onclick="getPatientById()">Get Patient by ID</button>
            </div>
            <div class="form-group">
                <input type="text" id="patientName" placeholder="Last Name">
                <button onclick="getPatientsByName()">Search by Last Name</button>
            </div>
            <div id="patientResult" class="result" style="display:none;"></div>
        </div>

        <!-- Medical History Section -->
        <div class="section">
            <h2>Medical History</h2>
            <div class="form-group">
                <input type="number" id="historyPatientId" placeholder="Patient ID">
                <button onclick="getMedicalHistory()">Get Medical History</button>
            </div>
            <div class="form-group">
                <input type="number" id="historyDoctorId" placeholder="Doctor ID">
                <button onclick="getMedicalHistoryByDoctor()">Get by Doctor</button>
            </div>
            <div id="historyResult" class="result" style="display:none;"></div>
        </div>

        <!-- Prescriptions Section -->
        <div class="section">
            <h2>Prescriptions</h2>
            <div class="form-group">
                <input type="number" id="prescPatientId" placeholder="Patient ID">
                <button onclick="getPrescriptions()">Get Prescriptions</button>
            </div>
            <div class="form-group">
                <select id="prescStatus">
                    <option value="">All Statuses</option>
                    <option value="Active">Active</option>
                    <option value="Completed">Completed</option>
                    <option value="Discontinued">Discontinued</option>
                </select>
                <button onclick="getPrescriptionsByStatus()">Get by Status</button>
            </div>
            <div id="prescResult" class="result" style="display:none;"></div>
        </div>

        <!-- Appointments Section -->
        <div class="section">
            <h2>Appointments</h2>
            <div class="form-group">
                <input type="number" id="apptPatientId" placeholder="Patient ID">
                <button onclick="getAppointments()">Get Patient Appointments</button>
            </div>
            <div class="form-group">
                <input type="date" id="apptDate" placeholder="Date">
                <button onclick="getAppointmentsByDate()">Get by Date</button>
            </div>
            <div class="form-group">
                <select id="apptStatus">
                    <option value="">All Statuses</option>
                    <option value="Scheduled">Scheduled</option>
                    <option value="Completed">Completed</option>
                    <option value="Cancelled">Cancelled</option>
                    <option value="No-Show">No-Show</option>
                </select>
                <button onclick="getAppointmentsByStatus()">Get by Status</button>
            </div>
            <div id="apptResult" class="result" style="display:none;"></div>
        </div>
    </div>

    <script>
        function showResult(elementId, data) {
            const element = document.getElementById(elementId);
            element.style.display = 'block';
            element.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
        }
        function getAllDoctors() {
            fetch('/api/doctors')
                .then(response => response.json())
                .then(data => showResult('doctorResult', data));
        }

        function getDoctorById() {
            const id = document.getElementById('doctorId').value;
            if (!id) return alert('Please enter Doctor ID');
            fetch(`/api/doctors/${id}`)
                .then(response => response.json())
                .then(data => showResult('doctorResult', data));
        }
        function getDoctorsBySpecialization() {
            const spec = document.getElementById('doctorSpecialization').value;
            if (!spec) return alert('Please enter specialization');
            fetch(`/api/doctors/specialization/${spec}`)
                .then(response => response.json())
                .then(data => showResult('doctorResult', data));
        }

        function getPatientById() {
            const id = document.getElementById('patientId').value;
            if (!id) return alert('Please enter Patient ID');
            fetch(`/api/patients/${id}`)
                .then(response => response.json())
                .then(data => showResult('patientResult', data));
        }

        function getPatientsByName() {
            const name = document.getElementById('patientName').value;
            if (!name) return alert('Please enter last name');
            fetch(`/api/patients/search/${name}`)
                .then(response => response.json())
                .then(data => showResult('patientResult', data));
        }

        function getMedicalHistory() {
            const id = document.getElementById('historyPatientId').value;
            if (!id) return alert('Please enter Patient ID');
            fetch(`/api/medical-history/patient/${id}`)
                .then(response => response.json())
                .then(data => showResult('historyResult', data));
        }

        function getMedicalHistoryByDoctor() {
            const id = document.getElementById('historyDoctorId').value;
            if (!id) return alert('Please enter Doctor ID');
            fetch(`/api/medical-history/doctor/${id}`)
                .then(response => response.json())
                .then(data => showResult('historyResult', data));
        }

        function getPrescriptions() {
            const id = document.getElementById('prescPatientId').value;
            if (!id) return alert('Please enter Patient ID');
            fetch(`/api/prescriptions/patient/${id}`)
                .then(response => response.json())
                .then(data => showResult('prescResult', data));
        }

        function getPrescriptionsByStatus() {
            const status = document.getElementById('prescStatus').value;
            if (!status) return alert('Please select a status');
            fetch(`/api/prescriptions/status/${status}`)
                .then(response => response.json())
                .then(data => showResult('prescResult', data));
        }
        function getAppointments() {
            const id = document.getElementById('apptPatientId').value;
            if (!id) return alert('Please enter Patient ID');
            fetch(`/api/appointments/patient/${id}`)
                .then(response => response.json())
                .then(data => showResult('apptResult', data));
        }

        function getAppointmentsByDate() {
            const date = document.getElementById('apptDate').value;
            if (!date) return alert('Please select a date');
            fetch(`/api/appointments/date/${date}`)
                .then(response => response.json())
                .then(data => showResult('apptResult', data));
        }

        function getAppointmentsByStatus() {
            const status = document.getElementById('apptStatus').value;
            if (!status) return alert('Please select a status');
            fetch(`/api/appointments/status/${status}`)
                .then(response => response.json())
                .then(data => showResult('apptResult', data));
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    """Main interface"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/doctors', methods=['GET'])
def get_all_doctors():
    """Get all doctors"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM doctors ORDER BY last_name, first_name")
        doctors = cursor.fetchall()
        return jsonify(doctors)
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor_by_id(doctor_id):
    """Get doctor by ID"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500  
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM doctors WHERE doctor_id = %s", (doctor_id,))
        doctor = cursor.fetchone()
        if doctor:
            return jsonify(doctor)
        else:
            return jsonify({'error': 'Doctor not found'}), 404
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
@app.route('/api/doctors/specialization/<string:specialization>', methods=['GET'])
def get_doctors_by_specialization(specialization):
    """Get doctors by specialization"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM doctors WHERE specialization LIKE %s ORDER BY last_name, first_name", 
                      (f"%{specialization}%",))
        doctors = cursor.fetchall()
        return jsonify(doctors)
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
@app.route('/api/patients/<int:patient_id>', methods=['GET'])
def get_patient_by_id(patient_id):
    """Get patient by ID"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patients WHERE patient_id = %s", (patient_id,))
        patient = cursor.fetchone()
        if patient:
            return jsonify(json.loads(json.dumps(patient, default=serialize_datetime)))
        else:
            return jsonify({'error': 'Patient not found'}), 404
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
@app.route('/api/patients/search/<string:name>', methods=['GET'])
def get_patients_by_name(name):
    """Search patients by last name"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patients WHERE last_name LIKE %s ORDER BY last_name, first_name", 
                      (f"%{name}%",))
        patients = cursor.fetchall()
        return jsonify(json.loads(json.dumps(patients, default=serialize_datetime)))
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
@app.route('/api/medical-history/patient/<int:patient_id>', methods=['GET'])
def get_medical_history_by_patient(patient_id):
    """Get medical history by patient ID"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT mh.*, 
               CONCAT(d.first_name, ' ', d.last_name) as doctor_name,
               d.specialization
        FROM medical_history mh
        JOIN doctors d ON mh.doctor_id = d.doctor_id
        WHERE mh.patient_id = %s
        ORDER BY mh.visit_date DESC, mh.visit_time DESC
        """
        cursor.execute(query, (patient_id,))
        history = cursor.fetchall()
        return jsonify(json.loads(json.dumps(history, default=serialize_datetime)))
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
@app.route('/api/medical-history/doctor/<int:doctor_id>', methods=['GET'])
def get_medical_history_by_doctor(doctor_id):
    """Get medical history by doctor ID"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT mh.*, 
               CONCAT(p.first_name, ' ', p.last_name) as patient_name,
               p.date_of_birth, p.gender
        FROM medical_history mh
        JOIN patients p ON mh.patient_id = p.patient_id
        WHERE mh.doctor_id = %s
        ORDER BY mh.visit_date DESC, mh.visit_time DESC
        """
        cursor.execute(query, (doctor_id,))
        history = cursor.fetchall()
        return jsonify(json.loads(json.dumps(history, default=serialize_datetime)))
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
@app.route('/api/prescriptions/patient/<int:patient_id>', methods=['GET'])
def get_prescriptions_by_patient(patient_id):
    """Get prescriptions by patient ID"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT p.*, 
               CONCAT(d.first_name, ' ', d.last_name) as doctor_name,
               d.specialization
        FROM prescriptions p
        JOIN doctors d ON p.doctor_id = d.doctor_id
        WHERE p.patient_id = %s
        ORDER BY p.prescription_date DESC
        """
        cursor.execute(query, (patient_id,))
        prescriptions = cursor.fetchall()
        return jsonify(json.loads(json.dumps(prescriptions, default=serialize_datetime)))
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
@app.route('/api/prescriptions/status/<string:status>', methods=['GET'])
def get_prescriptions_by_status(status):
    """Get prescriptions by status"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT p.*, 
               CONCAT(pat.first_name, ' ', pat.last_name) as patient_name,
               CONCAT(d.first_name, ' ', d.last_name) as doctor_name
        FROM prescriptions p
        JOIN patients pat ON p.patient_id = pat.patient_id
        JOIN doctors d ON p.doctor_id = d.doctor_id
        WHERE p.status = %s
        ORDER BY p.prescription_date DESC
        """
        cursor.execute(query, (status,))
        prescriptions = cursor.fetchall()
        return jsonify(json.loads(json.dumps(prescriptions, default=serialize_datetime)))
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
@app.route('/api/appointments/patient/<int:patient_id>', methods=['GET'])
def get_appointments_by_patient(patient_id):
    """Get appointments by patient ID"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT a.*, 
               CONCAT(d.first_name, ' ', d.last_name) as doctor_name,
               d.specialization
        FROM appointments a
        JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE a.patient_id = %s
        ORDER BY a.appointment_date DESC, a.appointment_time DESC
        """
        cursor.execute(query, (patient_id,))
        appointments = cursor.fetchall()
        return jsonify(json.loads(json.dumps(appointments, default=serialize_datetime)))
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
@app.route('/api/appointments/date/<string:date>', methods=['GET'])
def get_appointments_by_date(date):
    """Get appointments by date"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT a.*, 
               CONCAT(p.first_name, ' ', p.last_name) as patient_name,
               CONCAT(d.first_name, ' ', d.last_name) as doctor_name,
               d.specialization
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE a.appointment_date = %s
        ORDER BY a.appointment_time
        """
        cursor.execute(query, (date,))
        appointments = cursor.fetchall()
        return jsonify(json.loads(json.dumps(appointments, default=serialize_datetime)))
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/appointments/status/<string:status>', methods=['GET'])
def get_appointments_by_status(status):
    """Get appointments by status"""
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT a.*, 
               CONCAT(p.first_name, ' ', p.last_name) as patient_name,
               CONCAT(d.first_name, ' ', d.last_name) as doctor_name,
               d.specialization
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE a.status = %s
        ORDER BY a.appointment_date DESC, a.appointment_time DESC
        """
        cursor.execute(query, (status,))
        appointments = cursor.fetchall()
        return jsonify(json.loads(json.dumps(appointments, default=serialize_datetime)))
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)