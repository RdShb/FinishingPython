def posneg(n):
    n = int(n) 
    if n < 0:
        return "Es negativo"
    elif n > 0:
        return "Es positivo"
    else:
        return "Es 0"
if __name__ == "__main__":
    n=input("Escriba un numero:")
    posneg(n)