from flask import Flask, render_template
progress = Flask(__name__)

@progress.route('/')
def hello_world():
    author = "butt"
    name = "a butt"
    return render_template('index.html', author=author, name=name)

if __name__ == '__main__':
    progress.run()