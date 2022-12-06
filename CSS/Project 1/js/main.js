$('.owl-carousel').owlCarousel({
    loop:true,
    // margin: 0,
    nav:true,
    dots: false,
    // autoplay: true,
    // autoplayTimeout: 3000,
    navText: ['<i class="fa-solid fa-arrow-left"></i>','<i class="fa-solid fa-arrow-right"></i>'],
    // nav:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        }
        // 1000:{
        //     items:5
        // }
    }
}) 