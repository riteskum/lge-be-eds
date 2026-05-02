/**
 * Story sections for PDP: One Wall (centered) and Gaming (dark split layout).
 * @param {Element} block The block element
 */
export default function decorate(block) {
  const section = block.closest('.section');

  if (block.classList.contains('pdp-story-gaming')) {
    section?.classList.add('section-pdp-gaming');
    const row = block.firstElementChild;
    if (row) {
      row.classList.add('pdp-story-gaming-row');
      const cols = [...row.children];
      const eyebrow = cols[0]?.querySelector('p:first-child strong');
      if (eyebrow?.closest('p')) {
        eyebrow.closest('p').classList.add('pdp-story-eyebrow');
      }
      const stats = cols[0]?.querySelector(':scope > ul');
      if (stats) {
        stats.classList.add('pdp-story-stats');
      }
    }
    return;
  }

  if (block.classList.contains('pdp-story-wall')) {
    section?.classList.add('section-pdp-wall');
    const inner = block.querySelector(':scope > div > div');
    if (inner) inner.classList.add('pdp-story-wall-inner');
  }
}
