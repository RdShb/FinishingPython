from flask import Flask,request
import LetraDNI
import posneg
import cubo
import numeroprimo
import anagrama
import capicua


app = Flask(__name__)

@app.route('/')
def index():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Menu Principal</title>
    </head>
    <body>
        <h1>Menu</h1>
        <label for="numero">Elegir la pagina a la que desea ir:</label>
        <form method="get" action="/dni">
            <input type="submit" value="DNI">
        </form>
        <form method="get" action="/pon">
            <input type="submit" value="Positivo o Negativo">
        </form>
        <form method="get" action="/areacubo">
            <input type="submit" value="Area y Volumen del Cubo">
        </form>
        <form method="get" action="/numeroprimo">
            <input type="submit" value="Comprobar Numero Primo">
        </form>
        <form method="get" action="/anagrama">
            <input type="submit" value="Anagramas">
        </form>
        <form method="get" action="/capicua">
            <input type="submit" value="Capicua">
        </form>
    </body>
    </html>
    """
### DNI Letra
@app.route('/dni')
def dni():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Validar DNI</title>
    </head>
    <body>
        <h1>Validar DNI</h1>
        <form method="post" action="/validar">
            <label for="numero">Número:</label>
            <input type="number" name="dni" id="dni">
            <br>
            <label for="letra">Letra:</label>
            <input type="text" name="letra" id="letra" maxlength="1">
            <br>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/validar', methods=['POST'])
def validar():
     letraDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
     dniPagWeb= request.form["dni"]
     letPagWeb= request.form["letra"]
     resultado=LetraDNI.LetraDNI(dniPagWeb,letPagWeb)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Validar DNI</title>
    </head>
    <body>
        <h1>Validacion realizada</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """
### Positivo o Negativo
@app.route('/pon')
def pon():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Positivo o Negativo</title>
    </head>
    <body>
        <h1>Positivo o Negativo</h1>
        <form method="POST" action="/posneg">
            <label for="numero">Número:</label>
            <input type="number" name="numero" id="numero">
            <br>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/posneg', methods=['POST'])
def positoneg():
     numero= request.form["numero"]
     resultado = posneg.posneg(numero)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Positivo o Negativo</title>
    </head>
    <body>
        <h1>Validacion realizada</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

### Area y Volumen Cubo
@app.route('/areacubo')
def areacubo():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Calcular Area y Volumen del Cubo</title>
    </head>
    <body>
        <h1>Calcular Area y Volumen del Cubo</h1>
        <form method="POST" action="/cubo"> 
            <label for="lado">Tamaño del lado: </label>
            <input type="number" name="ladocubo" id="ladocubo">
            <br>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/cubo', methods=['POST'])
def cbo():
     l = request.form["ladocubo"]
     resultado = cubo.cubo(l)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Cubo</title>
    </head>
    <body>
        <h1>Validacion realizada</h1>
        <p>{resultado}</p>
    </body>
    </html>
    """

### Suma par TODO
@app.route('/numeroprimo')
def numprim():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Calculo Numero Primo</title>
    </head>
    <body>
        <h1>Calculo Numero Primo</h1>
        <form method="POST" action="/valnumeroprimo">
            <label for="numero">Número:</label>
            <input type="number" name="numero" id="numero">
            <br>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/valnumeroprimo', methods=['POST'])
def valnumprim():
     numero = request.form["numero"]
     resultado = numeroprimo.numeroprimo(numero)
     return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Numero Primo</title>
    </head>
    <body>
        <h1>Validacion realizada</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

###Anagrama
@app.route('/anagrama')
def anag():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Anagramas</title>
    </head>
    <body>
        <h1>Anagramas</h1>
        <form method="POST" action="/valanagrama">
            <label for="texto">Escriba una palabra : </label>
            <input type="texto" name="palabra1" id="palabra1">
            <br>
            <label for="texto">Escriba otra palabra : </label>
            <input type="texto" name="palabra2" id="palabra2">
            <br>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/valanagrama', methods=['POST'])
def valanagrama():
    palabra1 = request.form["palabra1"]
    palabra2 = request.form["palabra2"]
    resultado = anagrama.anagrama(palabra1,palabra2)
    return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Anagramas</title>
    </head>
    <body>
        <h1>Validacion realizada</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

###Capicua
@app.route('/capicua')
def capi():
    return """
   <!DOCTYPE html>
    <html>
    <head>
        <title>Capicua</title>
    </head>
    <body>
        <h1>Capicua</h1>
        <form method="POST" action="/valcapicua">
            <label for="number">Escriba un numero: </label>
            <input type="number" name="numero1" id="numero1">
            <br>
            <input type="submit" value="Entrar">
        </form>
    </body>
    </html>
    """

@app.route('/valcapicua', methods=['POST'])
def valcapicua():
    numero1 = request.form["numero1"]
    resultado = capicua.capicua(numero1)
    return f"""
   <!DOCTYPE html>
    <html>
    <head>
        <title>Capicua</title>
    </head>
    <body>
        <h1>Validacion realizada</h1>
        <p>{resultado}</p>
    </body>
    </html>
        """

if __name__ == "__main__":
    app.run()