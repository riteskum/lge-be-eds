export default function decorate(block) {
  const cols = [...block.querySelector(':scope > div')?.children || []];
  const count = cols[0]?.textContent?.trim() || '0';
  const sortLabel = cols[1]?.textContent?.trim() || 'Populaire';

  const bar = document.createElement('div');
  bar.className = 'results-header';

  const countEl = document.createElement('span');
  countEl.className = 'results-count';
  countEl.textContent = `${count} RÉSULTATS`;
  bar.append(countEl);

  const sortWrap = document.createElement('div');
  sortWrap.className = 'results-sort';

  const sortLabelEl = document.createElement('span');
  sortLabelEl.textContent = 'Trier par:';
  sortWrap.append(sortLabelEl);

  const select = document.createElement('select');
  select.setAttribute('aria-label', 'Sort products');
  const options = [sortLabel, 'Prix croissant', 'Prix décroissant', 'Nouveautés'];
  options.forEach((opt, i) => {
    const option = document.createElement('option');
    option.value = opt;
    option.textContent = opt;
    if (i === 0) option.selected = true;
    select.append(option);
  });
  sortWrap.append(select);
  bar.append(sortWrap);

  block.textContent = '';
  block.append(bar);
}
