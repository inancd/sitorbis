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



    var el = document.querySelector('.strbs-more');
    var btn = el.querySelector('.more-btn');
    var menu = el.querySelector('.more-menu');
    var visible = false;

    function showMenu(e) {
        e.preventDefault();
        if (!visible) {
            visible = true;
            el.classList.add('show-more-menu');
            menu.setAttribute('aria-hidden', false);
            document.addEventListener('mousedown', hideMenu, false);
        }
    }

    function hideMenu(e) {
        if (btn.contains(e.target)) {
            return;
        }
        if (visible) {
            visible = false;
            el.classList.remove('show-more-menu');
            menu.setAttribute('aria-hidden', true);
            document.removeEventListener('mousedown', hideMenu);
        }
    }

    btn.addEventListener('click', showMenu, false);