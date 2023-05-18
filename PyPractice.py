from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def hello():
    # print("Hello! I am PyApp!")
    # a = input("What's your name? : ")
    # b = str("Hey! Welcome " + a + "! You're Awesome!")
    # return b
    return "Hello! Welcome to Simple Python App!"

# """Run the app server on localhost:4449"""
# from waitress import serve
# serve(app, host="0.0.0.0", port=8080)


if __name__ == '__main__':
    app.run()
