const accordionItems = document.querySelectorAll(".accordion-item");

accordionItems.forEach((item) => {
  item.addEventListener("mouseenter", () => {
    accordionItems.forEach((entry) => entry.classList.toggle("is-open", entry === item));
  });
});

window.addEventListener("load", () => {
  if (!window.gsap || !window.ScrollTrigger) return;

  gsap.registerPlugin(ScrollTrigger);

  document.querySelectorAll("[data-image-reveal]").forEach((item) => {
    gsap.fromTo(
      item,
      { scale: 0.88, opacity: 0.72 },
      {
        scale: 1,
        opacity: 1,
        ease: "none",
        scrollTrigger: {
          trigger: item,
          start: "top 88%",
          end: "bottom 30%",
          scrub: true
        }
      }
    );
  });

  const scrubText = document.querySelector("[data-scrub-text]");
  if (scrubText) {
    const rawText = scrubText.textContent.trim();
    const words = rawText.split("");
    scrubText.innerHTML = words.map((word) => `<span>${word}</span>`).join("");

    gsap.fromTo(
      scrubText.querySelectorAll("span"),
      { opacity: 0.48 },
      {
        opacity: 1,
        stagger: 0.035,
        ease: "none",
        scrollTrigger: {
          trigger: scrubText,
          start: "top 74%",
          end: "bottom 36%",
          scrub: true
        }
      }
    );
  }
});
