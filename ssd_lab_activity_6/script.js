function validate_username() {
	var name = document.getElementById("username").value;
	var i = 0;
	var character = '';
	var uc = 0;
	var num = 0;

	while (i < name.length){
    	character = name.charAt(i);
    	
    	if (isUpperCase(character)) {
            uc = 1;
        }
        if (!isNaN(character * 1)) {
        	num = 1;
        }
    	
    	i = i + 1;
	}

	if (uc == 1 && num == 1) {
		document.getElementById("check_username").innerHTML("Valid");
	}
	else {
		document.getElementById("check_username").innerHTML("Invalid username");
	}
}

function validate_password() {
	var pass1 = document.getElementById("server_password").value;
	var pass2 = document.getElementById("server_password_confirm").value;

	if (pass1 != pass2) {
		alert("Passwords do not match");
		return false;
	}
	return true;
}

function onsubmitbutton() {
	alert("Hi");
}

function allowDrop(event) {
  event.preventDefault();
}

function drag(event) {
  event.dataTransfer.setData("text", event.target.id);
}

function drop(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  event.target.appendChild(document.getElementById(data));
}