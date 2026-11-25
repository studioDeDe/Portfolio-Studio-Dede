#!/usr/bin/env python3
"""Genereert alle HTML-pagina's. Gebruik:  python3 build/build.py
Projecten (tekst, beelden): build/content.json  |  Teksten van de homepage + e-mail: hieronder."""
import json,os,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C=json.load(open(os.path.join(ROOT,'build/content.json')))
E=html.escape
# ───────── TEKSTEN ─────────
SITE_URL=''   # bv. 'https://www.jouwdomein.be' (optioneel: voor canonical/social previews)
EMAIL='delphinedelie@hotmail.com'
NAME='Studio Dede'
HERO='Graphic designer with a love for good design, bold ideas and playful details.'
SERVICES=[('Graphic design','Van print tot digitaal: ik maak ontwerpen die de juiste boodschap op een heldere en aantrekkelijke manier overbrengen.'),
 ('Webdesign','Ik ontwerp websites die er goed uitzien en tegelijk gebruiksvriendelijk zijn, met aandacht voor structuur, uitstraling en beleving.'),
 ('Branding','Ik ontwikkel merken van logo, kleur en typografie tot de volledige uitwerking op drukwerk, social media en andere toepassingen.'),
 ('Illustration & animation','Ik voeg graag een speels extraatje toe met illustraties en animaties die een huisstijl versterken en een ontwerp tot leven brengen.')]
ABOUT=['Hallo, ik ben Delphine, graphic designer met een passie voor vormgeving en alles wat daarbij komt kijken. Al 8 jaar werk ik in een creatief agency, waar ik aan heel uiteenlopende projecten meewerk. Die ervaring heeft mijn liefde voor het vak alleen maar versterkt en me de kans gegeven om mijn creatieve blik en vaardigheden verder te ontwikkelen.',
 'Ik haal veel voldoening uit het bedenken en uitwerken van ideeën en experimenteer graag met beeld, kleur en typografie. Ik ben nieuwsgierig, sta open voor nieuwe uitdagingen en blijf mezelf graag uitdagen om bij te leren.']
# ───────────────────────────
PR={p['slug']:p for p in C['projects']}
BACK='<svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.75 12h-17M10 5.25 3.25 12 10 18.75"/></svg>'
ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.75 12h17M14 5.25 20.75 12 14 18.75"/></svg>'
def img(b,i,alt,cls='',eager=False,extra=''):
    a=' loading="eager" fetchpriority="high"' if eager else ' loading="lazy" decoding="async"'
    return f'<img src="{b}{i["src"]}" width="{i["w"]}" height="{i["h"]}" alt="{E(alt)}"{a}{" class=%s"%cls if cls else ""}{extra}>'
def page(path,title,desc,body,active=None,cls=''):
    b='../' if '/' in path else ''
    nav=[('WERK',b+'werk.html','werk'),('OVER MIJ',b+'index.html#over-mij',''),('CONTACT','#contact','')]
    n=''.join(f'<a href="{h}"{" aria-current=page" if k and k==active else ""}>{t}</a>' for t,h,k in nav)
    canon=f'<link rel="canonical" href="{SITE_URL}/{path if path!="index.html" else ""}">' if SITE_URL else ''
    out=f'''<!doctype html>
<html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">{canon}
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:type" content="website"><meta name="theme-color" content="#fffff7">
<link rel="icon" href="{b}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap">
<script>document.documentElement.className="js"</script><link rel="stylesheet" href="{b}assets/css/style.css"></head>
<body class="{cls}"><a class="skip" href="#main">Naar de inhoud</a>
<header class="site-header"><div class="wrap"><a class="logo" href="{b}index.html" aria-label="Studio Dede – home"><img src="{b}assets/img/logo.gif" width="429" height="161" alt="dede."></a><nav class="nav" aria-label="Hoofdmenu">{n}</nav></div></header>
<main id="main">{body}</main>
<footer class="footer" id="contact"><div class="wrap"><div><p data-r>(Contact)</p><h2 class="h1" data-r="split">{split("Let’s talk!")}</h2></div><a class="mail" data-r href="mailto:{EMAIL}">{EMAIL}</a></div></footer>
<script src="{b}assets/js/main.js" defer></script></body></html>'''
    fp=os.path.join(ROOT,path); os.makedirs(os.path.dirname(fp),exist_ok=True); open(fp,'w',encoding='utf-8').write(out)
def split(t):
    o=[];i=0
    for k in t.replace('<br>',' <br> ').split():
        if k=='<br>': o.append('<br>')
        else: o.append(f'<span class="w"><span style="--i:{i}">{k}</span></span>'); i+=1
    return ' '.join(o)
