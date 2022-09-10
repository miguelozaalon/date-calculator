#!/usr/bin/python3

from datetime import datetime, MINYEAR, MAXYEAR

today = datetime.date(datetime.today())

print(today)


year = int(input('Introduce el año: '))
while year > MAXYEAR or year < MINYEAR:
    year = int(input('Introduce el año de nuevo (Entre el año 1 y el 9999): '))
month = int(input('Introduce el mes (en número): '))
while month > 12 or month < 1:
    month = int(input('Introduce el mes (Entre el 1 y el 12): '))
day = int(input('Introduce el día: '))

dayToCompare = datetime.date(datetime(year, month, day))

print(abs(today - dayToCompare))