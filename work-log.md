# Work Log

**Student Name:** 

Instructions: Fill out one log for each course day. Content to consider: Course Sessions + Assignment

## Template:

---

## 1. ✅ What did I accomplish?

_Reflect on the activities, exercises, and work you completed today._

**Guiding questions:**
- What topics or concepts did you work with?
- What exercises or projects did you complete?
- What tools or technologies did you use?
- What did you learn or practice?



---

## 2. 🚧 What challenges did I face?

_Describe any difficulties, obstacles, or confusing moments you encountered._

**Guiding questions:**
- What was difficult to understand?
- Where did you get stuck?
- What errors or problems did you face?
- What felt frustrating or confusing?




---

## 3. 💡 How did I overcome them?

_Explain how you overcame the challenges or what help you needed._

**Guiding questions:**
- What strategies did you try?
- Who or what helped you (instructor, classmates, documentation)?
- What did you learn from solving the problem?
- What questions do you still have?


---

## Week 1

### Day 1

#### 1. ✅ What did I accomplish?
- Entwicklungsumgebung eingerichtet: Erfolgreiche Installation von Git, VS Code und dem Python-Paketmanager uv.
- Projekt-Setup: Ein neues Projektverzeichnis erstellt und die FastAPI-Bibliothek mittels uv add fastapi installiert.
- API-Entwicklung: Eine funktionierende Web-API mit insgesamt sechs Endpunkten erstellt (3 im Kurs erarbeitet, 3 als Hausaufgabe).
- Interaktive Dokumentation: Die automatische Dokumentation unter /docs genutzt, um die Endpunkte zu testen.
- Logik-Implementierung: Endpunkte mit Pfadparametern erstellt, um Berechnungen direkt über die URL durchzuführen.
---

#### 2. 🚧 What challenges did I face?
- Das Verständnis der FastAPI-Dekoratoren (z. B. @app.get("/")) und die korrekte Einrückung des Python-Codes.
- Sicherstellen, dass Pfadparameter wie {number} korrekt als Integer erkannt werden, damit Berechnungen funktionieren.
- Den API-Server über das Terminal (uv run fastapi dev) zu starten und bei Bedarf korrekt zu beenden oder neu zu laden.
---

#### 3. 💡 How did I overcome them?
- Bei Python-Fehlern im Terminal genau hingeschaut, da FastAPI sehr hilfreiche Fehlermeldungen zur Validierung liefert.
- Austausch mit Komiliton/-innen.
---

### Day 2

#### 1. ✅ What did I accomplish?
- Variablen, Datentypen (insb. Listen und Dictionaries), F-Strings und Funktionen mit Typ-Hinweisen (Type Hints) angewendet.
- Die Grundlagen von Request und Response gelernt sowie den Unterschied zwischen GET (Daten abrufen) und POST (Daten erstellen) verstanden.
- Eine API mit FastAPI zur Notizverwaltung aufgesetzt, inklusive automatischer Validierung über Pydantic-Modelle
- Hilfsfunktionen zum Laden und Speichern von Daten mittels json.load() und json.dump() geschrieben, sodass Notizen in einer notes.json-Datei dauerhaft gespeichert werden.
---

#### 2. 🚧 What challenges did I face?
- Sicherstellen, dass die ID in der URL (/notes/{note_id}) von FastAPI korrekt als Integer validiert und verarbeitet wird.
- Das Zusammenspiel und die Konvertierung zwischen Pydantic-Modellen, Python-Dictionaries und dem JSON-Format im Dateisystem durchschauen.
---

#### 3. 💡 How did I overcome them?
- Direktes Öffnen der generierten data/notes.json in VS Code, um visuell zu kontrollieren, ob das category-Feld und die IDs nach einem POST-Aufruf korrekt weggeschrieben wurden.
- Die Code-Snippets für das JSON-Handling Schritt für Schritt nachvollzogen.
---

### Day 3

#### 1. ✅ What did I accomplish?
- Gelernt, wie optionale und erforderliche Query-Parameter in FastAPI definiert werden, um Daten dynamisch zu filtern, ohne die URL-Struktur zu ändern.
- Endpunkte um Filter- (z. B. nach Kategorien oder Suchbegriffen) und Sortierfunktionen (z. B. nach Erstellungsdatum) erweitert.
- Eigene Fehlermeldungen mit HTTPException und den passenden Statuscodes (wie 400 Bad Request oder 404 Not Found) eingebaut, um Fehleingaben sauber abzufangen.
- Den bestehenden Code nach API-Best-Practices strukturiert, um die Lesbarkeit und Wartbarkeit der Anwendung zu erhöhen.
---

#### 2. 🚧 What challenges did I face?
- Die Logik im Python-Code so zu schreiben, dass mehrere optionale Query-Parameter reibungslos ineinandergreifen.
- Fehler abfangen, wenn User ungültige Sortier-Strings (z. B. sort=alles) übergeben
---

