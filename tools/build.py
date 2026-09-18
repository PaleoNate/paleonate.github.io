#!/usr/bin/env python3
"""Generates the plain HTML pages for the Jud Lab site.

You do not need this script to run the site — it just writes the .html files,
which are ordinary hand-editable HTML. Re-run it only if you want to change
something shared across every page (the nav bar, the footer).

    python3 tools/build.py
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = [
    ("index.html", "Home"),
    ("research.html", "Research"),
    ("publications.html", "Publications"),
    ("people.html", "People"),
    ("teaching.html", "Teaching"),
    ("gallery.html", "Gallery"),
    ("plants.html", "Plant photos"),
    ("blog.html", "Blog"),
    ("contact.html", "Contact"),
]


def shell(filename, title, body, description=""):
    nav = "\n".join(
        '      <a href="{h}"{cur}>{t}</a>'.format(
            h=h, t=t, cur=' aria-current="page"' if h == filename else ""
        )
        for h, t in NAV
    )
    desc = description or "Plant Biology Lab at William Jewell College — the lab of Dr. Nathan A. Jud, studying living and fossil plants."
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Jud Lab</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="style.css">
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html">Jud Lab <span>· William Jewell</span></a>
    <nav>
{nav}
    </nav>
  </div>
</header>

{body}

<footer class="site-footer">
  <div class="footer-inner">
    <div>Dr. Nathan A. Jud · Department of Biology · William Jewell College</div>
    <div class="footer-links">
      <a href="https://github.com/PaleoNate">GitHub</a>
      <a href="https://twitter.com/PaleoNate">Twitter</a>
      <a href="https://www.instagram.com/paleonate/">Instagram</a>
    </div>
  </div>
</footer>

</body>
</html>
"""


def figure(src, caption, note=""):
    """A gallery figure. Falls back to a labelled placeholder box."""
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return f"""    <figure>
      <img src="{src}" alt="{re.sub('<[^>]+>', '', caption) or 'Specimen photograph'}" loading="lazy">
      {cap}
    </figure>"""


# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------

home = """<div class="hero">
  <div class="hero-inner">
    <h1>Plant Biology Lab at William Jewell</h1>
    <p class="sub">Dr. Nathan A. Jud · Department of Biology · William Jewell College</p>
  </div>
</div>

<main>

<section>
  <h2>Welcome</h2>
  <p>We study living and fossil plants to understand the history of plant evolution and
  ecology. Our focus is paleobotany, because the fossil record is a rich source of data on
  the morphology, anatomy, distribution, and associations of extinct plants. These data can
  be used to test a variety of hypotheses in ecology and evolution.</p>

  <p>My primary interest is understanding how diversification and extinction change plant
  communities in deep time. I study the evolution of plant form and diversity through
  specimen-based work in plant systematics, and patterns of community structure and
  environmental change through field-based paleobotanical studies of plant diversity and
  distribution.</p>

  <p>Research projects are available for undergraduate students on a range of topics in
  organismal botany, paleontology, and (paleo)ecology. If you are a William Jewell student
  interested in joining the lab, please <a href="contact.html">get in touch</a>.</p>
</section>

<section>
  <h2>Explore</h2>
  <div class="cards">
    <div class="card">
      <h3><a href="research.html">Research</a></h3>
      <p>Cretaceous flowering plants, fossil woods and ancient forests, Patagonia, Panama.</p>
    </div>
    <div class="card">
      <h3><a href="publications.html">Publications</a></h3>
      <p>Peer-reviewed papers, with links to the published articles and PDFs.</p>
    </div>
    <div class="card">
      <h3><a href="people.html">People</a></h3>
      <p>Current students, lab alumni, and their research projects.</p>
    </div>
    <div class="card">
      <h3><a href="teaching.html">Teaching</a></h3>
      <p>Courses, undergraduate mentorship, and public science education.</p>
    </div>
  </div>
</section>

<section>
  <h2>Recent work</h2>
  <p class="pub"><span class="me">N.A. Jud</span>, G.C. Nunes, P. Wilf, and M.A. Gandolfo. 2026.
  <a href="https://doi.org/10.1639/0007-2745-129.3.206">Early Eocene leafy liverworts from West Gondwana</a>.
  <i>The Bryologist</i> 129(3): 206&ndash;219.</p>

  <p class="pub"><span class="me">N.A. Jud</span>, S.G. Lucas, and W.A. DiMichele. 2026.
  <a href="https://doi.org/10.1016/j.revpalbo.2026.105709">Late Desmoinesian plants from the Valley Ranch
  section, upper Alamitos Formation, New Mexico: New insights into tropical western Pangean
  vegetation</a>. <i>Review of Palaeobotany and Palynology</i> 355: 105709.</p>

  <p class="pub">E.A. Wilson*, C. Burch*, M. Schorr, and <span class="me">N.A. Jud</span>. 2025.
  <a href="https://doi.org/10.1086/734306">Revision of <i>Neuralethopteris lindahlii</i> White, an unusual
  medullosan foliage fossil from the Upper Pennsylvanian in Missouri</a>.
  <i>International Journal of Plant Sciences</i> 186(3): 167&ndash;177.</p>

  <p><a href="publications.html">All publications &rarr;</a></p>
</section>

<section>
  <h2>From the collection</h2>
  <div class="gallery">
""" + "\n".join([
    figure("images/gallery/lacinipetalum.jpg", "<em>Lacinipetalum spectabilum</em>"),
    figure("images/gallery/notiantha.jpg", "<em>Notiantha grandensis</em> Jud et al. 2017"),
    figure("images/gallery/stephania.jpg", "<em>Stephania psittaca</em> (Menispermaceae) fruit from the early Paleocene of Patagonia"),
    figure("images/gallery/rourea.jpg", "<em>Rourea blatta</em> Jud and Nelson 2017"),
    figure("images/gallery/fairlingtonia.jpg", "<em>Fairlingtonia thyrsopteroides</em> roots, showing the adventitious roots and slender young stem (Jud 2015)"),
    figure("images/gallery/todea.jpg", "Transverse section of <em>Todea tidwellii</em> showing the dark sclerenchymatous pith (Jud et al. 2008)"),
    figure("images/gallery/mammea.jpg", "<em>Mammea paramericana</em> Nelson and Jud 2017"),
    figure("images/gallery/parinari.jpg", "Transverse section of a <em>Parinari</em> endocarp from the lower Miocene of Panama. Scale bar = 1 cm (Jud et al. 2016)"),
    figure("images/gallery/ficus.jpg", "Fossil <em>Ficus</em> wood from the Cenozoic of Panama (Jud and Dunham)"),
]) + """
  </div>
  <p style="margin-top:18px"><a href="gallery.html">More specimens &rarr;</a></p>
</section>

</main>
"""

