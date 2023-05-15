from flask import Flask

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Harsh And Vivek Project


# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/hello')
def hello():
    print("Hello! I am PyApp!")
    a = input("What's your name? : ")
    b = str("Hey! Welcome " + a + "! You're Awesome!")
    return b

# """Run the app server on localhost:4449"""
# from waitress import serve
# serve(app, host="0.0.0.0", port=8080)


if __name__ == '__main__':
    app.run()
