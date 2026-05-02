#!/usr/bin/env node

/**
 * Pushes authored content to DA (da.live) via the Source API.
 *
 * Usage:
 *   1. Open https://da.live in your browser and log in with GitHub.
 *   2. Open DevTools (F12) → Network tab.
 *   3. Click any folder in DA – look for a request to admin.da.live.
 *   4. Copy the Authorization header value (the part after "Bearer ").
 *   5. Run:  node scripts/push-content.js <YOUR_TOKEN>
 */

const ORG = 'riteskum';
const REPO = 'lge-be-eds';
const API = `https://admin.da.live/source/${ORG}/${REPO}`;

const token = process.argv[2];
if (!token) {
  console.error('Usage: node scripts/push-content.js <DA_BEARER_TOKEN>');
  console.error('\nTo get your token:');
  console.error('  1. Open https://da.live and log in');
  console.error('  2. Open DevTools → Network tab');
  console.error('  3. Click any folder in DA');
  console.error('  4. Find a request to admin.da.live → copy the Authorization header value');
  process.exit(1);
}

/* ---------- NAV content ---------- */
const navHtml = `<body>
  <header></header>
  <main>
    <div>
      <p><strong><a href="/">LG Belgique</a></strong></p>
    </div>
    <div>
      <ul>
        <li><a href="/televisions">Téléviseurs</a></li>
        <li><a href="/audio">Audio</a></li>
        <li><a href="/electromenager">Électroménager</a></li>
        <li><a href="/informatique">Informatique</a></li>
        <li><a href="/climatisation">Climatisation</a></li>
        <li><a href="/support">Support</a></li>
      </ul>
    </div>
    <div>
      <p><span class="icon icon-account"></span><span class="icon icon-cart"></span></p>
    </div>
  </main>
  <footer></footer>
</body>`;

/* ---------- FOOTER content ---------- */
const footerHtml = `<body>
  <header></header>
  <main>
    <div>
      <div class="columns">
        <div>
          <div>
            <p><strong>LG Belgique</strong></p>
            <p>Innovation pour une vie meilleure. Découvrez l'univers LG et laissez-vous inspirer.</p>
          </div>
          <div>
            <h3>PRODUITS</h3>
            <ul>
              <li><a href="/televisions">Téléviseurs</a></li>
              <li><a href="/audio">Audio &amp; Barre de son</a></li>
              <li><a href="/lave-linge">Lave-linge</a></li>
              <li><a href="/refrigerateurs">Réfrigérateurs</a></li>
            </ul>
          </div>
          <div>
            <h3>SUPPORT</h3>
            <ul>
              <li><a href="/enregistrer">Enregistrer un produit</a></li>
              <li><a href="/assistance">Assistance</a></li>
              <li><a href="/newsletter">Newsletter</a></li>
              <li><a href="/aide">Aide</a></li>
            </ul>
          </div>
          <div>
            <h3>LÉGAL</h3>
            <ul>
              <li><a href="/conditions">Conditions d'utilisation</a></li>
              <li><a href="/confidentialite">Politique de confidentialité</a></li>
              <li><a href="/plan-du-site">Plan du site</a></li>
              <li><a href="/accessibilite">Accessibilité</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div>
      <p>Copyright © 2024 LG Electronics. Tous droits réservés.</p>
      <p><strong>LG Belgique (FR)</strong></p>
    </div>
  </main>
  <footer></footer>
</body>`;

/* ---------- INDEX (homepage) content ---------- */
function imgRef(filename) {
  const base = filename.replace(/\.[^.]+$/, '').replace(/[^a-z0-9]/gi, '');
  return `./media_${base}.${filename.split('.').pop()}`;
}

