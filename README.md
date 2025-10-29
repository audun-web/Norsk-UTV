# Akademiet VGS Oslo - Nettside

En enkel, men stilig nettside for Akademiet VGS Oslo, bygget med Python og Flask. Siden presenterer skolen, dens ansatte og gir grunnleggende informasjon gjennom et rent og moderne grensesnitt.

## Funksjoner

*   **Hjemmeside:** En innbydende forside med bakgrunnsbilde.
*   **Om Oss:** En side som beskriver skolen og linjen for Informasjonsteknologi og Medieproduksjon.
*   **Kontakt:** En dynamisk generert kontaktside med bilder og informasjon om ansatte, presentert i et pent CSS Grid-layout.
*   **Moderne Design:** Bruker CSS Flexbox og Grid for layout, med hover-effekter og en "loading"-animasjon ved sideinnlasting.

## Teknologier

*   **Backend:**
    *   Python 3
    *   Flask (for web-rammeverk og routing)
*   **Frontend:**
    *   HTML5
    *   CSS3 (Flexbox, Grid, Transitions)
    *   JavaScript (for "loading"-animasjon)
*   **Templating:**
    *   Jinja2 (integrert i Flask)

## Installasjon og Oppsett

Følg disse stegene for å kjøre prosjektet lokalt på din maskin.

### 1. Forutsetninger

Sørg for at du har [Python 3](https://www.python.org/downloads/) installert på systemet ditt.

### 2. Klon repositoriet

```bash
git clone <din-repository-url>
cd Norsk-UTV
```

### 3. Opprett et virtuelt miljø (anbefalt)

Det er god praksis å isolere prosjektets avhengigheter i et virtuelt miljø.

```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Installer avhengigheter

Prosjektet bruker kun Flask.

```bash
pip install Flask
```

### 5. Kjør applikasjonen

Start utviklingsserveren med følgende kommando:

```bash
python app.py
```

Åpne nettleseren din og gå til `http://127.0.0.1:5000` for å se nettsiden.

## Filstruktur

```
├── app.py              # Hovedfilen for Flask-applikasjonen
├── static/
│   ├── css/
│   │   └── style.css   # Stilark for hele siden
│   └── img/            # Bilder brukt på siden
├── templates/
│   ├── base.html       # Grunnmal med navigasjon og footer
│   ├── index.html      # Hjemmesiden
│   ├── kontakt.html    # Kontaktsiden
│   └── om_oss.html     # "Om oss"-siden
└── README.md           # Denne filen
```

---

Utviklet av Audun Midtgård Meckelborg.