import random

print("Vad vill du öva på?")

raknesatt = input() 
if raknesatt == "plus":
    print("Inte färdigt")

   
if raknesatt == "multiplikation":
    score = 0
    ratt_svar_i_rad = 0
    print("Vilken tabell vill du öva på?")
    siffra = int(input()) # int()

    while score < 10:
        annanSiffra = random.randint(0,10)
        svar = siffra * annanSiffra

        print(siffra, " * ", annanSiffra, " = ")
        spelarens_svar = int(input()) 

    if svar == spelarens_svar:
        print("Rätt! DU ÄR BRA!")
