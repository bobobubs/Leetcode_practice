def romanToInt(self, s: str) -> int:
    #look at the string in groups of two
    #If the group of two is IV, IX, XL, XC, CD, CM handle these cases uniquely
    #Otherwise add the two characters in the 2 -string independently. 
    
    weights = {
        'I': 1, 
        'V': 5,
        'X': 10, 
        'L': 50,
        'C': 100,
        'D': 500, 
        'M':1000,
    }
        
    unique_combos = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
    }

    # handdle the base case
    if len(s) == 1:
        return weights(s)





    

