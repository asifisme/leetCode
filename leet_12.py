def RomanInteger(num: int):
    roman_map = {
            "M"     : 1000,
            "CM"    : 900,
            "D"     : 500,
            "CD"    : 400,
            "C"     : 100,
            "XC"    : 90,
            "L"     : 50,
            "IL"    : 40,
            "X"     : 10,
            "IX"    : 9,
            "V"     : 5,
            "IV"    : 4,
            "I"     : 1, 
        }
    roman_map = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4),
        ('I', 1)
    ]

    res_roman = '' 
    for i, v in roman_map.items():
        while num >= v:
            res_roman += i 
            num -= v 
    return res_roman 

print(RomanInteger(58))