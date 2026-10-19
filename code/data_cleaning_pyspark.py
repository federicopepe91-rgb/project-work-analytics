!pip install python-pptx -q

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from google.colab import files

# Inizializzazione 16:9 Widescreen
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Palette Colori "Light Data Analytics"
BG_LIGHT = RGBColor(248, 250, 252)       # Sfondo Bianco/Ghiaccio
CARD_WHITE = RGBColor(255, 255, 255)     # Card candide per massimo contrasto foto
CARD_BORDER = RGBColor(226, 232, 240)    # Bordo delicato
NAVY_PRIMARY = RGBColor(15, 23, 42)      # Blu Notte profondo per titoli
BLUE_ACCENT = RGBColor(2, 132, 199)      # Blu Data Analytics (Cobalto)
TEXT_DARK = RGBColor(51, 65, 85)         # Testo corpo
TEXT_MUTED = RGBColor(100, 116, 139)     # Sottotitoli

# ==========================================
# --- SLIDE 1: TEAM DI PROGETTO (TEMA CHIARO) ---
# ==========================================
slide1 = prs.slides.add_slide(blank_layout)

# 1. Sfondo Chiaro Full-Bleed
bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
bg1.fill.solid()
bg1.fill.fore_color.rgb = BG_LIGHT
bg1.line.fill.background()

# Barra d'accento superiore (Blu Analytics)
top_bar1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
top_bar1.fill.solid()
top_bar1.fill.fore_color.rgb = BLUE_ACCENT
top_bar1.line.fill.background()

# Header Titolo
title_box = slide1.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.0))
tf = title_box.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "Team di Progetto | Data Analytics & BI"
p.font.size = Pt(28)
p.font.bold = True
p.font.color.rgb = NAVY_PRIMARY

p2 = tf.add_paragraph()
p2.text = "Pipeline end-to-end: PySpark Data Prep, Data Warehousing SQL & Power BI"
p2.font.size = Pt(13)
p2.font.color.rgb = BLUE_ACCENT

# Dati del Team
team_members = [
    {
        "name": "Membro Team 1",
        "role": "Data Engineer Specialist",
        "image": "immagine lavoro.jpg",
        "tasks": [
            "Bonifica dati grezzi su Google Colab con PySpark",
            "Validazione tipi dato e pulizia anomalie",
            "Export dataset pulito per ingestione SQL"
        ]
    },
    {
        "name": "Membro Team 2",
        "role": "SQL & Data Warehouse Specialist",
        "image": "WhatsApp Image 2026-09-30 at 17.16.05.jpeg",
        "tasks": [
            "Modellazione Star Schema e configurazione PK / FK",
            "Sviluppo Vista dbo.vw_VenditePowerBI per Governance",
            "Query di Audit e Prova di Conciliazione Contabile"
        ]
    },
    {
        "name": "Membro Team 3",
        "role": "BI Developer & UX Specialist",
        "image": "WhatsApp Image 2026-09-30 at 17.19.17.jpeg",
        "tasks": [
            "Modellazione Calendario DAX e Misure a 0 MB RAM",
            "Implementazione Time Intelligence YoY",
            "Design Dashboard, Tooltip, Drillthrough e Bookmarks"
        ]
    }
]

col_width = Inches(3.6)
col_gap = Inches(0.4)
left_margin = Inches(0.8)
top_pos = Inches(1.6)
card_height = Inches(5.3)

for i, member in enumerate(team_members):
    col_left = left_margin + i * (col_width + col_gap)

    # Card Contenitore Bianca
    card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_left, top_pos, col_width, card_height)
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_WHITE
    card.line.color.rgb = CARD_BORDER

    # Immagine Profilo
    img_path = member["image"]
    img_top = top_pos + Inches(0.25)
    img_size = Inches(1.8)
    img_left = col_left + (col_width - img_size) / 2

    if os.path.exists(img_path):
        # Cornice bianca sottile per risaltare la foto
        frame = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, img_left - Inches(0.04), img_top - Inches(0.04), img_size + Inches(0.08), img_size + Inches(0.08))
        frame.fill.solid()
        frame.fill.fore_color.rgb = CARD_WHITE
        frame.line.color.rgb = CARD_BORDER

        slide1.shapes.add_picture(img_path, img_left, img_top, width=img_size, height=img_size)
    else:
        ph = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, img_left, img_top, img_size, img_size)
        ph.fill.solid()
        ph.fill.fore_color.rgb = BG_LIGHT
        p_ph = ph.text_frame.paragraphs[0]
        p_ph.text = f"Carica foto:\n{img_path}"
        p_ph.font.size = Pt(10)
        p_ph.font.color.rgb = TEXT_MUTED
        p_ph.alignment = PP_ALIGN.CENTER

    # Testi dentro la Card
    txt_box = slide1.shapes.add_textbox(col_left + Inches(0.15), top_pos + Inches(2.25), col_width - Inches(0.3), Inches(2.8))
    tf_m = txt_box.text_frame
    tf_m.word_wrap = True

    p_name = tf_m.paragraphs[0]
    p_name.text = member["name"]
    p_name.font.size = Pt(16)
    p_name.font.bold = True
    p_name.font.color.rgb = NAVY_PRIMARY
    p_name.alignment = PP_ALIGN.CENTER

    p_role = tf_m.add_paragraph()
    p_role.text = member["role"]
    p_role.font.size = Pt(11)
    p_role.font.bold = True
    p_role.font.color.rgb = BLUE_ACCENT
    p_role.alignment = PP_ALIGN.CENTER

    tf_m.add_paragraph()

    for task in member["tasks"]:
        p_task = tf_m.add_paragraph()
        p_task.text = f"• {task}"
        p_task.font.size = Pt(10)
        p_task.font.color.rgb = TEXT_DARK

