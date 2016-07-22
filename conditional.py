from flask import Flask,render_template
app = Flask(__name__)


@app.route('/hello1/<int:score>')
def hello_name(score):
    if score < 50:
        return render_template('hello1.html',marks = score )
    else:
        @app.route('/hello3')
        def hello_name():
            return render_template('hello3.html',marks = score)

if __name__ == '__main__':
    app.run(debug = True)
    