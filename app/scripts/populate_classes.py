from app.models import YogaClass
from django.db import connection

# Drop existing entries in the table
def reset_table():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM app_yogaclass;")  # Clear all existing entries
        cursor.execute("ALTER TABLE app_yogaclass AUTO_INCREMENT = 1;")  # Reset the auto-increment ID
        cursor.execute("OPTIMIZE TABLE app_yogaclass;")  # Optimize the table (MySQL-specific)

# List of classes to populate
classes = [
    {
        "yoga_type": "Burnout-Yogini",
        "name": "Yin Kindness",
        "class_type": "Regulär",
        "key_features": "Lang gehaltene passive Positionen, Achtsamkeit",
        "ideal_for": "Stressabbau und Regulierung des Nervensystems",
        "ideal_for_short": "A"  # Burnout-Yogini
    },
    {
        "yoga_type": "Burnout-Yogini",
        "name": "The Yin of Kindness",
        "class_type": "Spezial",
        "key_features": "Yoga Nidra + tiefe Entspannung",
        "ideal_for": "Erholung von emotionaler Erschöpfung",
        "ideal_for_short": "A"  # Burnout-Yogini
    },
    {
        "yoga_type": "Burnout-Yogini",
        "name": "Kindness Under the Moon",
        "class_type": "Workshop",
        "key_features": "Tee-Rituale + Journaling",
        "ideal_for": "Ganzheitliche Selbstfürsorge",
        "ideal_for_short": "A"  # Burnout-Yogini
    },
    {
        "yoga_type": "Burnout-Yogini",
        "name": "Traumasensibles 1:1 Yoga",
        "class_type": "Privat",
        "key_features": "Traumasensibler Ansatz",
        "ideal_for": "Sicherer Raum für die Wiederverbindung mit dem Körper",
        "ideal_for_short": "A"  # Burnout-Yogini
    },
    {
        "yoga_type": "Ashtanga-Warrior",
        "name": "Ashtanga Kindness",
        "class_type": "Regulär",
        "key_features": "Strukturierte Ashtanga-Serie",
        "ideal_for": "Disziplinierte Suchende",
        "ideal_for_short": "B"  # Ashtanga-Krieger:in
    },
    {
        "yoga_type": "Ashtanga-Warrior",
        "name": "Ashtanga Practice Kindness",
        "class_type": "Regulär",
        "key_features": "Selbstgeführter Mysore-Stil",
        "ideal_for": "Autonome Praktizierende",
        "ideal_for_short": "B"  # Ashtanga-Krieger:in
    },
    {
        "yoga_type": "Ashtanga-Warrior",
        "name": "Vinyasa Kindness",
        "class_type": "Regulär",
        "key_features": "Kraftvolle, atemsynchrone Flows",
        "ideal_for": "Enthusiast:innen körperlicher Herausforderungen",
        "ideal_for_short": "B"  # Ashtanga-Krieger:in
    },
    {
        "yoga_type": "Homeoffice-Yogini",
        "name": "Basic-Kindness",
        "class_type": "Regulär",
        "key_features": "Einfache fließende Sequenzen",
        "ideal_for": "Flexible Zeitpläne",
        "ideal_for_short": "C"  # Homeoffice-Yogi:ni
    },
    {
        "yoga_type": "Homeoffice-Yogini",
        "name": "Music Kindness-Vinyasa Spezial",
        "class_type": "Spezial",
        "key_features": "Künstlerische/musikalische Themen-Flows",
        "ideal_for": "Kreativer Ausdruck",
        "ideal_for_short": "C"  # Homeoffice-Yogi:ni
    },
    {
        "yoga_type": "Homeoffice-Yogini",
        "name": "The Kind Flow of Words",
        "class_type": "Spezial",
        "key_features": "Yoga + Poesie/Schreiben",
        "ideal_for": "Integration von Körper und Geist",
        "ideal_for_short": "C"  # Homeoffice-Yogi:ni
    },
    {
        "yoga_type": "Casual-Stretcher",
        "name": "Kindness-Kurs für Anfänger:innen",
        "class_type": "Regulär",
        "key_features": "4-6 Wochen Einsteigerkurs",
        "ideal_for": "Yoga-Neulinge",
        "ideal_for_short": "D"  # Gelegenheits-Dehner:in
    },
    {
        "yoga_type": "Casual-Stretcher",
        "name": "Be Kind Social",
        "class_type": "Sonstiges",
        "key_features": "Kostenlose Gemeinschaftsstunde",
        "ideal_for": "Ungezwungene soziale Praxis",
        "ideal_for_short": "D"  # Gelegenheits-Dehner:in
    },
    {
        "yoga_type": "Casual-Stretcher",
        "name": "1:1 Kindness-Yoga",
        "class_type": "Privat",
        "key_features": "Personalisierte Sitzungen",
        "ideal_for": "Individuelles Lerntempo",
        "ideal_for_short": "D"  # Gelegenheits-Dehner:in
    }
]

# Populate the database
def populate_classes():
    for cls in classes:
        YogaClass.objects.create(
            yoga_type=cls["yoga_type"],
            name=cls["name"],
            class_type=cls["class_type"],
            key_features=cls["key_features"],
            ideal_for=cls["ideal_for"],
            ideal_for_short=cls["ideal_for_short"],  # Include this field
        )
    print("Klassen erfolgreich hinzugefügt!")

# Reset the table and populate it
reset_table()
populate_classes()