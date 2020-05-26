$(function() {

  try {
    if(js){
      charc();
    }
    function charc()
    {
      $('.charc').each(function(){
        var el= $(this);
        var textLength = el.html().length;
        if (textLength > 0) {
          el.css('font-size', '0.9em');
        }
        if (textLength > 3) {
          el.css('font-size', '0.8em');
        }
        if (textLength > 6) {
          el.css('font-size', '0.7em');
        }
        if (textLength > 9) {
          el.css('font-size', '0.6em');
        }
        if (textLength > 12) {
          el.css('font-size', '0.5em');
        }
        if (textLength > 15) {
          el.css('font-size', '0.4em');
        }
        if (textLength > 18) {
          el.css('font-size', '0.3em');
        }
      });
    }
  }
  catch(error) {
    alert('shithappns');
  }

});
