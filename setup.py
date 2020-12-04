from flaskr import create_app
from flask import render_template, redirect, url_for

app = create_app()

#home
@app.route('/')
def home():
    return render_template('home.html')

#redirect
@app.errorhandler(404)
def redirect_main_page(error):
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
