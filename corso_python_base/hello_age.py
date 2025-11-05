
from datetime import datetime

name = input("Come ti chiami? ")
age = int(input("Quanti anni hai? "))

current_year = datetime.now().year
year_100 = current_year + (100 - age)

print(f"Ciao {name}, compirai 100 anni nell'anno {year_100}!")
