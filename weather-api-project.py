import requests
import http.client as httplib

from datetime import datetime

def check_the_temp():
    f = open("logfile.txt", "a") #creates a text file to log the status of our current code

    # function to check internet connectivity
    def checkInternetHttplib(url="www.geeksforgeeks.org", timeout=3):
        connection = httplib.HTTPConnection(url, timeout=timeout)
        try:
            # only header requested for fast operation
            connection.request("HEAD", "/")
            connection.close()  # connection closed
            return True

        except Exception as exep:
            return False

    x = checkInternetHttplib()

    api_key = '87d845b0b6cf29baa1a73cc34b067a95'
    location = input("Enter the city name: ")

    # function to check the connectivity and debugging errors
    def getthedata(y):

        if y:
            try:
                complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
                api_link = requests.get(complete_api_link)
                api_data = api_link.json()
                return api_data
            except AttributeError as e:
                api_data = e
                return api_data
        else:
            api_data = "Check your internet connection and try again!"
            return api_data

    apidata = getthedata(x)



    # checking the presence of any errors to log it
    if (type(apidata) == str): #Log output and show the connection error

        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        f.write(f"{date_time.center(50, '-')}\n")
        f.write("*"*10)
        f.write("\n")

        f.write(apidata)
        f.write("\n")

        f.write("*"*10)
        f.write("\n")

        f.write("Status code - Failed\n")
        f.write("Error Message - Internet Connection Failure!\n")
        f.write("\n")
        print(apidata)


    # to log and print the error if the city name is invalid
    # to check if there are any cities present in the world which are not added to the data center
    elif ('message' in apidata.keys() and apidata['message'] == 'city not found'):
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        f.write(f"{date_time.center(50, '-')}\n")
        f.write("#"*10)
        f.write("\n")

        f.write(apidata['message'])
        f.write("\n")

        f.write("#"*10)
        f.write("\n")

        f.write("Status code - Failed\n")
        f.write("Error Message - City not found!\n")

        print("Error Message: " + apidata['message'].capitalize()) #Print the error message
        f.write("City Name - {}\n".format(location))
        f.write("\n")


    else: #IF no errors are caught, the required data is shown.
        temp_city = ((apidata['main']['temp']) - 273.15)
        weather_desc = apidata['weather'][0]['description']
        hmdt = apidata['main']['humidity']
        wind_spd = apidata['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
        f.write(f"{date_time.center(50, '-')}\n")
        #f.write(f"Log Time - {datetime.now().strftime('%d %b %Y | %I:%M:%S %p')}\n")


        f.write("City Name - {}\n".format(location))


        print("-------------------------------------------------------------")
        print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
        print("-------------------------------------------------------------")

        print("Current temperature is: {:.2f} deg C".format(temp_city))
        print("Current weather desc  :", weather_desc)
        print("Current Humidity      :", hmdt, '%')
        print("Current wind speed    :", wind_spd, 'kmph')

        f.write("The temperature is   : {:.2f} deg C\n".format(temp_city))
        f.write("Weather Description  : {}\n".format(weather_desc))
        f.write("Status code - Successful\n")
        f.write("\n")



    f.close() #Closing the end file

check_the_temp()# calling our function

