from app.models import YogaClass

# List of classes to populate
classes = [
    {"name": "Kindness-Kurs für Anfänger", "description": "Basic Einführung, ohne Druck, Basics wie Atmen, achtsames Spüren", "duration": "60 min", "type": "D"},
    {"name": "Basic Kindness", "description": "Offene Stunde für Anfänger:innen & Wiedereinsteiger:innen, sanfte Bewegungen", "duration": "60 min", "type": "D"},
    {"name": "Yin Kindness", "description": "Langsame, passive Haltungen, Raum zum Spüren und Loslassen", "duration": "60 min", "type": "A"},
    {"name": "Yin Extended Kindness (SO)", "description": "Verlängerte Yin Yoga Session mit noch mehr Raum für Ruhe", "duration": "75 min", "type": "A"},
    {"name": "Ashtanga Kindness", "description": "Strukturierte Ashtanga-Praxis ohne Leistungsdruck", "duration": "75 min", "type": "B"},
    {"name": "Ashtanga Practice Kindness (Self Practice)", "description": "Selbständige Ashtanga-Praxis mit achtsamer Begleitung", "duration": "120 min", "type": "B"},
    {"name": "Vinyasa Kindness", "description": "Achtsamer Flow, kraftvoll und sanft, im Rhythmus des Atems", "duration": "60 min", "type": "C"},
    {"name": "Be Kind Flow (Slow Flow/Basic Flow)", "description": "Sanfter Flow ohne Vinyasas – entspannt, kreativ, bewusst", "duration": "60 min", "type": "C"},
    {"name": "Rainbow Kindness-Vinyasa Special", "description": "Vinyasa Flow kombiniert mit Farben und Musik", "duration": "75–90 min", "type": "C"},
    {"name": "Music Kindness-Vinyasa Special", "description": "Flow im Rhythmus eines Musikthemas/Künstlers", "duration": "75–90 min", "type": "C"},
    {"name": "The Yin of Kindness", "description": "Kombination aus Yin Yoga & Yoga Nidra (tiefes Loslassen)", "duration": "90 min", "type": "A"},
    {"name": "The Kind Flow of Words", "description": "Yoga mit intuitivem Schreiben und Poesie", "duration": "90 min", "type": "A"},
    {"name": "Karma & Kindness (Soft Satsang)", "description": "Sanfter Deep Talk über Yoga-Philosophie und Alltagsthemen", "duration": "60 min", "type": "A"},
    {"name": "1:1 Kindness Yoga", "description": "Private Einzelstunde für individuelle Praxis", "duration": "60 min", "type": "C"},
    {"name": "Traumasensibles 1:1 Kindness Yoga", "description": "Traumainformierte Einzelbegleitung in deinem Tempo", "duration": "60 min", "type": "A"},
    {"name": "Kindness under the Moon (Workshop)", "description": "Neumond/Vollmond Zeremonie mit Yoga, Journaling, Ritualen", "duration": "2,5–3 h", "type": "A"},
    {"name": "Be Kind Safe Space Abend (Workshop)", "description": "Kakao, Sharing Circles, Ankommen im eigenen Raum", "duration": "2,5–3 h", "type": "A"},
    {"name": "Be Kind Brave Space Abend (Workshop)", "description": "Sanftes Wachsen an inneren Grenzen, mutiges Lernen", "duration": "2,5–3 h", "type": "B"},
    {"name": "Fuck-Up Session: Asana Fuck-Ups & Lebenslektionen", "description": "Ego loslassen auf und neben der Matte", "duration": "2–2,5 h", "type": "B"},
]

# Populate the database
for cls in classes:
    YogaClass.objects.create(**cls)

print("Classes added successfully!")