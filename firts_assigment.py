decimal = 10
try:
    decimal = int(input(f"Enter a positive number between 1 and 3999: "))
except:
    print("You must enter a number. Letters or special characters are not valid")

def romans_converted(decimal): 

    romans_numbers = ""

    if decimal > 0:
        thousand = decimal // 1000
        decimal = decimal - (thousand * 1000)
        
        if thousand > 0:
            for i in range(thousand):
                romans_numbers += 'M'
        
        
        nine_hundred = decimal // 900
        decimal = decimal - (nine_hundred * 900)
        
        if  nine_hundred > 0:
            for i in range(nine_hundred):
                romans_numbers += 'CM'
        
        five_hundred = decimal // 500
        decimal = decimal - (five_hundred * 500)
        
        if  five_hundred > 0:
            for i in range(five_hundred):
                romans_numbers += 'D'
        
        four_hundred = decimal // 400
        decimal = decimal - (four_hundred * 400)
        
        if  four_hundred > 0:
            for i in range(four_hundred):
                romans_numbers += 'CD'
        
        one_hundred = decimal // 100
        decimal = decimal - (one_hundred * 100)
        
        if one_hundred > 0:
            for i in range(one_hundred) :
                romans_numbers += 'C'
                
        
        ninety = decimal // 90
        decimal = decimal - (ninety * 90)
        
        if ninety > 0: 
            for i in range(ninety):
                romans_numbers += 'XC'
        
        fifty = decimal // 50
        decimal = decimal - (fifty * 50)
        
        if fifty > 0: 
            for i in range(fifty):
                romans_numbers += 'L'
        
        forty = decimal // 40
        decimal = decimal - (forty * 40)
        
        if forty > 0: 
            for i in range(forty):
                romans_numbers += 'XL'
        
        ten = decimal // 10
        decimal = decimal - (ten * 10)
        
        if ten > 0:
            for i in range(ten):
                romans_numbers += 'X'
        
        nine = decimal // 9
        decimal = decimal - (nine * 9)
        
        if nine > 0 :
            for i in range(nine):
                romans_numbers += 'IX'
        
        five = decimal // 5
        decimal = decimal - (five * 5)
        
        if five > 0 :
            for i in range(five):
                romans_numbers += 'V'
        
        four = decimal // 4
        decimal = decimal - (four * 4)
        
        if  four > 0:
            for i in range(four):
                romans_numbers += 'IV'
        
        one = decimal // 1
        decimal = decimal - (one * 1)
        
        if  one > 0:
            for i in  range(one):
                romans_numbers +=  'I'
        
        print(romans_numbers)
        
        return romans_numbers
        
    else:
        
        if decimal > 3999:
            print("You must enter a decimal value less than 3999, the value you have entered is:", decimal)    
        else:
            print("You must enter a decimal value greater than 0, the value you have entered is:", decimal) 
            
        
            
               
        
    
romans_converted(decimal)