$(function() {

    try {
        //set
        //alert(document.cookie);
        if(document.cookie == ''){
            document.cookie = 'js=true';
        }

        //get
        var cookies = {};
        document.cookie.split('; ').forEach(function(item) {
            cookies[item.split('=')[0]] = item.split('=')[1];
        });

        //set js == true or false
        js = cookies.js === 'true';

    }
    catch(error) {
        alert('shithappns');
    }

});
