from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm

# Création du PDF
pdf_file = "CV_Mariam_Sanoko.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# Couleurs
blue = colors.HexColor("#003366")
gray_light = colors.HexColor("#F5F5F5")
gray_text = colors.HexColor("#333333")

# Bande latérale gauche
c.setFillColor(gray_light)
c.rect(0, 0, 6*cm, height, fill=1, stroke=0)

# Infos personnelles
c.setFillColor(blue)
c.setFont("Helvetica-Bold", 16)
c.drawString(1*cm, height-2*cm, "Mariam Sanoko")
c.setFont("Helvetica", 11)
c.setFillColor(gray_text)
c.drawString(1*cm, height-3*cm, "Directrice Artistique | CDA")
c.drawString(1*cm, height-4*cm, "Consultante Microsoft CRM & Power Platform")
c.drawString(1*cm, height-5*cm, "📧 mariam.sanoko@gmail.com")
c.drawString(1*cm, height-5.7*cm, "📱 +33 6 03 60 82 74")
c.drawString(1*cm, height-6.4*cm, "🌐 msprods.fr")

# Compétences
c.setFont("Helvetica-Bold", 12)
c.setFillColor(blue)
c.drawString(1*cm, height-8*cm, "Compétences")
c.setFont("Helvetica", 10)
c.setFillColor(gray_text)
skills = [
    "Power Platform: Power Apps, Power BI, Power Automate, Power Pages, D365 CRM",
    "UX/UI: Adobe XD, Figma, Photoshop, Illustrator, InDesign",
    "No-code/low-code: Airtable, Tally, Make (GNU/free license), WordPress",
    "IA & ChatGy: chatbots IA intégrés",
    "Data analyse: Power BI, Dataverse, Power Query, DAX",
    "Développement web/mobile: React Native, API, Stripe, 2FA"
]
y = height-9*cm
for skill in skills:
    c.drawString(1*cm, y, "- " + skill)
    y -= 0.6*cm

# Formations
c.setFillColor(blue)
c.setFont("Helvetica-Bold", 12)
c.drawString(1*cm, y-0.5*cm, "Formations")
c.setFillColor(gray_text)
c.setFont("Helvetica", 10)
formations = [
    "CDA – Concepteur Développeur d’Applications, M2i Tech Academy, 2024",
    "Power Platform & D365 CRM – Webforce 3, 2022",
    "UX/UI Designer – Mediabox MS Prods, 2016",
    "Data Analyste – Databird Freelance, 2022"
]
y -= 1*cm
for f in formations:
    c.drawString(1*cm, y, "- " + f)
    y -= 0.6*cm

# Langues
c.setFillColor(blue)
c.setFont("Helvetica-Bold", 12)
c.drawString(1*cm, y-0.5*cm, "Langues")
c.setFillColor(gray_text)
c.setFont("Helvetica", 10)
c.drawString(1*cm, y-1.1*cm, "- Français : langue maternelle")
c.drawString(1*cm, y-1.8*cm, "- Anglais : professionnel")

# Section principale droite
x_offset = 6*cm + 1*cm
y = height - 2*cm

# Profil
c.setFillColor(blue)
c.setFont("Helvetica-Bold", 14)
c.drawString(x_offset, y, "Profil")
c.setFont("Helvetica", 10)
c.setFillColor(gray_text)
y -= 0.7*cm
profil_text = ("Directrice Artistique et CDA, experte UI/UX Design, Microsoft Dynamics 365 CRM, "
               "Power Platform et low-code/no-code, avec un solide background en data analyse "
               "et développement IA (ChatGy).")
for line in profil_text.split(". "):
    c.drawString(x_offset, y, line.strip())
    y -= 0.6*cm

# Expériences Freelance
y -= 0.4*cm
c.setFillColor(blue)
c.setFont("Helvetica-Bold", 12)
c.drawString(x_offset, y, "Expériences Freelance")
c.setFont("Helvetica", 10)
c.setFillColor(gray_text)
y -= 0.7*cm
freelance_exp = [
    "MS Prods (2023–Aujourd'hui): Power Apps, Power BI, Power Automate, Power Pages",
    "Prototypage UX/UI: Figma, Adobe XD",
    "ChatGy IA: chatbots intégrés aux apps",
    "No-code/low-code: Airtable, Tally, Make (GNU/free)",
    "Data analyse: Power BI dashboards, KPI, Dataverse",
    "Formation et accompagnement utilisateurs"
]
for exp in freelance_exp:
    c.drawString(x_offset, y, "- " + exp)
    y -= 0.6*cm

# Expériences Entreprise
y -= 0.4*cm
c.setFillColor(blue)
c.setFont("Helvetica-Bold", 12)
c.drawString(x_offset, y, "Expériences Entreprise")
c.setFont("Helvetica", 10)
c.setFillColor(gray_text)
y -= 0.7*cm
enterprise_exp = [
    "Publicis (2022–2023): Dashboards Power BI, Power Automate, Power Apps",
    "Lectra (2014–2016): Communication multimédia, branding, création graphique"
]
for exp in enterprise_exp:
    c.drawString(x_offset, y, "- " + exp)
    y -= 0.6*cm

# Projets / réalisations
y -= 0.4*cm
c.setFillColor(blue)
c.setFont("Helvetica-Bold", 12)
c.drawString(x_offset, y, "Projets & Réalisations")
c.setFont("Helvetica", 10)
c.setFillColor(gray_text)
y -= 0.7*cm
projects = [
    "ChatGy: chatbots IA intégrés à Power Apps et workflows automatisés",
    "No-code / low-code: Airtable, Tally, Make (GNU/free)",
    "Data analyse: reporting automatisé, création de KPI et dashboards Power BI",
    "UX/UI: prototypes Figma/Adobe XD, interfaces accessibles et intuitives"
]
for p in projects:
    c.drawString(x_offset, y, "- " + p)
    y -= 0.6*cm

# Génération du PDF
c.save()
print(f"PDF généré : {pdf_file}")
