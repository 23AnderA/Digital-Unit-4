import requests

# api_server = 'https://api.infrasolutions.au/api'


class Datastore:
    
    def get_clinician_stats(self, username):
        
        base_url = "https://api.infrasolutions.au/api/get_clinician_stats?username={}"
        url = base_url.format(username)
        print("API URL:", url)  # Add this line to check the formed URL
        response = requests.get(url)
        json_response = response.json()
        print("API Response:", json_response)  # Add this line to see the API response
        return json_response
    
    def get_usernames(self):
        response = requests.get("https://api.infrasolutions.au/api/get_usernames")
        json_respnose = response.json()
        return json_respnose

    def get_staff_names(self):
        response = requests.get("https://api.infrasolutions.au/api/get_staff_names")
        json_respnose = response.json()
        return json_respnose

    def get_assessments(self, firstname, lastname):
        url = "https://api.infrasolutions.au/api/get_assessments?first_name={}&last_name={}".format(firstname, lastname)
        print("API URL:", url)
        response = requests.get(url)
        print(response.text)
        json_response = response.json()
        print("API Response:", json_response)
        return json_response


    def add_patient(self, first_name, last_name, email, gender, address, suburb, phone):
        base_url = "https://api.infrasolutions.au/api/add_patient?firstname={}&lastname={}&email={}&gender={}&address{}&suburb{}&phone={}"
        url = base_url.format(
            first_name, last_name, email, gender, address, suburb, phone
        )
        response = requests.post(url)
        return response

    import requests


    def get_password(self, username):
        base_url = "https://api.infrasolutions.au/api/get_password?username={}"
        url = base_url.format(username)
        print("API URL:", url)  # Add this line to check the formed URL
        response = requests.get(url)
        json_response = response.json()
        print("API Response:", json_response)  # Add this line to see the API response
        return json_response


    def login(self, username, password):
        
        # url for Api Calls
        base_url = "https://api.infrasolutions.au/api/get_password?username={}"
        # format url
        url = base_url.format(username)

        response = requests.get(url)
        json_respnose = response.json()
        return json_respnose
        if password == response:
            print("Success, you logged in!")
        else:
            print("Wrong password!")
        json_respnose = response.json()
        
    def add_staff(self, username, name, password, profession):
        
        base_url = "https://api.infrasolutions.au/api/add_staff?username={}&name={}&password={}&profession={}"
        url = base_url.format(
            username, name, password, profession
        )
        response = requests.post(url)
        print("API URL:", url)  # Add this line to check the formed URL
        response = requests.get(url)
        json_response = response.json()
        print("API Response:", json_response)  # Add this line to see the API response
        return response
    
    def add_assessments(self, clinician, patient_id, date, hip_flexors=None, knee_extensors=None, dorsiflexors=None, great_toe_extensor=None, plantar_flexors=None, shoulder_abductors=None, elbow_flexors=None, elbow_extensors=None, wrist_extensors=None, finger_flexors=None, hand_intrinsics=None, aphasia=None, apraxia=None, dysarthria=None, dysphonia=None, memory=None, attention=None, judgement=None, neglect=None):
        
        base_url = "https://api.infrasolutions.au/api/add_assessments?clinician={}&patient_id={}&date={}&hip_flexors={}&knee_extensors={}&dorsiflexors={}&great_toe_extensor={}&plantar_flexors={}&shoulder_abductors={}&elbow_flexors={}&elbow_extensors={}&wrist_extensors={}&finger_flexors={}&hand_intrinsics={}&aphasia={}&apraxia={}&dysarthria={}&dysphonia={}&memory={}&attention={}&judgement={}&neglect={}"
        url = base_url.format(
            clinician,
            patient_id,
            date,
            hip_flexors if hip_flexors is not None else 'NULL',
            knee_extensors if knee_extensors is not None else 'NULL',
            dorsiflexors if dorsiflexors is not None else 'NULL',
            great_toe_extensor if great_toe_extensor is not None else 'NULL',
            plantar_flexors if plantar_flexors is not None else 'NULL',
            shoulder_abductors if shoulder_abductors is not None else 'NULL',
            elbow_flexors if elbow_flexors is not None else 'NULL',
            elbow_extensors if elbow_extensors is not None else 'NULL',
            wrist_extensors if wrist_extensors is not None else 'NULL',
            finger_flexors if finger_flexors is not None else 'NULL',
            hand_intrinsics if hand_intrinsics is not None else 'NULL',
            aphasia if aphasia is not None else 'NULL',
            apraxia if apraxia is not None else 'NULL',
            dysarthria if dysarthria is not None else 'NULL',
            dysphonia if dysphonia is not None else 'NULL',
            memory if memory is not None else 'NULL',
            attention if attention is not None else 'NULL',
            judgement if judgement is not None else 'NULL',
            neglect if neglect is not None else 'NULL'
        )
        
        print("API URL:", url)  # Add this line to check the formed URL
        response = requests.post(url)
        print(response.text)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Request failed with status code {response.status_code}")
            return None

        # Try to decode the JSON response
        try:
            json_response = response.json()
        except requests.exceptions.JSONDecodeError:
            print("JSON decoding failed. Server responded with:", response.text)
            return None
        
        print("API Response:", json_response)  # Add this line to see the API response
        return response

        