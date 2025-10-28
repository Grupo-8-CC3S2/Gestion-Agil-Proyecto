from flask import Flask,jsonify
import os
app = Flask(__name__)

ARCHIVO = "contador.txt"

def cargar_contador():
 if os.path.exists(ARCHIVO):
  with open(ARCHIVO,'r') as f:
   try:
    return int(f.read().strip())
   except ValueError:
    return 0
 return 0

def guardar_contador(valor):
 with open(ARCHIVO,'w') as f:
  f.write(str(valor))

contador = cargar_contador()


@app.route('/contador',methods = ['GET'])
def obtener_contador():
 return {'contador':contador}

@app.route('/contador/aumentar',methods=['POST'])
def aumentar_contador():
 contador = contador + 1 
 guardar_contador(contador)
 return {'contador':contador}

@app.route('/contador/resetear',methods =['POST'])
def resetear_contador():
 contador = 0
 guardar_contador(contador)
 return {'contador':contador}

if __name__=='__main__':
 app.run(debug=True)
