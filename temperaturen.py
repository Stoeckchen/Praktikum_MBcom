def CelsiusToFahrenheit(celsius):
    return celsius * 1.8 +32

def CelsiusToKelvin(celsius):
    return celsius + 273.15

def FahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def KelvinToCelsius(kelvin):
    return kelvin - 273.15

def readFloat(text):
    value = input("Temperatur in " + text.upper() + ": ")
    return float(value)
def printTemperature(celsius, fahrenheit, kelvin):
    print(celsius, "°C")
    print(fahrenheit, "°F")
    print(kelvin, "°K")


unit = input("Wähle die Einheit(C, F, K) ")
unit = unit.lower()
print(unit)

if(unit =="c"):
    celsius = readFloat("celsius")
    fahrenheit = CelsiusToFahrenheit(celsius)
   
    kelvin = CelsiusToKelvin(celsius)
    printTemperature(celsius, fahrenheit, kelvin)
    


elif(unit =="f"):
    fahrenheit = readFloat("fahrenheit")
    celsius = FahrenheitToCelsius(fahrenheit)
    
    kelvin = CelsiusToKelvin(celsius)
    printTemperature(celsius, fahrenheit, kelvin)
    
    

elif(unit =="k"):
    kelvin = readFloat("kelvin")
    celsius = KelvinToCelsius(kelvin)
    
    fahrenheit = CelsiusToFahrenheit(celsius)
    printTemperature(celsius, fahrenheit, kelvin)



else:
    print("falscher Input")