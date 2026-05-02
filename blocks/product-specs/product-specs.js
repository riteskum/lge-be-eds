export default function decorate(block) {
  block.closest('.section')?.classList.add('section-pdp-specs');

  const rows = [...block.children];
  const dl = document.createElement('dl');
  dl.className = 'product-specs-list';

  rows.forEach((row) => {
    const cols = [...row.children];
    if (cols.length < 2) return;
    const dt = document.createElement('dt');
    dt.textContent = cols[0]?.textContent?.trim() || '';
    const dd = document.createElement('dd');
    dd.textContent = cols[1]?.textContent?.trim() || '';
    dl.append(dt, dd);
  });

  block.textContent = '';
  block.append(dl);
}
