# Wasabi Japanese Restaurant website

Plain static HTML and CSS. No JavaScript, no build step. Edit the files directly.

## Pages
`index.html`, `lunch-menu.html`, `dinner-menu.html`, `about.html`, `contact.html`. All styling is in `style.css`.

## Before going live
- Add prices to the two menu pages and remove the "Prices will be added here." line.
- Set the "Order Delivery" link: search for `href="#"` in `index.html` and `contact.html`.
- Replace the placeholder About text with the owner's story.
- Remove the `<meta name="robots" content="noindex, nofollow">` line from every page (it keeps search engines from listing the prototype).
- Photos were cut from screenshots of the old site; replace them with originals if available (same file names in `images/`).

## Publishing
GitHub Pages: Settings > Pages > Deploy from branch > `main` / `(root)`.