#### 3. 💡 How did I overcome them?
- Bei den Filter-Funktionen erst einen Parameter isoliert implementiert und getestet, bevor der nächste optionale Parameter per if-Bedingung hinzugefügt wurde.
- Query-Parametern sinnvolle Default-Werte zugewiesen (z. B. limit: int = 10), um zu verhindern, dass die API abstürzt, wenn der User den Parameter nicht explizit angibt.
---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?
- Gelernt, wie man Entitäten über IDs miteinander verknüpft (z. B. eine Notiz einem bestimmten Benutzer über eine user_id zuweisen).
- Fortgeschrittene Validierungsfeatures von Pydantic eingesetzt, um die Qualität der Eingabedaten zu erhöhen.
- Gelernt, wie man bestehende Daten aktualisiert – sowohl durch kompletten Austausch (PUT) als auch durch partielle Updates (PATCH).
- Einen Endpunkt erstellt, der alle Notizen filtert und zurückgibt, die zu einer bestimmten Benutzer-ID gehören.
- Validierungsfehler abgefangen und saubere Fehlermeldungen (z. B. wenn ein User versucht, eine Notiz für einen nicht existierenden Benutzer anzulegen) implementiert.
---

#### 2. 🚧 What challenges did I face?
- Die begriffliche und logische Unterscheidung zwischen der vollständigen Ersetzung eines Objekts (PUT) und dem Aktualisieren einzelner Felder (PATCH) sauber im Code umzusetzen.
- Die Logik so zu schreiben, dass bei einem partiellen Update nur die Felder geändert werden, die der User mitschickt, während die restlichen Daten unberührt bleiben.
- Sicherstellen, dass die App blockiert, wenn eine user_id übergeben wird, die in der Benutzerdatenbank gar nicht existiert.
---

#### 3. 💡 How did I overcome them?
- Vor dem Speichern einer Notiz eine Abfrage eingebaut, die prüft, ob der zugehörige User existiert, und andernfalls sofort einen 404 Not Found-Fehler wirft.
- Im /docs-Interface gezielt ausprobiert, was passiert, wenn man beim PATCH-Endpunkt Felder im JSON-Body weglässt, um zu verifizieren, dass die Persistenz in der .json-Datei korrekt arbeitet.
---

### Day 5

#### 1. ✅ What did I accomplish?
- Gelernt, wie JWTs aufgebaut sind (Header, Payload, Signature) und wie man mit pyjwt sichere Tokens generiert und abgelaufene Tokens validiert.
- Einen /token-Endpunkt erstellt, der Benutzeranmeldedaten entgegennimmt, prüft und bei Erfolg ein Access-Token zurückgibt.
- FastAPI-Abhängigkeiten genutzt, um Endpunkte abzusichern, sodass nur authentifizierte Benutzer mit einem gültigen Token darauf zugreifen können.
---

#### 2. 🚧 What challenges did I face?
- Zu verstehen, warum der Server das Token nicht im klassischen Sinne "speichern" muss, sondern es rein kryptografisch über den SECRET_KEY verifiziert.
- Fehler bei der Login-Logik, weil versucht wurde, den eingegebenen Klartext direkt mit dem gespeicherten Hash zu vergleichen, statt die dafür vorgesehene Verifizierungsfunktion zu nutzen.
- „Internal Server Error“ (Fehler 500) im Terminal aufgrund von Problemen mit der lokalen notes.json Datei.
---

#### 3. 💡 How did I overcome them?
- Schrittweises durcharbeiten der Präsentation zum besseren Nachvollziehen.
- Die eingebaute OAuth2-Schnittstelle von /docs verwendet, um mich direkt im Browser einzuloggen und das Token automatisch an alle geschützten Endpunkte mitsenden zu lassen.
- Fehlende Pakete nachinstalliert.
---

### Day 6

#### 1. ✅ What did I accomplish?
- Gelernt, wie Dekoratoren funktionieren, um das Verhalten von Funktionen zu verändern und Programmlogik von administrativen Aufgaben zu trennen.
- Praktische Erfahrungen gesammelt, indem ein eigener klassenbasierter Dekorator (class_based_decorator.py) geschrieben wurde.
- Das Hilfsmittel icecream via uv add icecream in das Projekt integriert, um Variablen und Funktionsaufrufe komfortabler loggen zu können.
- Eine offizielle, externe Referenz-Testdatei (test_main.py) in das eigene Repository eingebunden, um die gesamte API zu prüfen.
- Bestehende Endpunkte und Validierungen überarbeitet, um alle Anforderungen der neuen, strikten Test-Suite erfolgreich zu erfüllen.
---

