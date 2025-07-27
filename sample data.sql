
USE healthcare_management;


INSERT INTO doctors (first_name, last_name, specialization, phone, email, department) VALUES
('John', 'Smith', 'Cardiology', '555-0101', 'john.smith@hospital.com', 'Cardiac Care'),
('Sarah', 'Johnson', 'Pediatrics', '555-0102', 'sarah.johnson@hospital.com', 'Pediatric Care'),
('Michael', 'Brown', 'Orthopedics', '555-0103', 'michael.brown@hospital.com', 'Orthopedic Surgery'),
('Emily', 'Davis', 'Dermatology', '555-0104', 'emily.davis@hospital.com', 'Dermatology'),
('Robert', 'Wilson', 'Neurology', '555-0105', 'robert.wilson@hospital.com', 'Neurology'),
('Lisa', 'Anderson', 'Gynecology', '555-0106', 'lisa.anderson@hospital.com', 'Women\'s Health'),
('David', 'Taylor', 'General Medicine', '555-0107', 'david.taylor@hospital.com', 'General Medicine'),
('Jennifer', 'Thomas', 'Psychiatry', '555-0108', 'jennifer.thomas@hospital.com', 'Mental Health'),
('James', 'Martinez', 'Ophthalmology', '555-0109', 'james.martinez@hospital.com', 'Eye Care'),
('Maria', 'Garcia', 'Endocrinology', '555-0110', 'maria.garcia@hospital.com', 'Endocrinology');


INSERT INTO patients (first_name, last_name, date_of_birth, gender, phone, email, address, emergency_contact_name, blood_group, allergies) VALUES
('Alice', 'Cooper', '1985-03-15', 'Female', '555-1001', 'alice.cooper@email.com', '123 Main St, City, State 12345', 'Bob Cooper', 'A+', 'Penicillin'),
('Bob', 'Williams', '1992-07-22', 'Male', '555-1002', 'bob.williams@email.com', '456 Oak Ave, City, State 12345', 'Mary Williams', 'O-', 'None'),
('Catherine', 'Jones', '1978-11-08', 'Female', '555-1003', 'catherine.jones@email.com', '789 Pine Rd, City, State 12345', 'Tom Jones', 'B+', 'Shellfish'),
('Daniel', 'Miller', '1995-01-30', 'Male', '555-1004', 'daniel.miller@email.com', '321 Elm St, City, State 12345', 'Susan Miller', 'AB+', 'Peanuts'),
('Eva', 'Moore', '1988-09-12', 'Female', '555-1005', 'eva.moore@email.com', '654 Maple Dr, City, State 12345', 'John Moore', 'A-', 'Latex'),
('Frank', 'Clark', '1970-05-25', 'Male', '555-1006', 'frank.clark@email.com', '987 Cedar Ln, City, State 12345', 'Helen Clark', 'O+', 'None'),
('Grace', 'Lewis', '1983-12-03', 'Female', '555-1007', 'grace.lewis@email.com', '147 Birch Ave, City, State 12345', 'Mark Lewis', 'B-', 'Sulfa drugs'),
('Henry', 'Walker', '1991-04-18', 'Male', '555-1008', 'henry.walker@email.com', '258 Spruce St, City, State 12345', 'Linda Walker', 'AB-', 'None'),
('Iris', 'Hall', '1976-08-07', 'Female', '555-1009', 'iris.hall@email.com', '369 Willow Rd, City, State 12345', 'Paul Hall', 'A+', 'Aspirin'),
('Jack', 'Young', '1989-10-14', 'Male', '555-1010', 'jack.young@email.com', '741 Poplar Dr, City, State 12345', 'Nancy Young', 'O-', 'Iodine');


