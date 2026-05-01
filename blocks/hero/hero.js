export default function decorate(block) {
  const rows = [...block.children];
  if (rows.length < 2) return;

  const pictureRow = rows[0];
  const contentRow = rows[1];
  const picture = pictureRow.querySelector('picture');
  const contentCell = contentRow.querySelector(':scope > div');

  if (!picture || !contentCell) return;

  block.textContent = '';

  const bgContainer = document.createElement('div');
  bgContainer.className = 'hero-bg';
  bgContainer.append(picture);
  block.append(bgContainer);

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

  const heading = contentCell.querySelector('h1');
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

  block.append(content);
}