# --------------------------------------------------------------------------
# Research
# --------------------------------------------------------------------------

research = """<main>

<h1 class="page-title">Research</h1>
<p class="page-intro">How diversification and extinction reshape plant communities in deep time,
studied through specimen-based systematics and field-based paleobotany.</p>

<section>
  <h2>Current topics</h2>

  <h3>Cretaceous flowering plants</h3>
  <p>The diversification of flowering plants during the Cretaceous was among the most important
  transitions in the history of life on earth. We examine how these plants were integrated into
  existing ecosystems and how they influenced other species. Fossils from the Cloverly Formation
  of Wyoming document the arrival of flowering plants in North America.</p>

  <h3>Fossil woods and ancient forests</h3>
  <p>Petrified wood is a substantial but underused source of data about prehistoric forests.
  Investigations of specimens from Hornby Island and elsewhere illuminate when angiosperms became
  canopy dominants, and reveal the composition of Cretaceous forests.</p>

  <h3>The Paleocene flora of Patagonia</h3>
  <p>Fossil flowers, leaves, fruit, and wood are preserved in the Paleocene rocks of Patagonia,
  Argentina, just above the Cretaceous&ndash;Paleogene boundary. This collaborative work explores
  recovery after the end-Cretaceous extinction and the biogeography of Gondwana.</p>

  <h3>The Miocene flora of Panama</h3>
  <p>The expansion of the Panama Canal exposed Miocene rocks containing abundant botanical remains.
  This research has identified multiple extinct species within genera that are still present today,
  including forest trees and climbing plants.</p>
</section>

<section>
  <h2>Previous work</h2>

  <h3>Community ecology through time</h3>
  <p>The ETE working group analyzed species associations across time scales, finding that fossil
  datasets show aggregations whereas recent data show segregations &mdash; a shift that coincides
  with the expansion of human populations.</p>

  <h3>Early Miocene monkeys</h3>
  <p>Fieldwork in Panama recovered fossilized primate teeth, leading to the description of
  <i>Panamacebus transitus</i>. Vegetation gradients appear to have restricted the northern
  distribution of monkeys despite otherwise suitable climate conditions.</p>

  <h3>Early eudicots</h3>
  <p>This work documented <i>Fairlingtonia thyrsopteroides</i>, widespread across eastern North
  America roughly 115 million years ago, and representative of early flowering plant diversity.</p>

  <h3><i>Potomacapnos apeleutheron</i></h3>
  <p>This species from Virginia shows the complex leaf architecture characteristic of eudicots. It
  was named in commemoration of the Civil War-era canal workers whose labor exposed the fossil site.</p>

  <h3>Late Pennsylvanian flora of Missouri</h3>
  <p>Specimens collected near William Jewell College document vegetation at a time when Missouri sat
  near the equator, revealing relationships between climate and vegetation during this period.</p>
</section>

</main>
"""

# --------------------------------------------------------------------------
# People
# --------------------------------------------------------------------------

