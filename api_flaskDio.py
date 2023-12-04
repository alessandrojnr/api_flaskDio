from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

sheet = [{
    "Number": 1,
    "Name": "Mahesh",
    "Age": 25,
    "City": "Bangalore",
    "Country": "India"
}, {
    "Number": 2,
    "Name": "Alex",
    "Age": 26,
    "City": "London",
    "Country": "UK"
},
    {
    "Number": 3,
    "Name": "David",
    "Age": 27,
    "City": "San Francisco",
    "Country": "USA"
},
    {
    "Number": 4,
    "Name": "John",
    "Age": 28,
    "City": "Toronto",
    "Country": "Canada"
},
   {
    "Number": 5,
    "Name": "Chris",
    "Age": 29,
    "City": "Paris",
    "Country": "France"
}
]

@app.route('/index')
def home():
  return sheet

run_with_ngrok(app)
app.run()