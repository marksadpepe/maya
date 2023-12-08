from flask import Flask, render_template, request, jsonify
import maya

app = Flask(__name__)
mobj = maya.Maya()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendMessage', methods=['POST'])
def send_message():
    user_input = request.json['message']
    m_mes = mobj.send_message_and_get_content(message=user_input)
    return jsonify(message=m_mes)

app.run(debug=True)