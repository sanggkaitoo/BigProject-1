window.onscroll = function() {myFunction()};

function myFunction() {
	var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
	var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
	if(winScroll >= 300) {
		$(".cursor-inner").css("background-color", "rgb(32, 32, 32)");
		$(".cursor-inner.cursor-hover").css("background-color", "rgb(32, 32, 32)");
		$(".cursor-outer").css("border-color", "rgb(32, 32, 32)");
	}
	if(winScroll < 300) {
		$(".cursor-inner").css("background-color", "#fff");
		$(".cursor-inner.cursor-hover").css("background-color", "#fff");
		$(".cursor-outer").css("border-color", "#fff");
	}
    if(winScroll >= 2000) {
		$(".cursor-inner").css("background-color", "#fff");
		$(".cursor-inner.cursor-hover").css("background-color", "#fff");
		$(".cursor-outer").css("border-color", "#fff");
        $("#content-container").css("background-color", "rgb(32, 32, 32)");
        $(".middle-text-menu-dining-wrap").css("color", "#fff");
	} else {
        $("#content-container").css("background-color", "#fff");
        $(".middle-text-menu-dining-wrap").css("color", "rgb(32, 32, 32)");
    }
    if(winScroll >= (document.documentElement.scrollHeight - document.documentElement.clientHeight - 400)) {
        $(".cursor-inner").css("background-color", "#fff");
		$(".cursor-inner.cursor-hover").css("background-color", "#fff");
		$(".cursor-outer").css("border-color", "#fff");
    }
}