def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        dct={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        }
        sub = {
        "IV":4,
        "IX":9,
        "XL":40,
        "XC":90,
        "CD":400,
        "CM":900,
        }
        aux = 0
        while len(s) != 0:
            for i in sub:
                if s.find(i) != -1:
                    aux += sub[i] 
                    s = s.replace(i, "")
            for i in dct:
                if s.find(i) != -1:
                    aux += dct[i]
                    s = s[0:s.find(i)]+s[s.find(i)+1:]
        return aux
                
        

s = "LVIII"
print(romanToInt(s))
        