people = """<main>

<h1 class="page-title">People</h1>

<div class="person-lead">
  <img src="images/people/nathan-jud.jpg" alt="Dr. Nathan A. Jud">
  <div>
    <h2 style="border:none;margin-top:0">Dr. Nathan A. Jud</h2>
    <p>Associate Professor, Department of Biology, William Jewell College. I study living and fossil
    plants, with a focus on the systematics of Cretaceous and Cenozoic angiosperms, fossil woods, and
    the assembly of ancient plant communities.</p>
    <p><a href="https://github.com/PaleoNate">GitHub</a> ·
       <a href="https://twitter.com/PaleoNate">Twitter</a> ·
       <a href="https://www.instagram.com/paleonate/">Instagram</a> ·
       <a href="contact.html">Contact</a></p>
  </div>
</div>

<section>
  <h2>Current students</h2>
  <ul class="people">
    <li><strong>Elizabeth Wilson</strong><br><span>Taxonomy of <i>Neuropteris lindahli</i> White from the Upper Pennsylvanian of Missouri</span></li>
    <li><strong>Paige Liston</strong><br><span>Evolution of seed size in <i>Serjania</i> (Paullinieae, Sapindaceae)</span></li>
    <li><strong>Jonas May</strong><br><span>Palynology of a Late Pennsylvanian flora from Liberty, Missouri</span></li>
    <li><strong>Michaela Massey</strong><br><span>Fossil woods from the Upper Cretaceous of western North America</span></li>
  </ul>
</section>

<section>
  <h2>Lab alumni</h2>
  <ul class="people">
    <li><strong>Ben Zahnd</strong><br><span>Fossil woods from the Upper Cretaceous of western North America</span></li>
    <li><strong>Claire Burch</strong><br><span>A preliminary morphotype catalog of a Late Pennsylvanian flora from Liberty, Missouri</span></li>
    <li><strong>Kiara Bradley</strong><br><span>Fossil woods from the Upper Cretaceous of western North America</span></li>
    <li><strong>Shane Cavallo</strong><br><span>Preparation of fossil cuticles from Late Pennsylvanian plant fossils</span></li>
    <li><strong>Kelly Hendershot</strong><br><span>Polyploidy in <i>Solidago nemoralis</i></span></li>
    <li><strong>Hayley Knapp</strong><br><span>A guide to the fossil invertebrates of the Martha Lafite Thompson Nature Sanctuary</span></li>
  </ul>
</section>

</main>
"""

# --------------------------------------------------------------------------
# Teaching
# --------------------------------------------------------------------------

teaching = """<main>

<h1 class="page-title">Teaching</h1>
<p class="page-intro">Courses at William Jewell College, undergraduate research mentorship, and
public science education.</p>

<section>
  <h2>Courses</h2>

  <h3>Introductory</h3>
  <ul>
    <li>Ecology and Evolution &mdash; lecture &amp; lab</li>
    <li>Biological Diversity &mdash; lecture &amp; lab</li>
  </ul>

  <h3>Upper level</h3>
  <ul>
    <li>Ecology &mdash; lecture &amp; lab</li>
    <li>Plant Biology &mdash; lecture &amp; lab</li>
    <li>Paleobotany &mdash; lecture &amp; lab</li>
  </ul>

  <h3>Non-majors (Core)</h3>
  <ul>
    <li>Life on Earth</li>
    <li>Ethnobotany</li>
  </ul>
</section>

<section>
  <h2>Undergraduate and post-baccalaureate mentorship</h2>
  <p>Students in the lab carry out specimen-based research projects of their own, from collection
  and preparation through analysis and publication. Several have gone on to co-author peer-reviewed
  papers &mdash; see the <a href="people.html">People</a> and
  <a href="publications.html">Publications</a> pages, where student co-authors are marked with an
  asterisk.</p>
</section>

<section>
  <h2>Museums and public science</h2>
  <p>I serve as museum internship coordinator, and previously worked with the Panama Canal Project
  Museum Internships Program during a 2014&ndash;16 appointment at the Florida Museum of Natural
  History. I am committed to science education for all, through museum events, exhibits, and public
  engagement.</p>
</section>

</main>
"""

# --------------------------------------------------------------------------
# Publications
# --------------------------------------------------------------------------

