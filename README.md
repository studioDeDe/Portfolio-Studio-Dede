# Portfolio Dede

Statische website (HTML/CSS, geen build nodig om te hosten). Pagina's: `index.html`, `werk.html` en 15 projectpagina's in `projects/`.

## Aanpassen
- Projectteksten en -beelden: `build/content.json`. Homepage-teksten en e-mailadres: bovenaan `build/build.py`.
- Daarna opnieuw genereren: `python3 build/build.py` (Python 3, geen extra pakketten).
- Kleuren en lettertypes (volgens de styleguide): bovenaan `assets/css/style.css`.

## Op GitHub zetten (GitHub Pages)
1. Maak op github.com een nieuwe repository (bv. `portfolio`, public) en upload alle bestanden uit deze map (of `git init`, `git add .`, `git commit`, `git push`).
2. Repository → **Settings → Pages** → Source: *Deploy from a branch* → branch `main`, map `/ (root)` → Save. Na een minuut staat de site op `https://<gebruikersnaam>.github.io/portfolio/`.

## Eigen domein koppelen
1. Settings → Pages → **Custom domain**: vul je domein in (bv. `www.jouwdomein.be`) → Save. GitHub maakt zelf een `CNAME`-bestand aan.
2. Stel bij je domeinregistrar DNS-records in:
   - `www`: **CNAME** → `<gebruikersnaam>.github.io`
   - kale domein (`jouwdomein.be`): **A**-records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
3. Wacht tot de DNS-check slaagt en vink **Enforce HTTPS** aan.
4. Optioneel: zet `SITE_URL = 'https://www.jouwdomein.be'` in `build/build.py` en run het script opnieuw (canonical-links).

Controleer de DNS-waarden eventueel in de GitHub-documentatie ("Managing a custom domain for your GitHub Pages site").

## Let op: lettertype
Geist wordt nu via Google Fonts geladen. Voor GDPR-vriendelijker hosten: download Geist (open source, Vercel), zet de `.woff2`-bestanden in `assets/fonts/`, voeg `@font-face`-regels toe aan `style.css` en verwijder de drie Google Fonts-`<link>`-regels in `build/build.py`.
