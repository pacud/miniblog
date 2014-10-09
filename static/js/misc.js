function getDate(today) {
	if (today == undefined) {
        var today = new Date();
	}
    var d = (today.getDate() < 10 ? '0'+today.getDate() : ''+today.getDate());
    var m = ((today.getMonth() + 1) < 10 ? '0'+(today.getMonth() + 1) : ''+(today.getMonth() + 1) ); // january is 0
    var y = today.getFullYear();
    return y+'-'+m+'-'+d;
}

function getDateTime() {
	var today = new Date();
	date = getDate(today);
	var h = (today.getHours() < 10 ? '0'+today.getHours() : ''+today.getHours());
	var m = (today.getMinutes() < 10 ? '0'+today.getMinutes() : ''+today.getMinutes());
	var s = (today.getSeconds() < 10 ? '0'+today.getSeconds() : ''+today.getSeconds());
	var tz = today.getTimezoneOffset() / 60;
	if (tz >= 0) { //in case of positive or null offset get +01 or +14
		tz = (tz < 10 ? '+0'+tz : '+'+tz);	}
	else { //in case of negative offset get -01 or -14
		tz = ( tz > -10 ? '-0'+(tz * -1) : ''+tz )
	}
	return date+'T'+h+':'+m+':'+s+tz+':00'
}