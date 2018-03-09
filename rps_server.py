from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThiIsSecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process/rock', methods=['POST'])
def rock():
	print('button was pushed')
	print(request.form['rock'])
	return redirect('/')

@app.route('/process/paper', methods=['POST'])
def paper():
	print('button was pushed')
	print(request.form['paper'])
	return redirect('/')

@app.route('/process/scissors', methods=['POST'])
def scissors():
	print('button was pushed')
	print(request.form['scissors'])
	return redirect('/')

app.run(debug=True)


	# session['rock'] = request.form['name']
	# session['paper'] = request.form['name']
	# session['scissors'] = request.form['name']