#### 2. 🚧 What challenges did I face?
- Die Konfrontation mit einer Vielzahl von fehlschlagenden Tests beim ersten Ausführen der neuen test_main.py, da diese auch unentdeckte Edge Cases abprüfte.
- Die abstrakte Funktionsweise von Wrappern zu verstehen.
- Bei komplexen Testfällen den genauen Grund für einen Fehlschlag (z. B. einen falschen HTTP-Statuscode oder eine ungenaue Fehlermeldung) in den Log-Ausgaben zu isolieren.
---

#### 3. 💡 How did I overcome them?
- Die Test-Suite gezielt im Terminal aufgerufen und die Fehler systematisch einen nach dem anderen behoben.
- Mit dem icecream-Paket (ic()) Variablenzustände und Kontrollflüsse während der Testausführung transparent gemacht, anstatt unübersichtliche print()-Befehle zu nutzen.
- Den eigenen Code Schritt für Schritt mit den Mustervorlagen und Validierungsregeln der Vortage (z. B. Tag 5) abgeglichen, um die referenzielle Integrität der Endpunkte sicherzustellen.
---

## Week 3

### Day 7

#### 1. ✅ What did I accomplish?
- Das Framework Streamlit als einfache Methode kennengelernt, um als Backend-Entwickler schnell grafische Oberflächen (GUIs) zu bauen.
- Verstanden, wie man den st.session_state in Streamlit nutzt, um Daten und Zustände über mehrere Benutzerinteraktionen und Page-Reruns hinweg zu speichern.
- Eine frontend.py erstellt, die sich mit der eigenen Notes-API verbindet, um alle Notizen übersichtlich aufzulisten.
---

#### 2. 🚧 What challenges did I face?
- Zu verstehen, dass Streamlit bei jeder Interaktion das komplette Skript von oben nach unten neu ausführt, was ohne den Einsatz von session_state zum Verlust von Variableninhalten führt.
- Die korrekte Bündelung von mehreren Eingabefeldern (Textfelder, Dropdowns für Kategorien), damit die Daten erst gesammelt an die API geschickt werden, wenn der User den Absende-Button drückt.
- Fehler bei der Transformation der Streamlit-Eingaben in das exakte JSON-Format, das die FastAPI-Endpunkte erwarten.
---

#### 3. 💡 How did I overcome them?
- Durch den Einsatz von Streamlit-Formularen konnte der Kontrollfluss so gesteuert werden, dass die API-Anfrage erst nach vollständiger Eingabe aller Notiz-Details ausgelöst wird.
- Zwei übersichtliche Terminal-Fenster in VS Code nebeneinandergelegt, um die Log-Ausgaben des Backends und des Frontends parallel im Blick zu behalten.
- Die bestehende test_main.py und die API-Dokumentation analysiert, um sicherzustellen, dass die requests.post()-Befehle im Frontend genau die richtige Struktur an die Notes-API senden.
---

### Day 8

#### 1. ✅ What did I accomplish?
- Eine saubere, modulare Ordnerstruktur für das Projekt aufgebaut und die .gitignore anhand von standardisierten Community-Vorlagen finalisiert und manuell erweitert.
- Die Rolle der pyproject.toml als zentrales Werkzeug zur Verwaltung von Abhängigkeiten, Metadaten und Build-Konfigurationen verstanden, welches veraltete Formate ablöst.
- Eine standardisierte Projektdokumentation in Markdown erstellt, inklusive präziser Setup-Instruktionen (uv run...) und syntaktisch hervorgehobenen Code-Beispielen (Syntax Highlighting) für API-Requests.
---

#### 2. 🚧 What challenges did I face?
- Beim Wechsel von der dateibasierten Speicherung hin zu einer relationalen Datenbank (SQLModel/SQLite) wurde eine korrupte notes.db erzeugt, was zu Fehlern in der automatisierten Test-Suite führte.
- Verwirrung bei der UI-Integration, da über das Streamlit-Frontend erstellte Notizen scheinbar verzögert oder nicht unmittelbar in der Datenbank registriert wurden.
- Der lokale Backup-Ordner (bus/) verlor durch unstrukturierte Zwischenspeicherungen stark an Übersichtlichkeit.
---

#### 3. 💡 How did I overcome them?
- Den Code konsequent von Altlasten befreit, fehlerhafte Pfade isoliert und die API-Architektur auf die funktionalen Kernkomponenten reduziert.
- sqlmodel sauber als Abhängigkeit deklariert, die korrupte SQLite-Datei (notes.db) manuell gelöscht.
- Durch Verifikation der Einträge direkt in der SQLite-Datenbank sowie via interaktiver Swagger-Dokumentation (/docs) festgestellt, dass kein logischer Fehler vorlag, sondern ein kurzes Synchronisations- bzw. Cache-Verzögerungsfenster im Frontend vorlag.
- Vergleich und Austausch von Code mit Kommilitonen um Altlasten loszuwerden und eine bessere Struktur zu gewährleisten.
---

# 🎉 Congratulations! You did it! 🎓✨