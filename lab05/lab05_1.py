from flask import Flask, request

app = Flask(__name__)

# Правильный пароль
CORRECT_PASSWORD = "secret123"

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    #time.sleep(1)  #задержка 1 секунда
    if password == CORRECT_PASSWORD:
        return "Доступ разрешен!"
    else:
        return "Неверный пароль!", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)