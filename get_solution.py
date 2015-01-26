import json, urllib, os

'''
url = http://codeforces.com/api/user.status?handle=Fefer_Ivan&from=1&count=11000
result -> contestID, problem.index, verdict
http://codeforces.com/contest/507/submission/9538072
'''

class Solution:
  def __init__(self, handle, contest, problemid):
    self.user = handle
    self.contest = contest
    self.problem = problemid
  
  def download_json(self, url):
    try:
      urllib.urlretrieve(url.format(self.user), '{}.json'.format(self.user))
    except:
      raise('Internet Connection Problem')

  def compute(self):
    if os.path.exists('{}.json'.format(self.user)) == False:
      self.download_json('http://codeforces.com/api/user.status?handle={}&from=1&count=1000000')
    
    f = json.loads( open('{}.json'.format(self.user)).read() )
    for submission in f['result']:
      if submission['verdict'] == 'OK':
        if submission['contestId'] == int(self.contest) and submission['problem']['index'] == self.problem.upper():
          return "http://codeforces.com/contest/{}/submission/{}".format(self.contest, submission['id'])

