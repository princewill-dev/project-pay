;(function($){

$(document).ready(function(){

//--===== HEADER STICKY STARTS =======//
if ($("#header").length > 0) {
$(window).on("scroll", function (event) {
var scroll = $(window).scrollTop();
  if (scroll < 1) {
$(".header-area").removeClass("sticky");
} else {
$(".header-area").addClass("sticky");
}
});
}
});

//--===== HEADER STICKY ENDS =======//
$(window).on('load', function(event) {

//--===== AOS =======//
 AOS.init();
 AOS.init({disable: 'mobile'});
});

//========== COUNTER UP============= //
const ucounter = $('.counter');
if (ucounter.length > 0) {
 ucounter.countUp();  
};

//--===== SLIDER AREA STARTS =======//

// swiper slider //
var sliderSelector = '.swiper-container',
  options = {
  init: false,
  loop: true,
  speed:800,
  slidesPerView: 3,
  autoplay:true,
  delay:500,
  centeredSlides : true,
  effect: 'coverflow',
  coverflowEffect: {
  rotate: 50,
  stretch: 0,
  depth: 100,
  modifier: 1,
  slideShadows : true,
  },
  grabCursor: true,
  parallax: true,
  pagination: {
  el: '.swiper-pagination',
  clickable: true,
  },
  navigation: {
  nextEl: '.swiper-button-next',
  prevEl: '.swiper-button-prev',
  },
  breakpoints: {
  0: {
  slidesPerView: 3,
  spaceBetween: 0
  },
  600: {
  slidesPerView: 3,
  spaceBetween: 0
  },
  1000: {
  slidesPerView: 3,
  spaceBetween: 0
  },
  },
  on: {
  imagesReady: function(){
  this.el.classList.remove('loading');
  }
  }
  };
var mySwiper = new Swiper(sliderSelector, options);
mySwiper.init();


// slick slider //
$(function () {
  $('.brand2-logos').slick({
    autoplay: true,
    autoplaySpeed: 0,
    speed: 3500,
    arrows: false,
    swipe: false,
    slidesToShow: 5,
    cssEase: 'linear',
    pauseOnFocus: true,
    pauseOnHover: true,
    responsive: [
    {
      breakpoint: 1024,
      settings: {
      slidesToShow: 5,
      slidesToScroll: 1,
      infinite: true,
      }
      },
      
      {
        breakpoint: 600,
        settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
      }
      },

      {
        breakpoint: 480,
        settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
      },

      {
        breakpoint: 375,
        settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
      },

      {
        breakpoint: 320,
        settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
      },
    ]
  });

  // rtl-logos //
  $('.brand2-logos-rtl').slick({
    autoplay: true,
    autoplaySpeed: 0,
    speed: 3500,
    arrows: false,
    swipe: false,
    rtl:true,
    slidesToShow: 5,
    cssEase: 'linear',
    pauseOnFocus: true,
    pauseOnHover: true,
    responsive: [
    {
      breakpoint: 1024,
      settings: {
      slidesToShow: 5,
      slidesToScroll: 1,
      infinite: true,
      }
      },
      
      {
        breakpoint: 600,
        settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
      }
      },

      {
        breakpoint: 480,
        settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
      },

      {
        breakpoint: 375,
        settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
      },

      {
        breakpoint: 320,
        settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
      },
    ]
  });

  

$('.brand3-logos').slick({
  autoplay: true,
  autoplaySpeed: 0,
   speed: 4500,
  arrows: false,
  swipe: false,
  slidesToShow: 5,
  cssEase: 'linear',
  pauseOnFocus: false,
  pauseOnHover: false,
  infinite: true,
  initialSlide: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
      slidesToShow: 5,
      slidesToScroll: 1,
       infinite: true,
    }
    },

    {
      breakpoint: 600,
      ettings: {
      slidesToShow: 3,
      slidesToScroll: 1,
      }
    },

    {
      breakpoint: 480,
      settings: {
      slidesToShow: 2,
      slidesToScroll: 1
    }
    },

    {
      breakpoint: 375,
      settings: {
      slidesToShow: 2,
      slidesToScroll: 1
    }
    },

    {
      breakpoint: 320,
      settings: {
      slidesToShow: 2,
      slidesToScroll: 1
    }
    },
    ]
  });
});


