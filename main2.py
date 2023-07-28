import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_RTR import Ui_MainWindow  # Importing the UI class from ui_RTR module
from api import Datastore  # Importing the Datastore class from the datastore module
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
        self.set_button_enabled(1)  # Enabling a specific button

    def set_button_enabled(self, val):
        self.ui.pushButton.setEnabled(val)  # Setting the enabled state of a button

    def signals(self):
        # Connecting the UI buttons to the corresponding functions

        # Login Page
        self.ui.pushButton.clicked.connect(self.login)  # Connects the clicked signal of pushButton to login function
        # Clinician Home Page
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_17))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_8))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_7))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_9))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_11))
        # Add Staff
        self.ui.pushButton_9.clicked.connect(self.add_staff)
        # Add Patient
        self.ui.pushButton_16.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_4))
        self.ui.pushButton_10.clicked.connect(self.add_patient)
        # Clinician Stats
        self.ui.pushButton_017.clicked.connect(self.get_clinician_stats)
        self.ui.pushButton_17.clicked.connect(lambda: self.ui.MainWindow_2.setCurrentWidget(self.ui.page_4))
        
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


            
    def show(self):
        # Show the main window
        self.main_win.show()
        self.ui.MainWindow_2.setCurrentWidget(self.ui.page_3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())