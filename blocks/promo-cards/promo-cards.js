export default function decorate(block) {
  const cards = [...block.children];
  const ul = document.createElement('ul');

  cards.forEach((row) => {
    const li = document.createElement('li');
    const cols = [...row.children];
    const imageCol = cols[0];
    const textCol = cols[1];

    if (imageCol) {
      const picture = imageCol.querySelector('picture');
      if (picture) {
        const imgWrap = document.createElement('div');
        imgWrap.className = 'promo-cards-image';
        imgWrap.append(picture);
        li.append(imgWrap);
      }
    }

    if (textCol) {
      const body = document.createElement('div');
      body.className = 'promo-cards-body';
      while (textCol.firstChild) body.append(textCol.firstChild);
      li.append(body);
    }

    ul.append(li);
  });

  block.textContent = '';
  block.append(ul);
}
