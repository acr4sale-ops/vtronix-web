document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      nav.classList.toggle("open");
      toggle.classList.toggle("open");
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.classList.remove("open");
      });
    });
  }

  /* Sticky header shadow on scroll */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* Scroll-reveal for section-level content */
  var revealTargets = document.querySelectorAll(
    "main > section > .wrap > *, main > .split, main > .link-block, .feature, .product-card, .why-card, .step"
  );

  if ("IntersectionObserver" in window && revealTargets.length) {
    revealTargets.forEach(function (el) {
      el.classList.add("reveal");
    });

    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -60px 0px" }
    );

    revealTargets.forEach(function (el) {
      io.observe(el);
    });
  }

  /* Reveal for the about strengths showcase (photo zoom, then staggered cards) */
  var strengthsShowcase = document.querySelector(".strengths-showcase");
  if (strengthsShowcase) {
    if ("IntersectionObserver" in window) {
      var strengthsIo = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              strengthsShowcase.classList.add("in-view");
              strengthsIo.disconnect();
            }
          });
        },
        { threshold: 0.15 }
      );
      strengthsIo.observe(strengthsShowcase);
    } else {
      strengthsShowcase.classList.add("in-view");
    }
  }

  /* Scroll-driven parallax for the about facility photo */
  var parallaxPhoto = document.querySelector(".about-facility-photo");
  var parallaxLayer = document.querySelector(".about-facility-parallax");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var isNarrow = window.matchMedia("(max-width: 620px)");

  if (parallaxPhoto && parallaxLayer && !reduceMotion) {
    var parallaxTicking = false;

    var updateParallax = function () {
      parallaxTicking = false;
      if (isNarrow.matches) {
        parallaxLayer.style.transform = "";
        return;
      }
      var rect = parallaxPhoto.getBoundingClientRect();
      var viewportH = window.innerHeight || document.documentElement.clientHeight;
      var progress = (viewportH - rect.top) / (viewportH + rect.height);
      var offset = (progress - 0.5) * rect.height * 0.3;
      parallaxLayer.style.transform = "translateY(" + offset + "px)";
    };

    var onParallaxScroll = function () {
      if (!parallaxTicking) {
        parallaxTicking = true;
        window.requestAnimationFrame(updateParallax);
      }
    };

    updateParallax();
    window.addEventListener("scroll", onParallaxScroll, { passive: true });
    window.addEventListener("resize", onParallaxScroll);
  }

  var form = document.getElementById("contactForm");
  if (form) {
    var note = form.querySelector(".form-note");
    var button = form.querySelector(".send-btn");
    var thanks = document.getElementById("formThanks");
    var againBtn = thanks && thanks.querySelector(".form-again");

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      var originalLabel = button.textContent;
      button.disabled = true;
      button.textContent = "Sending…";
      note.classList.remove("show", "error");

      var ajaxUrl = form.action.replace("formsubmit.co/", "formsubmit.co/ajax/");

      fetch(ajaxUrl, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" }
      })
        .then(function (res) {
          if (!res.ok) throw new Error("Request failed");
          return res.json();
        })
        .then(function (data) {
          // FormSubmit answers 200 even when it did not send (e.g. form not
          // yet activated), so only a success flag counts as sent.
          if (!data || String(data.success) !== "true") {
            throw new Error((data && data.message) || "Not sent");
          }
          form.reset();
          form.hidden = true;
          thanks.hidden = false;
          thanks.focus();
        })
        .catch(function () {
          note.textContent = "Something went wrong sending your message. Please email us directly at sales@vtronix.com.";
          note.classList.add("show", "error");
        })
        .finally(function () {
          button.disabled = false;
          button.textContent = originalLabel;
        });
    });

    if (againBtn) {
      againBtn.addEventListener("click", function () {
        thanks.hidden = true;
        form.hidden = false;
        form.querySelector("input:not([type=hidden]):not(.form-honey)").focus();
      });
    }
  }
});