const indexHtml = `<body>
  <header></header>
  <main>
    <div>
      <div class="hero">
        <div>
          <div>
            <picture>
              <img src="${imgRef('hero-oled-tv.jpg')}" alt="Modern living room with OLED TV">
            </picture>
          </div>
        </div>
        <div>
          <div>
            <p><em>NOUVEAUTÉ 2024</em></p>
            <h1>OLED evo. <em>La perfection.</em></h1>
            <p>Découvrez une clarté sans précédent et des noirs absolus. Plus qu'un écran, une fenêtre sur l'infini.</p>
            <p><strong><a href="/televisions/oled">En savoir plus</a></strong></p>
            <p><em><a href="/televisions/oled">Acheter</a></em></p>
          </div>
        </div>
        <div>
          <div>
            <picture>
              <img src="${imgRef('hero-audio.jpg')}" alt="LG Audio Headphones">
            </picture>
          </div>
        </div>
        <div>
          <div>
            <p><em>IMMERSION TOTALE</em></p>
            <h2>Son Pur. <em>Sans Limite.</em></h2>
            <p>Laissez-vous transporter par une clarté sonore exceptionnelle. Le futur de l'audio est ici.</p>
            <p><strong><a href="/audio">Explorer</a></strong></p>
            <p><em><a href="/audio">Acheter</a></em></p>
          </div>
        </div>
        <div>
          <div>
            <picture>
              <img src="${imgRef('hero-refrigerator.jpg')}" alt="LG InstaView Refrigerator">
            </picture>
          </div>
        </div>
        <div>
          <div>
            <p><em>ART DE VIVRE</em></p>
            <h2>Cuisine <em>Intelligente.</em></h2>
            <p>L'élégance rencontre la fraîcheur. Découvrez nos réfrigérateurs InstaView™ et optimisez votre quotidien.</p>
            <p><strong><a href="/electromenager">Découvrir</a></strong></p>
            <p><em><a href="/electromenager">Acheter</a></em></p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <h2>Offres spéciales</h2>
      <p>Le meilleur de la technologie LG, sélectionné pour vous. <a href="/offres">Voir toutes les offres</a></p>
      <div class="promo-cards">
        <div>
          <div>
            <picture>
              <img src="${imgRef('promo-electromenager.jpg')}" alt="Mois de l'Électroménager LG">
            </picture>
          </div>
          <div>
            <h3>Mois de l'Électroménager</h3>
            <p>Jusqu'à 500€ remboursés sur une sélection d'appareils économes en énergie.</p>
            <p><a href="/electromenager/offres">Découvrir →</a></p>
          </div>
        </div>
        <div>
          <div>
            <picture>
              <img src="${imgRef('promo-audio.jpg')}" alt="Série Audio LG">
            </picture>
          </div>
          <div>
            <h3>Série Audio</h3>
            <p>Un son pur, partout.</p>
            <p><a href="/audio/series">Explorer →</a></p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <h2>Produits Vedettes</h2>
      <p>Conçus avec précision pour améliorer votre quotidien.</p>
      <div class="product-cards">
        <div>
          <div>
            <picture>
              <img src="${imgRef('product-oled-c3.jpg')}" alt="LG OLED evo C3 65 pouces">
            </picture>
          </div>
          <div>
            <p><strong>OLED TV</strong></p>
            <h3>LG OLED evo C3 65''</h3>
            <ul>
              <li>Processeur α9 AI Gen6</li>
              <li>Luminosité accrue de 20%</li>
              <li>Design ultra-fin</li>
            </ul>
            <p>2 499 €</p>
            <p><a href="/televisions/oled-c3">Détails</a></p>
          </div>
        </div>
        <div>
          <div>
            <picture>
              <img src="${imgRef('product-vivace-v9.jpg')}" alt="LG Vivace V9 11kg">
            </picture>
          </div>
          <div>
            <p><strong>SOIN DU LINGE</strong></p>
            <h3>LG Vivace V9 11kg</h3>
            <ul>
              <li>Technologie AI DD™</li>
              <li>TurboWash™ 360°</li>
              <li>Classe énergétique A</li>
            </ul>
            <p>899 €</p>
            <p><a href="/lave-linge/vivace-v9">Détails</a></p>
          </div>
        </div>
        <div>
          <div>
            <picture>
              <img src="${imgRef('product-ultragear-27.jpg')}" alt="UltraGear 27 pouces OLED">
            </picture>
          </div>
          <div>
            <p><strong>INFORMATIQUE</strong></p>
            <h3>UltraGear™ 27'' OLED</h3>
            <ul>
              <li>Taux de rafraîchissement 240Hz</li>
              <li>Temps de réponse 0.03ms</li>
              <li>HDR10 Pro</li>
            </ul>
            <p>999 €</p>
            <p><a href="/informatique/ultragear-27">Détails</a></p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div class="features">
        <div>
          <div>
            <picture>
              <img src="${imgRef('features-smart-home.jpg')}" alt="Maison intelligente LG">
            </picture>
          </div>
          <div>
            <h2>L'intelligence au service de votre foyer.</h2>
            <p><span class="icon icon-smarthome"></span></p>
            <h4>LG ThinQ™</h4>
            <p>Contrôlez vos appareils à distance et recevez des notifications en temps réel sur votre smartphone.</p>
            <p><span class="icon icon-durability"></span></p>
            <h4>Technologie Durable</h4>
            <p>Nos compresseurs Linear Inverter sont garantis 10 ans pour une tranquillité d'esprit totale.</p>
            <p><span class="icon icon-design-icon"></span></p>
            <h4>Design Iconique</h4>
            <p>Une esthétique minimaliste qui s'intègre parfaitement dans tout intérieur moderne.</p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div class="support-links">
        <div>
          <div>
            <h2>Besoin d'aide ?</h2>
            <p>Nos experts LG Belgique sont à votre disposition pour vous accompagner.</p>
          </div>
          <div>
            <p><span class="icon icon-manual"></span></p>
            <p>Manuels</p>
          </div>
          <div>
            <p><span class="icon icon-download"></span></p>
            <p>Drivers</p>
          </div>
          <div>
            <p><span class="icon icon-repair"></span></p>
            <p>Réparation</p>
          </div>
          <div>
            <p><span class="icon icon-contact"></span></p>
            <p>Contact</p>
          </div>
        </div>
      </div>
    </div>
  </main>
  <footer></footer>
</body>`;

