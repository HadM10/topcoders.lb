from flask import Flask, render_template
from data import my_data

# create flask application
app = Flask(__name__, template_folder='templates', static_folder='static')


# main page route
@app.route('/')
def index():
    return render_template('index.html', title='Portfolio', my_data=my_data)


# run application [debug=True if dev mode, False in production mode]
if __name__ == '__main__':
    app.run(debug=False)
