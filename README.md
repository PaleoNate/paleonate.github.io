# Jud Lab website

A rebuild of the Wix site as plain HTML, ready to publish free on GitHub Pages.
No subscription, no storage limit that matters (GitHub Pages allows 1 GB, and
this site will be a small fraction of that once your photos are web-sized).

Everything here is ordinary HTML and CSS. You can edit any page in a text
editor — there is no build step and nothing to install to run the site.

---

## 1. Look at it first

Double-click `index.html` to open it in your browser. Everything works except
the photos, which are grey placeholders until you do step 2.

## 2. Add your photos

This is the step that fixes the storage problem, so it's worth understanding
why. Wix counted your **full-size camera originals** against the 500 MB limit —
several are over 3000 px wide — even though visitors only ever saw a version
Wix shrank to about 1000 px. Resizing the photos once, before uploading, is
what keeps the site small permanently.

**a. Get your originals out of Wix.** In your Wix dashboard, open the Media
Manager, select your photos, and download them. Put them somewhere easy to
find, like a `wix-originals` folder on your Desktop.

**b. Install Pillow** (a one-time thing, needed by the resizing script):

```
python3 -m pip install Pillow
```

**c. Resize them into the right folders:**

```
python3 tools/resize_images.py ~/Desktop/wix-originals/gallery  images/gallery
python3 tools/resize_images.py ~/Desktop/wix-originals/plants   images/plants
```

The script prints how much space each photo saved. It never modifies your
originals.

**d. Match the filenames.** The pages expect specific names:

| Folder | Expected filenames |
|---|---|
| `images/gallery/` | `lacinipetalum.jpg`, `notiantha.jpg`, `stephania.jpg`, `rourea.jpg`, `fairlingtonia.jpg`, `todea.jpg`, `mammea.jpg`, `parinari.jpg`, `ficus.jpg` |
| `images/plants/` | `plant-01.jpg` through `plant-24.jpg` |
| `images/people/` | `nathan-jud.jpg` |

Either rename your files to match, or edit the `src="..."` in the HTML to match
your filenames — whichever is less work. If you have fewer or more photos than
the placeholders, just delete or copy the `<figure>` blocks in `gallery.html`
and `plants.html`.

While you're there: the fossil and plant galleries had **no captions on Wix**.
Adding a line inside each `<figcaption>` would make those pages much more
useful, and it's good for search engines too.

## 3. Add your PDFs

Your publications page links to PDFs that are currently hosted on Wix
(`filesusr.com` URLs). **Those links will break the moment you stop paying for
Wix.** I have already pointed them at a local `pdfs/` folder instead, so:

1. Download each PDF from Wix.
2. Drop them in `pdfs/` using the exact names listed in `publications.html`
   (for example `pdfs/jud-2015-herbaceous-eudicots.pdf`).

If you'd rather not host PDFs at all, delete the `· <a href="pdfs/...">PDF</a>`
bits — every paper already links to its DOI, which never breaks.

## 4. Publish it on GitHub Pages

You already have a GitHub account (`PaleoNate`), so this is quick and free.

1. Go to <https://github.com/new> and create a repository named
   **`paleonate.github.io`** (this exact name matters — it makes the site live
   at that address). Set it to **Public**.
2. On the new repository page, click **uploading an existing file**.
3. Drag in *everything* from this folder — all the `.html` files, `style.css`,
   and the `images`, `pdfs`, and `tools` folders.
4. Click **Commit changes**.
5. Go to **Settings → Pages**. Under "Branch", choose `main` and `/ (root)`,
   then **Save**.

Wait a minute or two, then visit **https://paleonate.github.io**. That's it.

To update anything later, edit the file and upload it again the same way — or,
if you prefer the command line, clone the repo and use `git push`.

### Using your own domain (optional)

If you ever buy a domain like `judlab.org`, add a file named `CNAME` containing
just that domain, then point the domain's DNS at GitHub. Settings → Pages walks
you through it. This is the only part that ever costs money (~$12/year for the
domain), and it's optional.

## 5. Before you cancel Wix

Make sure you've saved everything, since the site disappears when you cancel:

- [ ] All photos downloaded from the Media Manager
- [ ] All publication PDFs downloaded
- [ ] Full text of the 13 blog posts copied out (see below)
- [ ] Any contact form submissions you want to keep
- [ ] Check whether anything links to `nathanajud.wixsite.com` — your papers,
      your email signature, your department's faculty page, Google Scholar

## 6. The blog posts

`blog.html` currently lists all 13 posts with their titles, dates, and opening
lines, but not the full text — those weren't reachable from the public pages in
a form I could pull automatically.

Two options:

1. **Copy them across yourself.** Open each post on Wix, copy the text, and
   paste it into `blog.html` in place of the excerpt.
2. **Ask me.** If you paste the post text into a chat, I'll format all 13 into
   proper individual post pages with their photos.

Once the posts are in, delete the yellow note box at the top of `blog.html`.

## 7. What changed from the Wix site

- **Publications** now uses this morning's corrected list: grouped by year, your
  name in bold, DOI links on every title, and the two papers that were published
  under new titles (*The Bryologist* 129(3) and *Review of Palaeobotany and
  Palynology* 355) updated accordingly.
- **The template placeholder page** ("BSA Paleobotany Sec. Library", which still
  had "This is a Paragraph. Click on Edit Text..." on it) is gone. If you want it
  back as a real page, say so and I'll add it.
- **The footer** no longer says "© 2023 by Actor & Model" — that was leftover
  Wix template text.
- **The contact form** is now a plain email link. GitHub Pages can't run a form.
  If you want a working form, [Formspree](https://formspree.io) has a free tier
  and drops into the HTML in about five lines.
- **The WJC Rocks & Fossils gallery** has been removed; `gallery.html` now shows the
  research specimens only.
- **Teaching** no longer says Paleobotany is "starting 2023".
- The site is responsive (works properly on phones) and follows dark mode.

## Files

```
index.html          Home
research.html       Research topics, current and previous
publications.html   Full publication list
people.html         You, current students, alumni
teaching.html       Courses, mentorship, outreach
gallery.html        Research specimens
plants.html         Living plant photos
blog.html           Post list (full text still to add)
contact.html        Address, email, prospective students
style.css           All the styling — colors and fonts live at the top
images/             Photos (placeholders until you add yours)
pdfs/               Publication PDFs (empty until you add yours)
tools/resize_images.py   Shrinks photos for the web
tools/build.py      Regenerates the pages' shared nav/footer (optional)
```
