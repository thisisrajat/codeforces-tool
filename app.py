from flask import Flask, render_template, jsonify, request
from get_solution import Solution

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

  _solution = Solution(user, contest, pid)

  return _solution.compute()

LOCAL = True

if __name__ == '__main__':
  app.run(debug=LOCAL)