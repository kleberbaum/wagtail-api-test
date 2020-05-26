$(function() {

	try {
		//check if js is on
		if(js){
			changecol(0)
		}
		function changecol(offset)
		{
			var party = $('#partyaudio')[0];
			var cols = ['#FF0000','#FF1100','#FF2200','#FF3300','#FF4400','#FF5500','#FF6600','#FF7700','#FF8800','#FF9900','#FFaa00','#FFbb00','#FFcc00','#FFdd00','#FFee00','#FFff00','#FFee00','#FFdd00','#FFcc00','#FFbb00','#FFaa00','#FF9900','#FF8800','#FF7700','#FF6600','#FF5500','#FF4400','#FF3300','#FF2200','#FF1100','#00FF00','#000000','#00FF00','#00FF00','#00FF00','#000000','#00FF00','#00FF00','#00FF00','#000000','#00FF00','#00FF00','#00FF00','#000000','#00FF00','#00FF00','#00FF00','#000000','#00FF00','#00FF00','#00FF00','#FF0000','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#00FF00','#FF0000','#FF4000','#FF8000','#FFC000','#FFFF00','#C0FF00','#80FF00','#40FF00','#00FF00','#00FF40','#00FF80','#00FFC0','#00FFFF','#00C0FF','#0080FF','#0040FF','#0000FF','#4000FF','#8000FF','#C000FF','#FF00FF','#FF00C0','#FF0080','#FF0040','#FF0000','#EE0000','#DD0000','#CC0000','#BB0000','#AA0000','#990000','#880000','#770000','#660000','#550000','#440000','#330000','#220000','#110000','#000000','#110000','#220000','#330000','#440000','#550000','#660000','#770000','#880000','#990000','#AA0000','#BB0000','#CC0000','#DD0000','#EE0000','#000000','#000000','#000000','#FFFFFF','#FFFFFF','#FFFFFF','#0000FF','#FFFF00','#0000FF','#FFFF00','#0000FF','#FFFF00','#0000FF','#FFFF00','#0000FF','#FFFF00','#0000FF','#FFFF00','#0000FF','#FFFF00','#0000FF','#FFFF00'];

			$.fn.clickToggle = function(a,b) {
				function cb(){ [b,a][this._tog^=1].call(this); }
				return this.on('click', cb);
			};

			$('#party').clickToggle(
				function() {
					party.loop = true;
					party.play();
					party.volume = 0.3;

					$('body').addClass('party');
					$('.nyan').addClass('party');
					$('.banner').addClass('party');
					$('.about').addClass('party');
					$('.motto-s').addClass('party');
					$('.mitsudomoe img').addClass('party');
					$('.nyanlink').addClass('party');
					$('#party').text('stop Party');

					setInterval(function time() {
						$('body').css({'background-color': cols[offset]});
						$('.nyan').css({'background-color': cols[offset]});
						offset = (offset >= cols.length) ? 0 : (offset+1);
					}, 10);
				}, function() {
					party.pause();
					party.currentTime = 0;

					$('body').removeClass('party');
					$('.nyan').removeClass('party');
					$('.banner').removeClass('party');
					$('.about').removeClass('party');
					$('.motto-s').removeClass('party');
					$('.mitsudomoe img').removeClass('party');
					$('.nyanlink').removeClass('party');
					$('#party').text('Party');

					setTimeout(function(){
                location.hash = "";
            }, 1);
				});
		}
	}
	catch(error) {
		alert('shithappns');
	}

});
