$(function() {

    try {
        //check if js is on
        if(js){
            boom();
        }
        function boom()
        {
            $('.triangulum').addClass('hiding');
            $('.boxes').addClass('hiding');

            setTimeout(function(){
                $('.triangulum').addClass('showing');
                $('.boxes').addClass('showing');
            }, 2100);

            setTimeout(function(){
                //set boxes rock => no move but position: absolute for 700 while triangulum moves
                $('.boxes').addClass('rock');
                $('.boxes').removeClass('showing');
            }, 2800);
        }
    }
    catch(error) {
        alert('shithappns');
    }

});
