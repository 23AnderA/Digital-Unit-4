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
        response = requests.get(
            "https://api.infrasolutions.au/api/get_assessments?firstname={}&lastname={}"
        )
        json_respnose = response.json()
        return json_respnose

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