publications = """<main>

<h1 class="page-title">Publications</h1>
<p class="page-intro">* denotes a student mentee. Linked titles go to the published article.</p>

<div class="pubs">

<h2>Accepted</h2>

<p class="pub"><span class="me">N.A. Jud</span>, B. Zahnd*, C. Che-Castaldo, J.A. Rosell, and M. Olson.
A Bayesian phylogenetic mixed model for predicting plant habit from fossil woods.
<i>New Phytologist</i>, accepted.</p>

<h2>2026</h2>

<p class="pub"><span class="me">N.A. Jud</span>, G.C. Nunes, P. Wilf, and M.A. Gandolfo.
<a href="https://doi.org/10.1639/0007-2745-129.3.206">Early Eocene leafy liverworts from West Gondwana</a>.
<i>The Bryologist</i> 129(3): 206&ndash;219.</p>

<p class="pub"><span class="me">N.A. Jud</span>, S.G. Lucas, and W.A. DiMichele.
<a href="https://doi.org/10.1016/j.revpalbo.2026.105709">Late Desmoinesian plants from the Valley Ranch
section, upper Alamitos Formation, New Mexico: New insights into tropical western Pangean
vegetation</a>. <i>Review of Palaeobotany and Palynology</i> 355: 105709.</p>

<p class="pub">D.L. Bridges, S.G. Lucas, and <span class="me">N.A. Jud</span>. Conodonts from a portion of
the Valley Ranch section, Sangre de Cristo Mountains, north-central New Mexico, U.S.A.
<i>Missouri Geological Survey, Report of Investigations</i> 78. 63 p.</p>

<p class="pub">J.R. Foster, C.T. Gee, <span class="me">N.A. Jud</span>, S.D. Sroka, B. Engh, S. Sternberg,
and F.V. Hoff. Seeing the forest and the trees: A preliminary look at the implications of giant trees
in the Morrison Formation for Late Jurassic climate in western North America.
<i>New Mexico Museum of Natural History and Science Bulletin</i> 102: 125&ndash;144.</p>

<h2>2025</h2>

<p class="pub">E.A. Wilson*, C. Burch*, M. Schorr, and <span class="me">N.A. Jud</span>.
<a href="https://doi.org/10.1086/734306">Revision of <i>Neuralethopteris lindahlii</i> White, an unusual
medullosan foliage fossil from the Upper Pennsylvanian in Missouri</a>.
<i>International Journal of Plant Sciences</i> 186(3): 167&ndash;177.</p>

<p class="pub">R.R. Pujana, <span class="me">N.A. Jud</span>, P. Wilf, and M.A. Gandolfo.
<a href="https://doi.org/10.1080/03115518.2024.2426030">Lauraceous fossil woods from the early Eocene of
Laguna del Hunco, Argentine Patagonia</a>. <i>Alcheringa</i> 49(1): 85&ndash;98.</p>

<h2>2024</h2>

<p class="pub"><span class="me">N.A. Jud</span>, K.E. Bradley*, B. Zahnd*, G.W. Rothwell, and R.A. Stockey.
<a href="https://doi.org/10.1163/22941932-bja10168">Anatomy of a fossil liana from the Upper Cretaceous of
British Columbia, Canada</a>. <i>IAWA Journal</i>.</p>

<h2>2023</h2>

<p class="pub">C.L. Poore*, <span class="me">N.A. Jud</span>, and M.A. Gandolfo.
<a href="https://doi.org/10.1016/j.revpalbo.2023.104940">Fossil fruits from the early Paleocene of
Patagonia, Argentina reveal a west Gondwanan history of Icacinaceae</a>.
<i>Review of Palaeobotany and Palynology</i> 317: 104940.
<span class="extra">· <a href="https://drive.google.com/file/d/1bdut_LGXy3Bzm27tudytNBXvlZnVVkBW/view?usp=sharing">PDF</a>
· <a href="https://github.com/PaleoNate/Patagonian_Icacinaceae">Supplement (GitHub)</a></span></p>

<p class="pub">E.M. Pessoa, A.C. Ribeiro, M.J.M. Christenhusz, A.I. Coan, and <span class="me">N.A. Jud</span>.
<a href="https://doi.org/10.1002/ajb2.16163">Is <i>Santaniella</i> a ranunculid? Reassessment of this
enigmatic fossil angiosperm from the Lower Cretaceous (Aptian, Crato Konservat-Lagerst&auml;tte, Brazil)
provides a new interpretation</a>. <i>American Journal of Botany</i> 110(5): e16163.</p>

<h2>2021</h2>

<p class="pub">E.M. Pessoa, A. Ribeiro, and <span class="me">N.A. Jud</span>.
<a href="https://doi.org/10.1002/ajb2.1751">A eudicot leaf from the Lower Cretaceous (Aptian, Araripe
Basin) Crato Konservat-Lagerst&auml;tte</a>. <i>American Journal of Botany</i> 108(10): 2055&ndash;2065.
<span class="extra">· <a href="pdfs/pessoa-2021-eudicot-leaf.pdf">PDF</a></span></p>

<p class="pub"><span class="me">N.A. Jud</span>, S.E. Allen, C.W. Nelson*, C.L. Bastos, and J.G. Chery.
<a href="https://doi.org/10.1371/journal.pone.0248369">Climbing since the early Miocene: the fossil record
of Paullinieae (Sapindaceae)</a>. <i>PLOS ONE</i> 16(4): e0248369.
<span class="extra">· <a href="pdfs/jud-2021-paullinieae.pdf">PDF</a></span></p>

<h2>2020</h2>

<p class="pub"><span class="me">N.A. Jud</span> and M.A. Gandolfo.
<a href="https://doi.org/10.1093/aob/mcaa154">Fossil evidence from South America for the diversification of
Cunoniaceae by the earliest Palaeocene</a>. <i>Annals of Botany</i> 127(3): 305&ndash;315.
<span class="extra">· <a href="https://academic.oup.com/aob/article/127/3/305/5898989?guestAccessKey=bc6b25ed-39a6-4416-a010-f3ca59a07101">Free access</a></span></p>

<h2>2019</h2>

<p class="pub">E.J. Hermsen, <span class="me">N.A. Jud</span>, F. De Benedetti, and M.A. Gandolfo.
<a href="https://doi.org/10.1086/704377"><i>Azolla</i> sporophytes and spores from the Upper Cretaceous and
Paleocene of Patagonia, Argentina</a>. <i>International Journal of Plant Sciences</i> 180(7): 737&ndash;754.</p>

<p class="pub">M.D. D'Emic, B.Z. Foreman, <span class="me">N.A. Jud</span>, B.B. Britt, M. Schmitz, and
J.L. Crowley. <a href="https://doi.org/10.3374/014.060.0101">Chronostratigraphic revision of the Cloverly
Formation (Lower Cretaceous, Western Interior, USA)</a>.
<i>Bulletin of the Peabody Museum of Natural History</i> 60(1): 3&ndash;40.
<span class="extra">· <a href="pdfs/demic-2019-cloverly.pdf">PDF</a></span></p>

<p class="pub">B.A. Thomas, <span class="me">N.A. Jud</span>, and L. Seyfullah.
<a href="https://doi.org/10.1016/j.geobios.2019.07.002">A comparison of Asturian lepidodendroid lycophytes
from the USA and the Euramerian Variscan Front</a>. <i>Geobios</i>.</p>

<p class="pub"><span class="me">N.A. Jud</span>. <a href="https://doi.org/10.1016/j.cub.2018.11.036">A vision
for historical biogeography</a>. Review of <i>Land Bridges: Ancient Environments, Plant Migrations, and New
World Connections</i> by Alan Graham. <i>Current Biology</i> 29(1).</p>

<p class="pub">S.L. Wing and <span class="me">N.A. Jud</span>. Commentary on Hickey and Doyle (1977), Early
Cretaceous fossil evidence for angiosperm evolution. <i>In</i> S.K. Lyons, A.K. Behrensmeyer, and
P.J. Wagner (eds.), <i>Foundations of Paleoecology</i>, p. 151. University of Chicago Press.</p>

<h2>2018</h2>

<p class="pub"><span class="me">N.A. Jud</span>, M.D. D'Emic, S.A. Williams, J.C. Mathews, K.M. Tremaine,
S.C. Bennett, and J. Bhattacharya. <a href="https://doi.org/10.1126/sciadv.aar8568">A new fossil assemblage
shows that large angiosperm trees grew in North America by the Turonian (Late Cretaceous)</a>.
<i>Science Advances</i> 4(9): eaar8568.</p>

<p class="pub"><span class="me">N.A. Jud</span>, M.A. Gandolfo, A. Iglesias, and P. Wilf.
<a href="https://doi.org/10.1002/ajb2.1092">Fossil moonseeds from the Paleogene of West Gondwana (Patagonia,
Argentina)</a>. <i>American Journal of Botany</i> 105(5): 927&ndash;942.</p>

<p class="pub"><span class="me">N.A. Jud</span>, M.A. Gandolfo, A. Iglesias, and P. Wilf.
<a href="https://doi.org/10.1093/aob/mcx173">Fossil flowers from the early Palaeocene of Patagonia,
Argentina, with affinity to Schizomerieae (Cunoniaceae)</a>. <i>Annals of Botany</i> 121(3): 431&ndash;442.</p>

<p class="pub">T.J. DeVries and <span class="me">N.A. Jud</span>.
<a href="https://www.sgp.org.pe/wp-content/uploads/8-DeVries-Chilcatay.pdf">Lithofacies patterns and
paleogeography of the Miocene Chilcatay and lower Pisco depositional sequences (East Pisco Basin, Peru)</a>.
<i>Bolet&iacute;n de la Sociedad Geol&oacute;gica del Per&uacute;</i>, Volumen Jubilar 8: 124&ndash;167.</p>

<h2>2017</h2>

<p class="pub">O. Rodriguez-Reyes, P. Gasson, C. Thornton*, H.J. Falcon-Lang, and <span class="me">N.A. Jud</span>.
<a href="https://doi.org/10.1163/22941932-20170178"><i>Panascleroticoxylon crystallosa</i> gen. et sp. nov.:
a new Miocene malpighialean tree from Panama</a>. <i>IAWA Journal</i> 38(4): 437&ndash;455.
<span class="extra">· <a href="pdfs/rodriguez-reyes-2017-panascleroticoxylon.pdf">PDF</a>
· <a href="pdfs/rodriguez-reyes-2017-taxonomic-note.pdf">Taxonomic note</a></span></p>

<p class="pub"><span class="me">N.A. Jud</span> and J.I. Dunham*.
<a href="https://doi.org/10.1163/22941932-20170176">Fossil woods from the Cenozoic of Panama (Azuero
Peninsula) reveal an ancient neotropical rainforest</a>. <i>IAWA Journal</i> 38(3): 366&ndash;S2.
<span class="extra">· <a href="pdfs/jud-2017-azuero-woods.pdf">PDF</a>
· <a href="pdfs/jud-2017-azuero-corrected-table2.pdf">Corrected Table 2</a></span></p>

<p class="pub"><span class="me">N.A. Jud</span> and C.W. Nelson*.
<a href="https://doi.org/10.3732/ajb.1700080">A liana from the lower Miocene of Panama and the fossil record
of Connaraceae</a>. <i>American Journal of Botany</i> 104(5).</p>

<p class="pub"><span class="me">N.A. Jud</span>, M.A. Gandolfo, A. Iglesias, and P. Wilf.
<a href="https://doi.org/10.1371/journal.pone.0176164">Flowering after disaster: Early Danian buckthorn
(Rhamnaceae) flowers and leaves from Patagonia</a>. <i>PLOS ONE</i> 12(5): e0176164.</p>

<p class="pub"><span class="me">N.A. Jud</span>, E.A. Wheeler, G.W. Rothwell, and R.A. Stockey.
<a href="https://doi.org/10.1163/22941932-20170164">Angiosperm wood from the Upper Cretaceous (Coniacian) of
Vancouver Island, BC, Canada</a>. <i>IAWA Journal</i> 38(2): 141&ndash;161.
<span class="extra">· <a href="pdfs/jud-2017-vancouver-island-wood.pdf">PDF</a></span></p>

<p class="pub">T.J. DeVries, M. Urbina, and <span class="me">N.A. Jud</span>.
<a href="https://app.ingemmet.gob.pe/biblioteca/pdf/BSGP-112-14.pdf">The Eocene-Oligocene Otuma depositional
sequence (East Pisco Basin, Peru): Paleogeographic and paleoceanographic implications of new data</a>.
<i>Bolet&iacute;n de la Sociedad Geol&oacute;gica del Per&uacute;</i> 112: 14&ndash;38.</p>

<p class="pub">C.W. Nelson* and <span class="me">N.A. Jud</span>.
<a href="https://doi.org/10.1086/689618">Biogeographic implications of <i>Mammea paramericana</i> sp. nov.
from the lower Miocene of Panama and the evolution of the Calophyllaceae</a>.
<i>International Journal of Plant Sciences</i> 178(3): 241&ndash;257.
<span class="extra">· <a href="pdfs/nelson-2017-mammea.pdf">PDF</a></span></p>

<p class="pub">B.J. MacFadden, D.S. Jones, <span class="me">N.A. Jud</span>, J.W. Moreno-Bernal, G.S. Morgan,
R.W. Portell, V.J. Perez, S.M. Moran, and A.R. Wood.
<a href="https://doi.org/10.1371/journal.pone.0170300">Integrated chronology, flora and faunas, and
paleoecology of the Alajuela Formation, late Miocene of Panama</a>. <i>PLOS ONE</i> 12(1): e0170300.</p>

<h2>2016</h2>

<p class="pub">M.D. D'Emic, B.Z. Foreman, and <span class="me">N.A. Jud</span>.
<a href="https://doi.org/10.1017/jpa.2015.67">Anatomy, systematics, paleoenvironment, and age of the sauropod
dinosaur <i>Sonorasaurus thompsoni</i> from the Cretaceous of Arizona, USA</a>.
<i>Journal of Paleontology</i> 90(1): 102&ndash;132.</p>

<p class="pub">S.K. Lyons et al. (28 authors, including <span class="me">N.A. Jud</span>).
<a href="http://www.nature.com/nature/journal/v537/n7618/full/nature19111.html">Lyons et al. reply</a>.
<i>Nature</i> 537: E5&ndash;E6.</p>

<p class="pub">J.I. Bloch, E.D. Woodruff, A.R. Wood, A.F. Rincon, A.R. Harrington, G.S. Morgan, D.A. Foster,
C. Montes, C.A. Jaramillo, <span class="me">N.A. Jud</span>, D.S. Jones, and B.J. MacFadden.
<a href="https://doi.org/10.1038/nature17415">The first Central American fossil primate and early Miocene
tropical biotic interchange</a>. <i>Nature</i> 533: 243&ndash;246.</p>

<p class="pub"><span class="me">N.A. Jud</span> and J. Sohn.
<a href="https://doi.org/10.1016/j.cretres.2016.02.019">Fossil evidence for an ancient association between
agromyzid flies and herbaceous eudicot angiosperms</a>. <i>Cretaceous Research</i> 63: 113&ndash;121.
<span class="extra">· <a href="pdfs/jud-2016-agromyzid.pdf">PDF</a>
· <a href="pdfs/jud-2016-agromyzid-taxonomic-note.pdf">Taxonomic note</a></span></p>

<p class="pub"><span class="me">N.A. Jud</span>, C.W. Nelson*, and F.H. Herrera.
<a href="https://doi.org/10.3732/ajb.1500425">New <i>Parinari</i> fossils from the early Miocene of Panama
and the fossil record of Chrysobalanaceae</a>. <i>American Journal of Botany</i> 103(2): 277&ndash;289.
<span class="extra">· <a href="pdfs/jud-2016-parinari.pdf">PDF</a></span></p>

<h2>2015</h2>

<p class="pub">S.K. Lyons et al. (30 authors, including <span class="me">N.A. Jud</span>).
<a href="https://doi.org/10.1038/nature16447">Holocene shifts in the assembly of plant and animal communities
implicate human impacts</a>. <i>Nature</i> 529: 80&ndash;83.
<span class="extra">· <a href="http://www.nature.com/nature/journal/v538/n7626/full/nature19104.html">Corrigendum</a></span></p>

<p class="pub"><span class="me">N.A. Jud</span>.
<a href="https://doi.org/10.1098/rspb.2015.1045">Fossil evidence for an herbaceous diversification of early
eudicot angiosperms during the Early Cretaceous</a>. <i>Proceedings of the Royal Society B</i> 282(1814):
20151045. <span class="extra">· <a href="pdfs/jud-2015-herbaceous-eudicots.pdf">PDF</a></span></p>

<h2>2014</h2>

<p class="pub"><span class="me">N.A. Jud</span>.
<a href="https://doi.org/10.3374/014.055.0204">Morphotype catalog of a Zone I (Aptian&ndash;earliest Albian)
flora from Fairlington, Virginia, USA</a>. <i>Bulletin of the Peabody Museum of Natural History</i> 55(2):
135&ndash;152. <span class="extra">· <a href="pdfs/jud-2014-fairlington-morphotypes.pdf">PDF</a></span></p>

<p class="pub">J.L. Blois et al. (23 authors, including <span class="me">N.A. Jud</span>).
<a href="https://doi.org/10.1111/ecog.00779">A framework for evaluating the influence of climate, dispersal
limitation, and biotic interactions using fossil pollen associations across the late Quaternary</a>.
<i>Ecography</i> 37(11): 1095&ndash;1108.</p>

<h2>2013</h2>

<p class="pub"><span class="me">N.A. Jud</span> and L.J. Hickey.
<a href="https://doi.org/10.3732/ajb.1300250">A new Early Cretaceous angiosperm from the Potomac Group and
its implications for the evolution of eudicot leaf architecture</a>.
<i>American Journal of Botany</i> 100(12): 2437&ndash;2449.
<span class="extra">· <a href="pdfs/jud-2013-potomacapnos.pdf">PDF</a></span></p>

<h2>2011</h2>

<p class="pub">A. Ficke, C. Myrick, and <span class="me">N.A. Jud</span>.
<a href="https://doi.org/10.1080/00028487.2011.638579">Swimming and jumping abilities of two plains fishes:
temperature effects and implications for fish passage</a>.
<i>Transactions of the American Fisheries Society</i> 140(6): 1521&ndash;1531.</p>

<p class="pub">H.J. Falcon-Lang, <span class="me">N.A. Jud</span>, W.A. DiMichele, D.S. Chaney, W.J. Nelson,
and S.G. Lucas. <a href="https://doi.org/10.1130/G31764.1">Pennsylvanian coniferopsid forests in sabkha
facies reveal the nature of seasonal tropical biome</a>. <i>Geology</i> 39(4): 371&ndash;374.
<span class="extra">· <a href="pdfs/falcon-lang-2011-coniferopsid.pdf">PDF</a></span></p>

<h2>2010</h2>

<p class="pub"><span class="me">N.A. Jud</span>, G.W. Rothwell, and R.A. Stockey.
<a href="https://doi.org/10.1086/655963">Paleoecological and phylogenetic implications of <i>Saxicaulis
meckertii</i> gen. et sp. nov.: a bennettitalean stem from the Upper Cretaceous of western North America</a>.
<i>International Journal of Plant Sciences</i> 171(8): 915&ndash;925.
<span class="extra">· <a href="pdfs/jud-2010-saxicaulis.pdf">PDF</a></span></p>

<h2>2008</h2>

<p class="pub"><span class="me">N.A. Jud</span>, G.W. Rothwell, and R.A. Stockey.
<a href="https://doi.org/10.3732/ajb.95.3.330">Anatomically preserved <i>Todea</i> from the Lower Cretaceous
of western North America: implications for the phylogeny of Osmundaceae</a>.
<i>American Journal of Botany</i> 95(3): 330&ndash;339.
<span class="extra">· <a href="pdfs/jud-2008-todea.pdf">PDF</a>
· <a href="https://morphobank.org/index.php/Projects/ProjectOverview/project_id/2691">Corrected data (MorphoBank)</a></span></p>

</div>

</main>
"""

