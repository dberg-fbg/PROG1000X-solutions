sek = int(input("Ange antalet sekunder: "))

tim = sek // 3600 # på en timme är det 60*60 = 3600 sekunder
sek = sek % 3600 # antalet sekunder som återstår efter vi dividerat med 3600

min = sek // 60

sek = sek % 60

print(f"{tim}h:{min}m:{sek}s")
