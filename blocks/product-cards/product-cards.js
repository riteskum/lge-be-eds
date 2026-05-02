export default function decorate(block) {
  const rows = [...block.children];
  const ul = document.createElement('ul');

  rows.forEach((row) => {
    const li = document.createElement('li');
    const cols = [...row.children];

    const imageCol = cols[0];
    if (imageCol) {
      let picNode = imageCol.querySelector('picture');
      const orphanImg = imageCol.querySelector(':scope img:not(picture img)');
      if (!picNode && orphanImg) {
        picNode = document.createElement('picture');
        orphanImg.replaceWith(picNode);
        picNode.append(orphanImg);
      }
      if (picNode) {
        const imgWrap = document.createElement('div');
        imgWrap.className = 'product-cards-image';

        const badge = imageCol.querySelector('strong');
        if (badge) {
          const badgeEl = document.createElement('span');
          const badgeText = badge.textContent.trim();
          badgeEl.className = 'product-cards-badge';
          const colorMap = {
            NOUVEAU: '#e91e63',
            WIRELESS: '#333',
            NEW: '#e91e63',
          };
          badgeEl.style.backgroundColor = colorMap[badgeText.toUpperCase()] || '#333';
          badgeEl.textContent = badgeText;
          imgWrap.append(badgeEl);
        }

        imgWrap.append(picNode);
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

      const modelEl = body.querySelector('p > em');
      if (modelEl) {
        const modelWrap = document.createElement('span');
        modelWrap.className = 'product-cards-model';
        modelWrap.textContent = modelEl.textContent;
        const heading = body.querySelector('h3');
        if (heading) heading.after(modelWrap);
        modelEl.closest('p')?.remove();
      }

      const allP = body.querySelectorAll('p');
      const priceP = [...allP].filter((p) => !p.querySelector('a') && p.textContent.includes('€'));
      if (priceP.length) {
        priceP[0].className = 'product-cards-price';
        const priceLabel = document.createElement('span');
        priceLabel.className = 'product-cards-price-label';
        priceLabel.textContent = 'Prix conseillé';
        priceP[0].before(priceLabel);
      }

      const detailLink = body.querySelector('a');
      if (detailLink) {
        const footer = document.createElement('div');
        footer.className = 'product-cards-footer';

        const buyBtn = document.createElement('a');
        buyBtn.className = 'product-cards-buy';
        buyBtn.href = detailLink.href;
        buyBtn.textContent = 'Acheter';
        footer.append(buyBtn);

        const actions = document.createElement('div');
        actions.className = 'product-cards-actions';

        const compareLabel = document.createElement('label');
        compareLabel.className = 'product-cards-compare';
        const radio = document.createElement('input');
        radio.type = 'checkbox';
        radio.name = 'compare';
        const compareText = document.createElement('span');
        compareText.textContent = 'Comparer';
        compareLabel.append(radio, compareText);
        actions.append(compareLabel);

        const detailsLink = document.createElement('a');
        detailsLink.className = 'product-cards-details';
        detailsLink.href = detailLink.href;
        detailsLink.textContent = 'Détails';
        actions.append(detailsLink);

        footer.append(actions);
        detailLink.closest('p')?.remove();
        body.append(footer);
      }

      li.append(body);
    }

    ul.append(li);
  });

  block.textContent = '';
  block.append(ul);
}
