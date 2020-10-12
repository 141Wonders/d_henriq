from flask import render_template
from landing import app

@app.route("/")
def landing():
	return render_template('work_page.html')

@app.route("/about/")
def about():
	return render_template('about.html')

@app.route("/contact/")
def contact():
	return render_template('contact.html')
