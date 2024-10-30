import numpy as np
import matplotlib.pyplot as plt 

print ("-------------------------------------------------------------")
p = input("Please enter a principal amount or press 'q' to quit: ")
r = int(input("Please enter the rate of interest: "))
years = int(input("Please enter the time period in years: "))
print ("-------------------------------------------------------------")
semis = 2
quarters = 4
months = 12
weeks = 52
days = 365
hours = days * 24
minutes = hours * 24
seconds = minutes * 60

if (str(p) != "q" ):
    p    = int(p)
    ciy  = (p*((1+(r/100))**years)) - p
    cisa = (p*((1+(r/(100*semis)))**(years*semis))) - p
    ciq  = (p*((1+(r/(100*quarters)))**(years*quarters))) - p
    cimo = (p*((1+(r/(100*months)))**(years*months))) - p
    ciw  = (p*((1+(r/(100*weeks)))**(years*weeks))) - p
    cid  = (p*((1+(r/(100*days)))**(years*days))) - p
    cih  = (p*((1+(r/(100*hours)))**(years*hours))) - p
    cimi = (p*((1+(r/(100*minutes)))**(years*minutes))) - p
    cise = (p*((1+(r/(100*seconds)))**(years*seconds))) - p
    ciy  = round(ciy, 2)
    cisa = round(cisa, 2)
    ciq  = round(ciq, 2)
    cimo = round(cimo, 2)
    ciw  = round(ciw, 2)
    cid  = round(cid, 2)
    cih  = round(cih, 2)
    cimi = round(cimi, 2)
    cise = round(cise, 2)
    piy  = ciy  / p * 100
    pisa = cisa / p * 100
    piq  = ciq  / p * 100
    pimo = cimo / p * 100
    piw  = ciw  / p * 100
    pid  = cid  / p * 100
    pih  = cih  / p * 100
    pimi = cimi / p * 100
    pise = cise / p * 100
    piy  = round(piy, 2)
    pisa = round(pisa, 2)
    piq  = round(piq, 2)
    pimo = round(pimo, 2)
    piw  = round(piw, 2)
    pid  = round(pid, 2)
    pih  = round(pih, 2)
    pimi = round(pimi, 2)
    pise = round(pise, 2)
    print ("Percentage Interest Per Annum      = " + str(piy))
    print ("Percentage Interest Per Semi-Annum = " + str(pisa))
    print ("Percentage Interest Per Quarter    = " + str(piq))
    print ("Percentage Interest Per Month      = " + str(pimo))
    print ("Percentage Interest Per Week       = " + str(piw))
    print ("Percentage Interest Per Day        = " + str(pid))
    print ("Percentage Interest Per Hour       = " + str(pih))
    print ("Percentage Interest Per Minute     = " + str(pimi))
    print ("Percentage Interest Per Second     = " + str(pise))
    print ("-------------------------------------------------------------")
    print ("C.I. Compounded Per Annum      = " + str(ciy))
    print ("C.I. Compounded Per Semi-Annum = " + str(cisa))
    print ("C.I. Compounded Per Quarter    = " + str(ciq))
    print ("C.I. Compounded Per Month      = " + str(cimo))
    print ("C.I. Compounded Per Week       = " + str(ciw))
    print ("C.I. Compounded Per Day        = " + str(cid))
    print ("C.I. Compounded Per Hour       = " + str(cih))
    print ("C.I. Compounded Per Minute     = " + str(cimi))
    print ("C.I. Compounded Per Second     = " + str(cise))
    print ("-------------------------------------------------------------")
    # creating the dataset
    data = {'Annum':piy, 'Semi-Annum':pisa, 'Quarter':piq, 'Month':pimo, 'Week':piw, 'Day':pid, 'Hour':pih, 'Minute':pimi, 'Second':pise}
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize = (10, 5))
 
    # creating the bar plot
    plt.bar(courses, values, color ='maroon', width = 0.4)

    plt.xlabel("Compounding Frequency")
    plt.ylabel("Interest Percentage")
    plt.title("Interest Percentage with relation to Compounding Frequencies")

    plt.show()