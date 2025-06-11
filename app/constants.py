# Default yoga type
DEFAULT_YOGA_TYPE = "Homeoffice-Yogini"

# Mapping of answer types to yoga types
QUESTIONS = [
    {
        "number": 1,
        "question": "Wie fühlt sich dein Körper aktuell an?",
        "answers": {
            "A": "Basically der Typ flexible Brezel – super elastisch in allen Positionen.",
            "B": "Solide, aber manchmal knarre ich beim Aufstehen wie ein Holzstuhl.",
            "C": "Mein Körper ist ein work in progress – ich bin da realistisch.",
            "D": "Bewegung gibt’s nur dann, wenn es unbedingt sein muss."
        }
    },
    {
        "number": 2,
        "question": "Wie läuft’s bei dir mit Verletzungen oder Einschränkungen?",
        "answers": {
            "A": "Momentan hab ich keine akuten oder chronischen Verletzungen.",
            "B": "Uff – meine Schulter erzählt noch vom Festival ’18.",
            "C": "Mein Körper kommt mir derzeit wie eine chronische Baustelle vor.",
            "D": "Ich bin aktuell völlig out of order — aber ich will zurück ins Game."
        }
    },
    {
        "number": 3,
        "question": "Dein Commitment-Level zu Yoga?",
        "answers": {
            "A": "Situationship-Yogi. Ich und Yoga waren immer schon on-off.",
            "B": "Yoga war Liebe auf den ersten Blick. Ich bin vollkommen committed!",
            "C": "YouTube-Yoga und ich haben eine intensive Fernbeziehung.",
            "D": "Ich schau mal. Ich hab gehört es gibt Snacks und Tee nach der Klasse."
        }
    },
    {
        "number": 4,
        "question": "Welche Vibes spürst du, wenn du an Yoga denkst?",
        "answers": {
            "A": "Faszien-Liebe: Entkrampfen, durchatmen, alles loslassen!",
            "B": "Power-Mover: Schwitzen, stretchen, strong AF werden.",
            "C": "Slow-Flow: Ich will flowen und chillen.",
            "D": "Zen-Seeker: Ich brauche mehr im Leben — vielleicht ist es Yoga."
        }
    },
    {
        "number": 5,
        "question": "Wie willst du dein Yoga erleben?",
        "answers": {
            "A": "Kollektiver Vibe like a Sunday Brunch – nur mit Asanas.",
            "B": "Mat Queen: Ich bleibe auf meiner Matte, alles andere blende ich aus.",
            "C": "Zen-Master: Hauptsache gemütlich, langsamer und tiefer.",
            "D": "Ich brauch klare Ansagen – step by step, sonst verlauf ich mich."
        }
    }
]

ANSWER_TO_TYPE = {
    'A': 'Ashtanga-Warrior',
    'B': 'Burnout-Yogini',
    'C': 'Homeoffice-Yogini',
    'D': 'Casual-Stretcher'
}

