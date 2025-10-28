from flask import Flask,jsonify

app = Flask(__name__)

contador = 0

@route('/contador',methods = ['GET'])
def obtener_contador():
 return {'contador':contador}

@rout('/contador/aumentar',methods=['POST'])
def aumentar_contador():
 contador = contador + 1 
 return {'contador':contador}

if __name__=='__main__':
 app.run(debug=True)
