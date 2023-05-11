def capicua(n):
    n = int(n)
    numinv = []*10
    num = [int(x) for x in str(n)]
    for i in reversed(num):
        numinv.append(i)
    if num == numinv:
        return "El número es capicua!"
    else:
        return "El número no es capicua"
if __name__ == "__main__":
    n=input("Escriba un numero:")
    capicua(n)