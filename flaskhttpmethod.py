from flask import Flask, request

app = Flask(__name__)
@app.route('/') #@decorator - way to wrap a function and modifying its behavior  "/" root directory of my home page
def index(): #tie the homepage with python function usualy the name is index.html
    return 'Method used: %s' % request.method


@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return  "u r using method post"
    else:
        return 'problably are u using GET'






if __name__ == "__main__": #only run this script if the page is running from here !
    app.run()
#    app.run(debug=True)