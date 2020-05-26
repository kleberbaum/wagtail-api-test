$(function() {

    try {
        if(js){
            nyan();
        }
        function nyan()
        {
            var nyan = $('#nyanaudio')[0];
            $('.nyan').hover(
                function() {
                    nyan.loop = true;
                    nyan.play();
                    nyan.volume = 0.2;
                    $('.nyan').addClass('animatedBackground');
                    $('body').addClass('nyan-background');
                    $('.nyan').addClass('nyan-background');
                }, function() {
                    nyan.pause();
                    nyan.currentTime = 0;
                    $('body').removeClass('nyan-background');
                    $('.nyan').removeClass('nyan-background');
                });
        }
    }
    catch(error) {
        alert('shithappns');
    }

});
