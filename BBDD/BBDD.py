import random
from pymongo.mongo_client import MongoClient

personas = []
resultados = {}

def connectdb():
    #cliente
    clientDB = MongoClient('mongodb://localhost:27017/')
    #Base de Datos
    db = clientDB["Listas"]
    #Comprobacion
    resultado = db.command('serverStatus')
    print('Host:',resultado['host'])
    print('Version:',resultado['version'])
    print('Process:',resultado['process'])
    print(clientDB.list_database_names())
    # #Coleccion
    col = db["Lista1"]
    return clientDB

def CreateDB(name,clientDb):
    database_name=name 
    db=clientDb[database_name]
    return db

def createCollection(name,db):
    collection_name=name
    collection=db[collection_name]
    return collection

def generar(personas):
    personas.clear()
    for i in range(0,100):
        genero=random.randint(0,1) #0 para mujeres y el 1 para hombres
        if (genero ==1):
            personas.append("H")
        else:
            personas.append("M")
    print(personas)

def recuperar(personas):
    num_id = input("Escriba el numero id de la lista que busca: ")         
    query={"_id":num_id}
    a = col.find_one(query)
    if a != None:
        print (a)
        personas = a["Genero"]
        return (personas)
    else: 
        print("Esa lista no existe, generado una nueva. ")
        generar(personas)
        guardar(col, personas, resultados)
         

def guardar(col, personas, resultados):
    dictPersonas = {}
    clave = "Genero"
    dictPersonas[clave] = []
    for i in personas:
        dictPersonas[clave].append(i)
    numid = input("Escriba el numero id con el que desea guardar esta lista: ")
    dictPersonas["_id"] = numid
    dictPersonas["Resultados"] = resultados
    col.insert_one(dictPersonas)

def calcular(personas):
    contadorH = 0
    contadorF = 0
    total = 0
    for i in range(0,100):
        if personas[i] == "H":
            contadorH += 1
            total +=1
        else:
            contadorF += 1
            total += 1
    porcentajeH = (contadorH/total)*100
    porcentajeF = (contadorF/total)*100
    print(f"En la lista hay {contadorF} mujeres y {contadorH} hombres")
    print(f"Hay un {porcentajeF}% de mujeres y un {porcentajeH}% de hombres")
    resultados = {"Total Personas" : total,
                    "Mujeres" : contadorF,
                    "Hombres" : contadorH,
                    "Porcentaje de Mujeres" : porcentajeF,
                    "Porcentaje de Hombres" : porcentajeH
                    }
    return resultados

if __name__ == "__main__":
    client=None
    db=None
    col=None
    client=connectdb()
    db=CreateDB('Listas',client)    
    col=createCollection('Lista1',db)  
    # generar(personas)
    # calcular(personas)
    # guardar(col, personas, resultados)
    # recuperar(personas)
    while 1:
        print('1 - Generar una nueva lista ')
        print('2 - Recuperar una lista guardada ')
        print('3 - Guardar una lista generada ')
        print('4 - Calcular los resultados estadisticos de la lista en uso ')
        print('0 - Salir del programa')
        b=input('Elegir una opcion:')
        if b == "1":
            generar(personas)
        elif b == "2":
            recuperar(personas)
        elif b == "3":
            guardar(col, personas, resultados)
        elif b == "4":
            calcular(personas)
        elif b == "0":
            break
        else:
            print('Opcion invalida')
        follow=input("Enter para continuar: ")