# --------------------------------------------------------------------------
# Galleries
# --------------------------------------------------------------------------

gallery_items = [
    ("images/gallery/lacinipetalum.jpg", "<em>Lacinipetalum spectabilum</em>"),
    ("images/gallery/notiantha.jpg", "<em>Notiantha grandensis</em> Jud et al. 2017"),
    ("images/gallery/stephania.jpg", "<em>Stephania psittaca</em> (Menispermaceae) fruit from the early Paleocene of Patagonia"),
    ("images/gallery/rourea.jpg", "<em>Rourea blatta</em> Jud and Nelson 2017"),
    ("images/gallery/fairlingtonia.jpg", "<em>Fairlingtonia thyrsopteroides</em> roots, showing the adventitious roots and slender young stem (Jud 2015)"),
    ("images/gallery/todea.jpg", "Transverse section of <em>Todea tidwellii</em> showing the dark sclerenchymatous pith (Jud et al. 2008)"),
    ("images/gallery/mammea.jpg", "<em>Mammea paramericana</em> Nelson and Jud 2017"),
    ("images/gallery/parinari.jpg", "Transverse section of a <em>Parinari</em> endocarp from the lower Miocene of Panama. Scale bar = 1 cm (Jud et al. 2016)"),
    ("images/gallery/ficus.jpg", "Fossil <em>Ficus</em> wood from the Cenozoic of Panama (Jud and Dunham)"),
]

