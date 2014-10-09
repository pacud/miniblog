function getDate() {
    var today = new Date();
    var d = (today.getDate() < 10 ? '0'+today.getDate() : ''+today.getDate());
    var m = ((today.getMonth() + 1) < 10 ? '0'+(today.getMonth() + 1) : ''+(today.getMonth() + 1) ); // january is 0
    var y = today.getFullYear();
    return y+'-'+m+'-'+d;
}