from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
return "En construction"
if __name__ == '__main__':
app.run(port=5050, debug=True)
