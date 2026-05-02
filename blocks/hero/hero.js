const AUTOPLAY_INTERVAL = 6000;

function buildSlide(pictureRow, contentRow) {
  const picture = pictureRow.querySelector('picture');
  const contentCell = contentRow.querySelector(':scope > div');
  if (!picture || !contentCell) return null;

  const slide = document.createElement('div');
  slide.className = 'hero-slide';

  const bgContainer = document.createElement('div');
  bgContainer.className = 'hero-bg';
  bgContainer.append(picture);
  slide.append(bgContainer);

  const content = document.createElement('div');
  content.className = 'hero-content';

  const badge = contentCell.querySelector('em');
  if (badge && !badge.closest('a')) {
    const badgeEl = document.createElement('span');
    badgeEl.className = 'hero-badge';
    badgeEl.textContent = badge.textContent;
    content.append(badgeEl);
    badge.closest('p')?.remove();
  }

  const heading = contentCell.querySelector('h1, h2');
  if (heading) content.append(heading);

  const desc = contentCell.querySelector('p:not(.button-wrapper)');
  if (desc) {
    desc.className = 'hero-description';
    content.append(desc);
  }

  const buttons = contentCell.querySelectorAll('.button-wrapper');
  if (buttons.length) {
    const btnGroup = document.createElement('div');
    btnGroup.className = 'hero-buttons';
    buttons.forEach((btn) => btnGroup.append(btn));
    content.append(btnGroup);
  }

  slide.append(content);
  return slide;
}

function goToSlide(block, index) {
  const slides = block.querySelectorAll('.hero-slide');
  const dots = block.querySelectorAll('.hero-dot');
  const total = slides.length;
  const next = ((index % total) + total) % total;

  slides.forEach((s, i) => s.classList.toggle('active', i === next));
  dots.forEach((d, i) => d.classList.toggle('active', i === next));
  block.dataset.active = next;
}

export default function decorate(block) {
  const rows = [...block.children];
  if (rows.length < 2) return;

  const slides = [];
  for (let i = 0; i < rows.length - 1; i += 2) {
    const slide = buildSlide(rows[i], rows[i + 1]);
    if (slide) slides.push(slide);
  }

  if (!slides.length) return;

  block.textContent = '';

  const track = document.createElement('div');
  track.className = 'hero-track';
  slides.forEach((s, i) => {
    if (i === 0) s.classList.add('active');
    track.append(s);
  });
  block.append(track);

  if (slides.length > 1) {
    const prevBtn = document.createElement('button');
    prevBtn.className = 'hero-arrow hero-prev';
    prevBtn.setAttribute('aria-label', 'Previous slide');
    prevBtn.innerHTML = '&#8249;';
    prevBtn.addEventListener('click', () => {
      goToSlide(block, Number(block.dataset.active) - 1);
    });

    const nextBtn = document.createElement('button');
    nextBtn.className = 'hero-arrow hero-next';
    nextBtn.setAttribute('aria-label', 'Next slide');
    nextBtn.innerHTML = '&#8250;';
    nextBtn.addEventListener('click', () => {
      goToSlide(block, Number(block.dataset.active) + 1);
    });

    block.append(prevBtn, nextBtn);

    const dotsContainer = document.createElement('div');
    dotsContainer.className = 'hero-dots';
    slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.className = `hero-dot${i === 0 ? ' active' : ''}`;
      dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
      dot.addEventListener('click', () => goToSlide(block, i));
      dotsContainer.append(dot);
    });
    block.append(dotsContainer);

    block.dataset.active = 0;

    let timer = setInterval(() => {
      goToSlide(block, Number(block.dataset.active) + 1);
    }, AUTOPLAY_INTERVAL);

    block.addEventListener('mouseenter', () => clearInterval(timer));
    block.addEventListener('mouseleave', () => {
      timer = setInterval(() => {
        goToSlide(block, Number(block.dataset.active) + 1);
      }, AUTOPLAY_INTERVAL);
    });
  } else {
    slides[0].classList.add('active');
    block.dataset.active = 0;
  }
}
