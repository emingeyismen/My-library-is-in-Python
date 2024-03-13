def getInt(prompt):
    while True:
        veri = input(prompt)
        try:
            veri = int(veri)
            break
        except ValueError:
            print("Girilen değer bir tam sayı değil.")
    return veri        
            

def getPozitifInt(prompt2):
    while True:
        result = getInt(prompt2)
        if result > 0:
            return result
        else:
            print("Girilen değer pozitif bir tamsayı değil.")
        

def getNegatifInt(prompt3):
    
    while True:
        result = getInt(prompt3)
        if result < 0:
            return result
        else:
            print("Girilen değer negatif bir tamsayı değil.")

def myUpper():
    veri = input("bir kelime giriniz ")
    return veri.upper()

def myLower():
    veri = input("bir kelime giriniz ")
    return veri.lower()