/* ---------- TELEVISIONS PLP content ---------- */
const televisionsHtml = `<body>
  <header></header>
  <main>
    <div>
      <div class="breadcrumb">
        <div><div>
          <p><a href="/">Accueil</a></p>
          <p><a href="/televisions">Téléviseurs</a></p>
        </div></div>
      </div>
    </div>
    <div>
      <div class="hero">
        <div><div>
          <picture><img src="${imgRef('hero-oled-tv.jpg')}" alt="TV OLED evo LG"></picture>
        </div></div>
        <div><div>
          <h1>TV OLED evo</h1>
          <p>L'apogée de l'image et du design. Plongez dans une immersion totale avec la technologie OLED la plus avancée de LG, offrant une luminosité exceptionnelle et des contrastes infinis.</p>
        </div></div>
      </div>
    </div>
    <div>
      <div class="product-sidebar">
        <div><div><p>DISPLAY TYPE</p></div><div><p>OLED evo, OLED</p></div></div>
        <div><div><p>SCREEN SIZE</p></div><div><p>42" - 48", 55" - 65", 77" +</p></div></div>
        <div><div><p>RESOLUTION</p></div><div><p>4K Ultra HD, 8K Ultra HD</p></div></div>
      </div>
      <div class="results-bar">
        <div><div><p>12</p></div><div><p>Populaire</p></div></div>
      </div>
      <div class="product-cards">
        <div>
          <div>
            <p><strong>NOUVEAU</strong></p>
            <picture><img src="${imgRef('product-oled-c3.jpg')}" alt="LG OLED evo G3 65 pouces"></picture>
          </div>
          <div>
            <h3>LG OLED evo G3 65'' 4K Smart TV 2024</h3>
            <p><em>OLED65G36LA</em></p>
            <p>2 799 €</p>
            <p><a href="/televisions/oled-g3">Voir le produit</a></p>
          </div>
        </div>
        <div>
          <div>
            <picture><img src="${imgRef('product-oled-c3.jpg')}" alt="LG OLED evo C3 55 pouces"></picture>
          </div>
          <div>
            <h3>LG OLED evo C3 55'' 4K Smart TV</h3>
            <p><em>OLED55C34LA</em></p>
            <p>1 899 €</p>
            <p><a href="/televisions/oled-c3">Voir le produit</a></p>
          </div>
        </div>
        <div>
          <div>
            <p><strong>WIRELESS</strong></p>
            <picture><img src="${imgRef('product-oled-c3.jpg')}" alt="LG OLED evo M3 77 pouces"></picture>
          </div>
          <div>
            <h3>LG OLED evo M3 77'' Wireless OLED TV</h3>
            <p><em>OLED77M39LA</em></p>
            <p>4 999 €</p>
            <p><a href="/televisions/oled-m3">Voir le produit</a></p>
          </div>
        </div>
        <div>
          <div>
            <p><strong>NOUVEAU</strong></p>
            <picture><img src="${imgRef('product-oled-c3.jpg')}" alt="LG OLED evo C4 65 pouces"></picture>
          </div>
          <div>
            <h3>LG OLED evo C4 65'' 4K Smart TV 2024</h3>
            <p><em>OLED65C46LA</em></p>
            <p>2 299 €</p>
            <p><a href="/televisions/oled-c4">Voir le produit</a></p>
          </div>
        </div>
        <div>
          <div>
            <picture><img src="${imgRef('product-oled-c3.jpg')}" alt="LG OLED B3 55 pouces"></picture>
          </div>
          <div>
            <h3>LG OLED B3 55'' 4K Smart TV</h3>
            <p><em>OLED55B36LA</em></p>
            <p>1 299 €</p>
            <p><a href="/televisions/oled-b3">Voir le produit</a></p>
          </div>
        </div>
        <div>
          <div>
            <p><strong>NOUVEAU</strong></p>
            <picture><img src="${imgRef('product-oled-c3.jpg')}" alt="LG OLED evo G4 77 pouces"></picture>
          </div>
          <div>
            <h3>LG OLED evo G4 77'' 4K Smart TV 2024</h3>
            <p><em>OLED77G46LS</em></p>
            <p>3 999 €</p>
            <p><a href="/televisions/oled-g4">Voir le produit</a></p>
          </div>
        </div>
      </div>
      <div class="section-metadata">
        <div><div><p>style</p></div><div><p>product-listing</p></div></div>
      </div>
    </div>
  </main>
  <footer></footer>
</body>`;

