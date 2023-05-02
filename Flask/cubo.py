def cubo(l):
    l = int(l)
    area = (l**2)*6
    volumen = l**3
    return f"El area es {area} y el volumen es {volumen}" 

if __name__ == "__main__":
    l=input("Escriba el tamaño del lado:")
    cubo(l)