#-*-coding:utf8;-*-

from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)

# session çalıştırabilmek için secret_key belirlememiz gerekiyor.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

""" 
	üyeler genişletilebilir veya bir json dosyasıdan çekilebilir.
	örneğin;
	import json
	members = json.loads(open("members.json").read())
"""
members = {"gecemor":"mrblk"}

@app.route("/path")
def path():
	if not "username" in session:
		return redirect(url_for("login"))
	echo = request.args.get("echo")
	return '''
		<center><span style="color:green;font-size:30px">ECHO: {}</span></center>
	'''.format(echo)
	

@app.route("/", methods=["GET"])
def index():
	if not "username" in session:
		return redirect(url_for("login"))
	html = '''
			<center>
				<span style="color:green;font-size:30px">{} Kullanıcı adı ile giriş yapıldı!</span>
			</center>	
		'''.format(session["username"])
	return html

	
@app.route("/login", methods=["GET", "POST"])
def login():
	if "username" in session:
		return redirect(url_for("index"))
	
	html = '''
		<center>
			<form method="POST" id="loginForm">
				<span>UserName:</span>
				<input name="user" type="text" /><br>
				<span>Password:</span>
				<input name="pass" type="password" /><br>
				<input type="submit" />
			</form>
		</center>
		'''
	if request.method == "POST":
		username = request.form['user']
		password = request.form['pass']
		if members.get(username) == password:
			session['username'] = username
			return redirect(url_for("index"))
	return html
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80) # uygun olan herhangi bir port kullanılabilir.
	
	