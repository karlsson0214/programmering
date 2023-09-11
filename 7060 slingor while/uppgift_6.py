svar = input("gissa på ett tal: ")

while svar != "4":
    if svar == "3":
        print("nästan rätt")
    elif svar == "5":
        print("nästa rätt")
    else:
        print("helt fel")
    svar = input("gissa på ett tal: ")

print("rätt, bra jobbat") 
print("Tack och hej!")