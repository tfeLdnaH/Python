from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/') #@decorator - way to wrap a function and modifying its behavior  "/" root directory of my home page
@app.route('/<user>')
def index(user=None): #none by default if is not pass value
    return render_template("user.html", user=user)


@app.route('/shopping')
def shopping():
    food = ['Cheese', 'Tuna', 'Beef']
    return render_template("shopping.html", food=food)


if __name__ == "__main__": #only run this script if the page is running from here !
    app.run()
#    app.run(debug=True)