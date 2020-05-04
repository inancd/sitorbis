// =============================================
// SITORBIS COMMENT AJAX
// =============================================

$(document).ready(function (event) {
    $(document).on('submit', '.comment-form', function (event) {
        event.preventDefault();
        console.log($(this).serialize());
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                $('.strbs-post-comment').html(response['form']);
                $('textarea').val('');
            },
            error: function (rs, e) {
                console.log(rs.responseText);
            },
        });
    });

    $(document).on('submit', '.reply-form', function (event) {
        event.preventDefault();
        console.log($(this).serialize());
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                $('.strbs-post-comment').html(response['form']);
                $('textarea').val('');
            },
            error: function (rs, e) {
                console.log(rs.responseText);
            },
        });
    });

});

// =============================================
// SITORBIS NEWSLETTER AJAX
// =============================================


// =============================================
// SITORBIS INSTAGRAM FEED - OWL CAROUSEL
// =============================================

if ($("#instafeed-gallery").length) {
    var galleryFeed = new Instafeed({
        get: "user",
        userId: 17053085883,
        accessToken: "17053085883.1677ed0.8286d891dd4146ae8e557cd7f1462ec1",
        resolution: "standard_resolution",
        useHttp: "true",
        template: '<ul class="strbs-instagram-feed instagram-icon"><li><a href="{{link}}" target="_blank"><img src="{{image}}" class="img-responsive"><span class="strbs-instagram-icon"><span class="fab fa-instagram"></span></span></a></li></ul>',
        target: "instafeed-gallery",
        limit: 9,

    });
    galleryFeed.run();
}
;
// =============================================
// SITORBIS POPULAR BLOG - OWL CAROUSEL
// =============================================

$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 13,
    responsiveClass: true,
    autoplay: true,
    responsive: {
        0: {
            items: 1,
            nav: true
        },
        600: {
            items: 3,
            nav: false
        },
        1240: {
            items: 5,
            nav: true,
            loop: false
        }
    }
});




