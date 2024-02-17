function doGet() {
  var ss = SpreadsheetApp.openByUrl('https://docs.google.com/document/d/1Qz0jqi1lAtIz6wdGIMiG2fTg630jVtwW_uL5553KlFw/edit" target="_blank');
  var sheet = ss.getSheets()[0];
  var data = sheet.getDataRange().getValues();

  var jsonData = [];
  var headers = data[0];

  for (var i = 1; i < data.length; i++) {
    var row = data[i];
    var rowData = {};

    for (var j = 0; j < headers.length; j++) {
      rowData[headers[j]] = row[j];
    }

    jsonData.push(rowData);
  }

  var result = JSON.stringify(jsonData);

  return ContentService.createTextOutput(result)
    .setMimeType(ContentService.MimeType.JSON);
}