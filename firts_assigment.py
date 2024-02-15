
decimal = 3900 #int(input(f"Enter a positive number between 1 and 3999: "))

print(decimal)

if decimal % 1 == 0:
    thousand = decimal // 1000
    decimal = decimal - (thousand * 1000)
    print(thousand)
    print("decimal: ", decimal)
    
    