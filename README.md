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
git clone https://github.com/VDaSO/web-email-discoverer.git
cd web-email-discoverer
pip install -r requirements.txt
```

## Utilisation

```bash
python3 scraper.py
```

Entrez une URL complète (par exemple : https://exemple.com), et l'outil va découvrir les liens internes et extraire les emails de chaque page trouvée.

## Exemple de sortie 

```bash
Provide an URL (e.g., https://example.com):
> https://example.com

PAGE FOUND : https://example.com
----------- 12 UNIQUE URLS FOUND -----------

https://example.com/contact
https://example.com/about
...

Searching emails in discovered pages...

Emails found on https://example.com/contact:
   contact@example.com
   support@example.com
```
