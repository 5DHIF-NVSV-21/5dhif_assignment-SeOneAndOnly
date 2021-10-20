# Temperatur Umwandler 
# °C zu °F: (0 °C × 9/5) + 32 = 32 °F
# °F zu °C: (32 °F − 32) × 5/9 = 0 °C
#  K zu °C: 0 K − 273,15 = -273,1 °C
# °C zu  K: 0 °C + 273,15 = 273,15
#  K zu °F: (0 K − 273,15) × 9/5 + 32 = -459,7 °F
# °F zu  K: (32 °F − 32) × 5/9 + 273,15 = 273,15
import random

def CtoF(value):
    return (value*9/5)+32

def CtoK(value):
    return value+273.15

def FtoC(value):
    return (value-32)*5/9

def FtoK(value):
    return FtoC(value)+273.15

def KtoC(value):
    return value-273.15

def KtoF(value):
    return CtoF(KtoC(value))

def default():
    return "Incorrect Number"
try:
    while True:
        print("1) Celsius nach Fahrenheit\n")
        print("2) Celsius nach Kelvin\n")
        print("3) Fahrenheit nach Celsius\n")
        print("4) Fahrenheit nach Kelvin\n")
        print("5) Kelvin nach Celsius\n")
        print("6) Kelvin nach Fahrenheit\n")
        print("7) Rolling a Dice just for fun\n")
        print("Press Ctrl+C to stop the program\n")

        opt = input("Gib die Nummer der gewünschten Option ein: ")

        if opt == "1":
            wert =  float(input("°C zu °F) Gib die umzurechnende Temperatur ein: "))
            print("%.2f °C ist umgerechnet %.2f °F \n" % (wert, CtoF(wert)))
            input("Press Enter to continue or Ctrl+c to stop \n")
        elif opt == "2":
            wert =  float(input("°C zu K) Gib die umzurechnende Temperatur ein: "))
            print("%.2f °C ist umgerechnet %.2f K \n\n" % (wert, CtoK(wert)))
        elif opt == "3":
            wert =  float(input("°F zu °C) Gib die umzurechnende Temperatur ein: "))
            print("%.2f °F ist umgerechnet %.2f °C \n\n" % (wert, FtoC(wert)))
        elif opt == "4":
            wert =  float(input("°F zu K) Gib die umzurechnende Temperatur ein: "))
            print("%.2f °F ist umgerechnet %.2f K \n\n" % (wert, FtoK(wert)))
        elif opt == "5":
            wert =  float(input(" K zu °C) Gib die umzurechnende Temperatur ein: "))
            print("%.2f K ist umgerechnet %.2f °C \n\n" % (wert, KtoC(wert)))
        elif opt == "6":
            wert =  float(input(" K zu °F) Gib die umzurechnende Temperatur ein: "))
            print("%.2f K ist umgerechnet %.2f °F \n\n" % (wert, KtoF(wert)))
        elif opt == "7":
            min = 1
            max = 6

            roll_again = "yes"

            while roll_again == "yes" or roll_again == "y":
                print ("Rolling the dices...")
                print ("The values are....")
                print (random.randint(min, max))
                print (random.randint(min, max))

                roll_again = input("Roll the dices again? (yes(y) or no)")
            print("\n\n")
except KeyboardInterrupt:
    pass


