from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
        return "app test"

if __name__ == "__main__":
    print ("Starting the application")
    app.run(host='0.0.0.0')