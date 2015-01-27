import json, urllib, os

'''
url = http://codeforces.com/api/user.status?handle=Fefer_Ivan&from=1&count=11000
result -> contestID, problem.index, verdict
http://codeforces.com/contest/507/submission/9538072
'''

class Solution:
  
  # Default constructor

  def __init__(self, handle, contest, problemid):
    self.user = handle
    self.contest = contest
    self.problem = problemid
  
  # Downloads the file from url

  def downloadFile(self, url, name):
    urllib.urlretrieve(url, name)

  def compute(self):
    jsonFileName = '{}.json'.format(self.user)
    urlPath = 'http://codeforces.com/api/user.status?handle={}&from=1&count=99999999'.format(self.user)

    if os.path.exists(jsonFileName) == False:
      self.downloadFile(urlPath, jsonFileName)
    
    f = json.loads( open('{}.json'.format(self.user)).read() )

    if f['status'] == 'FAILED':
      return { 'status' : '!ok', 'data' : '#', 'whose': self.user, 'error' : 'No user by this handle name.'}

    for submission in f['result']:
      if submission['verdict'] == 'OK':
        if submission['contestId'] == int(self.contest) and submission['problem']['index'] == self.problem.upper():
          return {'status' : 'ok', 'data' : "http://codeforces.com/contest/{}/submission/{}".format(self.contest, submission['id']), 'whose' : '{}'.format(self.user), 'error' : ''}

    return { 'whose' : '{}'.format(self.user), 'status' : '!ok', 'error' : "No Solution matching these Parameters.", 'data' : '#'}

