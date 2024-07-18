from flask import Flask, redirect, render_template, url_for, request

from flask import session as login_session


app = Flask(__name__, template_folder = "templates", static_folder = "static")

app.config['SECRET_KEY'] = "Your_secret_string"

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/naz")
def naz():
	return render_template("Nazereth.html")

@app.route("/tlv", methods=["GET","POST"])
def tlv():
	if request.method=="POST":
		selected_food = request.form['food']
		print(login_session)
		login_session['food_naz'] = selected_food
		print(login_session)


	return render_template("Tel Aviv.html")

@app.route("/jlm" , methods=['GET','POST'])
def jlm():
	if request.method=="POST":
		selected_food = request.form['food']
		print(login_session)
		login_session['food_tlv'] = selected_food
		print(login_session)
	return render_template("Jerusalem.html")

@app.route("/fnl", methods=['GET','POST'])
def fnl():
	if request.method=="POST":
		selected_food = request.form['food']
		print(login_session)
		login_session['food_jer'] = selected_food
		print(login_session)
	return render_template("final.html")

if __name__ == '__main__':
	app.run(debug=True)
