from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/profile/<name>') #@decorator - way to wrap a function and modifying its behavior  "/" root directory of my home page
def profile(name): #tie the homepage with python function usualy the name is index.html
    return render_template("profile.html", name=name)


if __name__ == "__main__": #only run this script if the page is running from here !
    app.run()
#    app.run(debug=True)