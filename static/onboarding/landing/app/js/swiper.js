var swiper = new Swiper(".swiper-thumb1", {
  spaceBetween: 10,
  slidesPerView: 3,
  freeMode: true,
  watchSlidesProgress: true,
});
var swiper2 = new Swiper(".swiper-testimonial-1", {
  spaceBetween: 10,

  thumbs: {
    swiper: swiper,
  },
});

var swiper3 = new Swiper(".swiper-thumb2", {
  spaceBetween: 10,
  slidesPerView: 6,
  freeMode: true,
  watchSlidesProgress: true,
});
var swiper4 = new Swiper(".swiper-testimonial-2", {
  spaceBetween: 10,
  loop: true,

  pagination: {
    el: ".swiper-pagination",
    type: "fraction",
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  thumbs: {
    swiper: swiper3,
  },
});

var swiper5 = new Swiper(".swiper-partner", {
  breakpoints: {
    0: {
      slidesPerView: 2,
      spaceBetween: 30,
    },
    768: {
      slidesPerView: 4,
      spaceBetween: 30,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 60,
    },
  },
  slidesPerView: 4,
});

var swiper6 = new Swiper(".blog-swiper", {
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});

var swiper = new Swiper(".img-swiper", {
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});
