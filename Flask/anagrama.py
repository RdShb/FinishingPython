def anagrama(a,b):
    a = str(a)
    b = str(b)
    if sorted(a) == sorted(b):
        return "Son anagramas!"
    else:
        return "No son anagramas!"

if __name__ == "__main__":
    a = input("Escriba una palabra: ")
    b = input("Escriba otra palabra: ")
    anagrama(a,b)