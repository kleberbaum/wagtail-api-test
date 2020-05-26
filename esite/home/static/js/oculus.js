$(function() {

    try {
        if(js){
            oculus();
        }
        function oculus()
        {
            var oldabout = $('input:checked + .about-s');

            $('input:radio[name=radioabout]').change(function() {

                oldabout.addClass('oldabout');

                $('.about').css({height:($('input:checked + .about-s').height()+'px')});

                setTimeout(function(){
                    $('.about').css({height: 'auto'});
                    $('.oldabout').removeClass('oldabout');
                }, 700);

                oldabout = $('input:checked + .about-s');

            });
        }
    }
    catch(error) {
        alert('shithappns');
    }

});
