from flask import Flask
from flask import request
from flask import render_template
import main as m

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/busqueda')
def busqueda():
    return render_template('busqueda.html')

@app.route('/resultados')
def resultados():

    user_input = request.args.get("user_input")
    address_list = user_input.split(',')
    results_list = list()
    results_list.append(('Valor buscado','Latitud','Longitud','Direccion'))
    
    for items in address_list:
        a = m.get_latlon(items)
        new_line = (items,a['lat'], a['lon'], a['f_add'])
        results_list.append(new_line)
    
    return render_template('resultados.html',results_list=results_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)