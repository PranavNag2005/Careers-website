from flask import Flask, render_template

app = Flask(__name__)

Jobs = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs.10,00,000'
}, {
    'id': 2,
    'title': 'Data scientist',
    'location': 'Hyderabad, India',
    'salary': 'Rs.12,00,000'
}, {
    'id': 3,
    'title': 'Front end Developer',
    'location': 'Remote',
    'salary': 'Rs.5,00,000'
}, {
    'id': 4,
    'title': 'Backend Developer',
    'location': 'california, U.S.A',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=Jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
