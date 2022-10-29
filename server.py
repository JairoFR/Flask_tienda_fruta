from flask import Flask, render_template, request
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():


    datos = {
    'nombre': request.form['nombre'],
    'apellido' : request.form['apellido'],
    'identificacion' : request.form['student_id'],
    'strawberry' : request.form['strawberry'],
    'raspberry' : request.form['raspberry'],
    'apple': request.form['apple']
    }


    print("Cobrando a ", request.form['nombre'], int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple']),  'frutas')
    return render_template("checkout.html", datos=datos)
    

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    