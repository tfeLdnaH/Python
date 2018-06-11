from flask import Flask, request

app = Flask(__name__)
@app.route('/') #@decorator - way to wrap a function and modifying its behavior  "/" root directory of my home page
def index(): #tie the homepage with python function usualy the name is index.html
    return 'This the homepagexxx'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is health</h2>'


@app.route('/profile/<username>')
def profile(username):
    return "Hey guys %s" % username


@app.route('/post/<int:post_id>')
def post(post_id):
    return "Looks goood postid: %s" % post_id


@app.route('/requestt')
def requestt():
    return 'Method used: %s' % request.method

if __name__ == "__main__": #only run this script if the page is running from here !
    app.run()
#    app.run(debug=True)