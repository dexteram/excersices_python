from calendar import month
from datetime import date
import datetime


currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
month = date.strftime("%m")
day = date.strftime("%d")

dia = int(input("Ingrese el día de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))
año = int(input("Ingrese el año de nacimiento: "))

print("fecha", day, month, year)

if int(day) < dia:
    edad = int(year) - int(año) -1
elif int(day) == dia:
    if int(month) < mes:
        edad = int(year) - int(año) -1
    elif int(month) == mes:
        if int(year) < año:
            edad = int(year) - int(año) -1
        else:
            edad = int(year) - int(año)

print("Su edad es: ", edad)