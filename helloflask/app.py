from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return f'<h1>Hello,<em>{name}</em>!</h1><p>I am super excited to learn Flask.</p>'
    return "Hello, world!"

# create another route like '/square/<number>', so the webapp will display the square of the number

@app.route('/square/')
@app.route('/square/<number>')
def square(number=None):
    if number:
        result = float(number)**2
        return str(result)
    return "You need to provide a number"
    
    

if __name__=="__main__":
    app.run(debug=True)