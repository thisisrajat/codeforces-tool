var x = new XMLHttpRequest;

function find() {
  var username = document.getElementById('username').value;
  var contest = document.getElementById('contest').value;
  var problem = document.getElementById('problem').value;
  var url = '/get_solution?user=' + username + '&contest=' + contest + '&problem=' + problem

  x.open('GET', url, true);
  x.onreadystatechange = function() {
    if(x.readyState == 4 && x.status == 200) {
      document.getElementById('url').href = x.responseText;
      document.getElementById('url').innerHTML = x.responseText; 
    }
  }
  x.send();
}