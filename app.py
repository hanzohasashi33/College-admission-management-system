from flask import Flask,render_template,request,redirect,url_for


import sqlite3 as sql

app=Flask(__name__)



@app.route("/")
def index():
	return render_template("1.html")

@app.route("/home",methods=["POST"])
def login():
	name=request.form.get("name")
	password=request.form.get("password")
	if name=="student" and password=="student":
		return render_template("2.html")
	elif name=="admin" and password =="admin":
		return render_template("2a.html")
	else:
		return render_template("11.html")


@app.route("/signout")
def signout():
	return render_template("1.html")


@app.route("/about")
def about():
	return render_template("about.html")


@app.route("/register")
def register():
	return render_template("r1.html")


@app.route("/student")
def student():
	return render_template("2.html")


@app.route("/reg",methods=["POST"])
def reg():
	name=request.form.get("name")
	father=request.form.get("Father")
	number=request.form.get("number")
	email=request.form.get("email")
	rank=request.form.get("rank")
	telephone=request.form.get("telephone")
	dorm=request.form.get("dorm")


	with sql.connect("database.db") as con:
		cur=con.cursor()
		if name!="" and father!="" and number!="" and email!="" and rank!="" and telephone!="":
			cur.execute("SELECT * FROM STUDENTS WHERE num=?",(number,))
			existing=cur.fetchall()


			if existing==[]:
				cur.execute("INSERT INTO STUDENTS(name,father,num,email,rank,telephone,dorm)VALUES(?,?,?,?,?,?,?)",(name,father,number,email,rank,telephone,dorm))
			else:
				return render_template("existing.html")

		else:
			return redirect(("register"))
		con.commit()
		return render_template("success.html")
		con.close()


@app.route('/list')
def list():
	con=sql.connect("database.db")
	con.row_factory=sql.Row

	cur=con.cursor()
	cur.execute("SELECT * FROM STUDENTS")

	rows=cur.fetchall()
	return render_template("list.html",rows=rows)


@app.route('/list2')
def list2():
	con=sql.connect("database.db")
	con.row_factory=sql.Row

	cur=con.cursor()
	cur.execute("SELECT * FROM STUDENTS")

	rows=cur.fetchall()
	return render_template("list2.html",rows=rows)


@app.route("/back")
def back():
	return render_template("2.html")


@app.route("/already")
def already():
	return render_template("alread.html")

@app.route("/see",methods=['POST'])
def see():
		phone=request.form.get("num")
		con=sql.connect("database.db")
		con.row_factory=sql.Row
		cur=con.cursor()
		cur.execute("SELECT * FROM STUDENTS WHERE num=?",(phone,))
		k=cur.fetchall()

		if k!=[]:
			return render_template("list.html",rows=k)
 		else:
 			return render_template("not.html")

@app.route("/admin")
def admin():
 	return render_template("2a.html")

@app.route("/cutoff")
def cutoff():
	return render_template("cutoff.html")

@app.route("/see2",methods=['POST'])
def see2():
	rank=request.form.get("cutoff")
	con=sql.connect("database.db")
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute("SELECT * FROM STUDENTS WHERE rank<=?",(rank,))
	k=cur.fetchall()
	return render_template("list2.html",rows=k)

if __name__=="__main__":
	app.run(debug=True)