INSERT INTO medical_history (patient_id, doctor_id, visit_date, visit_time, chief_complaint, diagnosis, symptoms, vital_signs, treatment_provided, notes, follow_up_date) VALUES
(1, 1, '2024-01-15', '09:30:00', 'Chest pain', 'Angina', 'Chest tightness, shortness of breath', '{"blood_pressure": "140/90", "temperature": "98.6", "pulse": "85", "oxygen_saturation": "98%"}', 'Prescribed nitroglycerin, lifestyle changes recommended', 'Patient responded well to treatment', '2024-02-15'),
(2, 2, '2024-01-20', '14:15:00', 'Fever and cough', 'Upper respiratory infection', 'Fever, persistent cough, runny nose', '{"blood_pressure": "120/80", "temperature": "101.2", "pulse": "95", "oxygen_saturation": "97%"}', 'Antibiotics and rest', 'Symptoms improving', '2024-02-03'),
(3, 3, '2024-01-25', '11:00:00', 'Knee pain', 'Osteoarthritis', 'Joint pain, stiffness', '{"blood_pressure": "130/85", "temperature": "98.4", "pulse": "78", "oxygen_saturation": "99%"}', 'Physical therapy, anti-inflammatory medication', 'Continue PT exercises', '2024-03-25'),
(4, 4, '2024-02-01', '16:30:00', 'Skin rash', 'Eczema', 'Itchy, red patches on arms', '{"blood_pressure": "125/82", "temperature": "98.8", "pulse": "72", "oxygen_saturation": "98%"}', 'Topical steroids, moisturizers', 'Rash clearing up', '2024-02-29'),
(5, 5, '2024-02-05', '10:45:00', 'Headaches', 'Migraine', 'Severe headaches, light sensitivity', '{"blood_pressure": "135/88", "temperature": "98.2", "pulse": "68", "oxygen_saturation": "99%"}', 'Migraine medication, trigger avoidance', 'Patient education provided', '2024-03-05'),
(6, 6, '2024-02-10', '13:20:00', 'Annual checkup', 'Routine examination', 'None', '{"blood_pressure": "118/75", "temperature": "98.6", "pulse": "65", "oxygen_saturation": "99%"}', 'Routine screening tests ordered', 'All normal', '2025-02-10'),
(7, 7, '2024-02-15', '08:00:00', 'Fatigue', 'Iron deficiency anemia', 'Weakness, fatigue, pale skin', '{"blood_pressure": "110/70", "temperature": "98.3", "pulse": "88", "oxygen_saturation": "97%"}', 'Iron supplements, dietary changes', 'Lab work pending', '2024-03-15'),
(8, 8, '2024-02-20', '15:45:00', 'Anxiety', 'Generalized anxiety disorder', 'Worry, restlessness, sleep issues', '{"blood_pressure": "125/80", "temperature": "98.5", "pulse": "82", "oxygen_saturation": "98%"}', 'Therapy referral, relaxation techniques', 'Coping strategies discussed', '2024-03-20'),
(9, 9, '2024-02-25', '12:30:00', 'Blurry vision', 'Refractive error', 'Difficulty seeing distant objects', '{"blood_pressure": "122/78", "temperature": "98.7", "pulse": "70", "oxygen_saturation": "99%"}', 'Prescription glasses', 'Vision corrected', '2025-02-25'),
(10, 10, '2024-03-01', '09:15:00', 'Frequent urination', 'Type 2 diabetes', 'Increased thirst, frequent urination', '{"blood_pressure": "145/92", "temperature": "98.1", "pulse": "76", "oxygen_saturation": "98%"}', 'Metformin, lifestyle counseling', 'Blood sugar monitoring started', '2024-04-01');


INSERT INTO prescriptions (patient_id, doctor_id, history_id, prescription_date, medication_name, dosage, frequency, duration, instructions, quantity_prescribed, refills_allowed, status) VALUES
(1, 1, 1, '2024-01-15', 'Nitroglycerin', '0.4mg', 'As needed', '30 days', 'Take under tongue for chest pain', 30, 2, 'Active'),
(2, 2, 2, '2024-01-20', 'Amoxicillin', '500mg', '3 times daily', '7 days', 'Take with food', 21, 0, 'Completed'),
(3, 3, 3, '2024-01-25', 'Ibuprofen', '400mg', '3 times daily', '14 days', 'Take with food to avoid stomach upset', 42, 1, 'Active'),
(4, 4, 4, '2024-02-01', 'Hydrocortisone cream', '1%', '2 times daily', '14 days', 'Apply thin layer to affected areas', 1, 0, 'Active'),
(5, 5, 5, '2024-02-05', 'Sumatriptan', '50mg', 'As needed', '30 days', 'Take at onset of migraine', 9, 2, 'Active'),
(6, 6, 6, '2024-02-10', 'Multivitamin', '1 tablet', 'Once daily', '90 days', 'Take with breakfast', 90, 3, 'Active'),
(7, 7, 7, '2024-02-15', 'Ferrous sulfate', '325mg', 'Once daily', '90 days', 'Take on empty stomach', 90, 2, 'Active'),
(8, 8, 8, '2024-02-20', 'Lorazepam', '0.5mg', 'As needed', '30 days', 'Take for anxiety, do not exceed 3 per day', 30, 0, 'Active'),
(9, 9, 9, '2024-02-25', 'Artificial tears', '0.5%', '4 times daily', '30 days', 'Use as needed for dry eyes', 4, 5, 'Active'),
(10, 10, 10, '2024-03-01', 'Metformin', '500mg', '2 times daily', '90 days', 'Take with meals', 180, 5, 'Active');


INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status, reason, notes) VALUES
(1, 1, '2024-03-15', '09:00:00', 'Scheduled', 'Follow-up for chest pain', 'Regular monitoring appointment'),
(2, 2, '2024-03-10', '14:30:00', 'Completed', 'Check-up after antibiotics', 'Patient recovered well'),
(3, 3, '2024-03-20', '11:15:00', 'Scheduled', 'Physical therapy assessment', 'Evaluate progress'),
(4, 4, '2024-03-05', '16:45:00', 'Completed', 'Skin condition follow-up', 'Rash improved significantly'),
(5, 5, '2024-03-25', '10:30:00', 'Scheduled', 'Migraine management', 'Medication adjustment needed'),
(6, 6, '2024-04-01', '13:00:00', 'Scheduled', 'Annual women\'s health exam', 'Routine screening'),
(7, 7, '2024-03-30', '08:30:00', 'Scheduled', 'Anemia follow-up', 'Check iron levels'),
(8, 8, '2024-04-05', '15:15:00', 'Scheduled', 'Therapy progress review', 'Assess anxiety management'),
(9, 9, '2024-12-25', '12:45:00', 'Scheduled', 'Annual eye exam', 'Vision check and prescription update'),
(10, 10, '2024-04-15', '09:45:00', 'Scheduled', 'Diabetes management', 'Blood sugar monitoring review'),
(1, 7, '2024-04-20', '14:00:00', 'Scheduled', 'General health check', 'Comprehensive physical'),
(5, 1, '2024-04-10', '11:30:00', 'Cancelled', 'Cardiac consultation', 'Patient rescheduled'),
(8, 2, '2024-03-28', '16:00:00', 'No-Show', 'Pediatric consultation', 'Patient did not attend'),
(2, 9, '2024-04-25', '10:15:00', 'Scheduled', 'Eye strain evaluation', 'Computer vision syndrome'),
(6, 4, '2024-04-12', '15:30:00', 'Scheduled', 'Skin cancer screening', 'Annual dermatology check');

INSERT INTO medical_history (patient_id, doctor_id, visit_date, visit_time, chief_complaint, diagnosis, symptoms, vital_signs, treatment_provided, notes, follow_up_date) VALUES
(1, 7, '2024-03-10', '10:00:00', 'General checkup', 'Hypertension monitoring', 'No specific symptoms', '{"blood_pressure": "138/88", "temperature": "98.4", "pulse": "78", "oxygen_saturation": "99%"}', 'Continue current medications', 'BP slightly elevated', '2024-06-10'),
(5, 1, '2024-03-08', '14:30:00', 'Chest discomfort', 'Non-cardiac chest pain', 'Mild chest discomfort during stress', '{"blood_pressure": "125/82", "temperature": "98.6", "pulse": "75", "oxygen_saturation": "98%"}', 'Stress management techniques', 'Likely stress related', NULL),
(3, 2, '2024-03-12', '11:45:00', 'Joint stiffness', 'Arthritis management', 'Morning stiffness in multiple joints', '{"blood_pressure": "128/84", "temperature": "98.2", "pulse": "80", "oxygen_saturation": "99%"}', 'Anti-inflammatory medication adjustment', 'Responding well to treatment', '2024-06-12');


INSERT INTO prescriptions (patient_id, doctor_id, history_id, prescription_date, medication_name, dosage, frequency, duration, instructions, quantity_prescribed, refills_allowed, status) VALUES
(1, 7, 11, '2024-03-10', 'Lisinopril', '10mg', 'Once daily', '90 days', 'Take in the morning', 90, 3, 'Active'),
(5, 1, 12, '2024-03-08', 'Aspirin', '81mg', 'Once daily', '90 days', 'Take with food', 90, 5, 'Active'),
(3, 2, 13, '2024-03-12', 'Naproxen', '220mg', '2 times daily', '30 days', 'Take with meals', 60, 2, 'Active');
