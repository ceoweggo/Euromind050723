from flask import Flask, render_template

app = Flask(__name__)

## APPLICATION SETTINGS

## ROUTES
class Routes:

    @app.route("/")
    def homepage():
        return render_template('index.html')

## ERRORS

## APPLICATION RUN
app.run(port=5000,debug=True)