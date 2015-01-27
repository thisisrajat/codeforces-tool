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
  
  user = user.replace(' ', '')
  contest = contest.replace(' ', '')
  pid = pid.replace(' ', '')

  try:
    int(pid)
    toChar = {'1' : 'A', '2' : 'B', '3' : 'C', '4' : 'D', '5' : 'E', '6' : 'F', '7' : 'G', '8' : 'I', '9' : 'J', '10' : 'K', '11' : 'L', '12' : 'M', '13' : 'N', '14' : 'O'}
    pid = toChar[pid]
  except:
    pid = pid.upper()

  try:
    int(contest)
  except:
    return jsonify( { "status" : "!ok", "data" : "#" , "whose" : "{}".format(user), "error" : "Contest ID invalid"} )

  _solution = Solution(user, contest, pid)
  _id = _solution.compute()

  return jsonify(_id)

if __name__ == '__main__':

  if os.environ.get('HEROKU') is None:
    app.run(debug=True)
  else:
    app.run()
