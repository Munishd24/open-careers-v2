from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

# database stored in cloud
def load_jobs_from_db():
    
    with engine.connect() as conn:
        result = conn.execute(text("Select * from jobs"))

        jobs = []
        for row in result.all():
            jobs.append(row._mapping)
        return jobs 
    
#template
@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs , company_name='open' )

#api
@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

#host
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
