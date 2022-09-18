    # save this as app.py
from flask import Flask #escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    #name = request.args.get("name", "World")
    #return f'Hello, {escape(name)}!'
    return '<h1>Hello from Flask & Docker - rolling deployment__neu</h2>'

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=8080, debug=True)
else: 
    print('The app did not start')