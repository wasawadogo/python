#Wendyam Alex Auguste Sawadogo
welcomeMsg = "Welcome to the fiber optic feet calculation"
print (welcomeMsg)
companyName = input ("What is your Company name?")
print ('welcome' , companyName + ".")
numberOfFeet = int(input ("What is the number of feet of fiber optic you want to install?"))


if numberOfFeet >= 100 and numberOfFeet < 250:
    result1 = 0.80 * numberOfFeet
    print (result1, "feet,"+" ", companyName)
elif numberOfFeet >= 250 and numberOfFeet < 500:
    result2 = 0.70 * numberOfFeet
    print (result2, "feet,"+" ", companyName)
elif numberOfFeet >= 500:
    result3 = 0.50 * numberOfFeet
    print (result3, "feet,"+" ", companyName)
else:
    result0 = 0.87 * numberOfFeet
    print (result0, "feet,"+" ", companyName)






#result = 0.80 * numberOfFeet
#print (result, "feet,"+" ", companyName)