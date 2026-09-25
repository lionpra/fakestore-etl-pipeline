# Fake Store ETL Pipeline

Dieses Projekt ist eine Python-basierte ETL-Pipeline (Extract, Transform, Load). Sie extrahiert Produkt- und Nutzerdaten von der Fake Store API, bereinigt diese mit Pandas und lädt sie anschließend automatisiert in eine PostgreSQL-Datenbank.

## Projektstruktur

* **`extract.py`**: Ruft Rohdaten über die Endpunkte `/products` und `/users` der `https://fakestoreapi.com` ab und speichert sie in DataFrames.
* **`transform.py`**: Bereinigt die Daten, passt Datentypen an und flacht verschachtelte JSON-Strukturen (wie Nutzeradressen) in flache Tabellenspalten ab.
* **`load.py`**: Nutzt SQLAlchemy, um die transformierten DataFrames in die Tabellen `products` und `users` der PostgreSQL-Datenbank `fake_store_db` zu schreiben.
* **`main.py`**: Das Hauptskript, das den gesamten ETL-Prozess orchestriert und ausführt.

## Voraussetzungen

* Python 3
* PostgreSQL-Datenbank
* Verwendete Python-Bibliotheken: `pandas`, `requests`, `SQLAlchemy`

## Installation & Setup

1. **Repository klonen:**
   ```bash
   git clone <deine-repo-url>
   cd <repo-ordner>
   ```

2. **Abhängigkeiten installieren:**
   ```bash
   pip install pandas requests sqlalchemy psycopg2-binary
   ```

3. **Datenbank konfigurieren:**
   * Stelle sicher, dass PostgreSQL lokal läuft.
   * Erstelle eine Datenbank namens `fake_store_db`.
   * Trage dein PostgreSQL-Passwort in der Datei `load.py` in der Variable `password` ein.

## Ausführung

Starte die Pipeline über das Hauptskript:

```bash
python main.py
```

Das Skript gibt den aktuellen Status (Start, Extracted, Transformed, Loaded) im Terminal aus.
