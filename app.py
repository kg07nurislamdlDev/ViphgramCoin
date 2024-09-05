from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/auth', methods=['GET'])
def auth():
    # Төмөнкүдөй код Telegram Web App'та авторизациялоо үчүн пайдаланылат
    data = request.args
    user_id = data.get('user_id')
    # Сервердик логикаңызды бул жерде түзүңүз
    return jsonify({"status": "success", "user_id": user_id})

if __name__ == '__main__':
    app.run(debug=True)
