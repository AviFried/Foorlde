from flask import Flask, render_template

app = Flask(__name__)
posts = [
    {
        'name': "Test"
    }
]
@app.route('/')
def hello_world():
    return render_template('home.html',posts = posts)
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()