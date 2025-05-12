#  Email & URL Scraper

Un script Python permettant de découvrir toutes les URLs internes d’un site web donné, puis de rechercher automatiquement les adresses e-mail présentes sur ces pages.

## Fonctionnalités

- Découverte des URLs internes d’un domaine (avec `BeautifulSoup`)
- Recherche automatique des e-mails (regex)
- Interface console colorée avec `colorama`
- Gestion des cookies et user-agent avec `requests`

## Dépendances

- beautifulsoup4  
- requests  
- colorama  

Tu peux les installer avec :

```bash
pip install -r requirements.txt
