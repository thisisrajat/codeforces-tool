window.onload = function() {
  document.getElementById('wrapper').innerHTML = '';
};

function get() {
  document.getElementById('wrapper').innerHTML = '';
  var usersList = document.getElementById('username').value;
  var contest = document.getElementById('contest').value;
  var problem = document.getElementById('problem').value;
  usersList = usersList.split('+');

  for(var i = 0; i < usersList.length; i++) {
    findSolutionId('/get_solution?user=' + usersList[i] + '&contest=' + contest + '&problem=' + problem);
  }
}

function findSolutionId(url) {
  var request = new XMLHttpRequest();
  request.open('GET', url, true);
  request.onreadystatechange = function() {
    if(request.readyState == 4 && request.status == 200) {
      var response = JSON.parse(request.responseText);
      if(response.status === '!ok') {
        var html = htmlToAppend('alert-danger', 'red', response.data, response.whose, response.error);
        document.getElementById('wrapper').innerHTML += html;
      }
      else {
        var html = htmlToAppend('alert-success', 'green', response.data, response.whose, response.error);
        document.getElementById('wrapper').innerHTML += html;
      }
    }
  }
  request.send();
}

function htmlToAppend(alertType, colorType, url, whose, error) {
  var html = "<div role = 'alert' class = 'alert " + alertType + " urlbox'>";
  html += "<a class = '" + colorType + "' href = '" + url + "'>";
  html += whose;
  if(error !== '') {
    html += ": " + error;
  } else {
    html += "'s solution :)"
  }
  html += "</a></div>"
  return html;
}