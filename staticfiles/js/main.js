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
          limit: 5,

        });
        galleryFeed.run();
      }

    let mainNav = document.getElementById("js-menu");
    let navBarToggle = document.getElementById("js-navbar-toggle");

    navBarToggle.addEventListener("click", function() {
        mainNav.classList.toggle("active");
      });