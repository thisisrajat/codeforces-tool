from flask import Flask, render_template, jsonify, request
from get_solution import Solution
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('base.html', title="Codeforces Solution by Handle Name")

@app.route('/get_solution', methods=['POST', 'GET'])
def get_solution():
  user = request.args.get('user')
  contest = request.args.get('contest')
  pid = request.args.get('problem')

  try:
    int(contest)
  except:
    return jsonify( { "status" : "!ok", "url" : "Invalid Contest Id" } )

  _solution = Solution(user, contest, pid)
  _id = _solution.compute()

  return jsonify(_id)

if __name__ == '__main__':

  if os.environ.get('HEROKU') is None:
    app.run(debug=True)
  else:
    app.run()
