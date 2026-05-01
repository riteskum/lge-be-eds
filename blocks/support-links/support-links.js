export default function decorate(block) {
  const row = block.children[0];
  if (!row) return;

  const cells = [...row.children];
  const textCell = cells.shift();

  block.textContent = '';

  if (textCell) {
    const intro = document.createElement('div');
    intro.className = 'support-links-intro';
    while (textCell.firstChild) intro.append(textCell.firstChild);
    block.append(intro);
  }

  const grid = document.createElement('div');
  grid.className = 'support-links-grid';

  cells.forEach((cell) => {
    const card = document.createElement('div');
    card.className = 'support-links-card';

    const icon = cell.querySelector('.icon');
    if (icon) {
      const iconWrap = document.createElement('div');
      iconWrap.className = 'support-links-icon';
      iconWrap.append(icon);
      card.append(iconWrap);
    }

    const paragraphs = cell.querySelectorAll('p');
    paragraphs.forEach((p) => {
      if (!p.querySelector('.icon') && p.textContent.trim()) {
        const label = document.createElement('span');
        label.className = 'support-links-label';
        label.textContent = p.textContent.trim();
        card.append(label);
      }
    });

    grid.append(card);
  });

  block.append(grid);
}
