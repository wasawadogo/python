#ConvertModule
constant = 1.621371



def milesToKilometers():
    miles = float(input ('What is the number of miles driven?'))
    result = miles * constant
    print ('You have driven', miles , 'miles,' ' ' , 'Which is,', result ,'kilometers')

milesToKilometers()
