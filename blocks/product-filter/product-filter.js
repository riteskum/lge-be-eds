export default function decorate(block) {
  const items = block.querySelectorAll('p');
  const nav = document.createElement('nav');
  nav.className = 'filter-bar';
  nav.setAttribute('aria-label', 'Product categories');

  const ul = document.createElement('ul');
  ul.className = 'filter-list';

  items.forEach((item) => {
    const li = document.createElement('li');
    const link = item.querySelector('a');
    if (link) {
      li.append(link);
    } else {
      const btn = document.createElement('button');
      btn.className = 'filter-btn active';
      btn.textContent = item.textContent.trim();
      li.append(btn);
    }
    ul.append(li);
  });

  block.textContent = '';
  nav.append(ul);
  block.append(nav);
}
