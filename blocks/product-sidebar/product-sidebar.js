export default function decorate(block) {
  const rows = [...block.children];
  const sidebar = document.createElement('aside');
  sidebar.className = 'sidebar';
  sidebar.setAttribute('aria-label', 'Filters');

  const heading = document.createElement('h3');
  heading.className = 'sidebar-title';
  heading.textContent = 'Filters';
  sidebar.append(heading);

  const subtitle = document.createElement('p');
  subtitle.className = 'sidebar-subtitle';
  subtitle.textContent = 'REFINE YOUR SELECTION';
  sidebar.append(subtitle);

  rows.forEach((row) => {
    const cols = [...row.children];
    if (cols.length < 2) return;

    const groupName = cols[0]?.textContent?.trim();
    const optionsText = cols[1]?.textContent?.trim();
    if (!groupName || !optionsText) return;

    const group = document.createElement('div');
    group.className = 'filter-group';

    const groupTitle = document.createElement('h4');
    groupTitle.className = 'filter-group-title';
    groupTitle.textContent = groupName;
    group.append(groupTitle);

    const options = optionsText.split(',').map((o) => o.trim()).filter(Boolean);
    options.forEach((opt) => {
      const label = document.createElement('label');
      label.className = 'filter-option';

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.name = groupName.toLowerCase().replace(/\s+/g, '-');
      checkbox.value = opt;

      const text = document.createElement('span');
      text.textContent = opt;

      label.append(checkbox, text);
      group.append(label);
    });

    sidebar.append(group);
  });

  const clearBtn = document.createElement('button');
  clearBtn.className = 'filter-clear';
  clearBtn.textContent = 'Clear All';
  clearBtn.addEventListener('click', () => {
    sidebar.querySelectorAll('input[type="checkbox"]').forEach((cb) => {
      cb.checked = false;
    });
  });
  sidebar.append(clearBtn);

  block.textContent = '';
  block.append(sidebar);
}