def card(p,b,caption=False):
    t,m=p['card'] or (p['name'],'')
    cap=f'<h3 class="h4">{E(t)}</h3><p class="h5">{E(m)}</p>' if caption else ''
    lab='' if caption else f' aria-label="{E(p["name"])}"'
    return f'<a class="card" data-r href="{b}projects/{p["slug"]}.html"{lab}><span class="thumb">{img(b,p["thumb"],p["name"] if caption else "")}</span>{cap}</a>'
# Home
H=C['home']
home=f'''<div class="wrap page-top"><section class="hero"><h1 class="h2" data-r="split">{split(E(HERO))}</h1><video class="hero-img" data-r="img" data-d=".35" src="assets/video/showreel.mp4" poster="assets/img/home/hero-poster.webp" autoplay muted loop playsinline preload="auto" disablepictureinpicture disableremoteplayback tabindex="-1" aria-label="Showreel van Delphine – graphic designer"></video></section></div>
<section class="work" id="werk"><div class="wrap"><p class="h5" data-r>(My work)</p><div class="work-head"><h2 class="h1" data-r="split">{split("Some projects <br>I worked on")}</h2><a class="btn" data-r href="werk.html">Zie meer werk {ARROW}</a></div>
<div class="grid grid--home">{''.join(card(PR[s],'',True) for s in C['home_order'])}</div></div></section>
<section class="services wrap"><p class="h5" data-r>(Services)</p><div class="services-head"><h2 class="h1" data-r="split">{split("What I love <br>to do")}</h2><p class="p" data-r>Ideeën vertalen naar doordachte ontwerpen, <br>van eerste concept tot de kleinste details.</p></div>
<div class="cards">{''.join(f'<article class="svc" data-r>{img("",H["icons"][i],"")}<div><h3 class="h4">{E(t)}</h3><p class="p">{E(d)}</p></div></article>' for i,(t,d) in enumerate(SERVICES))}</div></section>
<section class="about wrap" id="over-mij">{img('',H['portrait'],'Portret van Delphine','',False,' data-r="img"')}<div class="about-text"><div><p class="h5" data-r>(About Me)</p><h2 class="h1" data-r="split">{split("Hi there, <br>nice to meet you!")}</h2></div><div class="p" data-r>{''.join(f'<p>{E(t)}</p>' for t in ABOUT)}</div></div></section>'''
page('index.html',f'{NAME} – Graphic designer',HERO,home,cls='home')
# Werk
grid=''.join(card(PR[s],'') for s in C['werk_order'])
page('werk.html',f'Werk – {NAME}','Overzicht van projecten van Delphine, graphic designer: branding, drukwerk en webdesign.',
 f'<div class="wrap page-top has-back"><a class="back" data-r href="index.html" data-back>{BACK}Terug</a><nav class="crumbs solo" data-r aria-label="Kruimelpad"><span>Werk</span></nav><div class="grid">{grid}</div></div>','werk')
# Projecten
for p in C['projects']:
    rows=[];im=p['images'];i=0
    while i<len(im):
        if im[i]['w']>=1500: rows.append((1,[im[i]]));i+=1
        else: rows.append((2,im[i:i+2]));i+=2
    n=[0]
    def g(x):
        n[0]+=1; return img('../',x,x.get('alt') or f'{p["name"]} – beeld {n[0]}','bd' if x.get('border') else '',False,' data-r="img"')
    gal=''.join(f'<div class="row{" full" if k==1 else ""}">{"".join(g(x) for x in r)}</div>' for k,r in rows)
    cl=f'<p class="small" data-r>{E(p["client"])}</p>' if p['client'] else ''
    body=f'''<div class="wrap page-top has-back"><a class="back" data-r href="../werk.html" data-back>{BACK}Terug</a><nav class="crumbs" data-r aria-label="Kruimelpad"><a href="../werk.html">Werk</a><b>{E(p['name'])}</b></nav>
<section class="p-hero"><div class="p-text"><h1 class="h1" data-r="split">{split(p['title'])}</h1><p class="intro" data-r>{E(p['intro'])}</p>{cl}</div>{img('../',p['hero'],p['name'],'',True,' data-r="img"')}</section>
<section class="gallery" aria-label="Beelden van {E(p['name'])}">{gal}</section></div>'''
    page(f'projects/{p["slug"]}.html',f'{p["name"]} – {NAME}',p['intro'][:157].rsplit(' ',1)[0]+'…',body,'werk')
print('Klaar:',2+len(C['projects']),'pagina’s')
