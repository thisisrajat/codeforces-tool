var request = new XMLHttpRequest;

window.onload = function() {
  document.getElementById('url').style.display = 'none';
};

function find() {
  document.getElementById('url').style.display = 'none';
  var username = document.getElementById('username').value;
  var contest = document.getElementById('contest').value;
  var problem = document.getElementById('problem').value;
  var url = '/get_solution?user=' + username + '&contest=' + contest + '&problem=' + problem
  request.open('GET', url, true);
  
  request.onreadystatechange = function() {
    if(request.readyState == 4 && request.status == 200) {
      var data = JSON.parse(request.responseText);
      document.getElementById('url').style.display = 'block';
      if(data.status === '!ok') {
        document.getElementById('url').className = 'container alert alert-danger';
        var html = "<a href = '#' class = 'red url-center'>" + data['url'] + "</a>";
        document.getElementById('url').innerHTML = html;
      } else {
        document.getElementById('url').className = 'container alert alert-success';
        var html = "<a href = '" + data['url'] + "' class='green url-center'>" + data['url'] + "</a>"
        document.getElementById('url').innerHTML = html;
      }
    }
  }
  request.send();
}