# Yoga result types and their descriptions
YOGA_RESULT_TYPES = {
    "Burnout-Yogini": {
        "title": "Burnout-Yogini",
        "image": "https://bekindstudio.at/wp-content/uploads/2025/05/burnout_yogini-200x300.png",
        "description": [
            "Du checkst bei Yoga ein, wenn der Akku blinkt. Regelmäßigkeit wäre dein ultimativer Cheatcode!",
            "Yoga kann tatsächlich deine ganze Welt verändern: Schon mit einer Übung täglich wird dein Nervensystem stabil — statt hart zu crashen, wenn es wirklich ernst wird."
        ],
        "match": {
            "title": "Basic Kindness",
            "reason": "passt zu dir, weil du dich hier ohne Druck stabilisieren darfst."
        },
        "challenge": {
            "title": "Mond-Workshops",
            "reason": "In einem Mond-Workshop geht es nur um dich und deine Selbstfürsorge. Das ist nicht was du gerade willst — aber das was du brauchst."
        }
    },
    "Ashtanga-Warrior": {
        "title": "Ashtanga-Warrior",
        "image": "https://bekindstudio.at/wp-content/uploads/2025/05/ashtanga_warrior-200x300.png",
        "description": [
            "Du brauchst Power, Struktur und klare Ziele. Ashtanga matcht genau deinen Vibe: Kraft, Ausdauer, Fokus.",
            "Aber Achtung: Dein Superpower-Upgrade liegt in der bewussten Erholung, nicht nur im immer weiter Pushen. Dein Körper liebt Aktivität – aber Regeneration macht dich langfristig stärker."
        ],
        "match": {
            "title": "Ashtanga",
            "reason": "passt zu dir, weil du körperliche Challenge und fokussierte Energie liebst."
        },
        "challenge": {
            "title": "Yin",
            "reason": "Du bist endlich bereit dich deinem Erzfeind Savasana zu stellen? Yin ist dein Boot Camp in die Entspannung."
        }
    },
    "Homeoffice-Yogini": {
        "title": "Homeoffice-Yogini",
        "image": "https://bekindstudio.at/wp-content/uploads/2025/05/homeoffice_yogi-200x300.png",
        "description": [
            "Du bist flexibel im YouTube-Flow in der Homeoffice-Lunch-Session zwischen deinen Calls – love it!",
            "Aber Achtung: Ganz ohne echte Guidance gibt es das Risiko von Fehlhaltungen. Regelmäßiges Üben zuhause ist super, aber der Austausch in einer Gruppe gibt dir neue Energie, soziale Verbindung und oft auch ein Upgrade bei Technik und Motivation."
        ],
        "match": {
            "title": "Vinyasa",
            "reason": "passt zu dir, weil du kreative und strukturierte Flows liebst."
        },
        "challenge": {
            "title": "Ashtanga Kurse",
            "reason": "Du kennst alle Positionen. Bist du bereit genauer hinzusehen? Im Ashtanga feilst du an deinem Alignment und bügelst damit alle sich einschleichenden Fehlhaltungen aus."
        }
    },
    "Casual-Stretcher": {
        "title": "Casual-Stretcher",
        "image": "https://bekindstudio.at/wp-content/uploads/2025/05/casual_stretcher-200x300.png",
        "description": [
            "Für dich ist Yoga a whole mood und kein Plan. Es ist völlig okay vor sich hin zu yinnen und die Welt draußen zu lassen.",
            "Aber: Wenn du langfristig mehr Ausgeglichenheit spüren willst, kann es hilfreich sein, auch mal aktivierendere Einheiten einzubauen."
        ],
        "match": {
            "title": "Yin",
            "reason": "passt zu dir, weil dein Körper nach Ruhe und Loslassen ruft – und Yin dir genau den Raum gibt."
        },
        "challenge": {
            "title": "Basic Kindness",
            "reason": "Du willst entspannen. Plot Twist: Entspannung wirkt auch durch Aktivität! Mit einer regelmäßigen leichten Praxis kannst du die nötige Kraft und Kondition dafür aufbauen."
        }
    }
}

# Add these to your ollama_dictionary_enhanced:
ollama_dictionary_enhanced = {
    # Multiple space patterns (exactly as they appear)
    "At me  tief  durch": "Atme tief durch",
    "At me  tief  ein": "Atme tief ein", 
    "ents pan ne": "entspanne",
    "At  me": "Atme",
    "at  me": "atme",
    "tief  durch": "tief durch",
    "tief  ein": "tief ein",
    "lass  los": "lass los",
    "genie ße": "genieße",
    "Best es": "Bestes",
    "inn ere": "innere",
    "konzent riere": "konzentriere",
    "Ent spann": "Entspann",
    "deinen  Körper": "deinen Körper",
    "die  Ruhe": "die Ruhe",
    "und  lass": "und lass",
    "du  bist": "du bist",
    "ganz  frei": "ganz frei",
    "ihren  Frieden": "ihren Frieden",
    "jeden  Schritt": "jeden Schritt",
    "dich  leicht": "dich leicht",
    "dein  Best es": "dein Bestes",
}
