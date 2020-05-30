from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(url_for('index'))
    else:
        return render_template("login.html")

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('name', None)
    return redirect(url_for('login'))

@app.errorhandler(404)
def erro(error):
    return render_template('erro.html'), 404

@app.route('/')
def index():
    if not 'name' in session:
        return redirect(url_for('login'))
    return render_template('index.html', name = session['name'])

@app.route('/inicio')
def p1():
    return render_template('inicio.html', name = session['name'])
    
@app.route('/695')
def p2():
    return render_template('2.html', name = session['name']) 
    
    
@app.route('/935')
def p3():
    return render_template('3.html', name = session['name'])

@app.route('/120')
def p4():
    return render_template('4.html', name = session['name'])

@app.route('/963')
def p5():
    return render_template('5.html', name = session['name'])

@app.route('/sopas')
def p6():
    return render_template('6.html', name = session['name'])

@app.route('/145')
def p7():
    return render_template('7.html', name = session['name'])

@app.route('/varvbla')
def p8():
    return render_template('8.html', name = session['name'])
    
@app.route('/8650')
def p9():
    return render_template('9.html', name = session['name'])

@app.route('/345')
def final():
    return render_template('final.html', name = session['name'])



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
