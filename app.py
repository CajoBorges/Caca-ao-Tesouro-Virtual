from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def erro(error):
    return render_template('erro.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inicio')
def p1():
    return render_template('inicio.html')
    
@app.route('/695')
def p2():
    return render_template('2.html')
    
@app.route('/935')
def p3():
    return render_template('3.html')

@app.route('/120')
def p4():
    return render_template('4.html')

@app.route('/963')
def p5():
    return render_template('5.html')

@app.route('/sopas')
def p6():
    return render_template('6.html')

@app.route('/145')
def p7():
    return render_template('7.html')

@app.route('/varvbla')
def p8():
    return render_template('8.html')
    
@app.route('/8650')
def p9():
    return render_template('9.html')

@app.route('/345')
def final():
    return render_template('final.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
