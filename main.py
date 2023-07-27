import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_RTR import Ui_MainWindow  # Importing the UI class from ui_RTR module
from datastore import Datastore  # Importing the Datastore class from the datastore module
from PyQt6.QtGui import QPixmap  # Importing QPixmap from PyQt6.QtGui for working with images
import re  # Importing the re module for regular expression operations

class num_exercises:
    num_exercises = 0  # Class variable to keep track of the number of exercises

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()  # Creating a QMainWindow object
        self.ui = Ui_MainWindow()  # Creating an instance of the UI class
        self.ui.setupUi(self.main_win)  # Setting up the UI for the main window
        self.db = Datastore()  # Creating a Datastore object for data storage

        self.signals()  # Connecting UI buttons to corresponding functions
        self.display_gallows()  # Displaying the gallows
        self.set_button_enabled(1)  # Enabling a specific button

    def set_button_enabled(self, val):
        self.ui.pushButton.setEnabled(val)  # Setting the enabled state of a button

    def signals(self):
        # Connecting the UI buttons to the corresponding functions

        # Login Page
        self.ui.pushButton.clicked.connect(self.login)  # Connects the clicked signal of pushButton to login function
        # Clinician Home Page
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_17))
        

    # ----- slots ----- #

    def login(self):
        # Retrieve username and password from the input fields
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        # Retrieve stored password and admin status from the database based on the username
        stored_password = self.db.get_password(username)
        admin_status = self.db.get_admin_status(username)
        
        # Check if the stored password exists
        if stored_password != None:
            # Check if the stored password matches the entered password and the user is not an admin
            if stored_password == password and admin_status == 0:
                # Set the current page to page_4
                self.ui.MainWindow_2.setCurrentWidget(self.ui.page_4)
            # Check if the stored password matches the entered password and the user is an admin
            elif stored_password == password and admin_status != 0:
                # Set the current page to page_5
                self.ui.MainWindow_2.setCurrentWidget(self.ui.page_5)
            else:
                # Set the password input field to show "Incorrect Password"
                if stored_password != password:
                    self.ui.lineEdit_2.setText("Incorrect Password")
        else:
            # Set the username input field to show "Username not registered"
            self.ui.lineEdit.setText("Username not registered")

    def is_valid_date(date_string):
        # Split the date_string into day, month, and year
        try:
            day, month, year = date_string.split('/')
            day = int(day)
            month = int(month)
            year = int(year)

            # Check if the day is within the range 1-31
            if day < 1 or day > 31:
                return False
            # Check if the month is within the range 1-12
            if month < 1 or month > 12:
                return False
            # Check if the year is within the range 1000-9999
            if year < 1000 or year > 9999:
                return False

            # Additional validation rules can be added if needed

            return True
        except (ValueError, AttributeError):
            return False

    def insert_exercise(self):
        # Retrieve exercise name from the input field
        exercise_name = self.ui.lineEdit_165.text()
        # Get exercise ID from the database based on the exercise name
        exercise_id = self.db.get_exercise_id(exercise_name)
        
        # Check if the exercise ID is None (exercise name not found)
        if exercise_id is None:
            # Set the exercise name input field to show "Invalid Exercise"
            self.ui.lineEdit_165.setText("Invalid Exercise")
            return  # Fail condition
        
        # Retrieve reps, patient name, and full date from the input fields
        reps = self.ui.spinBox_58.value()
        patient_name = self.ui.lineEdit_164.text()
        # Split the patient name into first name and last name
        patient_list = patient_name.split(" ", 1)
        
        # Check if the patient name is valid (contains both first name and last name)
        if len(patient_list) != 2:
            # Set the patient name input field to show "Invalid Name"
            self.ui.lineEdit_164.setText("Invalid Name")
            return  # Fail condition
        
        # Retrieve patient's first name and last name
        patient_first, patient_last = patient_list
        # Get patient ID from the database based on the first name and last name
        patient_id = self.db.get_patient_id(patient_first, patient_last)
        
        # Check if the patient ID is None (patient not found)
        if patient_id is None:
            self.ui.lineEdit_164.setText("Invalid Name")
            return  # Fail condition
        
        full_date = self.ui.lineEdit_163.text()
        # Check if the full date is a valid date format
        if not self.is_valid_date(full_date):
            # Set the full date input field to show "Invalid date format"
            self.ui.lineEdit_163.setText("Invalid date format")
            return  # Fail condition
        
        # Insert patient's exercise regime into the database
        self.db.insert_patient_regime(patient_id, full_date)
        # Get the regime ID from the database based on the patient ID and full date
        regime_id = self.db.get_regime_id(patient_id, full_date)
        print(regime_id)
        # Insert exercise into the patient's regime
        self.db.insert_exercise_regime(regime_id, exercise_id, reps)
        # Get the list of exercises in the regime
        exercises = self.db.get_exercises(regime_id)
        print(exercises)
        # Increment the number of exercises
        num_exercises.num_exercises += 1
        # Update the label to show the current number of exercises
        self.ui.label_322.setText("Current Exercises: " + str(num_exercises.num_exercises))

    def add_patient_exercise_regime(self):
        patient_name = self.ui.lineEdit_164.text()
        # Split the patient name into first name and last name
        patient_list = patient_name.split(" ", 1)
        patient_first, patient_last = patient_list
        print(patient_first)
        print(patient_last)
        # Get patient ID from the database based on the first name and last name
        patient_id = self.db.get_patient_id(patient_first, patient_last)
        print(patient_id)
        full_date = self.ui.lineEdit_163.text()
        print(full_date)
        # Create a new exercise regime for the patient in the database
        self.db.make_regime(patient_id, full_date)
        # Set the success message for the button
        self.ui.pushButton_139.setText("Success")

    def clinician_statistics(self):
        clinician_name = self.ui.lineEdit_14.text()
        # Get clinician ID from the database based on the clinician name
        clinician_id = self.db.get_clinician_id(clinician_name)
        
        # Check if the clinician ID is None (clinician not found)
        if clinician_id is None:
            # Set the clinician name input field to show "Clinician not found"
            self.ui.lineEdit_14.setText("Clinician not found")
            return  # Fail condition
        
        # Get the list of appointments for the clinician from the database
        appointments = self.db.get_appointments_clinician(clinician_id)
        
        for record in appointments:
            # Add each appointment record to the combo box
            self.ui.comboBox_1.addItem(record)

    def add_OT_assessment(self):
        # Retrieve patient's first name and last name from the input fields
        first_name = self.ui.lineEdit_95.text()
        last_name = self.ui.lineEdit_95_1.text()
        # Get patient ID from the database based on the first name and last name
        patient_id = self.db.get_patient_id(first_name, last_name)
        # Retrieve appointment date from the input field
        appointment_date = self.ui.lineEdit_96.text()
        appointment_date = str(appointment_date)
        # Set appointment time to a default value of "00:00"
        appointment_time = "00:00"
        # Retrieve scores for different assessments from the spin boxes
        shoulder_abductors_score = self.ui.spinBox_28.value()
        elbow_flexors_score = self.ui.spinBox_29.value()
        elbow_extensors_score = self.ui.spinBox_30.value()
        wrist_extensors_score = self.ui.spinBox_31.value()
        finger_flexors_score = self.ui.spinBox_32.value()
        hand_intrinsics_score = self.ui.spinBox_33.value()
        print(patient_id, appointment_date, appointment_time)
        
        try:
            # Add OT assessment results to the database
            self.db.add_OT_results(patient_id, appointment_date, appointment_time, shoulder_abductors_score, elbow_flexors_score, elbow_extensors_score, wrist_extensors_score, finger_flexors_score, hand_intrinsics_score)
            # Set the success message for the button
            self.ui.pushButton_84.setText("Success")
        except:
            # Set the message for the button when the appointment is not found
            self.ui.pushButton_84.setText("Appointment not found")
            
    def is_valid_phone_number(self, phone_number):
        # This is a simple example that checks if the phone number consists of 10 digits
        if len(phone_number) != 10 or not phone_number.isdigit():
            return False
        return True

    def patient_assessments(self):
        # Retrieve patient details from the input fields
        first_name = self.ui.lineEdit_161.text()
        last_name = self.ui.lineEdit_161_1.text()
        # Get patient ID from the database based on the first name and last name
        patient_id = self.db.get_patient_id(first_name, last_name)
        # Retrieve appointment date and time from the input fields
        appointment_date = self.ui.lineEdit_162.text()
        appointment_time = self.ui.lineEdit_162_1.text()

    def view_OT_assessments(self):
        # Retrieve patient details from the input fields
        first_name = self.ui.lineEdit_161.text()
        last_name = self.ui.lineEdit_161_1.text()
        # Get patient ID from the database based on the first name and last name
        patient_id = self.db.get_patient_id(first_name, last_name)
        # Retrieve appointment date and time from the input fields
        appointment_date = self.ui.lineEdit_162.text()
        appointment_time = self.ui.lineEdit_162_1.text()
        # Get the appointment ID from the database
        appointment_id = self.db.get_appointment_id(appointment_date, patient_id)
        # Get the OT assessment scores from the database
        ot_score_list = self.db.get_OT_assessment(appointment_id)
        print(ot_score_list)
        # Extract individual scores from the list
        shoulder_abductors_score, elbow_extensors_score, elbow_flexors_score, wrist_extensors_score, finger_flexors_score, hand_intrinsics_score = ot_score_list
        # Update the UI labels with the scores
        self.ui.label_30.setText(str(shoulder_abductors_score))
        self.ui.label_31.setText(str(elbow_flexors_score))
        self.ui.label_32.setText(str(elbow_extensors_score))
        self.ui.label_33.setText(str(wrist_extensors_score))
        self.ui.label_34.setText(str(finger_flexors_score))
        self.ui.label_35.setText(str(hand_intrinsics_score))

    def add_clinician(self):
        # Retrieve clinician details from the input fields
        name = self.ui.lineEdit_3.text()
        username = self.ui.lineEdit_5.text()
        password = self.ui.lineEdit_6.text()
        clinician_type = self.ui.lineEdit_4.text()
        clinician = "0"
        # Check the clinician type and assign the corresponding value
        if clinician_type == "OT":
            clinician = 1
        elif clinician_type == "Physio":
            clinician = 2
        elif clinician_type == "Speech":
            clinician = 3
        elif clinician_type != "OT" or "Physio" or "Speech" or clinician == "0":
            self.ui.lineEdit_4.setText("Please choose 'OT', 'Physio', or 'Speech'")
        # Retrieve admin information from the input field
        admin = self.ui.lineEdit_03.text()
        admin_type = 2
        # Check the admin value and assign the corresponding admin type
        if admin == "Yes":
            admin_type = 1
        elif admin == "No":
            admin_type = 0
        elif admin != "Yes" or "No":
            self.ui.lineEdit_03.setText("Please enter either Yes or No")
        # Check if both admin type and clinician type are valid
        if admin_type == 0 or 1:
            if clinician == 1 or 2 or 3:
                self.db.add_clinician(name, username, password, clinician, admin_type)
                self.ui.pushButton_9.setText("Success")

    def view_clinician_statistics(self):
        # Switch the current widget in the UI to the clinician statistics page
        self.ui.MainWindow_2.setCurrentWidget(self.ui.page_8)

    def show(self):
        # Show the main window
        self.main_win.show()

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main_win = MainWindow()
        main_win.show()
        sys.exit(app.exec())
