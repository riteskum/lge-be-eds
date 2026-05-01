export default function decorate(block) {
  const rows = [...block.children];
  const ul = document.createElement('ul');

  rows.forEach((row) => {
    const li = document.createElement('li');
    const cols = [...row.children];

    const imageCol = cols[0];
    if (imageCol) {
      const picture = imageCol.querySelector('picture');
      if (picture) {
        const imgWrap = document.createElement('div');
        imgWrap.className = 'product-cards-image';
        imgWrap.append(picture);
        li.append(imgWrap);
      }
    }

    const textCol = cols[1];
    if (textCol) {
      const body = document.createElement('div');
      body.className = 'product-cards-body';

      const category = textCol.querySelector('p > strong');
      if (category && !category.closest('a')) {
        const catEl = document.createElement('span');
        catEl.className = 'product-cards-category';
        catEl.textContent = category.textContent;
        body.append(catEl);
        category.closest('p')?.remove();
      }

      while (textCol.firstChild) body.append(textCol.firstChild);

      const price = body.querySelector('.product-cards-price');
      if (!price) {
        const allP = body.querySelectorAll('p');
        const lastTextP = [...allP].filter((p) => !p.querySelector('a') && p.textContent.includes('€'));
        if (lastTextP.length) {
          lastTextP[0].className = 'product-cards-price';
        }
      }

      const detailLink = body.querySelector('a');
      if (detailLink) {
        const footer = document.createElement('div');
        footer.className = 'product-cards-footer';
        const priceEl = body.querySelector('.product-cards-price');
        if (priceEl) footer.append(priceEl);
        footer.append(detailLink.closest('p') || detailLink);
        body.append(footer);
      }

      li.append(body);
    }

    ul.append(li);
  });

  block.textContent = '';
  block.append(ul);
}
