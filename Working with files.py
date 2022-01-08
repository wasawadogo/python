# Author: <Wendyam Sawadogo>
# Creation Date: <11/07/2021
# This is a simple program to work with files


import os

def files():
    directory = input ('Please enter the directory you would like to save the file:' ' ')
    nameOfFile = input ('Please enter the name of the file: ')
    name = input ('Enter your name: ')
    address = input ('Enter your address: ')
    phone = int(input ('Enter your phone number: '))

    if os.path.isdir (directory):
        # creating the file.
        writeFile = open(os.path.join(directory,nameOfFile,),'w')

        #write on the file and separeted by comma
        writeFile.write(name+ ',' + address + (',') + phone + (','))
        writeFile.close()

        #reading the file
        print ("Your file Contents is:")
        readFile = open(os.path.join(directory, nameOfFile), 'r')
        for line in readFile:
            print (line)
            readFile.close()
    else:
        print ("Sorry the diectory does not exist.")
        
      



files()
