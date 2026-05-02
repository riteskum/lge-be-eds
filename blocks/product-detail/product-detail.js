export default function decorate(block) {
  const rows = [...block.children];
  const root = document.createElement('div');
  root.className = 'product-detail-inner';

  function enhanceBuyBox(buy) {
    const ps = [...buy.querySelectorAll(':scope > p')];
    ps.forEach((p) => {
      const strong = p.querySelector(':scope > strong');
      const em = p.querySelector(':scope > em');
      const hasBtn = p.querySelector('a.button');

      if (strong && !hasBtn && p.textContent.length < 80) {
        p.classList.add('product-detail-badge');
      } else if (em && !hasBtn && /^[A-Z0-9]{6,}$/i.test(em.textContent.trim())) {
        p.classList.add('product-detail-sku');
      } else if (!hasBtn && p.textContent.includes('€')) {
        if (!p.classList.contains('product-detail-price')) {
          p.classList.add('product-detail-price');
          const next = p.nextElementSibling;
          if (next && next.tagName === 'P' && /conseillé|conseille|TTC/i.test(next.textContent)) {
            next.classList.add('product-detail-price-note');
          }
        }
      }
    });

    const lists = buy.querySelectorAll(':scope > ul');
    lists.forEach((ul) => {
      ul.classList.add('product-detail-highlights');
    });

    const btnWraps = buy.querySelectorAll('.button-wrapper');
    if (btnWraps.length) {
      const actions = document.createElement('div');
      actions.className = 'product-detail-actions';
      btnWraps.forEach((w) => actions.append(w));
      const anchor = lists[0] || null;
      if (anchor) anchor.before(actions);
      else buy.append(actions);
    }
  }

  rows.forEach((row) => {
    const cols = [...row.children];
    const hasGallery = cols[0]?.querySelector('picture');

    if (cols.length >= 2 && hasGallery) {
      const gallery = document.createElement('div');
      gallery.className = 'product-detail-gallery';

      const col1 = cols[0];
      const pictures = [...col1.querySelectorAll(':scope picture')];
      if (pictures.length) {
        const mainWrap = document.createElement('div');
        mainWrap.className = 'product-detail-main-image';
        mainWrap.append(pictures[0]);
        gallery.append(mainWrap);
      }
      if (pictures.length > 1) {
        const thumbs = document.createElement('div');
        thumbs.className = 'product-detail-thumbs';
        pictures.slice(1).forEach((pic) => thumbs.append(pic));
        gallery.append(thumbs);
      }

      const buy = document.createElement('aside');
      buy.className = 'product-detail-buy';
      while (cols[1].firstChild) buy.append(cols[1].firstChild);
      enhanceBuyBox(buy);

      const rowWrap = document.createElement('div');
      rowWrap.className = 'product-detail-row';
      rowWrap.append(gallery, buy);
      root.append(rowWrap);
    } else {
      const extra = document.createElement('div');
      extra.className = 'product-detail-extra';
      while (row.firstChild) extra.append(row.firstChild);
      root.append(extra);
    }
  });

  block.textContent = '';
  block.append(root);
}
