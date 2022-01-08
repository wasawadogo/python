#Interest rate Calculation
initialAmont = float(input("please enter your initial amount:" + " "))
interestRate = float(input("please enter the anual interest as decimal number:" + " " ))
balance = initialAmont
years = 0
while balance <= 2*initialAmont:
    balance = balance + balance * ((float (interestRate)/100))
    years = years + 1
print ("Your initial amount will double in ",years,"years")
