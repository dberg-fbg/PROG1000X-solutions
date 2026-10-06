import math
half_time = 5730 # Halveringstid T angivet i år
decay_constant = math.log(2) / half_time # lambda 

t = int(input("Ange antalet år: "))

remaining = math.exp(-decay_constant * t)
print(f"Efter {t} år återstår {remaining * 100: .02f}%")
