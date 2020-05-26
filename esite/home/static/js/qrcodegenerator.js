$(function() {

    try {
        if(js){
            qrcodegenerator();
        }
        function qrcodegenerator()
        {
            $('#qr').qrcode({'text': 'SPOOOKY.TK'});
        }
    }
    catch(error) {
        alert('shithappns4');
    }

});
