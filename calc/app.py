from flask import Flask, request
import operations as Op

app = Flask(__name__)

operations_dict:dict = {'add': Op.add, 'sub': Op.sub, 'mult': Op.mult, 'div': Op.div}

@app.get('/add')
def getSum():
    a = request.args['a']
    b = request.args['b']

    try:
        result = Op.add(int(a), int(b))
        return f"<p>The result of {a} + {b} is {result}.</p>"
    except:
        return f"<h2>Something went wrong.</h2>"

@app.get('/sub')
def getDiff():
    a = request.args['a']
    b = request.args['b']

    try:
        result = Op.sub(int(a), int(b))
        return f"<p>The result of {a} - {b} is {result}.</p>"
    except:
        return f"<h2>Something went wrong.</h2>"

@app.get('/mult')
def getProd():
    a = request.args['a']
    b = request.args['b']

    try:
        result = Op.mult(int(a), int(b))
        return f"<p>The result of {a} * {b} is {result}.</p>"
    except:
        return f"<h2>Something went wrong.</h2>"

@app.get('/div')
def getQuot():
    a = request.args['a']
    b = request.args['b']

    try:
        result = Op.div(int(a), int(b))
        return f"<p>The result of {a} / {b} is {result}.</p>"
    except:
        return f"<h2>Something went wrong.</h2>"

@app.get('/math/<math>')
def getCalc(math:str):
    a = int(request.args['a'])
    b = int(request.args['b'])

    try:
        result = operations_dict[math](a, b)
        return f"<p>The result of this operation is {result}.</p>"
    except:
        return f"<h2>Something went wrong.</h2>"