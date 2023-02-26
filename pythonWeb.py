from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def post_handler():
    print("Success");
    return {'status': 'success', 'message': 'Received data successfully'}

if __name__ == '__main__':
    app.run(debug=True)
