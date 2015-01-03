from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

if __name__ == "__main__":
    print "Web Application Starting ..."
    
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 8067)

    app.run(host=host, port=port)
