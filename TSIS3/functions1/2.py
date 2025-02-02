def Fahrenheit_to_Centigrade(F):
    C = (5 / 9) * (F - 32)
    return C

F = float(input("Enter in a Fahrenheit temperature: "))
C = Fahrenheit_to_Centigrade(F)
print(F,"Fahrenheits in a Centigrade temperature is",C)
