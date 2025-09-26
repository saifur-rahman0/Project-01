document.addEventListener('DOMContentLoaded', () => {
    // Scroll-driven slideshow behavior
    const slideshowSection = document.getElementById('slideshow-section');
    const slidesEl = document.getElementById('slides');
    const dots = document.getElementById('slideshow-dots');
    if (slideshowSection && slidesEl) {
        const slides = Array.from(slidesEl.querySelectorAll('.slide'));
        const dotButtons = dots ? Array.from(dots.querySelectorAll('.dot')) : [];

        // helper to set active slide
        function setActive(index) {
            slides.forEach((s, i) => s.classList.toggle('active', i === index));
            dotButtons.forEach((d, i) => d.classList.toggle('active', i === index));
        }

        // click on dots
        dotButtons.forEach(btn => {
            btn.addEventListener('click', () => setActive(Number(btn.dataset.index)));
        });

        // compute scroll and pin behavior using full viewport height per slide
        let start = 0;
        let end = 0;

        // set explicit spacer height: number of slides * viewport height
        const spacer = document.getElementById('slideshow-spacer');
        function setSpacerHeight() {
            const h = slides.length * window.innerHeight;
            if (spacer) spacer.style.height = h + 'px';
        }

        function updateBounds() {
            // top of spacer relative to document
            if (!spacer) return; // guard against missing spacer
            const top = spacer.getBoundingClientRect().top + window.scrollY;
            start = top;
            end = top + (spacer ? spacer.offsetHeight : slides.length * window.innerHeight);
        }

        function onScroll() {
            if (!spacer) return; // guard against missing spacer
            const y = window.scrollY;
            const pinEnd = start + (spacer.offsetHeight - window.innerHeight);
            if (y >= start && y <= pinEnd) {
                slideshowSection.classList.add('is-pinned');
                const progress = (y - start) / (pinEnd - start);
                const index = Math.min(slides.length - 1, Math.floor(progress * slides.length));
                setActive(index);
            } else {
                slideshowSection.classList.remove('is-pinned');
                if (y < start) setActive(0);
                if (y > pinEnd) setActive(slides.length - 1);
            }
        }

        window.addEventListener('scroll', onScroll, {passive: true});
        window.addEventListener('resize', () => {
            setSpacerHeight();
            updateBounds();
        });

        setSpacerHeight();
        updateBounds();
    }
});
