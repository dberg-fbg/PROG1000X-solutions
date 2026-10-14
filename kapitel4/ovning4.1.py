smallest = 2**64 - 1
largest = 0
while True:
    n = int(input("Mata in ett tal: "))
    if n < 0:
        break
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print(f"{largest=}, {smallest=}")
