# Author: <Wendyam Sawadogo>
# Creation Date: <11/16/2021
#This is an app that gets input from the user to diplay weather data using API
import requests


print ('Welcome to the weather forcast.' "\n")

#city weather data requests
def UserCity ():
    city = (input('please enter you city:' ' '))
    cityUrl = requests.get('https://api.openweathermap.org/data/2.5/weather?q={},us&appid=fe1b236a74664961301899078bf63aea&units=imperial'.format(city))
    weatherData(cityUrl.json())

    askUser = input ('Do you want to continue? Y or N' ' ')
    if askUser == 'y':
        main()
    if askUser == 'n':
        print ('Thanks for using the weather app. Bye...')
        exit()

# Zipcode weather data requests
def UserZipCode ():
    zipCode = int(input('please enter you zipcode:' ' '))
    zipUrl = requests.get('https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=fe1b236a74664961301899078bf63aea'.format(zipCode))
    weatherData(zipUrl.json())

    askUser = input ('Do you want to continue? Y or N : ' ' ')
    if askUser == 'Y':
        main()  
    if askUser == 'N':
        print ('Thanks for using the weather app. Bye...')
        exit()


# data formating to a readable format

def weatherData (weatherData):
    temp = weatherData['main']['temp']
    hightemp = weatherData['main']['temp_max']
    lowtemp = weatherData['main']['temp_min']
    wind_speed = weatherData['wind']['speed']
    press = weatherData['main']['pressure']
    latitude = weatherData['coord']['lat']
    longitude = weatherData['coord']['lon']
    humid = weatherData['main']['humidity']
    description = weatherData['weather'][0]['description']

    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Pressure : {} hPa'.format(press))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description )) 
    
    "\n"
# The main fonction with a loop that ask the user and run the program.
def main():
    while True:
        choice = input ("please enter 1 for city and 2 for zip code.")

        if choice == '1':
            try:
                print ("connecting to the server...")
                UserCity()

            except Exception:
                print ("please enter 1 for city or 2 for zip code." ' ')
                UserCity()

        if choice == '2':
            try:
                print ("Connecting to the server...")
                UserZipCode()

            except Exception:
                print ("Please enter 1 for city and 2 for zip code")
                UserZipCode()

        else:
            print ("Let's get back to the beginning")
            main()
            



main ()
