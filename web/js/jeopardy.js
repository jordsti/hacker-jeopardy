var serverAddr = ""
var serverKey = ""
var serverVersion = 1
var teams = new Array()
var categories = new Array()

function hideTeams() {
  
  if($("#teams-div").is(":visible")) {
    $("#teams-div").hide()
    $("#teams-hide-btn").text("Show Teams")
  } else {
    $("#teams-div").show()
    $("#teams-hide-btn").text("Hide Teams")
  }
}

function getGameState() {

    var url = serverAddr + "/game/state"
    var req = $.ajax({
        url: url,
        crossDomain: true,
        dataType: "json"
    }).done(function(data){

        var game_on = data.game_on
        var state = data.state

        if(game_on) {
            $("#game_on").text("On going")
        } else {
            $("#game_on").text("Waiting to start the game")
            $("#game_on").append('<br /><button type="button" class="btn btn-primary" onclick="startGame();" id="btn-start-game">Start game</button>')
        }

        $("#game_state").text(data.defs[state])
    })
}

function addTeam() {
  teamName = $("#team-name").val()
  var url = serverAddr + "/team/add?key=" + serverKey + "&name=" + teamName
  
  req = $.ajax({
    url: url,
    crossDomain: true,
    dataType: "json"
  }).done(function(data) {
    if(data.func_error) {
    
      if($("#teams-alert").length == 0) {
	$("#teams-div").prepend('<div id="teams-alert" class="alert alert-danger" role="alert">'+data.func_error+'</div>')
      }
    } else {
      $("#teams-alert").remove()
    }
  });
  
  loadTeams();
}

function removeTeam(teamId) {
  url = serverAddr + "/team/remove?key=" + serverKey + "&team=" + teamId
  req = $.ajax({
    url: url,
    crossDomain: true,
    dataType: "json"
  })
  
  loadTeams();
}

function loadTeams() {
  
  $("#teams-list").empty()
  
  url = serverAddr + "/team/all"
  req = $.ajax({
    url: url,
    crossDomain: true,
    dataType: "json"
  }).done(function(data) {
    console.log(data)
    
    if(data.teams) {
      teams = data.teams
      for(var i=0; i<data.teams.length; i++) {
	var team = data.teams[i]
	$("#teams-list").append('<div id="team-info">'+team.name+' : '+team.points+' - <a onclick="removeTeam('+team.id+')">Remove</a></div>')
      }
    }
    
  });
}

function refreshCategories() {
  $.ajax({
    url: serverAddr + "/category/ranks",
    crossDomain: true,
    dataType: "json"
  }).done(function(data){
    console.log(data)
    if(data.categories) {
      categories = data.categories
    }
  })
  
}

function loadCategories() {
  
  var cats = new Array()
  
  $.ajax({
    url: serverAddr + "/category/all",
    crossDomain: true,
    dataType: "json"
  }).done(function(data){
    console.log(data)
    if(data.categories) {
      cats = data.categories
      for(var i=0; i<data.categories.length; i++) {
	if(i < 4) {
	  div_id = "#cat_head_"+i
	  console.log(div_id)
	  $(div_id).text(data.categories[i].name)
	  console.log(data.categories[i].name)
	}
      }
    }
  })
  
  $.ajax({
    url: serverAddr + "/points/table",
    crossDomain: true,
    dataType: "json"
  }).done(function(data){
    console.log(data)
    if(data.ranks) {
      for(var i=0; i<data.ranks.length; i++) {
	var html = '<div class="row" id="row_rank_'+i+'">'
	
	for(var j=0; j<cats.length; j++) {
	  rank_id = "rank_" + j + "_" + i
	  html += '<div class="col-sm-3 category-rank" id="'+rank_id+'">'+data.ranks[i].points+'</div>'
	}
	
	html += '</div>'
	$("#categories").append(html)
      }
    }
  })
  
  refreshCategories();
  
}

function connectToServer() {
  
  serverAddr = $("#server-addr").val()
  serverKey = $("#server-key").val()
  form = $("#connection-form")
  connection = $("#connection-div")
  //testing if the avaiable function are retrieved
  req = $.ajax({
    url: serverAddr,
    crossDomain: true,
    dataType: "json"
  })
    .done(function(data) {
      
      if(data.version != serverVersion) {
	if($("#server-alert").length == 0) {
	  form.prepend('<div id="server-alert" class="alert alert-danger" role="alert">Server version is invalid</div>')
	}
      } else {
	console.log("Version is "+serverVersion+", this version is supported")
	//testing the key
	keytest = $.ajax(
	  {
	    url: serverAddr + "/key?key=" + serverKey,
	    crossDomain: true,
	    dataType: "json"
	  }
	).done(function(data) {
	  if(data.valid) {
	    console.log("Server key is valid")
	    connection.remove()
	    
	    $("#teams").show()
	    
	        
	    loadTeams();
	    loadCategories();
	    getGameState();
	  } else {
	    if($("#server-alert").length == 0) {
		form.prepend('<div id="server-alert" class="alert alert-danger" role="alert">Server key is invalid</div>')
	    }
	  }
	})
      }
      
    })
    .fail(function() {
      if($("#server-alert").length == 0) {
	form.prepend('<div id="server-alert" class="alert alert-danger" role="alert">Server is not responding</div>')
      }
    })
    ;
}