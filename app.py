from flask import Flask, request, jsonify

app = Flask(__name__)

# Intentional hardcoded secret for demonstration
API_KEY = "sk_prod_1234567890abcdef"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Insecure comparison - SAST should flag this
    if username == "admin" and password == "password123":
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/execute', methods=['GET'])
def execute_command():
    command = request.args.get('cmd')
    # Insecure command execution - SAST should flag this
    import subprocess
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return jsonify({"output": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)