$('.testimonials2-boxarea').slick({
  loop:true,
  vertical:true,
  verticalSwiping:true,
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 0,
  speed:4000,
  cssEase: 'linear',
  infinite: true,
  arrows:false,
  touchMove:true,
  swipeToSlide:true,
  swipe:true,
});

$('.testimonials2-boxarea2').slick({
  loop:true,
  vertical:true,
  verticalSwiping:true,
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 0,
  speed:4000,
  cssEase: 'linear',
  infinite: true,
  arrows:false,
  touchMove:true,
  swipeToSlide:true,
  swipe:true,
});
//--===== SLIDER AREA ENDS =======//

//--===== VERTICAL TABS AREA STARTS =======//
// Acc
$(document).on("click", ".service-vertical-tabs .menu div", function() {
var numberIndex = $(this).index();
if (!$(this).is("active")) {
$(".service-vertical-tabs .menu div").removeClass("active");
$(".service-vertical-tabs ul li").removeClass("active");
$(this).addClass("active");
$(".service-vertical-tabs ul").find("li:eq(" + numberIndex + ")").addClass("active");
var listItemHeight = $(".service-vertical-tabs ul")
.find("li:eq(" + numberIndex + ")")
.innerHeight();
$(".service-vertical-tabs ul").height(listItemHeight + "px");
}
});

//--===== VERTICAL TABS AREA ENDS =======//

//--=====  TABS AREA STARTS =======//
$(function(){
  $('.nav-work a').click(function(){
    var tabId = $(this).attr('data-tab');
    $('.nav-work a').removeClass('active');
    $('.Tabcondent').removeClass('active');
    $(this).addClass('active');
    $('#'+tabId).addClass('active');
  });
});

//--=====  TABS AREA ENDS =======//

//--=====  TESTIMONIALS AREA STARTS =======//

  // testimonial //
$(".product-slider-nav").slick({
  slidesToShow: 5,
  slidesToScroll: 1,
  arrows: true,
  focusOnSelect: true,
  asNavFor: ".product-slider-single",
  autoplay:true,
  autoplayTimeout:500,
  prevArrow: $('.testimonial-next-arrow'),
  nextArrow: $('.testimonial-prev-arrow'),
});
$('.slider-nav1').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  asNavFor: '.foter-carousel',
  dots: false,
  arrows:true,
  nav:true,
  loop:true,
  centerMode: false,
  focusOnSelect: true,
  autoplay:true,
  autoplayTimeout:500,
  prevArrow: $('.testimonial-next-arrow'),
  nextArrow: $('.testimonial-prev-arrow'),
});
$('.foter-carousel').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: true,
  autoplay:true,
  nav:true,
  prevArrow: $('.testimonial-next-arrow'),
  nextArrow: $('.testimonial-prev-arrow'),
  fade: true,
  loop:true,
  asNavFor: '.slider-nav1',
});

// testimonial //
$('.tab-carousel-section').owlCarousel({
  loop:true,
  margin:30,
  nav:true,
  dots:false,
  items:10,
  navText:["<i class='fa-solid fa-angle-left'></i>","<i class='fa-solid fa-angle-right'></i>"],
  autoplay:true,
  smartSpeed:2000,
  autoplayTimeout:4000,
  responsiveClass:true,
  responsive:{
  0:{
    items:1,
    nav:true,    
    },
    600:{
    items:3,
    },
    1000:{
    items:4,
    }
    }
}); 

// testimonial //
$('.testimonial3-slider-area').owlCarousel({
  loop:true,
  margin:30,
  nav:false,
  dots:true,
  items:10,
  autoplay:true,
  smartSpeed:2000,
  autoplayTimeout:4000,
  responsiveClass:true,
  responsive:{
  0:{
    items:1,                
  },
  600:{
    items:2,
  },
  1000:{
    items:3,
  }
  }
});

