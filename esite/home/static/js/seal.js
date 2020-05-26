$(function() {

    try {

        if(js){
            seal();
        }
        function seal()
        {
            setInterval(function time() {
                var now = new Date();
                var hours = now.getHours();
                var minutes = now.getMinutes();
                var seconds = now.getSeconds();
                var abyss = (24 * 60 * 60) - ((hours * 60 * 60) + (minutes * 60) + seconds);

                if(hours == 0)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal12.gif');
                    $('#seal').prop('title', abyss);
                    $('.banner').css({
                        backgroundImage: 'url(https://erebos.xyz/PIC/veins2.png)'
                    })
                }
                else if(hours < 12)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal13.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 12)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal0.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 13)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal1.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 14)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal2.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 15)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal3.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 16)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal4.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 17)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal5.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 18)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal6.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 19)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal7.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 20)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal8.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 21)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal9.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 22)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal10.gif');
                    $('#seal').prop('title', abyss);
                }
                else if(hours == 23)
                {
                    $('#seal').prop('src', 'https://erebos.xyz/PIC/seal11.gif');
                    $('#seal').prop('title', abyss);
                }

            }, 1000);
        }
    }
    catch(error) {
        alert('shithappns');
    }

});
