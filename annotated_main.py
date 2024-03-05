def login(self):
    # Extract username and password from the input fields
    username = self.ui.lineEdit.text()
    password = self.ui.lineEdit_2.text()

    # Retrieve stored password for the given username from the database
    stored_password = self.db.get_password(username)
    password_value = stored_password['results'][0]['password']

    if stored_password is not None:
        # Check if input password matches the stored password
        if password_value == password:
            # If password matches, navigate to page_4
            self.ui.MainWindow_2.setCurrentWidget(self.ui.page_4)
        else:
            # If password doesn't match, display error message
            self.ui.lineEdit_2.setText("Incorrect Password")
    else:
        # If username doesn't exist in the database, display error message
        self.ui.lineEdit.setText("Username not registered")

def add_staff(self):
    # Extract staff details from the input fields
    name = self.ui.lineEdit_3.text()
    username = self.ui.lineEdit_5.text()
    password = self.ui.lineEdit_6.text()
    profession = self.ui.lineEdit_4.text()

    # Try to add staff member to the database
    try:
        self.db.add_staff(name, username, password, profession)
        self.ui.pushButton_9.setText("Success")
    except:
        # If there is an error during addition, display error message
        self.ui.pushButton_9.setText("Error")
        print("Error")

def get_clinician_stats(self):
    # Extract username from the input field
    username = self.ui.lineEdit_14.text()

    # Retrieve clinician stats from the database
    stats = self.db.get_clinician_stats(username)

    # For each record in the stats, add the relevant info to comboBox_1
    for record in stats['results']:
        item = f"{record['Patient_data.first_name || Patient_data.last_name']} - {record['date']}"
        self.ui.comboBox_1.addItem(item)
        
    # Call add_assessments function, add assessments to the database
    self.db.add_assessments(clinician, patient_id, appointment_date, shoulder_abductors_score, elbow_flexors_score, elbow_extensors_score, wrist_extensors_score, finger_flexors_score, hand_intrinsics_score)

    # Display success message
    self.ui.pushButton_84.setText("Success")

def get_assessments(self):
    # Extract patient's first and last name from the input fields
    patient_first_name = self.ui.lineEdit_161.text()
    patient_last_name = self.ui.lineEdit_162.text()

    # Retrieve assessments for the given patient from the database
    results = self.db.get_assessments(patient_first_name, patient_last_name)
    
    # Initialize an empty string to store formatted result string
    results_string = ""
    
    # For each result in the results, append key-value pairs to the result string
    for result in results['results']:
        results_string += "Date: " + result['date'] + "\n"
        for key, value in result.items():
            if key != 'date':
                value_str = str(value) if value is not None else 'Not Available'
                results_string += f"{key.replace('_', ' ').title()}: {value_str}\n"
        results_string += "-" * 50 + "\n"
    
    # Display the results_string in textEdit_1
    self.ui.textEdit_1.setText(results_string)

def get_exercise_regime(self):
    # Extract patient id from the input field
    patient_id = self.ui.lineEdit_161_1.text()

    # Retrieve exercise regime for the given patient from the database
    results = self.db.get_exercise_regime(patient_id)

    # Initialize an empty string to store formatted exercise regime
    formatted_text = ""
    
    # For each exercise in the results, append relevant details to the formatted_text
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

    # Display the formatted_text in textEdit_1_1
    self.ui.textEdit_1_1.setText(formatted_text)

def plot_exercise_scores(self, results, exercise):
    # Initialize empty lists to store dates and scores
    dates = []
    scores = []

    # For each result in the results, append date and score to respective lists
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

    # Fit a linear regression model to dates and scores
    m, b = np.polyfit(dates_num, scores, 1)

    # Create the line of best fit using the regression coefficients
    best_fit_line = [m * date + b for date in dates_num]

    # Plot the dates and scores, and line of best fit
    plt.scatter(dates, scores)
    plt.plot(dates, best_fit_line, color='red')  
    plt.xlabel('Date')
    plt.ylabel(f'{exercise.replace("_", " ").capitalize()} Score')
    plt.title(f'{exercise.replace("_", " ").capitalize()} Score over Time')
    plt.ylim(0, 5)  
    plt.xticks(rotation=45)
    plt.show()

def get_exercise_regime(self, patient_id):
    # Define the API URL
    url = "https://api.infrasolutions.au/api/get_exercise_regime?patient_id={}".format(patient_id)
    print("API URL:", url)  # Print the API URL for debugging
    
    # Send a GET request to the API
    response = requests.get(url)
    print(response.text)  # Print the raw response text for debugging
    
    # Parse the JSON response
    json_response = response.json()
    print("API Response:", json_response)  # Print the parsed response for debugging
    
    # Return the parsed response
    return json_response

def add_patient(self, first_name, last_name, email, gender, address, suburb, phone):
    # Define the API URL with placeholders for parameters
    base_url = "https://api.infrasolutions.au/api/add_patient?firstname={}&lastname={}&email={}&gender={}&address{}&suburb{}&phone={}"
    
    # Format the URL with the given parameters
    url = base_url.format(first_name, last_name, email, gender, address, suburb, phone)
    
    # Send a POST request to the API
    response = requests.post(url)
    
    # Return the response
    return response

def get_password(self, username):
    # Define the API URL with placeholders for parameters
    base_url = "https://api.infrasolutions.au/api/get_password?username={}"
    
    # Format the URL with the given parameters
    url = base_url.format(username)
    print("API URL:", url)  # Print the API URL for debugging
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Parse the JSON response
    json_response = response.json()
    print("API Response:", json_response)  # Print the parsed response for debugging
    
    # Return the parsed response
    return json_response

def login(self, username, password):
    # Define the API URL with placeholders for parameters
    base_url = "https://api.infrasolutions.au/api/get_password?username={}"
    
    # Format the URL with the given parameters
    url = base_url.format(username)
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Parse the JSON response
    json_respnose = response.json()
    
    # Check if the given password matches the password in the response
    if password == response:
        print("Success, you logged in!")  # Print a success message if the passwords match
    else:
        print("Wrong password!")  # Print an error message if the passwords don't match
    
    # Return the parsed response
    return json_respnose
