import numpy as np

p = input("Please enter a principal amount or press 'q' to quit: ")

while (str(p) != "q"):
    p = int(p)
    r = int(input("Please enter the rate of interest: "))
    t = int(input("Please enter the time period: "))
    si = (p*r*t)/100
    ci = (p*((1+(r/100))**t)) - p
    ci = round(ci, 2)
    si = round(si, 2)
    diff = ci - si
    pdiff = (diff/si)*100
    pdiff = round(pdiff, 2)
    print ("S.I. = " + str(si))
    print ("C.I. = " + str(ci))
    print ("Difference % = " + str(pdiff) + "%")
    print ("-------------------------------------------------------")

    p = input("Please enter a principal amount or press 'q' to quit: ")
    
print("Thank you for using the program :)")    