gallery = """<main>

<h1 class="page-title">Gallery</h1>
<p class="page-intro">Specimens from our research and from the teaching collection at William Jewell.</p>

<section>
  <h2>Research specimens</h2>
  <div class="gallery">
""" + "\n".join(figure(s, c) for s, c in gallery_items) + """
  </div>
</section>

<section>
  <h2>WJC rocks &amp; fossils</h2>
  <p>Specimens from the William Jewell College teaching collection.</p>
  <div class="gallery">
""" + "\n".join(
    figure(f"images/fossils/fossil-{i:02d}.jpg", "") for i in range(1, 26)
) + """
  </div>
</section>

</main>
"""

plants = """<main>

<h1 class="page-title">Plant photos</h1>
<p class="page-intro">Photographs of living plants, from the field and from the greenhouse.</p>

<section>
  <div class="gallery">
""" + "\n".join(
    figure(f"images/plants/plant-{i:02d}.jpg", "") for i in range(1, 25)
) + """
  </div>
</section>

</main>
"""

# --------------------------------------------------------------------------
# Blog
# --------------------------------------------------------------------------

POSTS = [
    ("Dispatch from the field #4", "July 15, 2021",
     "After July 4th our team grew a bit. Eric Gorscak and Sasha Prokuda arrived in time for a fourth-of-July picnic in Powell, Wyoming."),
    ("Dispatch from the field #3", "July 10, 2021",
     "The goal this summer was to collect fossils and geologic data from a Cretaceous lake deposit so that we can estimate its age."),
    ("Dispatch from the field #2", "July 3, 2021",
     "We spent the first morning gathering supplies and dealing with some emails. In Worland we visited with Mike Bies while we filled up."),
    ("Dispatch from the field #1", "July 2, 2021",
     "I started collecting plant fossils in the Bighorn Basin in 2009, but this was my first summer back to collect since starting at William Jewell."),
    ("Cretaceous angiosperm trees", "February 20, 2021",
     "A 2018 plot showing the age, size, and distribution of angiosperm woods through the Cretaceous."),
    ("Two new species of aquatic ferns", "July 22, 2019",
     "Salviniales are an unusual group of ferns: they are freshwater aquatic plants."),
    ("Flowers from the early Paleocene of Patagonia", "January 5, 2018",
     "Sixty-four million years ago, in what is now Patagonia, fossil evidence records the plants that flowered after the end-Cretaceous extinction."),
    ("Fossil buckthorn flowers from Patagonia", "July 27, 2017",
     "Sixty-five million years ago the southern continents were still in the process of separating."),
    ("Fossil wood reveals changes in ancient forests", "May 2, 2017",
     "How the diversification of flowering plants transformed the structure of ancient forests."),
    ("Piecing together the early Miocene forests of Panama", "February 25, 2017",
     "Plant fossils from the Panama Canal let us trace the history of neotropical forests."),
    ("Aloha from Volcanoes National Park", "February 12, 2017",
     "Hawaii is a hotspot for scientific research."),
    ("Imaging leaves on herbarium sheets", "October 31, 2016",
     "Herbaria are an essential source of comparative data for botanists."),
    ("Leaf-mining flies on early flowering plants", "October 29, 2016",
     "Leaf-miners are insects that dwell inside of leaves during their larval stage."),
]

