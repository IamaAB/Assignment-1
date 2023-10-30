def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

#main
temp = float(input("Enter a Temperature : "))
print(" ")
print("Displaying bY converting all temperature")
print(" ")

celcius = celsius_to_fahrenheit(temp)
print(f"Celcius to Farhenite {temp} is :",celcius)

fahrenheit = fahrenheit_to_celsius(temp)
print(f"Farhenite to Celcius {temp} is :",fahrenheit)

celcius_to_kelvin = celsius_to_kelvin(temp)
print(f"Celcius to Kelvin  {temp} is :",celcius)

kelvin_to_celsius_temp = kelvin_to_celsius(temp)
print(f"Kelvin to Celcius {temp} is :",kelvin_to_celsius_temp)
