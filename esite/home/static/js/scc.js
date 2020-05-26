$(function() {

	try {
		//check if js is on
		if(false){
			bg_color();
			$(window).scroll(bg_color);
		}
		function bg_color(){
			var hue = 211 + ($(document).scrollTop() / 1.3); //is a degree on the color wheel -> no max
			var saturation = '73%'; //percentage of saturation
			var lightness = '93%'; //percentage of lightness
			var alpha = 0.93; //number between 0.0 (fully transparent) and 1.0 (fully opaque)

			$('.triangulum').css({'background-color': 'hsla('+ hue +','+ saturation +','+ lightness +','+ alpha +')'});
			$('.boxes').css({'border-color': 'hsla('+ hue +','+ saturation +','+ lightness +','+ alpha +')'});
		}
	}
	catch(error) {
		alert('shithappns');
	}

});
