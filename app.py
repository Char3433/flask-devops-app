from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        message = request.form.get('message')
        if username and message:
            messages.append({'username': username, 'message': message})
        return redirect('/')
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