blog = """<main>

<h1 class="page-title">Blog</h1>
<p class="page-intro">Field dispatches and notes on new papers.</p>

<div class="note">
  <strong>Note for Nathan:</strong> these are the titles, dates, and opening lines of your Wix posts.
  The full text of each post still needs to be pasted in &mdash; see <code>README.md</code>, section 6.
  Delete this box once that's done.
</div>

<section>
  <ul class="post-list">
""" + "\n".join(
    f"""    <li>
      <h3>{t}</h3>
      <div class="date">{d}</div>
      <p>{e}</p>
    </li>""" for t, d, e in POSTS
) + """
  </ul>
</section>

</main>
"""

# --------------------------------------------------------------------------
# Contact
# --------------------------------------------------------------------------

contact = """<main>

<h1 class="page-title">Get in touch</h1>

<section>
  <p>Dr. Nathan A. Jud<br>
  Department of Biology<br>
  William Jewell College<br>
  500 College Hill<br>
  Liberty, MO 64068</p>

  <p>Email: <a href="mailto:judn@william.jewell.edu">judn@william.jewell.edu</a></p>

  <p><a href="https://github.com/PaleoNate">GitHub</a> ·
     <a href="https://twitter.com/PaleoNate">Twitter</a> ·
     <a href="https://www.instagram.com/paleonate/">Instagram</a></p>
</section>

<section>
  <h2>Prospective students</h2>
  <p>William Jewell students interested in research projects in organismal botany, paleontology, or
  paleoecology are welcome to email me directly. It helps if you mention which of the
  <a href="research.html">current research topics</a> interests you, and roughly when you would like
  to start.</p>
</section>

</main>
"""

PAGES = [
    ("index.html", "Home", home),
    ("research.html", "Research", research),
    ("publications.html", "Publications", publications),
    ("people.html", "People", people),
    ("teaching.html", "Teaching", teaching),
    ("gallery.html", "Gallery", gallery),
    ("plants.html", "Plant photos", plants),
    ("blog.html", "Blog", blog),
    ("contact.html", "Contact", contact),
]

if __name__ == "__main__":
    for filename, title, body in PAGES:
        with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as fh:
            fh.write(shell(filename, title, body))
        print("wrote", filename)
