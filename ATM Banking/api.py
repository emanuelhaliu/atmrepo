import flask
from flask import request, jsonify
from suds.client import Client

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# client = Client("http://DESKTOP-STFORFP:8080/WebAppTest/NewWebService?wsdl")

client = Client("http://desktop-stforfp:8080/BankWebService/BankWService?wsdl")
list_of_methods = [method for method in client.wsdl.services[0].ports[0].methods]
list_of_methods


# response = client.service.Addition(1,2)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/login', methods=['POST'])
def login():
    error = None
    print(request.form['accountNum'] + ' ' + request.form['pin'])
    client = Client("http://DESKTOP-STFORFP:8080/BankWebService/BankWService?wsdl")
    response = client.service.accountLogIn(request.form['accountNum'], request.form['pin'])
    return jsonify({"isSuccess": response})
	
@app.route('/balance', methods=['POST'])
def balance():
    error = None
    print(request.form['accountNum'])
    client = Client("http://DESKTOP-STFORFP:8080/BankWebService/BankWService?wsdl")
    response = client.service.getBalance(request.form['accountNum'])
    return jsonify({"isSuccess": True, "balance": response})
	
@app.route('/withdraw', methods=['POST'])
def withdraw():
    error = None
    print(request.form['accountNum'] + " " + request.form['amount'])
    client = Client("http://DESKTOP-STFORFP:8080/BankWebService/BankWService?wsdl")
    response = client.service.accountWithdrawal(request.form['accountNum'], request.form['amount'])
    return jsonify({"isSuccess": response})
	
@app.route('/transfer', methods=['POST'])
def transfer():
    error = None
    print(request.form['accountNumFrom'] + " " + request.form['accountNumTo'] + " " + request.form['amount'])
    client = Client("http://DESKTOP-STFORFP:8080/BankWebService/BankWService?wsdl")
    response = client.service.moneyTransfer(request.form['accountNumFrom'], request.form['accountNumTo'], request.form['amount'])
    return jsonify({"isSuccess": response})

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#app.run()
app.run(host= '0.0.0.0')
