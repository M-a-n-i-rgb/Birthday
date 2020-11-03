// Javascript
$(function() {
  var currentDate = new Date();
  $('.time').countdown("2020/11/05/00:00:00", function(event)

	{
    $this = $(this);
    switch(event.type) {
      case "seconds":
      case "minutes":
      case "hours":
      case "days":
      case "weeks":
      case "daysLeft":
        $this.find('span.'+event.type).html(event.value);
        break;
      case "finished":
        $this.fadeTo('slow', .5);
        document.getElementById("demo").innerHTML="<a href ='latern.html'>NEXT!!</a>" ;
        break;
    }
  });
});
