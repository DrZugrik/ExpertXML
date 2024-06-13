document.addEventListener("DOMContentLoaded", function() {
    'use strict';
  
    // preloader
    $(window).on('load', function() {
        $('.loader').fadeOut('slow');
    });
  
    // smooth scroll
    $("a").on("click", function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            var targetElement = $(hash);
            if (targetElement.length) {
                $("html, body").animate({
                    scrollTop: targetElement.offset().top - 50
                }, 850);
            }
        }
    });
  
    // magnific popup
    if (typeof $.fn.magnificPopup !== 'undefined') {
        $('.gallery').each(function() {
            $(this).magnificPopup({
                delegate: '.popup-image',
                type: 'image',
                gallery: {
                    enabled: true
                },
            });
        });
    }
  
    // swiper slider
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: 1,
        spaceBetween: 30,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        navigation: {
            nextEl: ".next-slide",
            prevEl: ".prev-slide"
        },
        breakpoints: {
            0: {
                slidesPerView: 1,
            },
            768: {
                slidesPerView: 1,
            },
            780: {
                slidesPerView: 1,
            }
        }
    });
  
    // hide navbar on click
    $('.navbar-nav>li>a').on('click', function(){
        $('.navbar-collapse').collapse('hide');
    });
  
    // navbar on scroll
    $(window).on("scroll", function() {
        var onScroll = $(this).scrollTop();
        if( onScroll > 50) {
            $(".navbar").addClass("navbar-fixed");
        }
        else {
            $(".navbar").removeClass("navbar-fixed");
        }
    });

    $("a").on("click", function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            var targetElement = $(hash);
            if (targetElement.length) {
                $("html, body").animate({
                    scrollTop: targetElement.offset().top - 50
                }, 850);
            } else {
                console.log("Элемент с идентификатором " + hash + " не найден на странице.");
            }
        }
    });
  
});
