/**
 * Accessory / bundle cards row (PDP).
 * @param {Element} block The block element
 */
export default function decorate(block) {
  block.closest('.section')?.classList.add('section-pdp-bundles');

  const rows = [...block.children];
  if (rows.length < 2) return;

  const titleRow = rows[0];
  const cardsRow = rows[1];

  const wrap = document.createElement('div');
  wrap.className = 'pdp-bundles-inner';

  const head = document.createElement('div');
  head.className = 'pdp-bundles-head';
  while (titleRow.firstChild) head.append(titleRow.firstChild);

  const grid = document.createElement('div');
  grid.className = 'pdp-bundles-grid';

  [...cardsRow.children].forEach((cell) => {
    cell.classList.add('pdp-bundles-card');
    grid.append(cell);
  });

  wrap.append(head, grid);
  block.textContent = '';
  block.append(wrap);
}
