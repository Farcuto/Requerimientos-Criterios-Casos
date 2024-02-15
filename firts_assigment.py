
decimal = 4 #int(input(f"Enter a positive number between 1 and 3999: "))

print(decimal)

if decimal % 1 == 0:
    thousand = decimal // 1000
    decimal = decimal - (thousand * 1000)
    print("M: ", thousand)
    print("decimal: ", decimal)
    
    nine_hundred = decimal // 900
    decimal = decimal - (nine_hundred * 900)
    print("CM: ",nine_hundred)
    print("decimal: ", decimal)
    
    five_hundred = decimal // 500
    decimal = decimal - (five_hundred * 500)
    print("D: ",five_hundred)
    print("decimal: ", decimal)
    
    four_hundred = decimal // 400
    decimal = decimal - (four_hundred * 400)
    print("CD: ",four_hundred)
    print("decimal: ", decimal)
    
    one_hundred = decimal // 100
    decimal = decimal - (one_hundred * 100)
    print("C: ",one_hundred)
    print("decimal: ", decimal)
    
    ninety = decimal // 90
    decimal = decimal - (ninety * 90)
    print("XC: ",ninety)
    print("decimal: ", decimal)
    
    fifty = decimal // 50
    decimal = decimal - (fifty * 50)
    print("L: ",fifty)
    print("decimal: ", decimal)
    
    forty = decimal // 40
    decimal = decimal - (forty * 40)
    print("XL: " ,forty)
    print("decimal: ", decimal)
    
    ten = decimal // 10
    decimal = decimal - (ten * 10)
    print("X: ",ten)
    print("decimal: ", decimal)
    
    nine = decimal // 9
    decimal = decimal - (nine * 9)
    print("IX: ",nine)
    print("decimal: ", decimal)
    
    five = decimal // 5
    decimal = decimal - (five * 5)
    print("V: ",five)
    print("decimal: ", decimal)
    
    four = decimal // 4
    decimal = decimal - (four * 4)
    print("IV: ",four)
    print("decimal: ", decimal)
    
    one = decimal // 1
    decimal = decimal - (one * 1)
    print("I: ",one)
    print("decimal: ", decimal)
    
    
    