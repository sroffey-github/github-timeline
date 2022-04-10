from flask import Flask, render_template, request, flash
import requests, json

app = Flask(__name__)

def getTimeline(user):
    req = requests.get(f'https://api.github.com/users/{user}/events')
    res = req.content.decode()
    
    return res

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form['username']
        data = getTimeline(user)
        if data:
            return render_template('index.html', data=data)
        else:
            flash('Error, cannot find user!')
            return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)