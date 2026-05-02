/**
 * Document Authoring / preview pipeline often strips /images/ URLs and emits src="about:error".
 * Repair using stable alt text → repo paths under /images/ (served from Git on *.aem.page).
 */

const ALT_TO_IMAGE_PATH = {
  /* PLP — Téléviseurs (distinct asset per row; matches push televisions.html) */
  'LG OLED evo G3 65 pouces': '/images/product-oled-c3.jpg',
  'LG OLED evo C3 55 pouces': '/images/pdp-g4-97-lifestyle.jpg',
  'LG OLED evo M3 77 pouces': '/images/pdp-g4-97-main.jpg',
  'LG OLED evo C4 65 pouces': '/images/pdp-g4-97-rear.jpg',
  'LG OLED B3 55 pouces': '/images/pdp-g4-97-side.jpg',
  'LG OLED evo G4 77 pouces': '/images/pdp-g4-97-wall.jpg',
  'LG OLED evo G4 97 pouces — vue principale': '/images/pdp-g4-97-main.jpg',
  'Vue de profil': '/images/pdp-g4-97-side.jpg',
  'Fixation murale': '/images/pdp-g4-97-wall.jpg',
  'Ambiance salon': '/images/pdp-g4-97-lifestyle.jpg',
  'Connectique arrière': '/images/pdp-g4-97-rear.jpg',
  'Support mural motorisé': '/images/pdp-g4-97-mount.jpg',
  'Ambiance LG OLED G4': '/images/pdp-g4-97-lifestyle.jpg',
  'LG OLED G4 fixé au mur — One Wall Design': '/images/pdp-g4-97-wall.jpg',
  'Jeu sur LG OLED G4': '/images/pdp-g4-97-rear.jpg',
  'LG Soundbar S95TR': '/images/promo-audio.jpg',
  'LG Premium Care+': '/images/features-smart-home.jpg',
};

/**
 * @param {Element} root Usually `main`
 */
export default function fixBrokenAemImages(root) {
  if (!root) return;
  root.querySelectorAll('img').forEach((img) => {
    const raw = img.getAttribute('src') || '';
    const alt = (img.getAttribute('alt') || '').trim();
    const path = ALT_TO_IMAGE_PATH[alt];
    if (!path) return;

    const broken = !raw || raw === 'about:error' || raw.startsWith('about:');
    const looksGood = (raw.startsWith('/images/') || raw.startsWith('http')) && !broken;
    if (looksGood) return;

    try {
      img.src = new URL(path, window.location.origin).href;
    } catch {
      img.setAttribute('src', path);
    }
  });
}
