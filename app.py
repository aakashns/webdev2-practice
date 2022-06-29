from flask import Flask, render_template, jsonify
from database import engine

app = Flask(__name__)

def load_jobs():
  with engine.connect() as conn:
    result = conn.execute('select * from jobs')
    return list(result.mappings())

def load_job(id):
  with engine.connect() as conn:
    result = conn.execute('select * from jobs where id = ' + id)
    jobs = list(result.mappings())
    if len(jobs) == 0:
      return None
    return dict(jobs[0])

@app.route("/")
def hello_jovian():
  jobs = load_jobs()
  return render_template('home.html', 
                         jobs=jobs, 
                         company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job(id)
  if job:
    return render_template('jobpage.html', job=job)
  else:
    return "Not Found", 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)