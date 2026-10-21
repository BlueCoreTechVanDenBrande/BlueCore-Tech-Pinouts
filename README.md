# BlueCore Tech Pinouts

A searchable directory of pinout resources for Arduino builders, curated by Danny van den Brande — BlueCore Tech.

**Website:** https://bluecoretechvandenbrande.github.io/BlueCore-Tech-Pinouts/

85 part/board collections, 99 links to original diagrams, eight categories, and official Arduino PDF links for UNO R3, Mega 2560 and classic Nano.

## Use

Search by part number, select a category, or save favourites in your browser. Diagram links open the original publisher's image. Source-guide links provide the accompanying documentation. Match your exact hardware revision and orientation.

## Hosting

Static HTML/CSS/JavaScript: no framework, build service, analytics or account system. Enable GitHub Pages from `main`, `/ (root)`. Open `index.html` locally or serve this folder to preview.

## Credits and images

References link to **Last Minute Engineers**, **Components101**, and **Arduino**. This repository does not contain their diagram image files or PDFs and does not claim rights to those materials. Publisher ownership, terms and licences continue to apply. The original local offline collection is separate and is not uploaded.

## Add a part

Edit `catalog.json`, then regenerate `catalog.js` as `const catalog = ` followed by the JSON and a semicolon. Each entry contains `name`, `category`, `group`, `source`, `publisher` and `diagrams` (each with `label`, HTTPS `url` and `kind`). Optional `official` is an official PDF URL. Use one of the existing eight categories. Link to original documentation; do not upload third-party diagrams without permission or an appropriate licence.

`build_catalog.py` is an optional maintainer tool for rebuilding from the separate local `../!PINOUTS/manifest.json`; it is not needed to run or deploy the website.

Favourites are stored only in browser localStorage. External source links navigate to third-party websites. No external images, fonts, or scripts are loaded automatically.
