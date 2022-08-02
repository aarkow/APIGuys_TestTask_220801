from flask import Flask, request, abort
#Flask is a microframework for a webserver in python.

#This next line sets up the app for flask.
app = Flask(__name__)

#This is the URI that the server is is listening on.
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)

#runs the application
if __name__ == '__main__':
    app.run()