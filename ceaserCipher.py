from flask import Flask,request,jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app,resources={r"/*": {"origins": "*"}})


def generate_random():
    return random.randint(1,25)


def ceaser_cipher(message,shift,mode='encryption'):
    if mode=='decryption':
        shift=-shift

    result = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-shift_base+shift)%26+shift_base)
        else:
            result += char
    return result


@app.route('/encrypted_text',methods=['POST'])
def encrypted_text():
    data = request.json
    text = data.get("text")
    shift = data.get("shift")
    shift = int(shift)

    if(shift==''):
        shift = generate_random()

    answer = ceaser_cipher(text,shift,'encryption')
    return jsonify({"encryption_text":answer,"shift":shift})


@app.route('/decrypted_text',methods=['POST'])
def decrypted_text():
    data = request.json
    text = data.get("text")
    shift = data.get("shift")
    shift = int(shift)

    if(shift==''):
        shift = generate_random()

    answer = ceaser_cipher(text,shift,'decryption')
    return jsonify({"decryption_text":answer,"shift":shift})


if __name__ == '__main__':
    app.run(debug=True)
