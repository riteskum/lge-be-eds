export default function decorate(block) {
  const links = block.querySelectorAll('a');
  const nav = document.createElement('nav');
  nav.setAttribute('aria-label', 'Breadcrumb');

  const ol = document.createElement('ol');
  ol.className = 'breadcrumb-list';

  links.forEach((link, i) => {
    const li = document.createElement('li');
    li.className = 'breadcrumb-item';
    if (i === links.length - 1) {
      li.setAttribute('aria-current', 'page');
      const span = document.createElement('span');
      span.textContent = link.textContent;
      li.append(span);
    } else {
      li.append(link.cloneNode(true));
    }
    ol.append(li);
  });

  block.textContent = '';
  nav.append(ol);
  block.append(nav);
}
