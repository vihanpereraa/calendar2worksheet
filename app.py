function getEvents(){


var ss = SpreadsheetApp.getActiveSpreadsheet();
var sheet = ss.getSheetByName("Mainv2");


var calendar = CalendarApp.getCalendarById("vihanperera334@gmail.com");
var events = calendar.getEvents(new Date("1/20/2023 12:00 AM"), new Date("12/30/2023 12:00 AM" ));

for(var i = 0;i<events.length;i++){
  var title = events[i].getTitle();
  var start_time = events[i].getStartTime();
  var end_time = events[i].getEndTime();
  var location = events[i].getLocation();

sheet.getRange(i+2,1).setValue(title)
sheet.getRange(i+2,2).setValue(start_time)
sheet.getRange(i+2,3).setValue(end_time)
sheet.getRange(i+2,4).setValue(location)

Logger.log("Events added.");

Logger.log("Verison1")
##this is only vrsion 1 it doesn't automatically update the sheets if you rsvp
#yes or convert the time to  hours/minutes

}









}