// testimonial //
$('.testimonial3-slider-area-rtl').owlCarousel({
  loop:true,
  margin:30,
  nav:false,
  dots:true,
  items:10,
  autoplay:true,
  rtl:true,
  smartSpeed:2000,
  autoplayTimeout:4000,
  responsiveClass:true,
  responsive:{
  0:{
    items:1,                
  },
  600:{
    items:2,
  },
  1000:{
    items:3,
  }
  }
});

// testimonial //
$('.testimonial-main-box').owlCarousel({
  loop:true,
  margin:30,
  nav:false,
  dots:true,
  items:10,
  autoplay:true,
  smartSpeed:2000,
  autoplayTimeout:4000,
  responsiveClass:true,
  responsive:{
  0:{
    items:1,                
  },
  600:{
    items:1,
  },
  1000:{
  items:1,
  }
 }
});  
//--=====  TESTIMONIALS AREA ENDS =======//

//========== PAGE PROGRESS STARTS ============= // 
var progressPath = document.querySelector(".progress-wrap path");
var pathLength = progressPath.getTotalLength();
progressPath.style.transition = progressPath.style.WebkitTransition =
"none";
progressPath.style.strokeDasharray = pathLength + " " + pathLength;
progressPath.style.strokeDashoffset = pathLength;
progressPath.getBoundingClientRect();
progressPath.style.transition = progressPath.style.WebkitTransition =
"stroke-dashoffset 10ms linear";
var updateProgress = function () {
var scroll = $(window).scrollTop();
var height = $(document).height() - $(window).height();
var progress = pathLength - (scroll * pathLength) / height;
progressPath.style.strokeDashoffset = progress;
};
updateProgress();
$(window).scroll(updateProgress);
var offset = 50;
var duration = 550;
jQuery(window).on("scroll", function () {
if (jQuery(this).scrollTop() > offset) {
jQuery(".progress-wrap").addClass("active-progress");
} else {
jQuery(".progress-wrap").removeClass("active-progress");
}
});
jQuery(".progress-wrap").on("click", function (event) {
event.preventDefault();
jQuery("html, body").animate({ scrollTop: 0 }, duration);
return false;
});
//========== PAGE PROGRESS ENDS ============= // 

//========== PRELOADER STARTS ============= //  
// $('#preloader').delay(1000).fadeOut('slow');
$('body').delay(1000).css({ 'overflow': 'visible' });
setTimeout(function () {
  $("#preloader").fadeToggle();
}, 2000);    

//========== PRELOADER ENDS ============= // 

//========== GSAP ANIMATION STARTS ============= //
gsap.registerPlugin(ScrollTrigger);
let revealContainers = document.querySelectorAll(".reveal");
revealContainers.forEach((container) => {
let image = container.querySelector("img");
let tl = gsap.timeline({
scrollTrigger: {
trigger: container,
toggleActions: "restart none none reset"
}
});

tl.set(container, { autoAlpha: 1 });
tl.from(container, 1.5, {
xPercent: -100,
ease: Power2.out
});
tl.from(image, 1.5, {
xPercent: 100,
scale: 1.1,
delay: -1.5,
ease: Power2.out
});
});
//========== GSAP ANIMATION ENDS ============= //

//========== PRICING-PLAN STARTS ============= //
$("#ce-toggle").click(function (event) {
$(".plan-toggle-wrap").toggleClass("active");
});

$("#ce-toggle").change(function () {
if ($(this).is(":checked")) {
$(".tab-content #yearly").hide();
$(".tab-content #monthly").show();
} else {
  $(".tab-content #monthly").hide();
$(".tab-content #yearly").show();
}
});

// pricing-plan-tab 2 //
$("#ce-toggle1").click(function (event) {
$(".plan-toggle-wrap1").toggleClass("active");
});

$("#ce-toggle1").change(function () {
if ($(this).is(":checked")) {
$(".tab-content #yearly1").hide();
$(".tab-content #monthly1").show();
} else {
$(".tab-content #yearly1").show();
$(".tab-content #monthly1").hide();
}
});
//========== PRICING-PLAN STARTS ============= //

//========== VIDEO POPUP STARTS ============= //
if ($(".popup-youtube").length > 0) {
$(".popup-youtube").magnificPopup({
type: "iframe",
});
}
//========== VIDEO POPUP ENDS ============= //

})(jQuery);