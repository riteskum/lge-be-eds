export default function decorate(block) {
  const row = block.children[0];
  if (!row) return;

  const cols = [...row.children];
  const imageCol = cols[0];
  const textCol = cols[1];

  block.textContent = '';

  if (imageCol) {
    const picture = imageCol.querySelector('picture');
    if (picture) {
      const imgWrap = document.createElement('div');
      imgWrap.className = 'features-image';
      imgWrap.append(picture);
      block.append(imgWrap);
    }
  }

  if (textCol) {
    const content = document.createElement('div');
    content.className = 'features-content';

    const heading = textCol.querySelector('h2');
    if (heading) content.append(heading);

    const items = textCol.querySelectorAll('h4');
    items.forEach((h4) => {
      const item = document.createElement('div');
      item.className = 'features-item';

      const icon = h4.previousElementSibling?.querySelector('.icon');
      if (icon) {
        const iconWrap = document.createElement('div');
        iconWrap.className = 'features-icon';
        iconWrap.append(icon);
        item.append(iconWrap);
      }

      const info = document.createElement('div');
      info.className = 'features-info';
      info.append(h4);

      let next = h4.nextElementSibling;
      while (next && next.tagName !== 'H4' && !next.querySelector('.icon')) {
        const curr = next;
        next = next.nextElementSibling;
        info.append(curr);
      }

      item.append(info);
      content.append(item);
    });

    block.append(content);
  }
}
