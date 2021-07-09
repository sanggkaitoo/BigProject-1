/* ====================== [ Change background when scroll JS ] ====================== */

window.onscroll = function() {myFunction()};

function myFunction() {
	var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
	var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
	if(winScroll >= 500) {
		$("#content-container").css("background-color", "rgb(32, 32, 32)");
		$(".cursor-inner").css("background-color", "#fff");
		$(".cursor-inner.cursor-hover").css("background-color", "#fff");
		$(".cursor-outer").css("border-color", "#fff");
	}
	if(winScroll >= 1000) {
		$("#content-container").css("background-color", "#fff");
		$(".cursor-inner").css("background-color", "rgb(32, 32, 32)");
		$(".cursor-inner.cursor-hover").css("background-color", "rgb(32, 32, 32)");
		$(".cursor-outer").css("border-color", "rgb(32, 32, 32)");
	} 
	if(winScroll < 500) {
		$("#content-container").css("background-color", "#fff");
		$(".cursor-inner").css("background-color", "#fff");
		$(".cursor-inner.cursor-hover").css("background-color", "#fff");
		$(".cursor-outer").css("border-color", "#fff");
	}
	if(winScroll >= 2800) {
		$("#content-container").css("background-color", "rgb(32, 32, 32)");
		$(".cursor-inner").css("background-color", "#fff");
		$(".cursor-inner.cursor-hover").css("background-color", "#fff");
		$(".cursor-outer").css("border-color", "#fff");
	}
	if(winScroll >= 3500) {
		$("#content-container").css("background-color", "#fff");
		$(".cursor-inner").css("background-color", "rgb(32, 32, 32)");
		$(".cursor-inner.cursor-hover").css("background-color", "rgb(32, 32, 32)");
		$(".cursor-outer").css("border-color", "rgb(32, 32, 32)");
	}
	if(winScroll >= 5000) {
		$("#content-container").css("background-color", "#111");
		$(".cursor-inner").css("background-color", "#fff");
		$(".cursor-inner.cursor-hover").css("background-color", "#fff");
		$(".cursor-outer").css("border-color", "#fff");
	}
}

/* ====================== [ End Change background when scroll JS ] ====================== */