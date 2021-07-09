/* ====================== [ Top top JS ] ====================== */

window.onscroll = function() {topTopFunc(), myFunction()};

function topTopFunc() {
	var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
	var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
	if(winScroll >= 10) {
		$(".to-top").css("opacity", "1");
	} else {
        $(".to-top").css("opacity", "0");
    }
}

function page_scrollToTop(){
    $('html,body').animate({
        scrollTop: 0
    }, 50000, 'linear');
}

/* ====================== [ End to top JS ] ====================== */

/* ====================== [ Change Mouse JS ] ====================== */

function mousecursor() {
    if ($("body")) {
        const e = document.querySelector(".cursor-inner"),
            t = document.querySelector(".cursor-outer");
        let n, i = 0,
            o = !1;
        window.onmousemove = function (s) {
            o || (t.style.transform = "translate(" + s.clientX + "px, " + s.clientY + "px)"), e.style.transform = "translate(" + s.clientX + "px, " + s.clientY + "px)", n = s.clientY, i = s.clientX
        }, $("body").on("mouseenter", "a, .cursor-pointer", function () {
            e.classList.add("cursor-hover"), t.classList.add("cursor-hover")
        }), $("body").on("mouseleave", "a, .cursor-pointer", function () {
            $(this).is("a") && $(this).closest(".cursor-pointer").length || (e.classList.remove("cursor-hover"), t.classList.remove("cursor-hover"));
        }), e.style.visibility = "visible", t.style.visibility = "visible"

        window.onmousemove = function (s) {
            o || (t.style.transform = "translate(" + s.clientX + "px, " + s.clientY + "px)"), e.style.transform = "translate(" + s.clientX + "px, " + s.clientY + "px)", n = s.clientY, i = s.clientX
        }, $("body").on("mouseenter", "input, .cursor-pointer", function () {
            e.classList.add("cursor-hover"), t.classList.add("cursor-hover")
        }), $("body").on("mouseleave", "input, .cursor-pointer", function () {
            $(this).is("input") && $(this).closest(".cursor-pointer").length || (e.classList.remove("cursor-hover"), t.classList.remove("cursor-hover"));
        }), e.style.visibility = "visible", t.style.visibility = "visible"
    }
};

$(function () {
    mousecursor();
});

/* ====================== [ End Change Mouse JS ] ====================== */

/* ====================== [ Change navbar when scroll JS ] ====================== */

$(function () {
    mousecursor();
    $(document).scroll(function () {
        var $nav = $(".nav-bar");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});

/* ====================== [ End Change navbar when scroll JS ] ====================== */

/* ====================== [ Calendar JS ] ====================== */

$(function () {

	rome(input_from, {
		dateValidator: rome.val.beforeEq(input_to),
		time: false,
		inputFormat: "DD-MM-YYYY"
	});

	rome(input_to, {
		dateValidator: rome.val.afterEq(input_from),
		time: false,
		inputFormat: "DD-MM-YYYY"
	});


});

/* ====================== [ End Calendar JS ] ====================== */

/* ====================== [ Mouse Driven Vertical Carousel JS ] ====================== */

class VerticalMouseDrivenCarousel {
	constructor(options = {}) {
		const _defaults = {
			carousel: ".js-carousel",
			bgImg: ".js-carousel-bg-img",
			list: ".js-carousel-list",
			listItem: ".js-carousel-list-item"
		};

		this.posY = 0;

		this.defaults = Object.assign({}, _defaults, options);

		this.initCursor();
		this.init();
		this.bgImgController();
	}

	//region getters
	getBgImgs() {
		return document.querySelectorAll(this.defaults.bgImg);
	}

	getListItems() {
		return document.querySelectorAll(this.defaults.listItem);
	}

	getList() {
		return document.querySelector(this.defaults.list);
	}

	getCarousel() {
		return document.querySelector(this.defaults.carousel);
	}

	init() {
		TweenMax.set(this.getBgImgs(), {
			autoAlpha: 0,
			scale: 1.05
		});

		TweenMax.set(this.getBgImgs()[0], {
			autoAlpha: 1,
			scale: 1
		});

		this.listItems = this.getListItems().length - 1;

		this.listOpacityController(0);
	}

	initCursor() {
		const listHeight = this.getList().clientHeight;
		const carouselHeight = this.getCarousel().clientHeight;

		this.getCarousel().addEventListener(
			"mousemove",
			event => {
				this.posY = event.pageY - this.getCarousel().offsetTop;
				let offset = -this.posY / carouselHeight * listHeight;

				TweenMax.to(this.getList(), 0.3, {
					y: offset,
					ease: Power4.easeOut
				});
			},
			false
		);
	}

	bgImgController() {
		for (const link of this.getListItems()) {
			link.addEventListener("mouseenter", ev => {
				let currentId = ev.currentTarget.dataset.itemId;

				this.listOpacityController(currentId);

				TweenMax.to(ev.currentTarget, 0.3, {
					autoAlpha: 1
				});

				TweenMax.to(".is-visible", 0.2, {
					autoAlpha: 0,
					scale: 1.05
				});

				if (!this.getBgImgs()[currentId].classList.contains("is-visible")) {
					this.getBgImgs()[currentId].classList.add("is-visible");
				}

				TweenMax.to(this.getBgImgs()[currentId], 0.6, {
					autoAlpha: 1,
					scale: 1
				});
			});
		}
	}

	listOpacityController(id) {
		id = parseInt(id);
		let aboveCurrent = this.listItems - id;
		let belowCurrent = parseInt(id);

		if (aboveCurrent > 0) {
			for (let i = 1; i <= aboveCurrent; i++) {
				let opacity = 0.5 / i;
				let offset = 5 * i;
				TweenMax.to(this.getListItems()[id + i], 0.5, {
					autoAlpha: opacity,
					x: offset,
					ease: Power3.easeOut
				});
			}
		}

		if (belowCurrent > 0) {
			for (let i = 0; i <= belowCurrent; i++) {
				let opacity = 0.5 / i;
				let offset = 5 * i;
				TweenMax.to(this.getListItems()[id - i], 0.5, {
					autoAlpha: opacity,
					x: offset,
					ease: Power3.easeOut
				});
			}
		}
	}
}

new VerticalMouseDrivenCarousel();


/* ====================== [ End Mouse Driven Vertical Carousel JS ] ====================== */