# ==========================================
# --- SLIDE 2: CHIUSURA PROGETTO & Q&A ---
# ==========================================
slide2 = prs.slides.add_slide(blank_layout)

bg2 = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
bg2.fill.solid()
bg2.fill.fore_color.rgb = BG_LIGHT
bg2.line.fill.background()

top_bar2 = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
top_bar2.fill.solid()
top_bar2.fill.fore_color.rgb = BLUE_ACCENT
top_bar2.line.fill.background()

# Header Titolo
title_box2 = slide2.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.0))
tf2 = title_box2.text_frame
tf2.word_wrap = True

p_s2 = tf2.paragraphs[0]
p_s2.text = "Conclusioni & Valore Aziendale Generato"
p_s2.font.size = Pt(28)
p_s2.font.bold = True
p_s2.font.color.rgb = NAVY_PRIMARY

p2_s2 = tf2.add_paragraph()
p2_s2.text = "Project Delivery | AdventureWorks Enterprise Analytics"
p2_s2.font.size = Pt(13)
p2_s2.font.color.rgb = BLUE_ACCENT

# Colonna 1: Risultati
col1_left = Inches(0.8)
col_w2 = Inches(5.6)
top_pos2 = Inches(1.6)

card1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col1_left, top_pos2, col_w2, Inches(5.3))
card1.fill.solid()
card1.fill.fore_color.rgb = CARD_WHITE
card1.line.color.rgb = CARD_BORDER

tf_c1 = card1.text_frame
tf_c1.word_wrap = True
p_c1_title = tf_c1.paragraphs[0]
p_c1_title.text = "Risultati Chiave Raggiunti"
p_c1_title.font.size = Pt(18)
p_c1_title.font.bold = True
p_c1_title.font.color.rgb = NAVY_PRIMARY

bullets1 = [
    ("Pipeline Certificata 100%", "Dati integrati senza disallineamenti contabili (€ 465,4 M Ricavi e 60.398 righe) con zero perdite dati e zero duplicazioni."),
    ("Single Source of Truth", "Centralizzazione delle formule aziendali e della Data Governance all'interno della Vista SQL Server."),
    ("UX Direzionale Avanzata", "Report interattivo con navigazione guidata tramite Drillthrough, Tooltip territoriali e Bookmarks di reset.")
]

for title, desc in bullets1:
    p_b = tf_c1.add_paragraph()
    p_b.text = f"\n• {title}: "
    p_b.font.bold = True
    p_b.font.size = Pt(11)
    p_b.font.color.rgb = BLUE_ACCENT

    p_desc = tf_c1.add_paragraph()
    p_desc.text = f"  {desc}"
    p_desc.font.size = Pt(10)
    p_desc.font.color.rgb = TEXT_DARK

# Colonna 2: Sviluppi Futuri & Q&A
col2_left = Inches(6.9)

card2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col2_left, top_pos2, col_w2, Inches(5.3))
card2.fill.solid()
card2.fill.fore_color.rgb = NAVY_PRIMARY
card2.line.fill.background()

tf_c2 = card2.text_frame
tf_c2.word_wrap = True
p_c2_title = tf_c2.paragraphs[0]
p_c2_title.text = "Prospettive Future & Q&A"
p_c2_title.font.size = Pt(18)
p_c2_title.font.bold = True
p_c2_title.font.color.rgb = CARD_WHITE

bullets2 = [
    "Automazione flussi ETL tramite Azure Data Factory",
    "Ottimizzazione DirectQuery / Incremental Refresh",
    "Integrazione modelli ML in Python per il Sales Forecast"
]

for bullet in bullets2:
    p_b2 = tf_c2.add_paragraph()
    p_b2.text = f"\n• {bullet}"
    p_b2.font.size = Pt(11)
    p_b2.font.color.rgb = RGBColor(226, 232, 240)

qa_box = tf_c2.add_paragraph()
qa_box.text = "\n\nGRAZIE PER L'ATTENZIONE\nDomande & Demo Live"
qa_box.font.size = Pt(18)
qa_box.font.bold = True
qa_box.font.color.rgb = BLUE_ACCENT
qa_box.alignment = PP_ALIGN.CENTER

# Salvataggio e Download
filename = "Presentazione_Light_DataAnalytics.pptx"
prs.save(filename)
files.download(filename)
