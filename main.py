from flask import Flask, render_template

app = Flask(__name__, template_folder='Templates', static_folder='StaticFiles')

@app.route('/')
def hello():
    return render_template('main.html')

if __name__ == '__main__':
    app.run()