/* ---------- Push logic ---------- */
const pages = [
  { path: 'nav.html', label: 'Navigation', html: navHtml },
  { path: 'footer.html', label: 'Footer', html: footerHtml },
  { path: 'index.html', label: 'Homepage', html: indexHtml },
  { path: 'televisions.html', label: 'Televisions PLP', html: televisionsHtml },
];

/* ---------- Image files to upload ---------- */
/* eslint-disable global-require */
const fs = require('node:fs');
const nodePath = require('node:path');

const imageDir = nodePath.resolve(__dirname, '../images');

const imageFiles = [
  'hero-oled-tv.jpg',
  'hero-refrigerator.jpg',
  'hero-audio.jpg',
  'promo-electromenager.jpg',
  'promo-audio.jpg',
  'product-oled-c3.jpg',
  'product-vivace-v9.jpg',
  'product-ultragear-27.jpg',
  'features-smart-home.jpg',
];

/* ---------- Push helpers ---------- */
async function pushHtml(page) {
  const blob = new Blob([page.html], { type: 'text/html' });
  const form = new FormData();
  form.append('data', blob, page.path);

  const url = `${API}/${page.path}`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { Authorization: `Bearer ${token}` },
    body: form,
  });

  if (res.ok) {
    const json = await res.json();
    console.log(`  ✓ ${page.label} → ${json.aem?.previewUrl || 'done'}`);
  } else {
    const text = await res.text().catch(() => '');
    console.error(`  ✗ ${page.label} (${res.status}) ${text}`);
  }
}

function toMediaName(filename) {
  const ext = nodePath.extname(filename).slice(1);
  const base = filename.replace(/\.[^.]+$/, '').replace(/[^a-z0-9]/gi, '');
  return `media_${base}.${ext}`;
}

async function pushImage(filename) {
  const filePath = nodePath.join(imageDir, filename);
  if (!fs.existsSync(filePath)) {
    console.error(`  ✗ ${filename} — file not found at ${filePath}`);
    return;
  }
  const buffer = fs.readFileSync(filePath);
  const ext = nodePath.extname(filename).slice(1).toLowerCase();
  const mimeMap = {
    jpg: 'image/jpeg', jpeg: 'image/jpeg', png: 'image/png', gif: 'image/gif', svg: 'image/svg+xml',
  };
  const mediaName = toMediaName(filename);
  const blob = new Blob([buffer], { type: mimeMap[ext] || 'image/jpeg' });
  const form = new FormData();
  form.append('data', blob, mediaName);

  const url = `${API}/${mediaName}`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { Authorization: `Bearer ${token}` },
    body: form,
  });

  if (res.ok) {
    console.log(`  ✓ ${filename} → ${mediaName}`);
  } else {
    const text = await res.text().catch(() => '');
    console.error(`  ✗ ${filename} (${res.status}) ${text}`);
  }
}

/* ---------- Main ---------- */
(async () => {
  console.log(`\nPushing content to DA (${ORG}/${REPO}) …\n`);

  console.log('Uploading images as media_ blobs …');
  for (const img of imageFiles) {
    await pushImage(img);
  }

  console.log('\nPushing pages …');
  for (const page of pages) {
    await pushHtml(page);
  }

  console.log('\nDone! Visit https://main--lge-be-eds--riteskum.aem.page/ to see the result.\n');
})();
