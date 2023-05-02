def numeroprimo(n):
    n = int(n)
    if n < 2:
        return "No es primo!"
    for i in range(2, int(n)):
        if n % i == 0:
            return "No es primo!"
    return "Es primo"
if __name__ == "__main__":
    n = int(input("Ingrese un numero: "))
    numeroprimo(n)