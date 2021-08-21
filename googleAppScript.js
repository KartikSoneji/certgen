function getCerts() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getDataRange().getValues().slice(1);
  console.log(data);
  for(var [name, email] of data){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "https://certs.tech/?name=" + name + "&email=" + email); 
    xmlHttp.send( null );
  }
}
