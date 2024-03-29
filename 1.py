# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:59:30 2024
Ejercicio Basic Python
@author: andrea.garcia

"""

#Part I: Lists and Loops

##1) Create a list with the names of every planet in the solar system (in order)
planet = ["Mercurio", "Venus", "Tierra","Marte","Jupiter","Saturno","Urano","Neptuno"]

##2) Have Python tell you how many planets there are by examining your list
print(len(planet))

##3) Use slicing to display the first four planets (the rocky planets)
print(planet[:4])

##4) Iterate through your planets and print the planet name only if it has an s at the end
for p in planet:
    if p.endswith("s"):
        print (p)
    else:
        None

#Part II: Dictionaries

##1) Now create a dictionary that maps each planet name to its mass
mass = [0.330E24, 4.87E24, 5.97E24, 0.642E24, 1898E24, 568E24, 86.8E24, 102E24]
diccionario = {planet:mass for (planet,mass) in zip(planet,mass)}
print (diccionario)

#Para que salga en notación science-->
#sn = "{:e}".format(124510000000)
#print(sn)

##2) Use your dictionary to look up Earth’s mass

print("La masa terrestre es: " + str(diccionario.get('Tierra')))

##3) Loop through the data and create a list of planets whose mast is greater than 100 x 10^24 kg
planetMayores = [] 
for key, val in diccionario.items():
    if val > 100E24:
        planetMayores.append(key)
print (planetMayores)       

##4)Now add pluto to your dictionary
diccionario.update({"Pluton": 0.0130E24})
print(diccionario)

#Part III: Functions

##1. Write a function to convert temperature from kelvin to celsius
def conversorT(t,u):
    """Introduces temperatura en Kelvin y convierte a Celsius o viceversa, dependiendo de la unidad"""
    u = input("Introduce la unidad Kelvin (K) ó Celsius (C): ")    
    if u == "K":
        t = float(input("Introduce temperatura en Kelvin: "))
        return "La temperatura en Celsius es: " + str(t - 273.15)
    elif u == "C":
        t = float(input("Introduce temperatura en Celsius: "))
        return "La temperatura en Kelvin es: " + str(t + 273.15)
    else:
        print("Error en la unidad, vuelve a intentarlo.")

conversorT(input,input)

##2. Write a function to convert temperature to fahrenheit.
##Include an optional keyword argument to specify whether the input is in celcius or kelvin.
def conversorF (t, celsius=True):
    """Convierte desde C/K a Fahrenheit"""
    if celsius == True:
        t = float(input("Introduce temperatura en Celsius: "))
        return "La temperatura en Fahrenheit es: " + str((t*9/5)+32)
        
    else:
        t = float(input("Introduce temperatura en Kelvin: "))
        return "La temperatura en Fahrenheit es: " + str(((t-273.15)*9/5)+32)
    
conversorF(input)

##3.Check that the outputs are sensible by trying a few examples
conversorF(input, False)
conversorF(input)

##4. Now write a function that converts from farenheit 
##and uses a keyword argument to specify whether you want the output in celcius or kelvin
def conversorFromF (F,celsius=True):
    """Convierte desde Fahrenheit a Celsius ó Kelvin"""
    if celsius==True:
        F = float(input("Introduce temperatura en Fahrenheit: "))
        return "La temperatura en Celsius es: " + str((F-32)*5/9)
    else: 
        F = float(input("Introduce temperatura en Fahrenheit: "))
        return "La temperatura en Kelvin es: " + str(((F-32)*5/9)+273.15)

conversorFromF(input)   

##5. Write a function that takes two arguments (feet and inches) and returns height in meters

def conversorMetros(feet, inches):
    """Convierte de pies y pulgadas a metros"""
    total_inches = feet * 12 + inches
    total_meters = total_inches * 0.0254
    return "La altura en metros es: " + str(total_meters)
conversorMetros(5,2)

##6. Write a function takes one argument (height in meters) and returns two arguments
##(feet and inches)
def conversorFeetInches(metros):
    """Convierte de metros a pies y pulgadas""" """No me salió"""
    metros = float(input("Introduce la altura en metros:"))
    metros_in_ft =(( metros / 0.3048) % 1) * 12
    metros_in_in = metros_in_ft % 12
    return metros_in_ft, metros_in_in
conversorFeetInches(input)


