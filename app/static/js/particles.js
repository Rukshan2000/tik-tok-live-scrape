const particlesContainer = document.querySelector('.particles');
for (let i = 0; i < 50; i++) {
    const particle = document.createElement('div');
    particle.classList.add('particle');
    particle.style.left = Math.random() * 100 + '%';
    particle.style.animationDelay = Math.random() * 3 + 's';
    particle.style.setProperty('--tx', (Math.random() * 200 - 100) + 'px');
    particlesContainer.appendChild(particle);
}