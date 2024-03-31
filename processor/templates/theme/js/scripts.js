//  Preloader
jQuery(window).on("load", function () {
  $('#preloader').fadeOut(500);
  $('#main-wrapper').addClass('show');
});


(function ($) {
"use strict"

$('.duration-option a')
  .on('click', function () {
      $(".duration-option a.active")
        .removeClass("active");
      $(this)
        .addClass('active');
  });

/* ---------------------------------------------
  Search
--------------------------------------------- */
$('.search-btn').on('click', function () {
  $(".search-form .form").toggleClass("show");
});

  /* ---------------------------------------------
  venobox
  --------------------------------------------- */
  // $('.venobox').venobox(); 

  /* ---------------------------------------------
  Slick
--------------------------------------------- */
$('.slider').slick({
  slidesToShow:1,
  slidesToScroll:1,
  autoplay: true,
  dots: true,
  autoplaySpeed: 3000,
  speed: 1000,
  prevArrow:'<div><button class="nextArrow arrowBtn"><i class="las la-arrow-left"></i></button></div>',
  nextArrow:'<div><button class="prevArrow arrowBtn"><i class="las la-arrow-right"></i></button></div>',
});

/* ---------------------------------------------
  File Upload
--------------------------------------------- */
$(".file-upload-wrapper").on("change", ".file-upload-field", function () {
  $(this).parent(".file-upload-wrapper").attr("data-text", $(this).val().replace(/.*(\/|\\)/, ''));
});

/* ---------------------------------------------
  to keep the current page active
--------------------------------------------- */
$(function () {
    for (var nk = window.location,
        o = $(".menu a").filter(function () {
            return this.href == nk;
        })
            .addClass("active")
            .parent()
            .addClass("active"); ;) {
        // console.log(o)
        if (!o.is("li")) break;
        o = o.parent()
            .addClass("show")
            .parent()
            .addClass("active");
    }

});

$('[data-toggle="tooltip"]').tooltip();

$('.sidebar-right-trigger').on('click', function () {
  $('.sidebar-right').toggleClass('show');
});

})(jQuery);