document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('.hero-carousel');
    if (carousel) {
        const items = carousel.querySelectorAll('.carousel-item');
        const prevButton = carousel.querySelector('.carousel-control-prev');
        const nextButton = carousel.querySelector('.carousel-control-next');
        let currentIndex = 0;

        function showSlide(index) {
            items.forEach((item, i) => {
                item.classList.toggle('active', i === index);
            });
        }

        function nextSlide() {
            currentIndex = (currentIndex + 1) % items.length;
            showSlide(currentIndex);
        }

        function prevSlide() {
            currentIndex = (currentIndex - 1 + items.length) % items.length;
            showSlide(currentIndex);
        }

        setInterval(nextSlide, 2000);

        if (prevButton && nextButton) {
            prevButton.addEventListener('click', prevSlide);
            nextButton.addEventListener('click', nextSlide);
        }
    }
});

// Stat counter animation
const statCounters = document.querySelectorAll('.stat-num');

const animateCount = (element) => {
    const target = parseInt(element.dataset.target);
    let current = 0;
    const duration = 2000; // 2 seconds
    const increment = target / (duration / 10); // Calculate increment based on duration and update interval

    const updateCount = () => {
        if (current < target) {
            current += increment;
            element.textContent = Math.floor(current);
            requestAnimationFrame(updateCount);
        } else {
            element.textContent = target + '+'; // Append '+' here
        }
    };
    updateCount();
};

const options = {
    root: null, // viewport
    rootMargin: '0px',
    threshold: 0.5 // Trigger when 50% of the element is visible
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCount(entry.target);
            observer.unobserve(entry.target); // Stop observing once animated
        }
    });
}, options);

statCounters.forEach(counter => {
    observer.observe(counter);
});