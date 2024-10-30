import numpy as np

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
    ciy  = round(ciy, 5)
    cisa = round(cisa, 5)
    ciq  = round(ciq, 5)
    cimo = round(cimo, 5)
    ciw  = round(ciw, 5)
    cid  = round(cid, 5)
    cih  = round(cih, 5)
    cimi = round(cimi, 5)
    cise = round(cise, 5)
    piy  = ciy  / p * 100
    pisa = cisa / p * 100
    piq  = ciq  / p * 100
    pimo = cimo / p * 100
    piw  = ciw  / p * 100
    pid  = cid  / p * 100
    pih  = cih  / p * 100
    pimi = cimi / p * 100
    pise = cise / p * 100
    piy  = round(piy, 5)
    pisa = round(pisa, 5)
    piq  = round(piq, 5)
    pimo = round(pimo, 5)
    piw  = round(piw, 5)
    pid  = round(pid, 5)
    pih  = round(pih, 5)
    pimi = round(pimi, 5)
    pise = round(pise, 5)
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