import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_RTR import Ui_MainWindow  # Importing the UI class from ui_RTR module
from api import Datastore  # Importing the Datastore class from the datastore module
from PyQt6.QtGui import QPixmap  # Importing QPixmap from PyQt6.QtGui for working with images
import re  # Importing the re module for regular expression operations
import json
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

class num_exercises:
    num_exercises = 0  # Class variable to keep track of the number of exercises

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()  # Creating a QMainWindow object
        self.ui = Ui_MainWindow()  # Creating an instance of the UI class
        self.ui.setupUi(self.main_win)  # Setting up the UI for the main window
        self.db = Datastore()  # Creating a Datastore object for data storage

        self.signals()  # Connecting UI buttons to corresponding functions
        self.set_button_enabled(1)  # Enabling a specific button

    def set_button_enabled(self, val):
        self.ui.pushButton.setEnabled(val)  # Setting the enabled state of a button

    def signals(self):
        # Connecting the UI buttons to the corresponding functions

        # Login Page
        self.ui.pushButton.clicked.connect(self.login)  # Connects the clicked signal of pushButton to login function
        self.ui.pushButton_01.clicked.connect(self.Admin_login)
        # Clinician Home Page
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_11_1))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_8))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_7))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_9))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_11))
        # Add Staff
        self.ui.pushButton_9.clicked.connect(self.add_staff)
        self.ui.pushButton_15.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_4))
        # Add Patient
        self.ui.pushButton_16.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_4))
        self.ui.pushButton_10.clicked.connect(self.add_patient)
        # Clinician Stats
        self.ui.pushButton_017.clicked.connect(self.get_clinician_stats)
        self.ui.pushButton_17.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_5))
        # Appointment Assessments
        self.ui.pushButton_11.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_64))
        # OT Assessments
        self.ui.pushButton_84.clicked.connect(self.add_OT_assessment)
        # Get Assessments
        self.ui.pushButton_136.clicked.connect(self.get_assessments)
        self.ui.pushButton_136_2.clicked.connect(self.get_and_plot_scores)
        self.ui.pushButton_22.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_4))
        # Get Exercise Regime
        self.ui.pushButton_136_1.clicked.connect(self.get_exercise_regime)
        self.ui.pushButton_22_1.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_4))
        # Admin Home Page
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_6))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_8))
        
        # ----- slots ----- #

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        stored_password = self.db.get_password(username)
        password_value = stored_password['results'][0]['password']
        
        if stored_password is not None:
            if password_value == password:
                # Set the current page to page_4
                self.ui.MainWindow_2.setCurrentWidget(self.ui.page_4)
            else:
                self.ui.lineEdit_2.setText("Incorrect Password")
        else:
            self.ui.lineEdit.setText("Username not registered")
            
    def Admin_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        stored_password = self.db.get_password(username)
        password_value = stored_password['results'][0]['password']
        
        if stored_password is not None:
            if password_value == password:
                # Set the current page to page_4
                self.ui.MainWindow_2.setCurrentWidget(self.ui.page_5)
            else:
                self.ui.lineEdit_2.setText("Incorrect Password")
        else:
            self.ui.lineEdit.setText("Username not registered")
            
    def add_staff(self):
        # Retrieve staff details from the input fields
        name = self.ui.lineEdit_3.text()
        username = self.ui.lineEdit_5.text()
        password = self.ui.lineEdit_6.text()
        profession = self.ui.lineEdit_4.text()
        try:
            self.db.add_staff(name, username, password, profession)
            self.ui.pushButton_9.setText("Success")
        except:
            self.ui.pushButton_9.setText("Error")
            print("Error")
        
    def add_patient(self):
        first_name = self.ui.lineEdit_7.text()
        last_name = self.ui.lineEdit_8.text()
        email = self.ui.lineEdit_9.text()
        gender = self.ui.lineEdit_10.text()
        address = self.ui.lineEdit_11.text()
        suburb = self.ui.lineEdit_12.text()
        phone = self.ui.lineEdit_13.text()
        try:
            self.db.add_patient(first_name, last_name, email, gender, address, suburb, phone)
            self.ui.pushButton_10.setText("Success")
        except:
            self.ui.pushButton_10.setText("Error")
            print("Error")
            
    def get_clinician_stats(self):
        username = self.ui.lineEdit_14.text()
        stats = self.db.get_clinician_stats(username)
        for record in stats['results']:
            item = f"{record['Patient_data.first_name || Patient_data.last_name']} - {record['date']}"
            self.ui.comboBox_1.addItem(item)
            
    def add_OT_assessment(self):
        clinician = self.ui.lineEdit_95_1.text()
        patient_id = self.ui.lineEdit_95.text()
        appointment_date = self.ui.lineEdit_96.text()
        shoulder_abductors_score = self.ui.spinBox_28.value()
        elbow_flexors_score = self.ui.spinBox_29.value()
        elbow_extensors_score = self.ui.spinBox_30.value()
        wrist_extensors_score = self.ui.spinBox_31.value()
        finger_flexors_score = self.ui.spinBox_32.value()
        hand_intrinsics_score = self.ui.spinBox_33.value()
        print(patient_id, appointment_date)
        
        self.db.add_assessments(clinician, patient_id, appointment_date, shoulder_abductors_score, elbow_flexors_score, elbow_extensors_score, wrist_extensors_score, finger_flexors_score, hand_intrinsics_score)
        # Set the success message for the button
        self.ui.pushButton_84.setText("Success")

    def get_assessments(self):
        patient_first_name = self.ui.lineEdit_161.text()
        patient_last_name = self.ui.lineEdit_162.text()

        results = self.db.get_assessments(patient_first_name, patient_last_name)
        
        # Initialize an empty string to build the user-friendly result
        results_string = ""
        
        # Loop through each result in the results list
        for result in results['results']:
            results_string += "Date: " + result['date'] + "\n"
            
            # Loop through each key and value in the result dictionary except the 'date'
            for key, value in result.items():
                if key != 'date':
                    # Convert None values to a human-readable string
                    value_str = str(value) if value is not None else 'Not Available'
                    results_string += f"{key.replace('_', ' ').title()}: {value_str}\n"
            
            # Add a separator line between each result
            results_string += "-" * 50 + "\n"
        
        self.ui.textEdit_1.setText(results_string)

    def get_exercise_regime(self):
        patient_id = self.ui.lineEdit_161_1.text()
        results = self.db.get_exercise_regime(patient_id)

        formatted_text = ""
        for exercise in results['results']:
            name = exercise['name']
            date = exercise['date']
            reps = exercise['reps']
            body_location = exercise['body_location']
            target_muscles = exercise['target_muscles']
            equipment_required = exercise['equipment_required']
            animated_image = exercise['animated_image']
            
            exercise_text = f"Exercise: {name}\nDate: {date}\nReps: {reps}\nBody Location: {body_location}\nTarget Muscles: {target_muscles}\nEquipment Required: {equipment_required}\nAnimated Image: {animated_image}\n\n"
            formatted_text += exercise_text

        self.ui.textEdit_1_1.setText(formatted_text)

    def plot_exercise_scores(self, results, exercise):
        dates = []
        scores = []

        for result in results['results']:
            date_str = result['date']
            score = result[exercise]
            
            if score is not None:
                score = int(score)
                date = datetime.strptime(date_str, '%d/%m/%Y')
                
                dates.append(date)
                scores.append(score)

        # Convert dates to numerical format for regression
        dates_num = [d.timestamp() for d in dates]

        # Fit a linear regression model
        m, b = np.polyfit(dates_num, scores, 1)

        # Create the line of best fit using the regression coefficients
        best_fit_line = [m * date + b for date in dates_num]

        plt.scatter(dates, scores)
        plt.plot(dates, best_fit_line, color='red')  # Plotting the line of best fit
        plt.xlabel('Date')
        plt.ylabel(f'{exercise.replace("_", " ").capitalize()} Score')
        plt.title(f'{exercise.replace("_", " ").capitalize()} Score over Time')
        plt.ylim(0, 5)  # Setting the y-axis range to go up to 5
        plt.xticks(rotation=45)
        plt.show()
        
    def get_and_plot_scores(self):
        patient_first_name = self.ui.lineEdit_161.text()
        patient_last_name = self.ui.lineEdit_162.text()
        results = self.db.get_assessments(patient_first_name, patient_last_name)
        exercise = self.ui.lineEdit_161_2.text()
        self.plot_exercise_scores(results, exercise)



            
    def show(self):
        # Show the main window
        self.main_win.show()
        self.ui.MainWindow_2.setCurrentWidget(self.ui.page_3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())