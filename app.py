from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
    'id' : 1,
    'title': 'Data Analyst',
    'location' : 'Chennai',
    'salary' : 'Rs. 30,00,000'
},
{
    'id' : 2,
    'title': 'ML engineer',
    'location' : 'Antartica',
    'salary' : '$120,000'
},
{
    'id' : 3,
    'title': 'VLSI engineer',
    'location' : 'Ohio',
    'salary' : '$250,000'
},
{
    'id' : 4,
    'title': 'Salesman',
    'location' : 'North Korea',
    'salary' : '₩. 4,200,000'
},
{
    'id' : 5,
    'title': 'QA Tester',
    'location' : 'Remote',
}
]

#template
@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS , company_name='open' )

#api
@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

#host
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
