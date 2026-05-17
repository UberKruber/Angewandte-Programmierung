# 📝 Notizen-Verwaltungssystem (API & UI)

Ein kompaktes und leistungsstarkes Python-Projekt, das eine moderne REST-Schnittstelle (FastAPI) zur strukturierten Ablage von Notizen mit einer interaktiven Weboberfläche (Streamlit) verbindet. Die Anwendung ermöglicht das einfache Verwalten, Filtern und Sortieren von Notizen über Kategorien und Schlagwörter (Tags).

---

## 📦 1. Komponenten des Repositories

### Kern-Dateien
* **`main.py`** — Das Anwendungs-Backend: Steuert die FastAPI-Routen, das relationale Datenbank-Setup via SQLModel sowie die SQLite-Integration.
* **`frontend.py`** — Das Anwendungs-Frontend: Eine übersichtliche Streamlit-Oberfläche, um Datensätze im Browser einzusehen, zu filtern und neue Einträge über Formulare zu erfassen.
* **`notes.db`** — Der lokale Datenspeicher: Eine relationale SQLite-Datenbankdatei, die sich beim Erststart selbstständig generiert.
* **`test_main.py`** — Die automatisierte Test-Suite (`pytest`), um die Integrität aller API-Endpunkte und Validierungsregeln sicherzustellen.
* **`work-log.md`** — Persönliches Arbeitsprotokoll zur lückenlosen Dokumentation des Lernfortschritts.

### Ordnerstruktur
* **`explorationen/`** — Archivordner mit früheren Entwürfen und experimentellen Testdateien aus der Entstehung des Projekts.
* **`presentationen/`** — Begleitendes Präsentations- und Anschauungsmaterial zu den einzelnen Kurstagen (Tag 1 bis 7).
* **`bus/`** — Lokale Sicherheitskopien und strukturierte Backups älterer Zwischenstände der Arbeit.

---


## 🛠️ 2. Systemanforderungen & Vorbereitung

* **Python:** Version 3.12 oder aktueller
* **Paketmanager:** `uv` zur effizienten Ausführung und deklarativen Verwaltung der Umgebung.

Um das Projekt mitsamt allen benötigten Bibliotheken (FastAPI, SQLModel, Streamlit, Pytest) aufzusetzen, genügt dieser Befehl im Projektordner:

"uv sync"

## 🚀 3. Ausführung des Systems

Das System besteht aus zwei Komponenten, die am besten parallel in zwei getrennten Terminal-Fenstern gestartet werden:

### 1. Backend (FastAPI) starten
Wechsle in das Projektverzeichnis und starte den Server im Entwicklungsmodus:

"uv run fastapi dev main.py"

Die interaktive, automatiche API-Dokumentation ist anschließend sofort unter http://127.0.0.1:8000/docs (Swagger UI) erreichbar.

### 2. Frontend (Streamlit) starten

Öffne ein zweites Terminal und starte die grafische Benutzeroberfläche:

"uv run streamlit run frontend.py"

Das Frontend öffnet sich automatisch im Standardbrowser unter http://localhost:8501.

### 3. Automatisierte Tests ausführen

Um die vollständige Funktionalität der API-Routen zu überprüfen, führe pytest aus:

"uv run pytest test_main.py -v"

## 🗺️ 4. API-Endpunkte (REST-Schnittstelle)

Die API implementiert ein vollständiges CRUD-Muster (Create, Read, Update, Delete):

| Methode | Pfad | Beschreibung |
| :--- | :--- | :--- |
| **`GET`** | `/` | Ruft Anwendungs-Metadaten (Titel, Version) ab. |
| **`POST`** | `/notes` | Erstellt eine neue Notiz (gibt HTTP 201 zurück). |
| **`GET`** | `/notes` | Listet alle Notizen auf (unterstützt Query-Filter wie `category`, `tag`, `search`). |
| **`GET`** | `/notes/{id}` | Ruft eine spezifische Notiz anhand ihrer ID ab. |
| **`PUT`** | `/notes/{id}` | Ersetzt eine bestehende Notiz vollständig. |
| **`PATCH`** | `/notes/{id}` | Aktualisiert Teilfelder einer Notiz (schont unübergebene Attribute). |
| **`DELETE`** | `/notes/{id}` | Löscht eine Notiz permanent aus der Datenbank. |
| **`GET`** | `/notes/stats` | Liefert statistische Auswertungen (Gesamtanzahl, Top-Tags, Verteilung). |
| **`GET`** | `/categories` | Listet alle aktuell genutzten, eindeutigen Kategorien auf. |
| **`GET`** | `/tags` | Listet alle aktuell registrierten, eindeutigen Tags sortiert auf. |

---

## 🛡️ 5. Datenvalidierung & Business-Logik

Das System setzt strikte Datenintegrität mithilfe von **Pydantic v2** und **SQLModel** um. Da relationale SQLite-Datenbanken native Listen nur schwer verarbeiten, werden Tags als serialisierte JSON-Strings (`tags_json`) abgelegt und beim API-Datentransfer vollautomatisch transformiert:

* **Titel (`title`):** Zwingend erforderlich; Textlänge muss zwischen `1` und `100` Zeichen liegen.
* **Inhalt (`content`):** Zwingend erforderlich; muss mindestens `1` Zeichen enthalten.
* **Kategorien (`category`):** Muss aus einer vordefinierten White-List stammen (`work`, `personal`, `school`, `ideas`, `general`). Eingaben werden automatisch in Kleinschreibung überführt (`.lower()`).
* **Tags (`tags`):**
  * Maximal `10` Schlagwörter pro Notiz erlaubt.
  * Jedes Tag muss mindestens `1` Zeichen lang sein.
  * Führende/nachfolgende Leerzeichen werden entfernt, alle Buchstaben werden kleingeschrieben.
  * Identische Stichwörter innerhalb eines Requests werden automatisch dedupliziert, wobei die ursprüngliche Reihenfolge erhalten bleibt.
* **Robuste Absicherung (`extra="forbid"`):** Das Senden nicht im Schema definierter Zusatzfelder im JSON-Body führt sofort zu einem clientseitigen Validierungsfehler (**HTTP 422 Unprocessable Entity**).

---

## 🔄 6. System zurücksetzen

Möchte man die Anwendung in den Auslieferungszustand versetzen, alte Testdaten verwerfen und alle gespeicherten Notizen löschen, reicht es aus, die lokale Datenbankdatei im Hauptverzeichnis zu entfernen:

# Unter Windows (PowerShell) oder Linux/macOS
"rm notes.db"