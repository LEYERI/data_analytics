# Week_03 schrittweise lösen

> Data Analytics: Wir müssen nun die Aufgabe "Week_03" lösen. wir lösen schritt von schritt und du erklärst mir alles genau was es tut, was es bedeuteut etc. damit ich es verstehe und ein profi bin und die prüfung bestehe

<details><summary>1 previous message</summary>

> Ich schaue zuerst nach den Unterlagen zu „Week_03“. Danach gehen wir die Aufgaben Schritt für Schritt durch: mit Erklärungen zu den Begriffen, dem Vorgehen und der Bedeutung der Ergebnisse.
</details>

Wir bearbeiten **Week_03 gemeinsam Schritt für Schritt**, damit du die Lösungen selbst erklären und ähnliche Aufgaben in der Prüfung lösen kannst.

Bei jeder Teilaufgabe besprechen wir:

1. **Was ist gefragt?** Wir übersetzen die Aufgabenstellung in verständliche Worte.
2. **Welche Grundlagen brauchst du?** Ich erkläre Begriffe und Formeln mit Beispielen.
3. **Wie lösen wir sie?** Wir gehen den Rechenweg oder Code durch und erklären jede wichtige Zeile.
4. **Was bedeutet das Ergebnis?** Wir interpretieren es und prüfen, ob es plausibel ist.
5. **Hast du es verstanden?** Mit einer kurzen Verständnisfrage festigen wir das Gelernte.


Wir beginnen mit **Aufgabe 1, Schritt 1: Bibliotheken laden und die Daten einlesen**. Öffne dafür `apartments_data_preparation_zuerich.ipynb` in VS Code. Wir bearbeiten zunächst nur die ersten beiden Codezellen.

Ein **Notebook** besteht aus Zellen: Textzellen erklären etwas, Codezellen führen Python aus. Mit **Shift + Enter** führst du die ausgewählte Zelle aus. Variablen bleiben danach im laufenden Python-Kernel gespeichert. Deshalb ist die Reihenfolge der Zellen wichtig.

Die erste Codezelle enthält:

```python
# Libraries
import os
import re
import fnmatch
import datetime
import numpy as np
import pandas as pd
```

Eine **Bibliothek** stellt fertige Funktionen bereit. Mit `import` machen wir sie in unserem Programm verfügbar.

| Code | Zweck |
|---|---|
| `import os` | Mit Ordnern und Dateipfaden arbeiten |
| `import re` | Muster in Text erkennen, etwa eine Zimmerzahl herauslesen |
| `import fnmatch` | Namen anhand von Mustern vergleichen |
| `import datetime` | Mit Datum und Uhrzeit arbeiten |
| `import numpy as np` | Numerische Berechnungen durchführen |
| `import pandas as pd` | Tabellen einlesen, bearbeiten und analysieren |

`as pd` vergibt einen Kurznamen. Wir können dadurch später `pd.read_csv(...)` schreiben. **`pd` ist also der Kurzname der Bibliothek, keine Tabelle.**

Danach steht:

```python
import warnings
warnings.filterwarnings("ignore")
```

Das blendet Warnungen aus. Warnungen weisen beispielsweise auf Funktionen hin, deren Verhalten sich künftig ändern könnte. **Fehlermeldungen werden dadurch nicht ausgeblendet.** Zum Lernen kann es sinnvoll sein, die zweite Zeile vorübergehend mit `#` auszukommentieren, damit du Warnungen siehst.

Zum Schluss:

```python
print(os.getcwd())
```

Von innen nach aussen gelesen:

1. `os.getcwd()` liefert den aktuellen Arbeitsordner.
2. `print(...)` zeigt diesen Pfad an.

Der Arbeitsordner ist wichtig, weil Python dort nach Dateien sucht, wenn wir nur einen Dateinamen angeben.

Die nächste Codezelle liest die Wohnungsdaten:

```python
df = pd.read_csv(
    'apartments_data_zuerich.csv',
    sep=',',
    encoding='utf-8'
)

df.shape
```

Die Zeilenumbrüche dienen hier nur der Lesbarkeit. Im Notebook steht derselbe Aufruf in einer Zeile.

- **`pd.read_csv(...)`** liest eine CSV-Datei als Tabelle ein.
- **`'apartments_data_zuerich.csv'`** ist der Dateiname. Ohne weiteren Pfad muss die Datei im aktuellen Arbeitsordner liegen.
- **`sep=','`** bedeutet: Kommas trennen die Spalten.
- **`encoding='utf-8'`** legt fest, wie Zeichen wie `ü` und `ä` gelesen werden.
- **`df = ...`** speichert die eingelesene Tabelle unter dem Namen `df`.

Diese Tabelle heisst in pandas **DataFrame**. Stell sie dir wie ein Excel-Tabellenblatt vor: Zeilen enthalten Beobachtungen, Spalten enthalten Merkmale. Hier entspricht eine Zeile einem Wohnungsinserat.

```python
df.shape
```

liefert die Form der Tabelle als **`(Anzahl Zeilen, Anzahl Spalten)`**. Die bereitgestellte CSV enthält 1’008 Datenzeilen und 7 Spalten. Erwartet wird deshalb:

```python
(1008, 7)
```

`shape` ist eine **Eigenschaft**, deshalb schreiben wir keine Klammern dahinter. `read_csv(...)` ist eine **Funktion**, die wir mit Klammern aufrufen. Im Notebook wird das Ergebnis des letzten Ausdrucks einer Codezelle automatisch angezeigt – deshalb braucht `df.shape` hier kein `print()`.

**Führe jetzt diese beiden Codezellen aus.** Welche Ausgabe bekommst du bei `df.shape`? Und zur Verständnisprüfung: Wofür steht die Zahl `7`?

> ich eerhalte fehlermeldung

Bitte kopiere die **vollständige Fehlermeldung** hier hinein oder sende einen Screenshot der Codezelle samt Fehlermeldung.

Sag auch kurz, welche Zelle du ausgeführt hast: die mit **`import os`** oder die mit **`pd.read_csv(...)`**. Dann erklären und beheben wir den Fehler gemeinsam.

> &#x20; \# Read the data to a pandas data frame\
> df = pd.read_csv('apartments_data_zuerich.csv', sep=',', encoding='utf-8')\
> \
> \# Get number of rows and columns\
> df.shape

Das ist der Code der Zelle. Für die Diagnose brauche ich noch die **Fehlermeldung, die nach dem Ausführen darunter erscheint**.

Kopiere bitte die Ausgabe von `Traceback` bis zur letzten Zeile hier hinein – oder sende einen Screenshot. Besonders die letzte Zeile zeigt meist die Ursache, beispielsweise `NameError` oder `FileNotFoundError`.

> was ist trtraceback?

**Traceback** ist der Fehlerbericht von Python. Er zeigt, **an welcher Stelle ein Fehler aufgetreten ist**.

Zum Beispiel:

```text
Traceback (most recent call last):
  ...
  df = pd.read_csv(...)

NameError: name 'pd' is not defined
```

Das bedeutet:

- **`Traceback ...`**: Hier beginnt der Fehlerbericht.
- **`df = pd.read_csv(...)`**: In dieser Codezeile ist der Fehler aufgetreten.
- **Die letzte Zeile** erklärt den Fehler. In diesem Beispiel kennt Python `pd` noch nicht, weil `import pandas as pd` zuvor nicht ausgeführt wurde.

Klicke auf deine Codezelle und drücke **Shift + Enter**. Falls darunter eine Fehlermeldung erscheint, kopiere sie hier hinein oder sende einen Screenshot. Dann schauen wir uns deinen konkreten Fehler an.

> ...
> *Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...*


```text
FileNotFoundError: [Errno 2] No such file or directory:
'apartments_data_zuerich.csv'
```

Dein `pd.read_csv(...)` wurde erkannt – pandas ist also bereits geladen. Der Fehler liegt beim **Dateipfad**.

Du hast das Notebook über die GitHub-Ansicht von VS Code geöffnet. Die dort sichtbaren Dateien stehen deinem lokalen Python nicht automatisch als lokale Dateien zur Verfügung. Ich habe die Daten inzwischen lokal bereitgestellt.

Ersetze deine Codezelle durch diesen Code und führe sie aus:

```python
# Wohnungsdaten über den vollständigen lokalen Dateipfad einlesen
df = pd.read_csv(
    '/tmp/data_analytics_week03/Week_03/apartments_data_zuerich.csv',
    sep=',',
    encoding='utf-8'
)

# Anzahl Zeilen und Spalten anzeigen
df.shape
```

Der Unterschied ist der **absolute Pfad**:

- `'apartments_data_zuerich.csv'` ist ein **relativer Pfad**: Python sucht ausgehend vom aktuellen Arbeitsordner.
- `'/tmp/data_analytics_week03/Week_03/apartments_data_zuerich.csv'` ist ein **absoluter Pfad**: Er gibt den vollständigen Speicherort an.

Erwartete Ausgabe:

```python
(1008, 7)
```

Das bedeutet **1’008 Wohnungsinserate und 7 Spalten**. Der Ordner `/tmp` ist eine vorübergehende Arbeitskopie; für die weitere Bearbeitung sollten wir das Projekt anschliessend dauerhaft lokal speichern.

Führe die geänderte Zelle aus und sag mir, welche Ausgabe erscheint.

> hat funktioniert, wo sind wir in der aufgabe nun?

Wir sind bei **Aufgabe 1, Teilpunkt 1**: Du sollst das Notebook `apartments_data_preparation_zuerich.ipynb` Schritt für Schritt ausführen und verstehen.

Bisher hast du:

- die Bibliotheken geladen, insbesondere **pandas** für die Tabellenbearbeitung;
- die CSV-Datei erfolgreich eingelesen und als DataFrame **`df`** gespeichert;
- mit **`df.shape`** die Anzahl der Zeilen und Spalten geprüft: **1’008 Inserate und 7 Spalten**.

Die zusätzlichen Variablen wie `furnished`, `balcony` und `central` kommen später. Zuerst verstehen wir die vorhandene Datenaufbereitung.

**Als Nächstes folgt diese Codezelle:**

```python
# Dimension (rows, columns)
print('Dimension:', df.shape)

# Number of rows
print('Number of rows:', df.shape[0])

# Number of columns
print('Number of columns:', df.shape[1])
```

`df.shape` liefert zwei Werte:

```python
(1008, 7)
```

Mit den eckigen Klammern greifen wir auf einen einzelnen Wert zu. **Python zählt Positionen ab 0:**

| Ausdruck | Bedeutung | Ergebnis |
|---|---|---|
| `df.shape` | Zeilen und Spalten | `(1008, 7)` |
| `df.shape[0]` | Erster Wert: Anzahl Zeilen | `1008` |
| `df.shape[1]` | Zweiter Wert: Anzahl Spalten | `7` |

`print('Number of rows:', df.shape[0])` zeigt einen erklärenden Text und den berechneten Wert zusammen an. Die Ausgabe sollte so aussehen:

```text
Dimension: (1008, 7)
Number of rows: 1008
Number of columns: 7
```

**Führe diese Zelle aus.** Zur Verständnisprüfung: Was würde deiner Meinung nach bei `df.shape[2]` passieren?

> dritter wert?

Ja, **`[2]` würde auf den dritten Wert zugreifen** – die Zählweise hast du richtig verstanden:

```text
Position:    0     1
Wert:      1008    7
```

Aber `df.shape` enthält hier **nur zwei Werte**, weil unsere Tabelle zwei Dimensionen hat: Zeilen und Spalten. Ein dritter Wert existiert nicht.

Deshalb verursacht:

```python
df.shape[2]
```

diesen Fehler:

```text
IndexError: tuple index out of range
```

Das bedeutet: **Du greifst auf eine Position zu, die es nicht gibt.**

Merksatz für die Prüfung: Bei **n Elementen** reichen die Positionen von **0 bis n − 1**. Bei zwei Elementen also von `0` bis `1`.

> weiter

Die nächste Zelle zeigt uns die **Datentypen der Spalten**:

```python
df.dtypes
```

- `df` ist unsere Tabelle.
- `.dtypes` zeigt für jede Spalte, als welchen Datentyp pandas ihre Werte gespeichert hat.
- Es braucht keine Klammern, weil `dtypes` eine Eigenschaft der Tabelle ist.

Ein Datentyp bestimmt, **wie Python Werte behandelt**:

| Datentyp | Bedeutung | Beispiel |
|---|---|---|
| `int64` | Ganze Zahl | `3` Zimmer |
| `float64` | Zahl mit möglichen Nachkommastellen | `3.5` Zimmer |
| `object` | Häufig Text; kann auch gemischte Werte enthalten | `"3.5 Zimmer, 80 m²"` |
| `bool` | Wahrheitswert | `True` oder `False` |

Warum ist das wichtig? **Eine Zahl als Text lässt sich nicht unmittelbar wie eine Zahl berechnen.**

```python
"100" + "200"   # ergibt "100200": Texte werden verbunden
100 + 200       # ergibt 300: Zahlen werden addiert
```

Unsere Daten stammen aus **Web Scraping**, also dem automatischen Auslesen einer Website. Deshalb können Zahlen noch in Texten stecken, beispielsweise:

```text
"3.5 Zimmer, 80 m²"
```

Für Berechnungen müssen wir daraus später getrennte numerische Werte für Zimmerzahl und Fläche gewinnen.

**Führe jetzt `df.dtypes` aus und schicke mir die Ausgabe.** Dann erklären wir die Datentypen deiner tatsächlichen Spalten.

> web-scraper-order        object\
> web-scraper-start-url    object\
> rooms_area_price_raw     object\
> address_raw              object\
> price_raw                object\
> description_raw          object\
> text_raw                 object\
> dtype: object

**Alle sieben Spalten haben aktuell den Datentyp `object`.** Bei unseren Rohdaten sind das Textspalten.

| Spalte | Bedeutung |
|---|---|
| `web-scraper-order` | Kennung aus dem Scraping-Vorgang |
| `web-scraper-start-url` | Ausgangsadresse der abgefragten Website |
| `rooms_area_price_raw` | Rohtext mit Angaben zu Zimmern, Fläche und Preis |
| `address_raw` | Adresse als Rohtext |
| `price_raw` | Preis als Rohtext |
| `description_raw` | Beschreibung des Inserats |
| `text_raw` | Weiterer ausgelesener Inseratstext |

**`raw` bedeutet „roh“:** Die Inhalte wurden noch nicht für die Analyse aufbereitet. Selbst ein Preis kann als Text gespeichert sein, etwa `"CHF 2'500"`. Daraus müssen wir erst die Zahl `2500` machen, bevor wir zuverlässig einen Durchschnitt berechnen können.

Die letzte Zeile:

```text
dtype: object
```

bezieht sich auf die ausgegebene **Liste der Datentypen**. Sie ist keine achte Spalte.

Als Nächstes werden wir die **Zimmerzahl aus dem Rohtext extrahieren**. Schauen wir uns vorher die tatsächlichen Inhalte an. Füge direkt vor dem Abschnitt **„Extract number of rooms“** eine Codezelle ein und führe sie aus:

```python
df['rooms_area_price_raw'].head(5)
```

Das bedeutet:

- **`df['rooms_area_price_raw']`** wählt diese eine Spalte aus. Eine einzelne pandas-Spalte heisst **Series**.
- **`.head(5)`** zeigt ihre ersten fünf Einträge. Das ist ein Funktionsaufruf, deshalb stehen hier Klammern.
- Die Tabelle wird dabei nur angezeigt, nicht verändert.

Schicke mir die Ausgabe. Dann können wir am echten Text nachvollziehen, wie der nächste Code die Zimmerzahl herausliest.

> [/](https://vscode-vfs+github-002b7b2276223a312c22726566223a7b2274797065223a342c226964223a226d6173746572227d7d.vscode-resource.vscode-cdn.net/)&#x20;
> (1008, 7)
> Dimension: (1008, 7) Number of rows: 1008 Number of columns: 7&#x20;
> web-scraper-order        object web-scraper-start-url    object rooms_area_price_raw     object address_raw              object price_raw                object description_raw          object text_raw                 object dtype: object
> 0      3 Zimmer, 49 m², CHF 1441.— 1    3,5 Zimmer, 65 m², CHF 1850.— 2                19 m², CHF 2686.— 3      2 Zimmer, 54 m², CHF 4853.— 4      2 Zimmer, 49 m², CHF 4335.— Name: rooms_area_price_raw, dtype: object   0    3.0 1    3.5 2    NaN 3    2.0 4    2.0 Name: rooms, dtype: float64  &#x20;
> 0      3 Zimmer, 49 m², CHF 1441.— 1    3,5 Zimmer, 65 m², CHF 1850.— 2                19 m², CHF 2686.— 3      2 Zimmer, 54 m², CHF 4853.— 4      2 Zimmer, 49 m², CHF 4335.— Name: rooms_area_price_raw, dtype: object

Du hast bereits auch die Zelle **„Extract number of rooms“** ausgeführt. Sie hat aus dem Rohtext eine neue numerische Spalte `rooms` erstellt:

| Rohtext | Extrahierte Zimmerzahl |
|---|---:|
| `3 Zimmer, 49 m², CHF 1441.—` | `3.0` |
| `3,5 Zimmer, 65 m², CHF 1850.—` | `3.5` |
| `19 m², CHF 2686.—` | `NaN` |
| `2 Zimmer, 54 m², CHF 4853.—` | `2.0` |

Schauen wir uns genau an, wie der Code das erreicht:

```python
rooms = []
```

Das erstellt eine **leere Liste**. Darin sammeln wir die Zimmerzahlen.

```python
for i in df['rooms_area_price_raw']:
```

Die **Schleife** geht jeden Eintrag der Spalte durch. `i` enthält jeweils den aktuellen Text, beispielsweise:

```python
"3,5 Zimmer, 65 m², CHF 1850.—"
```

Dann folgt:

```python
d1 = re.findall('(.*)Zimmer', i)
```

`re.findall(...)` sucht mithilfe eines **regulären Ausdrucks**, kurz **Regex**, nach einem Textmuster:

- `Zimmer` sucht das Wort „Zimmer“.
- `.` steht für ein beliebiges Zeichen, ausser einem Zeilenumbruch.
- `*` bedeutet „nullmal oder beliebig oft“.
- `(…)` legt fest, welchen Teil wir als Ergebnis erhalten.

Hier bekommen wir den Text **vor „Zimmer“** als Liste:

```python
['3,5 ']
```

Danach wird das Ergebnis bereinigt:

```python
try:
    d2 = d1[0].strip().replace(',', '.')
except:
    d2 = None
```

Für unser Beispiel passiert Folgendes:

```python
d1[0]                 # '3,5 ' — erster gefundener Wert
.strip()              # '3,5'  — Leerzeichen am Rand entfernen
.replace(',', '.')    # '3.5'  — Komma durch Punkt ersetzen
```

Python benötigt bei der späteren Umwandlung in eine Zahl den **Dezimalpunkt**.

**Was passiert beim dritten Inserat?**

```text
19 m², CHF 2686.—
```

Darin steht kein „Zimmer“. `findall` liefert deshalb eine leere Liste `[]`. Der Zugriff auf `d1[0]` verursacht einen Fehler. `except` fängt diesen ab und setzt `d2` auf `None`, also einen fehlenden Wert.

```python
rooms.append(d2)
```

Das hängt das aktuelle Ergebnis an die Liste an. Nach den ersten fünf Inseraten enthält sie:

```python
['3', '3.5', None, '2', '2']
```

Zum Schluss:

```python
df['rooms'] = pd.Series(rooms, dtype="float64")
```

Diese Zeile:

1. erstellt aus der Liste eine pandas-Spalte;
2. wandelt die Texte in Zahlen vom Typ `float64` um;
3. speichert die Spalte unter dem Namen `rooms` in `df`.

Dabei wird `None` zu **`NaN`**, einem Marker für einen fehlenden numerischen Wert.

**Wichtig für die Interpretation:** `NaN` bedeutet hier „Zimmerzahl nicht aus dem Text ermittelbar“. Es bedeutet **nicht null Zimmer**. Auch `3.0` bedeutet einfach drei Zimmer – die Nachkommastelle entsteht durch den Zahlentyp `float64`.

Kurze Verständnisfrage: **Warum wäre es problematisch, die fehlende Zimmerzahl einfach durch `0` zu ersetzen, wenn wir später die durchschnittliche Zimmerzahl berechnen?**

> weil 0 nicht existiert?

Ja, du meinst das Richtige: **Die `0` steht nicht in den Daten – wir würden sie erfinden.** Wir wissen beim dritten Inserat nicht, wie viele Zimmer es hat.

Eine `0` würde bei der Durchschnittsberechnung mitgezählt und das Ergebnis nach unten verzerren:

```text
Bekannte Zimmerzahlen:       3, 3.5, 2, 2
Durchschnitt:                10.5 / 4 = 2.625

Fehlenden Wert durch 0 ersetzen:
                             3, 3.5, 0, 2, 2
Durchschnitt:                10.5 / 5 = 2.1
```

**`NaN` bedeutet „unbekannt“, `0` ist ein konkreter Zahlenwert.** Deshalb behalten wir hier `NaN`. pandas lässt fehlende Werte bei `df['rooms'].mean()` standardmässig aus und berechnet den Durchschnitt aus den bekannten Zimmerzahlen.

> weiter mit aufgabe

<details><summary>2 previous messages</summary>

> Ich schaue mir die nächste Codezelle an, damit wir genau in der Reihenfolge deines Notebooks weitermachen.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> p='/tmp/data_analytics_week03/Week_03/apartments_data_preparation_zuerich.ipynb'
> n=json.load(open(p))
> for i,c in enumerate(n['cells'][12:18],12):
>  print('CELL',i,c['cell_type']);print(''.join(c['source']))
> PY`
>
> </details>
</details>

Als Nächstes kommt **„Extract living area“**: Wir extrahieren die **Wohnfläche in Quadratmetern** und speichern sie als Zahl in der neuen Spalte `area`.

Führe diese vorhandene Zelle aus:

```python
# Wohnfläche aus dem Rohtext extrahieren
area = []

for i in df['rooms_area_price_raw']:
    d1 = re.findall('Zimmer, (.*)m²', i)

    try:
        d2 = d1[0].strip()
    except:
        d2 = None

    area.append(d2)

# Als numerische Spalte speichern
df['area'] = pd.Series(area, dtype="float64")

# Erste fünf Rohtexte und Ergebnisse anzeigen
print(df['rooms_area_price_raw'].head(5), '\n')
print(df['area'].head(5), '\n')
```

Der Ablauf ist derselbe wie bei der Zimmerzahl: **leere Liste erstellen → Texte durchlaufen → Wert suchen → bereinigen → sammeln → als Zahl speichern**.

Neu ist vor allem das Suchmuster:

```python
'Zimmer, (.*)m²'
```

Es sucht nach dem Text **zwischen `Zimmer, ` und `m²`**:

```text
3 Zimmer, 49 m², CHF 1441.—
          ↑
     gesuchter Teil
```

Für dieses Inserat ergibt sich:

```python
d1 = ['49 ']        # Ergebnis der Suche
d2 = '49'           # Nach .strip(): ohne Leerzeichen
```

Beim Erstellen der Spalte wandelt `dtype="float64"` den Text `'49'` in die Zahl `49.0` um. Damit können wir später beispielsweise die durchschnittliche Wohnfläche berechnen.

**Das vorhandene Suchmuster hat allerdings eine Schwäche.** Beim dritten Inserat steht:

```text
19 m², CHF 2686.—
```

Die Fläche ist vorhanden, aber das Wort `Zimmer` fehlt. Weil unser Muster ausdrücklich `Zimmer, ` voraussetzt, findet es die `19` nicht. Daher erwarten wir:

```text
0    49.0
1    65.0
2     NaN
3    54.0
4    49.0
Name: area, dtype: float64
```

Hier entsteht der fehlende Wert also **durch ein zu enges Suchmuster**, obwohl die Information im Rohtext vorhanden ist. Das ist ein wichtiger Unterschied zur tatsächlich fehlenden Zimmerzahl.

Die letzten beiden `print(...)`-Zeilen zeigen Rohtexte und Ergebnisse zum Vergleichen an. **`'\n'` erzeugt dabei einen Zeilenumbruch.**

Führe die Zelle aus. Erhältst du ebenfalls `NaN` beim dritten Inserat?

> ja, also bei zahl 2

Genau: **Index `2` bezeichnet das dritte Inserat**, weil Python bei `0` beginnt.

Hier ist die Fläche `19 m²` vorhanden. Unser Suchmuster übersieht sie, weil es zusätzlich `Zimmer, ` verlangt.

Wir verbessern deshalb diese Zeile in der Flächen-Zelle:

```python
d1 = re.findall('Zimmer, (.*)m²', i)
```

Ersetze sie durch:

```python
d1 = re.findall(r'(\d+(?:[.,]\d+)?)\s*m²', i)
```

Das neue Muster sucht **eine Zahl direkt vor `m²`**, unabhängig davon, ob davor eine Zimmerzahl steht:

| Bestandteil | Bedeutung |
|---|---|
| `\d+` | Eine oder mehrere Ziffern, etwa `19` |
| `(?:[.,]\d+)?` | Optionaler Dezimalteil, etwa `,5` oder `.5` |
| `(...)` | Die Zahl als Ergebnis herausgeben |
| `\s*` | Beliebig viele Leerzeichen, auch keines |
| `m²` | Die Einheit, die nach der Zahl stehen muss |

Das `r` vor den Anführungszeichen kennzeichnet einen **Raw String**. Damit werden die Backslashes für das Regex-Muster unverändert weitergegeben.

Damit auch Flächen mit Dezimalkomma in Zahlen umgewandelt werden können, ändere zusätzlich:

```python
d2 = d1[0].strip()
```

zu:

```python
d2 = d1[0].strip().replace(',', '.')
```

**Führe danach die gesamte Flächen-Zelle erneut aus.** Die ersten fünf Flächen sollten jetzt so aussehen:

```text
0    49.0
1    65.0
2    19.0
3    54.0
4    49.0
```

Damit haben wir einen Fehler in der Datenaufbereitung behoben: Eine vorhandene Fläche wird jetzt korrekt erkannt.

> wird das in der aufgabenstellung verlangt?

**Nein, diese Änderung wird nicht ausdrücklich verlangt.** Das war ein zusätzlicher Verbesserungsvorschlag von mir; ich hätte ihn klar als optional kennzeichnen sollen.

In **Aufgabe 1, Teilpunkt 1** sollst du das vorhandene Notebook ausführen und verstehen. Dafür reicht hier zu erkennen: Das ursprüngliche Suchmuster erzeugt beim dritten Inserat `NaN`, weil es `Zimmer, ` voraussetzt.

Die ausdrücklich geforderten Ergänzungen kommen später:

- binäre Variablen **`furnished`**, **`balcony`** und **`central`** erstellen;
- aus **`price_per_m2`** eine Kategorie mit **`low`**, **`medium`** und **`high`** bilden.

Wir bleiben ab jetzt beim geforderten Ablauf und kennzeichnen zusätzliche Verbesserungen als optional. Als Nächstes folgt **„Extract rental price“**, also das Extrahieren des Mietpreises.

:codex-file-citation{path="/tmp/data_analytics_week03/Week_03/Excercises_Week_03.pdf" purpose="source"}

> nein, dann bitte genau die afugaben durchgehen

Wir bleiben genau bei der Aufgabenstellung. **Aufgabe 1, Teilpunkt 1** verlangt weiterhin, das vorhandene Notebook auszuführen und zu verstehen. Wir ändern den vorgegebenen Code dabei nicht.

Als Nächstes folgt **„Extract rental price“** – den Mietpreis aus dem Rohtext herauslesen:

```python
# Extract values from 'price_raw' strings
price = []
for i in df['price_raw']:
    d1 = re.findall('[0-9]+', i)
    try:
        d2 = d1[0].strip()
    except:
        d2 = None
    price.append(d2)

# Save as new variable in the pandas data frame
df['price'] = pd.Series(price, dtype="float64")

# Print first 5 values
print(df['price_raw'].head(), '\n')
print(df['price'].head())
```

Der Ablauf ist dir bereits bekannt:

1. **`price = []`** erstellt eine leere Liste für die Preise.
2. **`for i in df['price_raw']:`** geht jeden Text der Spalte `price_raw` durch.
3. **`re.findall('[0-9]+', i)`** sucht zusammenhängende Ziffernfolgen. `[0-9]` bedeutet „eine Ziffer“, `+` bedeutet „mindestens einmal“.
4. **`d1[0].strip()`** nimmt den ersten Treffer und entfernt Leerzeichen an den Rändern.
5. Falls kein Treffer existiert, setzt **`except`** den Wert auf `None`.
6. **`price.append(d2)`** fügt das Ergebnis der Liste hinzu.

Zum Beispiel würde die Suche bei diesem Text:

```text
CHF 1441.—
```

die Liste `['1441']` liefern.

Diese Zeile erstellt anschliessend die numerische Preisspalte:

```python
df['price'] = pd.Series(price, dtype="float64")
```

Aus dem Text `'1441'` wird die Zahl `1441.0`. Fehlende Werte werden als `NaN` gespeichert.

Die letzten beiden Zeilen zeigen die ersten fünf **Rohwerte und extrahierten Preise** an, damit wir sie vergleichen können. `.head()` zeigt ohne Zahl in den Klammern standardmässig fünf Einträge.

**Führe die vorhandene Zelle „Extract rental price“ aus und schicke mir die Ausgabe.**

> 0    CHF 1441.—\
> 1    CHF 1850.—\
> 2    CHF 2686.—\
> 3    CHF 4853.—\
> 4    CHF 4335.—\
> Name: price_raw, dtype: object \
> \
> 0    1441.0\
> 1    1850.0\
> 2    2686.0\
> 3    4853.0\
> 4    4335.0\
> Name: price, dtype: float64

<details><summary>2 previous messages</summary>

> Ich prüfe den nächsten Abschnitt im Notebook, damit wir genau beim vorgegebenen Ablauf bleiben.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> with open('/tmp/data_analytics_week03/Week_03/apartments_data_preparation_zuerich.ipynb') as f: n=json.load(f)
> for i,c in enumerate(n['cells'][16:23],16):
>  print('CELL',i,c['cell_type']); print(''.join(c['source']))
> PY`
>
> </details>
</details>

**Die Preise wurden für diese fünf Inserate korrekt extrahiert.** Aus dem Text `CHF 1441.—` wurde beispielsweise die Zahl `1441.0`.

Du siehst auch den Wechsel des Datentyps:

- `price_raw`: **`object`**, also hier Text.
- `price`: **`float64`**, also Zahlen, mit denen wir rechnen können.

Nun folgt im Notebook **„Change strings … to uppercase“**. Wir bleiben bei **Aufgabe 1, Teilpunkt 1** und führen den vorhandenen Code aus:

```python
# Change strings to uppercase
df['description_raw'] = df['description_raw'].str.upper()
print(df['description_raw'].head(10), '\n')

df['text_raw'] = df['text_raw'].str.upper()
print(df['text_raw'].head(10))
```

Die erste Zeile lässt sich von rechts nach links lesen:

```python
df['description_raw'].str.upper()
```

- **`df['description_raw']`** wählt die Beschreibungsspalte aus.
- **`.str`** stellt Textfunktionen für die Werte dieser Spalte bereit.
- **`.upper()`** wandelt die Texte in Grossbuchstaben um.

Beispiel:

```text
Helle Wohnung mit Seesicht
```

wird zu:

```text
HELLE WOHNUNG MIT SEESICHT
```

Durch die Zuweisung:

```python
df['description_raw'] = ...
```

**überschreiben wir die bestehende Spalte im DataFrame** mit den umgewandelten Texten. Die CSV-Datei auf der Festplatte wird dadurch nicht verändert.

Dasselbe passiert danach mit `text_raw`. Die beiden `print(...)`-Zeilen zeigen jeweils die ersten zehn Einträge.

**Warum machen wir das?** Später suchen wir nach bestimmten Wörtern. Durch die einheitliche Grossschreibung können wir beispielsweise `SEESICHT` finden, unabhängig davon, ob im ursprünglichen Text `Seesicht`, `seesicht` oder `SEESICHT` stand.

Führe diese Zelle aus. Die angezeigten Texte sollten danach in Grossbuchstaben stehen.

> ja

Als Nächstes folgt **„Calculate length of strings“**: Wir zählen die Zeichen in den Texten.

Führe die nächste vorhandene Zelle aus:

```python
# Show first item of variable 'description_raw'
print(df['description_raw'][0])

# Length of the strings in 'description_raw'
df['description_raw_len'] = df['description_raw'].str.len()
print(df['description_raw_len'], '\n')

# Show first item of variable 'text_raw'
print(df['text_raw'][0])

# Length of the strings in 'text_raw'
df['text_raw_len'] = df['text_raw'].str.len()
print(df['text_raw_len'])
```

Die erste Zeile:

```python
print(df['description_raw'][0])
```

zeigt den Beschreibungstext des Inserats mit dem **Index `0`** an – in unseren Daten das erste Inserat.

Danach:

```python
df['description_raw_len'] = df['description_raw'].str.len()
```

- **`.str.len()`** zählt für jeden Text die Zeichen.
- Buchstaben, Zahlen, Leerzeichen und Satzzeichen zählen mit.
- Das Ergebnis wird in der neuen Spalte **`description_raw_len`** gespeichert.

Beispiel:

```text
Text:    HELLE WOHNUNG
Länge:   13
```

Das sind fünf Buchstaben, ein Leerzeichen und sieben weitere Buchstaben. **Wir zählen Zeichen, nicht Wörter.**

Der zweite Teil macht dasselbe für `text_raw` und erstellt die Spalte **`text_raw_len`**.

Damit besitzt jedes Inserat nun zwei zusätzliche Merkmale: die Länge seiner Beschreibung und die Länge seines weiteren Inseratstextes. Das kann beispielsweise helfen, sehr kurze oder leere Texte zu erkennen.

Führe die Zelle aus. Danach kommen wir zum vorgegebenen Beispiel **`luxurious`**, auf dem deine eigenen Variablen aufbauen.

> weiter

Nun kommen wir zu **Aufgabe 1, Teilpunkt 2**: das Beispiel für die binäre Variable **`luxurious`** verstehen.

**Binär** bedeutet, dass eine Variable zwei mögliche Werte hat: hier `0` und `1`.

Führe die vorhandene Zelle aus:

```python
# Create a pattern which can be used to search the variable 'description_raw'
pattern = 'LOFT|SEESICHT'

# Create new variable 'luxurious' as binary dummy (0/1) variable
df['luxurious'] = df['description_raw'].str.contains(pat=pattern).astype(int)
print(df['luxurious'].sum())

# Show values
df[['description_raw', 'rooms', 'area', 'price', 'luxurious']]
```

Zuerst legen wir das **Suchmuster** fest:

```python
pattern = 'LOFT|SEESICHT'
```

Das Zeichen **`|` bedeutet in diesem Regex-Muster „oder“**. Wir suchen also nach `LOFT` oder `SEESICHT`. Dafür war die vorherige Umwandlung in Grossbuchstaben hilfreich.

Danach prüft:

```python
df['description_raw'].str.contains(pat=pattern)
```

für jede Beschreibung, ob mindestens einer der beiden Begriffe enthalten ist. `pat=pattern` übergibt unser Suchmuster an die Funktion.

Das Ergebnis besteht zunächst aus Wahrheitswerten:

| Beschreibung | Treffer |
|---|---|
| `MODERNE LOFTWOHNUNG` | `True` |
| `WOHNUNG MIT SEESICHT` | `True` |
| `HELLE WOHNUNG MIT BALKON` | `False` |

Auch `LOFTWOHNUNG` wird gefunden, weil `LOFT` darin als Teil des Textes vorkommt.

Mit:

```python
.astype(int)
```

wandeln wir diese Wahrheitswerte in ganze Zahlen um:

```text
True  → 1
False → 0
```

Die Zuweisung speichert sie in der neuen Spalte `luxurious`.

**Die Bedeutung ist also genau:**

- **`1`**: Die Beschreibung enthält `LOFT` oder `SEESICHT`.
- **`0`**: Keiner der beiden Begriffe wurde gefunden.

Das ist eine vereinfachte Definition von „luxuriös“ für diese Übung. Eine `0` beweist deshalb nicht, dass eine Wohnung keinen Luxus bietet.

Anschliessend zählt:

```python
print(df['luxurious'].sum())
```

die Treffer. Da jeder Treffer `1` und jeder andere Eintrag `0` beiträgt, ist die **Summe gleich der Anzahl der Inserate mit Treffer**.

Die letzte Zeile zeigt fünf ausgewählte Spalten nebeneinander. Die **doppelten eckigen Klammern** bedeuten hier: Wir wählen eine Liste mehrerer Spalten aus.

**Führe die Zelle aus und schicke mir die ausgegebene Anzahl.** Danach bearbeiten wir Teilpunkt 3 und erstellen die ausdrücklich verlangten Variablen.

> |      |                               **description_raw** | **rooms** | **area** | **price** | **luxurious** |
> | ---: | ------------------------------------------------: | --------: | -------: | --------: | ------------: |
> |    0 |                    «GEMÜTLICHE WOHNUNG IM GRÜNEN» |       3.0 |     49.0 |    1441.0 |             0 |
> |    1 |     «ATTRAKTIVE 3.5-ZIMMER-EG-WOHNUNG IN NEERACH» |       3.5 |     65.0 |    1850.0 |             0 |
> |    2 |                 «STUDIO APARTMENT JUNIOR BALCONY» |       NaN |      NaN |    2686.0 |             0 |
> |    3 |              «2 BEDROOM APARTMENT SENIOR BALCONY» |       2.0 |     54.0 |    4853.0 |             0 |
> |    4 |              «2 BEDROOM APARTMENT JUNIOR TERRACE» |       2.0 |     49.0 |    4335.0 |             0 |
> |  ... |                                               ... |       ... |      ... |       ... |           ... |
> | 1003 |   «CHARMANTE WOHNUNG IN HOTTINGEN, NÄHE RÖMERHOF» |       3.5 |     82.0 |    2830.0 |             0 |
> | 1004 |   «HEIMELIGE 4-ZIMMER-WOHNUNG IN WINTERTHUR-HEGI» |       4.0 |     73.0 |    1713.0 |             0 |
> | 1005 | «EXKLUSIVE WOHNUNG FÜR HÖCHSTE ANSPRÜCHE - MIT... |       4.5 |    110.0 |    3500.0 |             1 |
> | 1006 |                 «MODERNE WOHNUNG AN RUHIGER LAGE» |       3.0 |     68.0 |    1650.0 |             0 |
> | 1007 |          «QUARTIERLEBEN DIREKT VOR DER HAUSTÜRE!» |       4.5 |    114.0 |    3262.0 |             0 |
>
> 1008 rows × 5 columns

Die neue Spalte **`luxurious`** ist vorhanden. Bei Index `1005` wurde ein Suchbegriff gefunden, deshalb steht dort `1`. Die Anzeige ist gekürzt; mit `...` lässt pandas mittlere Zeilen und lange Texte weg.

Jetzt folgt **Aufgabe 1, Teilpunkt 3**: Erstelle nach diesem Beispiel die drei binären Variablen:

| Variable | Bedeutung | Deutscher Suchbegriff |
|---|---|---|
| `furnished` | möbliert | `MÖBLIERT` |
| `balcony` | Balkon | `BALKON` |
| `central` | zentral gelegen | `ZENTRAL` |

Füge **direkt unter dem Beispiel zu `luxurious` eine neue Codezelle** ein:

```python
# Möblierung anhand der Beschreibung erkennen
df['furnished'] = (
    df['description_raw']
    .str.contains('MÖBLIERT')
    .astype(int)
)

# Balkon anhand der Beschreibung erkennen
df['balcony'] = (
    df['description_raw']
    .str.contains('BALKON')
    .astype(int)
)

# Zentrale Lage anhand der Beschreibung erkennen
df['central'] = (
    df['description_raw']
    .str.contains('ZENTRAL')
    .astype(int)
)

# Anzahl der Treffer je Merkmal anzeigen
print(df[['furnished', 'balcony', 'central']].sum())

# Beschreibungen und neue Variablen vergleichen
df[['description_raw', 'furnished', 'balcony', 'central']].head(10)
```

Die Zeilenumbrüche innerhalb der runden Klammern machen den Code lesbarer. Die Verarbeitung funktioniert genauso wie beim Beispiel:

```text
Beschreibung → Suchbegriff enthalten? → True/False → 1/0
```

`ZENTRAL` findet beispielsweise auch **`ZENTRALE LAGE`**, weil es darin enthalten ist.

**Wichtig für die Interpretation:** Wir erfassen Texttreffer. Eine `0` bei `balcony` bedeutet „BALKON nicht in dieser Beschreibung gefunden“. Sie beweist nicht, dass die Wohnung keinen Balkon hat. Auch Verneinungen wie „nicht möbliert“ würde die einfache Suche als Treffer zählen.

Die Aufgabenstellung verlangt deutsche Suchbegriffe. Daher verwenden wir hier `BALKON`; das englische `BALCONY` in deinen angezeigten Inseraten wird damit nicht erfasst.

**Führe die neue Zelle aus und schicke mir die drei Trefferzahlen.**

> furnished    38\
> balcony      40\
> central      70\
> dtype: int64

Damit ist **Aufgabe 1, Teilpunkt 3 erledigt**. Die drei neuen Variablen liefern:

| Variable | Anzahl der Inserate mit Texttreffer |
|---|---:|
| `furnished` | 38 |
| `balcony` | 40 |
| `central` | 70 |

Die Zahlen zählen jeweils die **Einsen** in der Spalte. Ein Inserat kann mehrere Merkmale haben und daher in mehreren dieser Zahlen enthalten sein.

**`dtype: int64`** bedeutet hier: Die ausgegebenen Summen sind ganze Zahlen.

Als Nächstes folgt **Teilpunkt 4**: das vorhandene Beispiel **„Create categorical variable based on apartment area“** verstehen. Dabei wird die Wohnfläche in Kategorien eingeteilt. Schicke mir bitte den Code dieser Zelle, damit wir ihn genau wie im Notebook durchgehen.

> *# Define classes (labels)*
> labels = ['0 - 49', '50 - 99', '100 - 9999']
>
> *# Use the .cut method from pandas to divide the numeric values in classes*
> df["area_cat"] = pd.cut(df['area'], bins=[0, 50, 100, 10000], labels=labels)
>
> *# Show original data and classes*
> df[['area', 'area_cat']]

Hier bearbeiten wir **Aufgabe 1, Teilpunkt 4**: Aus der numerischen Wohnfläche wird eine **kategoriale Variable**.

Bisher enthält `area` einzelne Zahlen wie `49.0`, `65.0` oder `110.0`. Die neue Spalte `area_cat` ordnet diese Werte Grössengruppen zu.

```python
labels = ['0 - 49', '50 - 99', '100 - 9999']
```

`labels` ist eine Liste mit den drei **Beschriftungen**. Sie bestimmen nur, wie die Kategorien heissen. Die tatsächlichen Grenzen legt die nächste Zeile fest:

```python
df["area_cat"] = pd.cut(
    df['area'],
    bins=[0, 50, 100, 10000],
    labels=labels
)
```

- **`pd.cut(...)`** teilt Zahlen anhand festgelegter Grenzen in Kategorien ein.
- **`df['area']`** enthält die einzuordnenden Wohnflächen.
- **`bins`** gibt die Grenzen an. Vier Grenzen ergeben drei Intervalle.
- **`labels=labels`** weist diesen Intervallen die drei Beschriftungen zu.
- **`df["area_cat"] = ...`** speichert das Ergebnis als neue Spalte.

**Wichtig: Die Beschriftungen im vorgegebenen Code passen an den Grenzen nicht genau zum tatsächlichen Verhalten.** Standardmässig schliesst `pd.cut` die rechte Grenze ein und die linke aus:

| Tatsächliches Intervall | Beschriftung im Notebook | Beispiel |
|---|---|---|
| `0 < area ≤ 50` | `0 - 49` | Auch **50 m²** gehört hierhin |
| `50 < area ≤ 100` | `50 - 99` | Auch **100 m²** gehört hierhin |
| `100 < area ≤ 10000` | `100 - 9999` | Beispielsweise **110 m²** |

Wir lassen den vorgegebenen Code für diese Aufgabe unverändert. Merke dir aber: **Die Grenzen in `bins` bestimmen die Zuordnung; die Texte in `labels` benennen sie nur.**

Fehlende Flächenwerte bleiben auch in `area_cat` fehlend. Ebenso erhalten Werte ausserhalb der Intervalle keine Kategorie.

```python
df[['area', 'area_cat']]
```

zeigt die ursprüngliche Fläche und die zugeordnete Kategorie nebeneinander. Die ursprüngliche Spalte `area` bleibt erhalten.

**Führe die Zelle aus.** Kurze Verständnisfrage: Welche Beschriftung erhält eine Wohnung mit **65 m²**?

> 50-99
>
> |      | **area** | **area_cat** |
> | ---: | -------: | -----------: |
> |    0 |     49.0 |       0 - 49 |
> |    1 |     65.0 |      50 - 99 |
> |    2 |      NaN |          NaN |
> |    3 |     54.0 |      50 - 99 |
> |    4 |     49.0 |       0 - 49 |
> |  ... |      ... |          ... |
> | 1003 |     82.0 |      50 - 99 |
> | 1004 |     73.0 |      50 - 99 |
> | 1005 |    110.0 |   100 - 9999 |
> | 1006 |     68.0 |      50 - 99 |
> | 1007 |    114.0 |   100 - 9999 |
>
> 1008 rows × 2 columns

<details><summary>2 previous messages</summary>

> Ich prüfe noch, wo im Notebook `price_per_m2` berechnet wird. Diese Spalte brauchen wir für den letzten Teil von Aufgabe 1.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> with open('/tmp/data_analytics_week03/Week_03/apartments_data_preparation_zuerich.ipynb') as f:n=json.load(f)
> for i,c in enumerate(n['cells'][23:],23):
>  print('CELL',i,c['cell_type']);print(''.join(c['source']))
> PY`
>
> </details>
</details>

Genau: **65 m² erhält die Kategorie `50 - 99`.** Deine Ausgabe passt zum vorgegebenen Code.

Für **Aufgabe 1, Teilpunkt 5** brauchen wir nun den **Preis pro Quadratmeter**. Diesen berechnet die nächste vorhandene Zelle:

```python
# Create the new variable
df['price_per_m2'] = round(df['price'] / df['area'], 2)

# Show values
df[['description_raw', 'rooms', 'area', 'price',
    'luxurious', 'price_per_m2']]
```

Die Berechnung lautet:

\[
\text{Preis pro m²} = \frac{\text{Mietpreis}}{\text{Wohnfläche}}
\]

Für das erste Inserat:

```text
1441 CHF ÷ 49 m² ≈ 29.41 CHF pro m²
```

Die Bestandteile des Codes:

- **`df['price'] / df['area']`** teilt für jede Zeile den Mietpreis durch die dazugehörige Fläche. Du brauchst dafür keine Schleife: pandas verarbeitet die Spalten zeilenweise miteinander.
- **`round(..., 2)`** rundet die Ergebnisse auf zwei Nachkommastellen.
- **`df['price_per_m2'] = ...`** speichert sie in einer neuen numerischen Spalte.
- Die letzte Zeile zeigt ausgewählte Spalten zum Vergleichen an.

Wenn die Fläche `NaN` ist, bleibt auch das Divisionsergebnis `NaN`: Ohne bekannte Fläche können wir keinen Quadratmeterpreis berechnen.

**Warum brauchen wir diese Kennzahl?** Der gesamte Mietpreis allein berücksichtigt die Wohnungsgrösse nicht. Der Preis pro Quadratmeter macht unterschiedlich grosse Wohnungen besser vergleichbar.

Führe diese Zelle aus. Danach erstellen wir daraus die geforderten Kategorien **`low`**, **`medium`** und **`high`**.

> weiter

Jetzt lösen wir **Aufgabe 1, Teilpunkt 5**: Wir erstellen aus `price_per_m2` eine kategoriale Variable mit den Stufen **`low`**, **`medium`** und **`high`**.

Die Aufgabe gibt keine Preisgrenzen vor. Für unsere Lösung wählen wir:

| Kategorie | Preis pro m² |
|---|---|
| `low` | bis einschliesslich 20 CHF |
| `medium` | über 20 bis einschliesslich 30 CHF |
| `high` | über 30 CHF |

Das sind **selbst gewählte Grenzen für die Übung**, keine allgemeingültigen Marktgrenzen.

Füge direkt nach der Berechnung von `price_per_m2` eine neue Codezelle ein:

```python
# Kategorien benennen
price_labels = ['low', 'medium', 'high']

# Quadratmeterpreise anhand selbst gewählter Grenzen einteilen
df['price_per_m2_cat'] = pd.cut(
    df['price_per_m2'],
    bins=[0, 20, 30, float('inf')],
    labels=price_labels,
    include_lowest=True
)

# Quadratmeterpreise und Kategorien vergleichen
df[['price_per_m2', 'price_per_m2_cat']]
```

Das funktioniert wie beim Beispiel zur Wohnfläche:

- **`bins`** legt die Grenzen fest.
- **`labels`** benennt die drei Intervalle in derselben Reihenfolge.
- **`float('inf')`** bedeutet „unendlich“. Dadurch werden auch Preise über 30 ohne feste Obergrenze erfasst.
- **`include_lowest=True`** schliesst die unterste Grenze `0` mit ein.
- Fehlende Quadratmeterpreise bleiben in der neuen Kategorie **`NaN`**.

Beispiele:

```text
18.50 → low
20.00 → low
29.41 → medium
30.00 → medium
35.00 → high
```

**Führe die Zelle aus.** Das erste Inserat mit **29.41 CHF pro m²** sollte die Kategorie **`medium`** erhalten. Damit ist die geforderte Ergänzung aus Teilpunkt 5 umgesetzt; danach gehen wir die verbleibenden Zellen des Notebooks weiter durch.

> ja, weiter

Damit ist **Teilpunkt 5 umgesetzt**. Wir setzen nun das Ausführen und Verstehen des Notebooks aus **Teilpunkt 1** fort.

Die nächste vorhandene Zelle heisst **„Including current datetime“**:

```python
# Get and format datetime
df['datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Show values
df[['description_raw', 'rooms', 'area', 'price',
    'luxurious', 'price_per_m2', 'datetime']]
```

Sie erstellt die Spalte **`datetime`** und trägt den Zeitpunkt der Ausführung ein.

Diesen Ausdruck lesen wir schrittweise:

```python
datetime.datetime.now()
```

Er liefert das aktuelle Datum und die aktuelle Uhrzeit der Python-Umgebung. Das erste `datetime` bezeichnet die importierte Bibliothek, das zweite die darin enthaltene Klasse.

```python
.strftime("%Y-%m-%d %H:%M:%S")
```

wandelt diesen Zeitpunkt in einen formatierten Text um:

| Platzhalter | Bedeutung |
|---|---|
| `%Y` | Jahr mit vier Ziffern |
| `%m` | Monat |
| `%d` | Tag |
| `%H` | Stunde im 24-Stunden-Format |
| `%M` | Minute |
| `%S` | Sekunde |

Eine mögliche Ausgabe wäre:

```text
2026-11-14 20:35:08
```

**Achte auf `%m` und `%M`:** Klein steht für Monat, gross für Minute.

Durch:

```python
df['datetime'] = ...
```

wird derselbe Zeitstempel in jede Zeile eingetragen. Er dokumentiert, **wann diese Zelle ausgeführt wurde** – nicht, wann die Inserate veröffentlicht wurden. Der gespeicherte Wert aktualisiert sich erst, wenn du die Zelle erneut ausführst.

**Führe diese Zelle aus.** Danach folgt das Erkennen und Entfernen fehlender Werte.

> weiter

Jetzt folgt **„Count, identify and remove missing values“**: fehlende Werte zählen, die betroffenen Zeilen anzeigen und anschliessend entfernen.

Führe die nächste vorhandene Zelle aus:

```python
# Count missing values
print('Count missing values per variable')
print(pd.isna(df).sum(), '\n')

# Identify rows with missing values
print('Identify rows with missing values')
print(df.loc[df.isna().any(axis=1)][['rooms', 'area', 'price']], '\n')

# Drop rows where at least one element is missing.
df2 = df.dropna()
df2.head()
```

Wir zerlegen die drei Schritte.

**1. Fehlende Werte pro Spalte zählen**

```python
pd.isna(df).sum()
```

`pd.isna(df)` prüft jede Tabellenzelle:

- `True`: Der Wert fehlt.
- `False`: Der Wert ist vorhanden.

`.sum()` zählt diese Treffer **pro Spalte**, weil `True` beim Summieren als `1` zählt. So sehen wir beispielsweise, wie viele Zimmerzahlen oder Flächen fehlen.

**2. Betroffene Zeilen anzeigen**

```python
df.loc[df.isna().any(axis=1)][['rooms', 'area', 'price']]
```

Von innen nach aussen:

- **`df.isna()`** prüft wieder jede Zelle auf fehlende Werte.
- **`.any(axis=1)`** prüft für jede Zeile: „Fehlt mindestens ein Wert?“ `axis=1` bedeutet hier, dass über die Spalten einer Zeile geprüft wird.
- **`df.loc[...]`** wählt die Zeilen aus, bei denen diese Bedingung `True` ist.
- **`[['rooms', 'area', 'price']]`** beschränkt die Anzeige auf diese drei Spalten.

Die Prüfung umfasst dabei **alle Spalten von `df`**. Nur die anschliessende Anzeige ist auf drei Spalten begrenzt.

**3. Zeilen mit fehlenden Werten entfernen**

```python
df2 = df.dropna()
```

Ohne weitere Einstellungen entfernt `.dropna()` jede Zeile, in der **mindestens ein Wert in irgendeiner Spalte fehlt**.

Das Ergebnis speichern wir als **`df2`**. Die ursprüngliche Tabelle **`df` bleibt erhalten**.

```python
df2.head()
```

zeigt die ersten fünf verbliebenen Zeilen. Ihre ursprünglichen Indexnummern bleiben bestehen; Lücken im Index sind deshalb normal.

**Führe die Zelle aus und schicke mir den Abschnitt „Count missing values per variable“.** Dann besprechen wir, welche Werte in deinen Daten fehlen.

> Count missing values per variable web-scraper-order          0 web-scraper-start-url      0 rooms_area_price_raw       0 address_raw                0 price_raw                  0 description_raw            0 text_raw                   0 rooms                     45 area                     135 price                     15 description_raw_len        0 text_raw_len               0 luxurious                  0 furnished                  0 balcony                    0 central                    0 area_cat                 135 price_per_m2             143 price_per_m2_cat         143 datetime                   0 dtype: int64   Identify rows with missing values      rooms  area   price
> ...
> 993    3.5   NaN  3087.0  [143 rows x 3 columns]  &#x20;
> *Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...*

Deine Ausgabe zeigt: **143 Inserate haben mindestens einen fehlenden Wert.** Deshalb bleiben nach `df.dropna()` **865 von 1’008 Inseraten** übrig.

Die wichtigsten Ergebnisse:

| Spalte | Fehlende Werte | Bedeutung |
|---|---:|---|
| `rooms` | 45 | Zimmerzahl konnte nicht extrahiert werden |
| `area` | 135 | Fläche konnte nicht extrahiert werden |
| `price` | 15 | Preis konnte nicht extrahiert werden |
| `area_cat` | 135 | Ohne Fläche keine Flächenkategorie |
| `price_per_m2` | 143 | Ohne Preis oder Fläche kein Quadratmeterpreis |
| `price_per_m2_cat` | 143 | Ohne Quadratmeterpreis keine Preiskategorie |

**Diese Zahlen darfst du nicht zusammenzählen:** Dasselbe Inserat kann in mehreren Spalten fehlende Werte haben. Deshalb zählen wir 143 betroffene Zeilen insgesamt.

Die Rohtextspalten enthalten keine fehlenden Werte. Trotzdem fehlen extrahierte Zahlen: Ein vorhandener Text garantiert nicht, dass er die gesuchte Angabe enthält oder dass unser Suchmuster sie erkennt.

`Output is truncated` bedeutet lediglich, dass VS Code die lange Ausgabe gekürzt anzeigt. **Das ist kein Fehler.**

Als Nächstes folgt die vorhandene Zelle **„Count, identify & remove duplicated values“**:

```python
# Count duplicated values in the whole data set
print('Sum of missing values:', df.duplicated().sum(), '\n')

# Identify duplicated values
print('Duplicated values')
print(df.loc[df.duplicated(keep='last')])

# Drop the rows with duplicated values
df3 = df2.drop_duplicates()
```

**Duplikate** sind hier Zeilen, deren Werte in **allen Spalten** übereinstimmen.

- **`df.duplicated().sum()`** zählt doppelte Zeilen. Standardmässig gilt das erste Vorkommen als Original; weitere gleiche Zeilen werden als Duplikate markiert.
- **`df.duplicated(keep='last')`** markiert stattdessen alle gleichen Zeilen ausser dem letzten Vorkommen. `df.loc[...]` zeigt die markierten Zeilen an.
- **`df2.drop_duplicates()`** entfernt Duplikate aus der bereits um fehlende Werte bereinigten Tabelle. Standardmässig bleibt jeweils das erste Vorkommen erhalten. Das Ergebnis heisst **`df3`**.

Zwei Details zum vorgegebenen Code: Der Ausgabetext **`Sum of missing values:`** ist hier falsch beschriftet – gezählt werden **Duplikate**. Ausserdem erfolgen Zählung und Anzeige auf `df`, die Entfernung dagegen auf `df2`.

**Führe die Zelle aus und schicke mir die ausgegebene Anzahl der Duplikate.**

> Sum of missing values: 0 \
> \
> Duplicated values\
> Empty DataFrame\
> Columns: [web-scraper-order, web-scraper-start-url, rooms_area_price_raw, address_raw, price_raw, description_raw, text_raw, rooms, area, price, description_raw_len, text_raw_len, luxurious, furnished, balcony, central, area_cat, price_per_m2, price_per_m2_cat, datetime]\
> Index: []

**Es wurden keine vollständig identischen Zeilen gefunden.**

- **`0`** bedeutet: keine Duplikate über alle Spalten.
- **`Empty DataFrame`** bedeutet: Die Auswahl der doppelten Zeilen ist leer.
- Deshalb entfernt `df2.drop_duplicates()` keine weiteren Zeilen. `df3` enthält weiterhin **865 Inserate**.

Das beweist allerdings nicht, dass jede Wohnung nur einmal vorkommt: Zwei Inserate derselben Wohnung könnten unterschiedliche Kennungen oder Texte haben.

Als Nächstes folgt **„Save data to file“**. Die vorhandene Zelle speichert `df3` als CSV:

```python
df3.to_csv('apartments_data_prepared.csv',
           sep=",",
           encoding='utf-8',
           index=False)
```

Die Bestandteile:

| Code | Bedeutung |
|---|---|
| `df3.to_csv(...)` | Schreibt die bereinigte Tabelle in eine CSV-Datei |
| `'apartments_data_prepared.csv'` | Name der Ausgabedatei |
| `sep=","` | Trennt die Spalten durch Kommas |
| `encoding='utf-8'` | Speichert auch Umlaute korrekt |
| `index=False` | Speichert die pandas-Zeilennummern nicht als zusätzliche Spalte |

**Vor dem Ausführen müssen wir noch den Speicherort berücksichtigen:** Dein Arbeitsordner war `/`. Ein Dateiname ohne vollständigen Pfad würde deshalb versuchen, dort zu speichern.

Verwende für unsere lokale Arbeitskopie diesen vollständigen Pfad:

```python
df3.to_csv(
    '/tmp/data_analytics_week03/Week_03/apartments_data_prepared.csv',
    sep=",",
    encoding='utf-8',
    index=False
)
```

Damit liegt die vorbereitete Datei neben den anderen Dateien für Week_03. **Wenn die Zelle ohne Ausgabe und ohne Fehlermeldung durchläuft, wurde sie gespeichert.** Eine bereits vorhandene Datei mit diesem Namen wird dabei überschrieben.

Führe die Speicherzelle aus. Danach folgt noch die letzte Infozelle des Notebooks.

> weiter

Zum Abschluss dieses Notebooks folgt die **„Jupyter notebook — footer info“**-Zelle:

```python
import os
import platform
import socket
from platform import python_version
from datetime import datetime

print('-----------------------------------')
print(os.name.upper())
print(platform.system(), '|', platform.release())
print('Datetime:', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('Python Version:', python_version())
print('-----------------------------------')
```

Sie dokumentiert die **Umgebung, in der du das Notebook ausgeführt hast**:

| Ausdruck | Bedeutung |
|---|---|
| `os.name.upper()` | Allgemeine Betriebssystemfamilie, auf deinem Mac typischerweise `POSIX` |
| `platform.system()` | Betriebssystem, auf macOS typischerweise `Darwin` |
| `platform.release()` | Version des Betriebssystem-Kernels |
| `datetime.now().strftime(...)` | Zeitpunkt der Ausführung als formatierter Text |
| `python_version()` | Verwendete Python-Version |

`socket` wird zwar importiert, in dieser Zelle aber nicht verwendet. Die Zeilen mit Bindestrichen dienen nur der übersichtlichen Anzeige. **Deine Wohnungsdaten werden durch diese Zelle nicht verändert.**

Ein Detail: Hier steht

```python
from datetime import datetime
```

Dadurch bezeichnet der Name `datetime` anschliessend direkt die Klasse. Deshalb funktioniert hier `datetime.now()`. Weiter oben hatten wir nach `import datetime` noch `datetime.datetime.now()` verwendet. Wenn du das Notebook später erneut ausführst, gehe wieder von oben nach unten vor, damit die Imports in der vorgesehenen Reihenfolge laufen.

**Führe diese letzte Zelle aus.** Wenn auch das Speichern davor ohne Fehler funktioniert hat, ist **Aufgabe 1 vollständig erledigt**:

- vorhandenen Code ausgeführt und verstanden;
- `furnished`, `balcony` und `central` erstellt;
- `price_per_m2_cat` mit `low`, `medium` und `high` erstellt;
- bereinigte Daten gespeichert.

Danach beginnen wir **Aufgabe 2** mit dem Notebook `combining_and_organizing_data.ipynb`.

> aber warte, ich sehe die datei gar nicht von "save data to file"

<details><summary>2 previous messages</summary>

> Ich prüfe, ob die gespeicherte Datei im angegebenen lokalen Ordner liegt.
>
> <details><summary>Explored a list</summary>
>
> - Listed files in `apartments_data_prepared.csv`
>
> </details>
</details>

**Die Datei wurde gespeichert – ich habe sie gerade überprüft.** Sie liegt hier und ist etwa 785 KB gross:

```text
/tmp/data_analytics_week03/Week_03/apartments_data_prepared.csv
```

Du siehst sie nicht im geöffneten Projektbaum, weil dieser dein **GitHub-Projekt** anzeigt. Gespeichert haben wir die Datei dagegen **lokal auf deinem Mac**. Meine vorherige Erklärung hat diesen Unterschied nicht deutlich genug gemacht.

So findest du sie im Finder:

1. Öffne den **Finder**.
2. Drücke **Cmd + Shift + G** („Gehe zum Ordner“).
3. Füge diesen Ordnerpfad ein:

   ```text
   /tmp/data_analytics_week03/Week_03
   ```

4. Drücke **Enter**.

Dort solltest du `apartments_data_prepared.csv` sehen.

**Wichtig:** `/tmp` ist ein temporärer Ordner. Die Datei ist damit noch nicht dauerhaft in deinem GitHub-Projekt gespeichert. Bevor wir mit Aufgabe 2 weitermachen, sollten wir die Arbeitsdateien dauerhaft lokal ablegen.

> nein es soll in diesem projekt gespeochert werden!

<details><summary>2 previous messages</summary>

> Ich prüfe, wie dein GitHub-Projekt eingebunden ist, damit wir die Datei im richtigen Projekt speichern.
>
> <details><summary>Ran a command</summary>
>
> - Ran `ls -la '/Users/leyla.erikci/Library/Application Support/Code/User/globalStorage/github.remotehub'; command -v git; command -v code; ls -la /Users/leyla.erikci/Documents/Codex`
>
> </details>
</details>

Ja, die Datei gehört in **`Week_03` deines geöffneten Projekts**. Mein Vorschlag mit `/tmp` war dafür nicht ausreichend.

Weil das Projekt über die virtuelle GitHub-Ansicht geöffnet ist, kann dein lokales Python dort nicht direkt mit `to_csv()` speichern. Die bereits erzeugte Datei kannst du so ins Projekt übernehmen:

1. Öffne im **Finder** mit **Cmd + Shift + G** diesen Ordner:

   ```text
   /tmp/data_analytics_week03/Week_03
   ```

2. Ziehe **`apartments_data_prepared.csv`** aus dem Finder auf den Ordner **`Week_03` im VS-Code-Explorer**.
3. Wähle **Kopieren**, falls VS Code danach fragt.

Damit soll die Datei im Projektbaum unter `Week_03` erscheinen. Die Übernahme nach GitHub erfolgt anschliessend über die Quellcodeverwaltung.

**Sag mir, ob die Datei nach dem Ziehen im Projektbaum erscheint.** Wir bleiben beim Speichern, bis das erledigt ist.

> ja erscheint, in zukunft immer die sachen in diesem projekt speichern!

Ab jetzt speichern wir **alle Ergebnisse im geöffneten Projekt**, jeweils im passenden Ordner wie `Week_03`.

Die CSV ist nun dort sichtbar. Damit ist dieser Speicherschritt erledigt. Wenn eine technische Einschränkung das direkte Speichern verhindert, klären wir den Weg ins Projekt, bevor wir weitermachen.

> weiter mit aufgabe

<details><summary>2 previous messages</summary>

> Wir beginnen mit Aufgabe 2. Ich lese die ersten Zellen des zweiten Notebooks, damit wir wieder genau dem vorgegebenen Ablauf folgen.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> with open('/tmp/data_analytics_week03/Week_03/combining_and_organizing_data.ipynb') as f:n=json.load(f)
> for i,c in enumerate(n['cells'][:9]):
>  print('CELL',i,c['cell_type']);print(''.join(c['source']))
> PY`
>
> </details>
</details>

Wir beginnen mit **Aufgabe 2a**: Das Notebook **`combining_and_organizing_data.ipynb`** schrittweise ausführen und verstehen.

Hier werden die aufbereiteten Wohnungsdaten mit weiteren Informationen verknüpft, beispielsweise mit der Gemeinde, in der eine Wohnung liegt.

Öffne das Notebook **in `Week_03` deines Projekts** und führe zunächst nur die erste Codezelle aus:

```python
# Libraries
import os
import pandas as pd
import numpy as np
import fnmatch

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Show current working directory
print(os.getcwd())
```

Diese Befehle kennst du bereits:

- **`import ...`** lädt die benötigten Bibliotheken.
- **`warnings.filterwarnings("ignore")`** blendet Warnungen aus, aber keine Fehler.
- **`print(os.getcwd())`** zeigt den Arbeitsordner des laufenden Python-Kernels.

Auch im zweiten Notebook führen wir die Imports aus: Ein Notebook kann einen eigenen Kernel haben und kennt dann die Variablen und Imports des ersten Notebooks nicht.

**Schicke mir den ausgegebenen Arbeitsordner.** Wir prüfen ihn vor dem Einlesen, damit wir den Dateipfad diesmal von Anfang an richtig verwenden. Ergebnisse speichern wir weiterhin in deinem Projekt.

> \--------------------------------------------------------------------------- FileNotFoundError                         Traceback (most recent call last) Cell In[2], line 2&#x20;**&#x20;     1** # Read data to pandas data frame ----> 2 df_orig = pd.read_csv('apartments_data_prepared.csv', &#x20;**&#x20;     3**                       sep=',', &#x20;**&#x20;     4**                       encoding='utf-8')&#x20;**&#x20;     6** # Copy of data with selected colums&#x20;**&#x20;     7** columns = [ 'web-scraper-order', &#x20;**&#x20;     8**             'address_raw',&#x20;**&#x20;     9**             'rooms',     (...)&#x20;**&#x20;    12**             'price',&#x20;**&#x20;    13**             'price_per_m2']  File /opt/anaconda3/lib/python3.11/site-packages/pandas/io/parsers/readers.py:948, in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)&#x20;**&#x20;   935** kwds_defaults = \_refine_defaults_read(&#x20;**&#x20;   936**     dialect,&#x20;**&#x20;   937**     delimiter,    (...)&#x20;**&#x20;   944**     dtype_backend=dtype_backend,&#x20;**&#x20;   945** )&#x20;**&#x20;   946** kwds.update(kwds_defaults) --> [948](https://vscode-vfs+github-002b7b2276223a312c22726566223a7b2274797065223a342c226964223a226d6173746572227d7d.vscode-resource.vscode-cdn.net/opt/anaconda3/lib/python3.11/site-packages/pandas/io/parsers/readers.py:948) return \_read(filepath_or_buffer, kwds)&#x20;
> ...
> \--> [872](https://vscode-vfs+github-002b7b2276223a312c22726566223a7b2274797065223a342c226964223a226d6173746572227d7d.vscode-resource.vscode-cdn.net/opt/anaconda3/lib/python3.11/site-packages/pandas/io/common.py:872)         handle = open(handle, ioargs.mode)&#x20;**&#x20;   873**     handles.append(handle)&#x20;**&#x20;   875** # Convert BytesIO or file objects passed with an encoding  FileNotFoundError: [Errno 2] No such file or directory: 'apartments_data_prepared.csv'
> *Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...*

**Die Datei ist im Projekt vorhanden, aber dein lokales Python kann die virtuelle GitHub-Ansicht nicht direkt lesen.** Meine bisherige Lösung hat dieses grundsätzliche Problem nicht behoben.

Damit Einlesen **und Speichern direkt im Projekt** funktionieren, müssen wir das GitHub-Projekt lokal öffnen.

Gehe in VS Code so vor:

1. **Speichere zuerst deine Änderungen** an den Notebooks mit **Cmd + S**.
2. Öffne mit **Cmd + Shift + P** die Befehlspalette.
3. Suche nach **`Git: Clone`**.
4. Wähle dein Repository **`LEYERI/data_analytics`** beziehungsweise gib dessen Adresse ein:

   ```text
   https://github.com/LEYERI/data_analytics.git
   ```

5. Wähle einen dauerhaften Speicherort, beispielsweise **Dokumente**.
6. Öffne anschliessend das geklonte Projekt.

**Wichtig:** Beim Klonen werden nur die bereits auf GitHub gespeicherten Änderungen übernommen. Lass das bisherige Projekt deshalb geöffnet, bis wir geprüft haben, dass deine bearbeiteten Notebooks und `apartments_data_prepared.csv` auch in der lokalen Kopie vorhanden sind.

Danach können wir im lokalen Ordner `Week_03` mit den vorgesehenen Dateinamen arbeiten:

```python
df_orig = pd.read_csv(
    'apartments_data_prepared.csv',
    sep=',',
    encoding='utf-8'
)
```

Wir bleiben jetzt bei diesem Einrichtungsschritt. **Sag mir, ob das Klonen funktioniert hat oder welche Meldung erscheint.**

> aber wenn ich es auf deksptop lokal habe, dann ist ja das pronelme, dass wenn der benutzer, von dem ich es forked habe, ändeurngen macht, es nicht synronisiert? dann lieber remote mit temp oder?

**Eine lokale Kopie verhindert die Synchronisierung nicht.** Ein Fork wird auch in der Remote-Ansicht **nicht automatisch** mit dem ursprünglichen Repository synchronisiert.

Dabei gibt es drei Orte:

```text
Ursprüngliches Repository
          ↓ Änderungen übernehmen
Dein Fork auf GitHub
          ↕ Pull / Push
Deine lokale Projektkopie
```

- **Fork synchronisieren:** Änderungen des ursprünglichen Repositorys in deinen Fork übernehmen.
- **Pull:** Änderungen von deinem Fork auf den Rechner holen.
- **Push:** Deine lokal gespeicherten Änderungen zu deinem Fork hochladen.

**Remote mit temporären Dateien funktioniert ebenfalls**, wie wir gesehen haben. Allerdings musst du neue Ergebnisse jedes Mal wieder ins Projekt kopieren. Python kann die Dateien im virtuellen Projektbaum weiterhin nicht direkt lesen oder dort speichern.

Für unsere Python-Aufgaben empfehle ich deshalb **eine lokale Projektkopie, die mit deinem Fork verbunden ist**. Damit funktionieren die vorgesehenen Dateipfade, deine Ergebnisse bleiben im Projekt, und Änderungen aus dem ursprünglichen Repository können weiterhin übernommen werden.

Meine bisherige Erklärung war missverständlich: **„lokal“ bedeutet hier eine mit GitHub verbundene Arbeitskopie**, nicht eine losgelöste Kopie ohne Synchronisierung.

> also ich habe es bon einem benutzer forked. wenn er änderungen macht, kann ich es bei mir snycohriniersen?

**Ja.** Wenn der ursprüngliche Benutzer Änderungen macht, kannst du sie in deinen Fork übernehmen – auch wenn du dein Projekt lokal bearbeitest.

Der Ablauf ist:

1. **Auf GitHub deinen Fork synchronisieren:** Änderungen vom ursprünglichen Repository übernehmen.
2. **Lokal einen Pull ausführen:** Diese Änderungen auf deinen Rechner holen.

Deine eigenen Änderungen bleiben dabei grundsätzlich erhalten. Wenn ihr beide dieselben Stellen verändert habt, kann ein **Konflikt** entstehen, den wir gemeinsam lösen können.

**Du kannst also lokal arbeiten und trotzdem weiterhin Änderungen des ursprünglichen Benutzers übernehmen.** Die Synchronisierung musst du jeweils anstossen; sie geschieht nicht automatisch.

> muss ich die lokale dann auf hithub publizeiren als repositiry?

**Nein, du brauchst kein neues Repository.** Dein Fork ist bereits dein Repository auf GitHub.

Wenn du **deinen Fork klonst**, entsteht eine lokale Arbeitskopie, die mit diesem bestehenden Repository verbunden bleibt.

Du arbeitest dann so:

1. **Speichern:** Änderungen liegen auf deinem Rechner.
2. **Commit:** Git hält einen Stand deiner Änderungen fest.
3. **Push:** Überträgt die Commits in deinen bestehenden Fork auf GitHub.

Wichtig ist nur: **Wir klonen deinen Fork**, nicht direkt das Repository des ursprünglichen Benutzers. Du musst dafür nichts neu „publizieren“.

> also es wird alles synchoornisiert, damit die lokale datei aktuell ist?

**Ja, du kannst die lokale Projektkopie aktuell halten – aber nicht automatisch.** Du stösst die Übertragung jeweils an:

| Richtung | Aktion |
|---|---|
| Ursprüngliches Repository → dein Fork | **Fork synchronisieren** |
| Dein Fork → lokale Projektkopie | **Pull** |
| Lokale Änderungen → dein Fork | **Commit + Push** |

**Nur auf „Speichern“ zu klicken aktualisiert die Datei auf deinem Rechner**, noch nicht auf GitHub.

Für unseren Ablauf bedeutet das: Vor dem Arbeiten holen wir verfügbare Änderungen herunter. Nach dem Arbeiten speichern wir deine Änderungen mit Commit und Push in deinem Fork. So bleiben beide Seiten auf demselben Stand.

> ich mzss in diesem fall imemr commut push machen=0

**Nicht nach jeder Änderung.** Beim Arbeiten reicht zunächst **Speichern** – deine Dateien sind dann lokal gesichert.

**Commit + Push** machst du an sinnvollen Zwischenständen, zum Beispiel nach einer abgeschlossenen Aufgabe oder am Ende einer Lernsitzung. Dadurch kommen deine Änderungen auch auf GitHub.

**Pull** brauchst du nur, wenn du Änderungen von GitHub auf deinen Rechner holen möchtest. Dafür musst du nicht jedes Mal selbst etwas pushen.

> gut weiter mit aufgaben

Wir sind weiterhin bei **Aufgabe 2a**, beim Einlesen der vorbereiteten Wohnungsdaten. Die letzte Zelle ist noch am Dateipfad gescheitert.

Damit wir jetzt den richtigen Pfad verwenden, führe im zweiten Notebook diese kurze Zelle aus:

```python
import os

print(os.getcwd())
```

Sie zeigt den **Arbeitsordner deines Python-Kernels**. Dort sucht Python nach `apartments_data_prepared.csv`, wenn nur der Dateiname angegeben ist.

**Schicke mir die Ausgabe.** Dann lösen wir den Pfad passend zu deinem aktuellen Projekt und fahren mit dem Einlesen fort.

> /Users/leyla.erikci/Desktop/data_analytics/Week_03

**Der Arbeitsordner passt jetzt:** Python arbeitet direkt im lokalen Projektordner `Week_03`. Dateien aus diesem Ordner können wir mit ihrem Namen einlesen und Ergebnisse dort speichern.

Führe die vorhandene Importzelle erneut aus:

```python
# Vorbereitete Wohnungsdaten einlesen
df_orig = pd.read_csv(
    'apartments_data_prepared.csv',
    sep=',',
    encoding='utf-8'
)

# Benötigte Spalten auswählen
columns = [
    'web-scraper-order',
    'address_raw',
    'rooms',
    'area',
    'luxurious',
    'price',
    'price_per_m2'
]

df = df_orig[columns]

# Dimension und erste fünf Zeilen anzeigen
print(df.shape)
df.head(5)
```

Neu gegenüber dem ersten Notebook ist die **Spaltenauswahl**:

- **`df_orig`** enthält die gesamte eingelesene Tabelle.
- **`columns`** ist eine Liste mit den sieben Spaltennamen, die wir für die nächsten Schritte brauchen.
- **`df_orig[columns]`** wählt diese Spalten aus und weist das Ergebnis `df` zu. Die übrigen Spalten werden dadurch nicht aus `df_orig` gelöscht.
- **`df.head(5)`** zeigt die ersten fünf Zeilen der ausgewählten Tabelle.

Wenn du die zuvor erstellte Datei verwendest, erwarten wir:

```text
(865, 7)
```

Also **865 bereinigte Inserate und sieben ausgewählte Spalten**.

Falls erneut `FileNotFoundError` erscheint, fehlt die vorbereitete CSV noch in dieser lokalen Projektkopie. Schicke mir dann die Meldung; andernfalls die Ausgabe von `df.shape`.

> hat geklappt

<details><summary>2 previous messages</summary>

> Ich lese die nächste Zelle zum Einlesen der Geodaten. Danach erklären wir, welche Informationen sie den Wohnungen hinzufügen.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> from pathlib import Path
> p=Path('/Users/leyla.erikci/Desktop/data_analytics/Week_03/combining_and_organizing_data.ipynb')
> if not p.exists(): p=Path('/tmp/data_analytics_week03/Week_03/combining_and_organizing_data.ipynb')
> n=json.loads(p.read_text())
> for c in n['cells'][5:10]:
>  print(c['cell_type']);print(''.join(c['source']))
> PY`
>
> </details>
</details>

Jetzt folgt in **Aufgabe 2a** der Abschnitt **„Reading rental apartment data with geocoded addresses“**.

**Geocodierung** bedeutet: Einer Adresse werden geografische Koordinaten zugeordnet. Diese Informationen liegen bereits in einer zweiten CSV-Datei vor.

Führe die nächste vorhandene Zelle aus:

```python
# Geodaten einlesen
df_geo = pd.read_csv(
    'apartments_data_geocoded.csv',
    sep=',',
    encoding='utf-8'
)

# Spalten umbenennen
df_geo = df_geo.rename(columns={
    'web-scrape': 'web-scraper-order',
    'address_ra': 'address_raw',
    'BFS_NUMMER': 'bfs_number',
    'NAME': 'bfs_name'
})

# Ausgewählte Spalten anzeigen
df_geo[[
    'web-scraper-order',
    'address_raw',
    'lat',
    'lon',
    'bfs_number',
    'bfs_name'
]].head()
```

**`df_geo`** ist eine weitere Tabelle. Sie enthält unter anderem:

| Spalte | Bedeutung |
|---|---|
| `web-scraper-order` | Kennung des Inserats |
| `address_raw` | Adresse als Text |
| `lat` | Geografischer Breitengrad: Position in Nord-Süd-Richtung |
| `lon` | Geografischer Längengrad: Position in Ost-West-Richtung |
| `bfs_number` | Amtliche Gemeindenummer des Bundesamts für Statistik |
| `bfs_name` | Name der Gemeinde |

Neu ist dieser Aufruf:

```python
df_geo.rename(columns={...})
```

Er benennt Spalten um. Die geschweiften Klammern enthalten ein **Dictionary**, also Zuordnungen nach dem Prinzip:

```python
'alter Name': 'neuer Name'
```

Zum Beispiel:

```python
'BFS_NUMMER': 'bfs_number'
```

**Die Werte bleiben dabei unverändert; nur die Spaltenüberschriften ändern sich.** Durch die Zuweisung `df_geo = ...` behalten wir die umbenannte Tabelle.

Besonders wichtig ist `web-scraper-order`: Diese Kennung steht auch in unserer Wohnungstabelle. Im nächsten Schritt verwenden wir sie, um **jedem Inserat seine Geoinformationen zuzuordnen**.

Führe die Zelle aus. Werden dir die ersten fünf Zeilen mit Koordinaten und Gemeindeangaben angezeigt?

> Ja

Jetzt folgt **„Join geo-information to rental apartment data using `.merge()`“**: Wir verknüpfen die Wohnungsdaten mit den Geodaten.

Führe die nächste vorhandene Zelle aus:

```python
df2 = df.merge(
    df_geo[[
        'web-scraper-order',
        'lat',
        'lon',
        'bfs_number',
        'bfs_name'
    ]],
    on="web-scraper-order"
)

df2.head()
```

**`merge()` verbindet zwei Tabellen anhand einer gemeinsamen Kennung.** Diese Kennung nennt man hier den **Verknüpfungsschlüssel**.

Unsere Tabellen enthalten unterschiedliche Informationen zum selben Inserat:

```text
df:      Inserat-ID | Zimmer | Fläche | Preis
df_geo:  Inserat-ID | Breitengrad | Längengrad | Gemeinde
```

Der Code sucht passende Werte in `web-scraper-order` und führt die Informationen zusammen:

```text
df2:     Inserat-ID | Zimmer | Fläche | Preis | Koordinaten | Gemeinde
```

Die einzelnen Bestandteile:

- **`df.merge(...)`** verknüpft die Wohnungstabelle mit einer zweiten Tabelle.
- **`df_geo[[...]]`** wählt aus den Geodaten nur die Kennung und die vier zusätzlich benötigten Spalten aus.
- **`on="web-scraper-order"`** legt fest, welche Spalte zum Zuordnen verwendet wird.
- **`df2 = ...`** speichert das Ergebnis als neue Tabelle. `df` und `df_geo` bleiben erhalten.

**Wichtig:** Die Zuordnung erfolgt über die Kennung, nicht über die Reihenfolge der Zeilen. Das passende Inserat darf in den beiden Tabellen an unterschiedlichen Positionen stehen.

Da der Code keinen Verbindungstyp angibt, verwendet pandas standardmässig einen **Inner Join**: Nur Kennungen, die in beiden Tabellen vorkommen, werden übernommen. Falls eine Kennung mehrfach vorkommt, können dabei mehrere Ergebniszeilen entstehen.

**Führe die Zelle aus.** Du solltest nun neben den Wohnungsmerkmalen auch `lat`, `lon`, `bfs_number` und `bfs_name` sehen.

> ja

<details><summary>2 previous messages</summary>

> Ich lese den nächsten Abschnitt des Notebooks, damit wir beim vorgegebenen Ablauf bleiben.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> from pathlib import Path
> p=Path('/Users/leyla.erikci/Desktop/data_analytics/Week_03/combining_and_organizing_data.ipynb')
> if not p.exists():p=Path('/tmp/data_analytics_week03/Week_03/combining_and_organizing_data.ipynb')
> n=json.loads(p.read_text())
> for i,c in enumerate(n['cells'][10:18],10):
>  print('CELL',i,c['cell_type']);print(''.join(c['source']))
> PY`
>
> </details>
</details>

Als Nächstes folgt **„Reading municipality-level data“**: Wir lesen Daten über die Gemeinden ein.

```python
# Gemeindedaten aus einer Excel-Datei einlesen
df_municip = pd.read_excel(
    'municipality_data.xlsx',
    sheet_name='data_for_import'
)

# Erste fünf Zeilen anzeigen
df_municip.head(5)
```

Bisher haben wir CSV-Dateien mit `pd.read_csv()` eingelesen. **`pd.read_excel()`** liest dagegen eine Excel-Datei.

- **`'municipality_data.xlsx'`** ist die Datei im Projektordner `Week_03`.
- **`sheet_name='data_for_import'`** wählt das Tabellenblatt mit diesem Namen aus. Eine Excel-Datei kann mehrere Tabellenblätter enthalten.
- **`df_municip`** speichert die eingelesene Tabelle.
- **`.head(5)`** zeigt die ersten fünf Zeilen.

Laut den Kommentaren im Notebook enthält die Tabelle folgende Merkmale:

| Spalte | Bedeutung |
|---|---|
| `bfs_number` | Amtliche Gemeindenummer |
| `bfs_name` | Gemeindename |
| `pop` | Einwohnerzahl |
| `pop_dens` | Bevölkerungsdichte: Einwohner pro km² |
| `frg_pct` | Ausländeranteil in Prozent |
| `emp` | Anzahl der Beschäftigten |

**Der Unterschied zu den bisherigen Tabellen:** Hier beschreibt eine Zeile eine **Gemeinde**, nicht ein Wohnungsinserat. Mehreren Wohnungen derselben Gemeinde können wir später dieselben Gemeindeinformationen zuordnen. Dafür verwenden wir `bfs_number`.

**Führe diese Zelle aus.** Danach öffnen wir die Excel-Datei selbst, wie es Aufgabe 2b verlangt, und schauen uns ihren Aufbau an.

> ja

Nun folgt **Aufgabe 2b**: Öffne **`municipality_data.xlsx`** aus deinem lokalen Projektordner `Week_03` in **Excel** und wähle das Tabellenblatt **`data_for_import`**.

Vergleiche es mit der Ausgabe im Notebook: Es sind dieselben Daten. Python hat dieses Tabellenblatt als `df_municip` eingelesen.

Achte besonders auf **`bfs_number`**, die amtliche Gemeindenummer. Sie dient später als eindeutige Kennung, um Gemeindeinformationen einer Wohnung zuzuordnen.

Beispiel:

```text
Wohnung A ─┐
Wohnung B ─┼─ gleiche bfs_number → gleiche Gemeindeinformationen
Wohnung C ─┘
```

**Warum verwenden wir die Nummer statt des Gemeindenamens?** Namen können unterschiedlich geschrieben sein. Die amtliche Nummer ermöglicht eine verlässliche Zuordnung, sofern beide Dateien denselben Gemeindestand verwenden.

Die nächsten Teilpunkte bearbeiten wir ausdrücklich **in Excel**: Wir ergänzen das durchschnittliche steuerbare Einkommen pro Person aus `fiscal_data.xlsx`.

**Hast du das Blatt `data_for_import` in Excel geöffnet und siehst du die Spalte `bfs_number`?**

> ich kann die xlsx datei nicht lesen, hat komische zeichen

**Vermutlich wurde die `.xlsx`-Datei im Texteditor von VS Code geöffnet.** Eine Excel-Datei enthält intern komprimierte Daten. Als Text angezeigt wirken diese wie „komische Zeichen“ – das bedeutet nicht, dass die Datei beschädigt ist.

Öffne sie so:

1. Öffne den **Finder**.
2. Gehe zu **Desktop → data_analytics → Week_03**.
3. Klicke mit der rechten Maustaste auf **`municipality_data.xlsx`**.
4. Wähle **Öffnen mit → Microsoft Excel**.

Wähle in Excel anschliessend unten das Tabellenblatt **`data_for_import`**.

**Ändere die komischen Zeichen in VS Code nicht.** Falls du dort versehentlich etwas bearbeitet hast, schliesse die Datei ohne Speichern.

Siehst du die Datei danach als Tabelle in Excel?

> kann man nicht ein add in machen?

<details><summary>2 previous messages</summary>

> Ich prüfe, welche VS-Code-Erweiterung Excel-Dateien als Tabelle anzeigen kann und ob sie für den nächsten Aufgabenschritt ausreicht.
>
> <details><summary>Searched the web</summary>
>
> Searched the web for `site.marketplace.visualstudio.com Excel Viewer GrapeCity xlsx readonly`
>
> </details>
</details>

**Ja – in VS Code heisst das „Erweiterung“.** Mit **[CSV & Excel Viewer](https://marketplace.visualstudio.com/items?itemName=Development42.csv-excel-viewer)** kannst du `.xlsx`-Dateien als Tabelle anzeigen und zwischen Tabellenblättern wechseln.

So installierst du sie:

1. Öffne die Erweiterungen mit **Cmd + Shift + X**.
2. Suche nach **`Development42.csv-excel-viewer`**.
3. Klicke auf **Installieren**.
4. Öffne `municipality_data.xlsx` erneut und wähle unten **`data_for_import`**.

**Für das Anschauen in Aufgabe 2b reicht das.** Für die folgenden Teilaufgaben benötigen wir aber **Microsoft Excel**, weil die Aufgabenstellung ausdrücklich das Bearbeiten mit **`SVERWEIS` beziehungsweise `VLOOKUP` in Excel** verlangt. Die Vorschau ersetzt diesen Arbeitsschritt nicht.

> hat geklappt

Dann können wir **Aufgabe 2b** abschliessen: Wähle unten im Viewer das Blatt **`data_for_import`** aus. Dort stehen die Gemeindeinformationen, die du bereits als `df_municip` eingelesen hast.

Jetzt folgen **Aufgabe 2c–e**: Wir ergänzen das **durchschnittliche steuerbare Einkommen pro Person** aus `fiscal_data.xlsx` in `municipality_data.xlsx`.

Die Verknüpfung erfolgt über:

| Datei | Gemeindekennung |
|---|---|
| `municipality_data.xlsx` | `bfs_number` |
| `fiscal_data.xlsx` | `Regions-ID` |

**Wichtig:** Gesucht ist das Einkommen **pro Person**, nicht das gesamte Einkommen einer Gemeinde. Sonst würden grosse Gemeinden allein wegen ihrer Einwohnerzahl höhere Werte aufweisen.

Die nächsten Schritte verlangt die Aufgabe ausdrücklich **in Microsoft Excel**. Öffne deshalb jetzt beide Dateien aus deinem lokalen Projektordner `Week_03` in Excel. Die Erweiterung können wir weiterhin zum Anschauen verwenden.

**Sind beide Dateien in Excel geöffnet?** Danach schauen wir uns zuerst den Aufbau von `fiscal_data.xlsx` an, bevor wir eine Formel schreiben.

> ja

<details><summary>2 previous messages</summary>

> Ich nutze die Tabellen-Skill und prüfe den Aufbau der beiden Dateien, damit wir die richtigen Spalten für den SVERWEIS verwenden.
>
> <details><summary>Ran a command</summary>
>
> <details><summary>Explored a file</summary>
>
> - Read `/Users/leyla.erikci/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.1112.11217/skills/spreadsheets/SKILL.md`
>
> </details>
>
> - Ran `python3 - <<'PY'
> from pathlib import Path
> from zipfile import ZipFile
> import xml.etree.ElementTree as E
> ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
> base=Path('/Users/leyla.erikci/Desktop/data_analytics/Week_03')
> for name in ['fiscal_data.xlsx','municipality_data.xlsx']:
>  p=base/name
>  if not p.exists():p=Path('/tmp/data_analytics_week03/Week_03')/name
>  print('FILE',p)
>  with ZipFile(p) as z:
>   strings=[]
>   if 'xl/sharedStrings.xml' in z.namelist():
>    strings=[''.join(e.itertext()) for e in E.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns)]
>   print(z.read('xl/workbook.xml').decode()[:2500])
>   for s in sorted(x for x in z.namelist() if x.startswith('xl/worksheets/sheet') and x.endswith('.xml')):
>    root=E.fromstring(z.read(s));print('SHEET',s)
>    for row in root.findall('m:sheetData/m:row',ns)[:14]:
>     vals=[]
>     for c in row.findall('m:c',ns):
>      v=c.find('m:v',ns);value=v.text if v is not None else ''.join(c.find('m:is',ns).itertext()) if c.find('m:is',ns) is not None else ''
>      if c.get('t')=='s':value=strings[int(value)]
>      if value:vals.append(c.get('r')+'='+value)
>     print(' | '.join(vals)[:1800])
> PY`
>
> </details>
</details>

Wir beginnen mit **Aufgabe 2c–d**: die richtige Einkommensspalte erkennen.

Schau in der geöffneten **`fiscal_data.xlsx`** auf das Blatt **`Worksheet`**:

| Spalte | Inhalt | Verwendung |
|---|---|---|
| A | `Regions-ID` | Gemeindenummer für die Zuordnung |
| B | `Regionsname` | Gemeindename |
| C | Steuerbares Einkommen **in Millionen Franken** | Gesamteinkommen – nicht gesucht |
| D | Steuerbares Einkommen **pro Steuerpflichtigem/-r in Franken** | **Diese Werte brauchen wir** |

Die erste Gemeinde steht in **Zeile 7**: **Aeugst am Albis**, mit der Regions-ID `1`.

**Eine Präzisierung:** Die Quelle misst das Einkommen **pro steuerpflichtiger Person**, nicht pro Einwohner. Kinder und andere nicht steuerpflichtige Personen sind damit nicht einfach im Nenner enthalten. Diesen bereits berechneten Wert aus Spalte D übernehmen wir; wir teilen ihn nicht nochmals durch die Einwohnerzahl.

Bevor wir den SVERWEIS einsetzen, prüfen wir den Hinweis aus der Aufgabe: Die `Regions-ID` ist als **Text** gespeichert, muss aber als **Zahl** vorliegen.

Gib dafür in eine freie Zelle, beispielsweise **F7**, diese Formel ein:

```excel
=ISTZAHL(A7)
```

Sie prüft den tatsächlichen Datentyp:

- **`WAHR`**: A7 enthält bereits eine Zahl.
- **`FALSCH`**: A7 enthält keine echte Zahl, auch wenn dort optisch `1` steht.

Bei englischer Excel-Funktionssprache lautet sie `=ISNUMBER(A7)`.

**Welches Ergebnis erhältst du: `WAHR` oder `FALSCH`?**

:codex-file-citation{path="/Users/leyla.erikci/Desktop/data_analytics/Week_03/fiscal_data.xlsx" purpose="source"}

> mach du das formeln funktonieren nicht im vs code

<details><summary>9 previous messages</summary>

> Ich übernehme die Excel-Schritte: Ich wandle die Gemeinde-IDs in Zahlen um und ergänze das Einkommen mit einer SVERWEIS-Formel. Die Dateien speichere ich direkt in deinem lokalen Projekt unter `Week_03`. Danach erkläre ich dir die Formel.
>
> <details><summary>Created a file, explored 4 files, 2 lists, ran 5 commands</summary>
>
> <details><summary>Explored 3 files</summary>
>
> - Read `/Users/leyla.erikci/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.1112.11217/skills/spreadsheets/SKILL.md`
> - Read `/Users/leyla.erikci/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.1112.11217/skills/spreadsheets/references/read_only_qna.md`
> - Read `/Users/leyla.erikci/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.1112.11217/skills/spreadsheets/workflows/edit_workflows.md`
>
> </details>
>
> - Ran `ls -la /Users/leyla.erikci/.cache/codex-runtimes/codex-primary-runtime/dependencies; ls -la /Users/leyla.erikci/.codex/plugins/cache/openai-primary-runtime; command -v node; command -v libreoffice; python3 - <<'PY'
> import importlib.util
> for m in ['openpyxl','PIL']:
>  print(m,bool(importlib.util.find_spec(m)))
> PY`
>
> <details><summary>Explored 2 files, 2 lists</summary>
>
> - Read `/Users/leyla.erikci/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.1112.11217/skills/spreadsheets/artifact_tool_docs/API_QUICK_START.md`
> - Read `/Users/leyla.erikci/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.1112.11217/skills/spreadsheets/style_guidelines.md`
> - Listed files in `node`
> - Listed files in `.codex`
>
> </details>
>
> - Ran `ls -ld /Users/leyla.erikci/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool; python3 - <<'PY'
> from openpyxl import load_workbook
> from pathlib import Path
> p=Path('/Users/leyla.erikci/Desktop/data_analytics/Week_03')
> for name in ['fiscal_data.xlsx','municipality_data.xlsx']:
>  w=load_workbook(p/name)
>  print(name,[(s.title,s.max_row,s.max_column) for s in w])
>  if name=='fiscal_data.xlsx':
>   s=w['Worksheet'];print('A7 type',s['A7'].data_type,repr(s['A7'].value));print('tail',list(s.values)[-12:])
> PY`
>
> - Ran `python3 - <<'PY'
> from openpyxl import load_workbook
> from collections import Counter
> from pathlib import Path
> p=Path('/Users/leyla.erikci/Desktop/data_analytics/Week_03')
> w=load_workbook(p/'municipality_data.xlsx');s=w['data_for_import']
> for row in s.iter_rows(min_row=1,max_row=5):print([(c.coordinate,c.value,c.data_type) for c in row])
> f=load_workbook(p/'fiscal_data.xlsx')['Worksheet'];ids={int(str(r[0])):r[3] for r in f.values if str(r[0]).isdigit()}
> keys=[r[0].value for r in s.iter_rows(min_row=2)]
> print('matched',sum(k in ids for k in keys),'unmatched',[(k) for k in keys if k not in ids][:30]);print('non_numeric_income',[(k,v) for k,v in ids.items() if not isinstance(v,(int,float))][:20]); print('duplicates',len(ids),sum(str(r[0]).isdigit() for r in f.values))
> PY`
>
> - Ran `mkdir -p /tmp/week03_excel_tools; ln -s /Users/leyla.erikci/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules /tmp/week03_excel_tools/node_modules`
>
> - Wrote `/tmp/week03_excel_tools/inspect.mjs` (+9 -0)
>
> - Ran `node /tmp/week03_excel_tools/inspect.mjs`
>
> </details>
>
> Viewed 2 images
>
> Die Gemeinde-IDs sind tatsächlich als Text gespeichert. Ich habe ausserdem fünf Gemeinden ohne passende ID in den Steuerdaten gefunden; einige Einkommenswerte sind aus Datenschutzgründen mit `X` markiert. Diese Angaben behandle ich nicht als null Franken. Für die Zuordnung hinterlege ich die benötigten Steuerdaten zusätzlich in derselben Arbeitsmappe, damit die Formel ohne externe Dateiverknüpfung funktioniert.
>
> <details><summary>Created a file, ran 3 commands</summary>
>
> - Ran `node /Users/leyla.erikci/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.1112.11217/skills/spreadsheets/container_tools/mark_artifact_operation_started.mjs --operation-kind edit --expected-output-count 2 --output-format xlsx`
> - Wrote `/tmp/week03_excel_tools/edit.mjs` (+45 -0)
> - Ran `node /tmp/week03_excel_tools/edit.mjs`
> - Ran `python3 - <<'PY'
> from pathlib import Path
> from openpyxl import load_workbook
> from collections import Counter
> import math
> base=Path('/Users/leyla.erikci/Desktop/data_analytics/Week_03');out=Path('/tmp/week03_excel_tools')
> for name in ['fiscal_data.xlsx','municipality_data.xlsx']:
>  before=load_workbook(base/name);after=load_workbook(out/name);diff=[]
>  for s in before:
>   a=after[s.title]
>   for row in s:
>    for c in row:
>     if name=='fiscal_data.xlsx' and c.column==1 and 7<=c.row<=2204:continue
>     if c.value!=a[c.coordinate].value:
>      if isinstance(c.value,(int,float)) and isinstance(a[c.coordinate].value,(int,float)) and math.isclose(c.value,a[c.coordinate].value,rel_tol=1e-12):continue
>      diff.append((s.title,c.coordinate,str(c.value)[:60],str(a[c.coordinate].value)[:60]))
>  print(name,'unexpected_value_differences',len(diff),diff[:8]);assert not diff
> w=load_workbook(out/'municipality_data.xlsx',data_only=True);s=w['data_for_import'];src=w['fiscal_data']
> lookup={r[0]:r[3] for r in src.iter_rows(min_row=2,values_only=True)}
> counts=Counter()
> for row in s.iter_rows(min_row=2,values_only=True):
>  expected=lookup.get(row[0]);actual=row[6]
>  if expected is None:assert actual in (None,'');counts['unmatched']+=1
>  elif isinstance(expected,str):assert actual==expected;counts['suppressed']+=1
>  else:assert math.isclose(actual,expected,rel_tol=1e-12);counts['numeric']+=1
> print('Verified lookup values:',dict(counts));print('First value',s['G2'].value)
> f=load_workbook(out/'municipality_data.xlsx')['data_for_import'];assert all(f.cell(r,7).data_type=='f' for r in range(2,2174));print('Verified formulas:',2172)
> PY`
>
> </details>
>
> Viewed 2 images
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> from pathlib import Path
> from openpyxl import load_workbook
> from collections import Counter
> import math
> base=Path('/Users/leyla.erikci/Desktop/data_analytics/Week_03');out=Path('/tmp/week03_excel_tools')
> for name in ['fiscal_data.xlsx','municipality_data.xlsx']:
>  before=load_workbook(base/name);after=load_workbook(out/name);diff=[]
>  for s in before:
>   a=after[s.title]
>   for row in s:
>    for c in row:
>     if name=='fiscal_data.xlsx' and c.column==1 and 7<=c.row<=2204:continue
>     if name=='municipality_data.xlsx' and s.title=='data_for_import' and c.column==7:continue
>     x,y=c.value,a[c.coordinate].value
>     if x!=y and not (isinstance(x,(int,float)) and isinstance(y,(int,float)) and math.isclose(x,y,rel_tol=1e-12)):diff.append((s.title,c.coordinate,x,y))
>  print(name,'unrelated value changes:',len(diff));assert not diff
> w=load_workbook(out/'municipality_data.xlsx',data_only=True);s=w['data_for_import'];lookup={r[0]:r[3] for r in w['fiscal_data'].iter_rows(min_row=2,values_only=True)};counts=Counter()
> for row in s.iter_rows(min_row=2,values_only=True):
>  expected=lookup.get(row[0]);actual=row[6]
>  if expected is None:assert actual in (None,'');counts['unmatched']+=1
>  elif isinstance(expected,str):assert actual==expected;counts['suppressed']+=1
>  else:assert math.isclose(actual,expected,rel_tol=1e-12);counts['numeric']+=1
> print('Verified lookup values:',dict(counts));print('First value',s['G2'].value)
> f=load_workbook(out/'municipality_data.xlsx')['data_for_import'];assert all(f.cell(r,7).data_type=='f' for r in range(2,2174));print('Verified formulas:',2172)
> s=load_workbook(out/'fiscal_data.xlsx')['Worksheet'];assert all(s.cell(r,1).data_type=='n' for r in range(7,2205));print('Numeric fiscal IDs:',2198)
> PY`
>
> </details>
>
> Die Zuordnung ist geprüft: 2’099 Gemeinden erhalten einen Zahlenwert, 68 behalten die Datenschutzmarkierung `X`, und bei fünf fehlt eine passende Gemeindenummer. Ich habe auch kontrolliert, dass die vorhandenen Datenwerte unverändert bleiben. Jetzt ersetze ich die beiden Dateien im Projekt durch die bearbeiteten Fassungen; die bisherigen Dateien sichere ich vorher.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `cp /Users/leyla.erikci/Desktop/data_analytics/Week_03/fiscal_data.xlsx /tmp/week03_excel_tools/fiscal_data.original.xlsx
> cp /Users/leyla.erikci/Desktop/data_analytics/Week_03/municipality_data.xlsx /tmp/week03_excel_tools/municipality_data.original.xlsx`
> - Ran `cp /tmp/week03_excel_tools/fiscal_data.xlsx /Users/leyla.erikci/Desktop/data_analytics/Week_03/fiscal_data.xlsx
> cp /tmp/week03_excel_tools/municipality_data.xlsx /Users/leyla.erikci/Desktop/data_analytics/Week_03/municipality_data.xlsx`
> - Ran `python3 - <<'PY'
> from pathlib import Path
> import hashlib
> from openpyxl import load_workbook
> p=Path('/Users/leyla.erikci/Desktop/data_analytics/Week_03')
> for n in ['municipality_data.xlsx','fiscal_data.xlsx']:
>  assert hashlib.sha256((p/n).read_bytes()).digest()==hashlib.sha256((Path('/tmp/week03_excel_tools')/n).read_bytes()).digest()
> s=load_workbook(p/'municipality_data.xlsx',data_only=True)['data_for_import']
> print('Saved in project; G1:',s['G1'].value,'G2:',s['G2'].value)
> PY`
>
> </details>
</details>

**Erledigt – beide Dateien sind direkt in deinem Projekt unter `Week_03` gespeichert.** Damit sind die Excel-Ergänzungen aus Aufgabe 2c–e umgesetzt.

Die Gemeinde-IDs sind jetzt Zahlen:

:codex-file-citation{path="/Users/leyla.erikci/Desktop/data_analytics/Week_03/fiscal_data.xlsx" purpose="output"}

Im Blatt `data_for_import` steht die neue Spalte **`mean_taxable_income`**. Das zusätzliche Blatt `fiscal_data` enthält die Quelldaten für die Formel:

:codex-file-citation{path="/Users/leyla.erikci/Desktop/data_analytics/Week_03/municipality_data.xlsx" purpose="output"}

Die Formel in **G2** entspricht auf Deutsch:

```excel
=WENNNV(SVERWEIS(A2;'fiscal_data'!$A$2:$D$2199;4;FALSCH);"")
```

Sie bedeutet:

- **`A2`**: Suche die Gemeindenummer dieser Zeile.
- **`$A$2:$D$2199`**: Durchsuche diesen festen Bereich im Quellenblatt.
- **`4`**: Gib den Wert der vierten Spalte zurück – Einkommen pro steuerpflichtiger Person.
- **`FALSCH`**: Verwende ausschliesslich eine exakte Übereinstimmung.
- **`WENNNV(...;"")`**: Wenn die Gemeinde nicht gefunden wird, lasse das Ergebnis leer.

Ich habe alle **2’172 Zuordnungen geprüft**: 2’099 Zahlenwerte, 68 Datenschutzmarkierungen `X` und fünf fehlende Zuordnungen. Die berechneten Ergebnisse sind mitgespeichert und damit auch für Python lesbar.

**Öffne die Datei im Viewer erneut**, damit du die neue Spalte siehst. Anschliessend übernehmen wir sie im Notebook mit `.merge()` in die Wohnungsdaten.

> ok

Jetzt bearbeiten wir **Aufgabe 2f–g**: Wir übernehmen das Einkommen aus den Gemeindedaten in die Wohnungstabelle.

**1. Gemeindedaten erneut einlesen**

Führe diese vorhandene Zelle nochmals aus:

```python
df_municip = pd.read_excel(
    'municipality_data.xlsx',
    sheet_name='data_for_import'
)

df_municip.head(5)
```

Das ist nötig, weil `df_municip` noch den früher eingelesenen Stand enthält. **Eine Änderung an der Excel-Datei aktualisiert eine bereits geladene Python-Tabelle nicht automatisch.**

Du solltest nun auch **`mean_taxable_income`** sehen.

**2. Die vorhandene Merge-Zelle ergänzen**

Im Abschnitt **„Join municipality data to rental apartment data using .merge()“** ergänzen wir die neue Spalte:

```python
# Gemeindeinformationen anhand der Gemeindenummer zuordnen
df3 = df2.merge(
    df_municip[[
        'bfs_number',
        'pop',
        'pop_dens',
        'frg_pct',
        'emp',
        'mean_taxable_income'
    ]],
    on='bfs_number'
)

df3.head(5)
```

Der Ablauf:

- **`df2`** enthält die Wohnungen samt Geodaten und Gemeindenummer.
- **`df_municip[[...]]`** wählt die Gemeindeinformationen aus, die wir hinzufügen möchten.
- **`on='bfs_number'`** ordnet jeder Wohnung die Informationen ihrer Gemeinde zu.
- **`df3`** speichert die angereicherte Wohnungstabelle.

**Wichtig für die Bedeutung:** Jede Wohnung derselben Gemeinde erhält denselben Einkommenswert. Dieser beschreibt das **durchschnittliche steuerbare Einkommen der steuerpflichtigen Personen in der Gemeinde** – nicht das Einkommen der Bewohner dieser konkreten Wohnung.

Die Gemeinde muss in der rechten Tabelle nur einmal stehen, darf aber vielen Wohnungen zugeordnet werden. Das nennt man eine **Viele-zu-eins-Verknüpfung**.

**Führe beide Zellen in dieser Reihenfolge aus. Siehst du anschliessend `mean_taxable_income` in `df3`?**

> ja, kurze frage, was ist nochmals dr3?

Du meinst **`df3`**: Das ist der **Variablenname unserer zuletzt erstellten Tabelle**.

In diesem Notebook bauen die Tabellen aufeinander auf:

| Variable | Inhalt |
|---|---|
| `df_orig` | Alle eingelesenen, vorbereiteten Wohnungsdaten |
| `df` | Daraus ausgewählte Spalten |
| `df_geo` | Separat eingelesene Geodaten |
| `df2` | Wohnungsdaten **mit Koordinaten und Gemeindezuordnung** |
| `df_municip` | Separat eingelesene Gemeindeinformationen |
| **`df3`** | Wohnungsdaten **mit Geodaten und Gemeindeinformationen, inklusive Einkommen** |

`df` ist eine gebräuchliche Abkürzung für **DataFrame**, also eine pandas-Tabelle. Die Zahl `3` hat für Python keine besondere Bedeutung – sie gehört einfach zum Namen.

Bei:

```python
df3 = df2.merge(...)
```

wird das Ergebnis der Verknüpfung unter dem Namen **`df3`** gespeichert. Danach können wir mit `df3` auf diese Tabelle zugreifen.

> weiter

Jetzt folgt die vorhandene Zelle **„Export data to file“**. Wir entfernen fehlende Werte und speichern die angereicherten Wohnungsdaten im Projekt.

```python
# Zeilen mit fehlenden Werten entfernen
df3 = df3.dropna()

# Verbleibende fehlende Werte pro Spalte zählen
print(df3.isna().sum())

# Anzahl Zeilen und Spalten anzeigen
print(df3.shape)

# Angereicherte Daten speichern
df3.to_csv(
    'apartments_data_enriched.csv',
    sep=',',
    encoding='utf-8'
)
```

**`df3 = df3.dropna()`** entfernt jede Zeile, in der mindestens ein Wert fehlt. Hier überschreiben wir `df3` mit dem bereinigten Ergebnis. Das betrifft nun auch Wohnungen, deren Gemeinde kein Einkommen zugeordnet werden konnte.

**Achtung:** Die Datenschutzmarkierung **`X`** ist Text und kein `NaN`. Solche Einträge werden durch `.dropna()` nicht entfernt.

Danach prüfen wir:

```python
print(df3.isna().sum())
```

Für jede Spalte sollte **`0`** erscheinen. Anschliessend zeigt `df3.shape`, wie viele Inserate und Spalten übrig sind.

**`df3.to_csv(...)`** speichert das Ergebnis als:

```text
Week_03/apartments_data_enriched.csv
```

Das funktioniert direkt im Projekt, weil dein Arbeitsordner jetzt der lokale Ordner `Week_03` ist. Eine vorhandene Datei gleichen Namens wird überschrieben.

Ein Detail des vorgegebenen Codes: Hier fehlt **`index=False`**. Deshalb werden die pandas-Zeilennummern als zusätzliche Spalte in der CSV gespeichert. Wir lassen den Code wie vorgegeben.

**Führe die Zelle aus und schicke mir die Ausgabe von `df3.shape`.** Dann gehen wir zur nächsten Notebook-Zelle weiter.

> web-scraper-order      0\
> address_raw            0\
> rooms                  0\
> area                   0\
> luxurious              0\
> price                  0\
> price_per_m2           0\
> lat                    0\
> lon                    0\
> bfs_number             0\
> bfs_name               0\
> pop                    0\
> pop_dens               0\
> frg_pct                0\
> emp                    0\
> mean_taxable_income    0\
> dtype: int64\
> (816, 16)

Deine Tabelle enthält jetzt **816 Inserate und 16 Spalten**. In keiner Spalte sind noch als fehlend erkannte Werte vorhanden. Die Daten wurden als `apartments_data_enriched.csv` im Projekt gespeichert, sofern die Zelle ohne Fehler durchgelaufen ist.

Die nächste vorhandene Zelle behandelt **„Sorting data“**, also das Sortieren:

```python
# Nach Preis und Fläche absteigend sortieren
df3.sort_values(
    by=['price', 'area'],
    ascending=False
).head()
```

So funktioniert sie:

- **`sort_values(...)`** sortiert anhand von Spaltenwerten.
- **`by=['price', 'area']`** legt die Reihenfolge der Sortierkriterien fest: zuerst Preis, bei gleichem Preis zusätzlich Fläche.
- **`ascending=False`** bedeutet absteigend: grosse Werte stehen oben.
- **`.head()`** zeigt die ersten fünf Zeilen des sortierten Ergebnisses.

Beispiel:

| Preis | Fläche |
|---:|---:|
| 5’000 | 120 |
| 5’000 | 80 |
| 4’500 | 150 |

Die Wohnung mit 150 m² steht hier hinter den beiden anderen, weil **der Preis das erste Kriterium ist**. Die Fläche entscheidet nur bei gleichem Preis.

**Wichtig:** Diese Zeile zeigt eine sortierte Tabelle an, verändert die Reihenfolge von `df3` aber nicht dauerhaft. Dafür müsste das Ergebnis wieder einer Variablen zugewiesen werden. Im vorgegebenen Code ist die Sortierung nur zur Ansicht gedacht.

**Führe die Zelle aus. Welcher Mietpreis steht ganz oben?**

> | 9950.0 |   |
> | ------ | - |

**9’950 CHF ist damit der höchste Mietpreis in unserer bereinigten Tabelle.** Falls mehrere Inserate diesen Preis haben, steht das mit der grössten Fläche zuerst.

Weiter mit der nächsten Zelle: Bitte kopiere den Code des folgenden Abschnitts hier hinein, damit wir genau der Reihenfolge deines Notebooks folgen.

> *# Aggregation using .groupby()*
> df3[['rooms', 'price']].groupby(['rooms']).mean()

Diese Zelle berechnet den **durchschnittlichen Mietpreis je Zimmerzahl**:

```python
df3[['rooms', 'price']].groupby(['rooms']).mean()
```

Wir lesen sie von links nach rechts:

1. **`df3[['rooms', 'price']]`** wählt die Spalten Zimmerzahl und Mietpreis aus.
2. **`.groupby(['rooms'])`** bildet Gruppen: Alle Inserate mit derselben Zimmerzahl kommen in dieselbe Gruppe.
3. **`.mean()`** berechnet innerhalb jeder Gruppe den durchschnittlichen Preis.

Ein kleines, erfundenes Beispiel:

| Zimmer | Preis |
|---:|---:|
| 2 | 1’500 |
| 2 | 2’000 |
| 3 | 2’400 |
| 3 | 2’800 |

Daraus entsteht:

| Zimmer | Durchschnittlicher Preis |
|---:|---:|
| 2 | 1’750 |
| 3 | 2’600 |

Für die Zweizimmerwohnungen wird beispielsweise gerechnet:

\[
\frac{1500 + 2000}{2} = 1750
\]

Das nennt man **Aggregation**: Viele einzelne Beobachtungen werden zu einem zusammenfassenden Wert pro Gruppe verdichtet.

**Wichtig:** `rooms` dient als Gruppenschlüssel und wird zum Index der Ergebnistabelle. Berechnet wird der Mittelwert von `price`. Die ursprüngliche Tabelle `df3` bleibt unverändert.

Führe die Zelle aus und schicke mir die Ausgabe. Dann interpretieren wir deine tatsächlichen Ergebnisse.

> |           |   **price** |
> | --------: | ----------: |
> | **rooms** |             |
> |       1.0 | 1306.346154 |
> |       1.5 | 2092.054054 |
> |       2.0 | 2138.775000 |
> |       2.5 | 2414.993056 |
> |       3.0 | 1950.434783 |
> |       3.5 | 2664.813084 |
> |       4.0 | 2798.200000 |
> |       4.5 | 3065.211765 |
> |       5.0 | 2773.750000 |
> |       5.5 | 3523.094340 |
> |       6.0 | 3833.333333 |
> |       6.5 | 3623.625000 |
> |       7.0 | 6350.000000 |
> |       7.5 | 4765.000000 |
> |       8.0 | 5500.000000 |
> |       8.5 | 8500.000000 |

Deine Tabelle zeigt den **durchschnittlichen Mietpreis je Zimmerzahl**. Zum Beispiel:

- **1 Zimmer:** rund **1’306 CHF**
- **3 Zimmer:** rund **1’950 CHF**
- **4,5 Zimmer:** rund **3’065 CHF**
- **8,5 Zimmer:** **8’500 CHF**

**Insgesamt steigen die Durchschnittspreise mit der Zimmerzahl, aber nicht durchgehend.** Beispielsweise sind Dreizimmerwohnungen in diesen Daten durchschnittlich günstiger als Zweizimmerwohnungen:

```text
2 Zimmer: rund 2’139 CHF
3 Zimmer: rund 1’950 CHF
```

Das ist kein Widerspruch: Wir vergleichen unterschiedliche Gruppen von Wohnungen. Auch Lage, Fläche, Zustand und Ausstattung beeinflussen den Preis. Aus dieser Tabelle allein können wir nicht erkennen, welcher dieser Faktoren die Unterschiede erklärt.

Zudem zeigt die Tabelle **nicht, wie viele Inserate in jeder Gruppe enthalten sind**. Ein Durchschnitt aus wenigen Wohnungen kann stark durch einzelne teure oder günstige Angebote geprägt sein.

**Für die Prüfung:** `.groupby(...).mean()` beschreibt Gruppenunterschiede. Es beweist nicht, dass eine zusätzliche Zimmerzahl allein eine bestimmte Preisänderung verursacht.

> weiter

<details><summary>2 previous messages</summary>

> Ich schaue nach der nächsten Zelle im Notebook, damit wir genau in der vorgegebenen Reihenfolge weitermachen.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> from pathlib import Path
> p=Path('/Users/leyla.erikci/Desktop/data_analytics/Week_03/combining_and_organizing_data.ipynb')
> n=json.loads(p.read_text())
> for i,c in enumerate(n['cells']):
>  s=''.join(c['source'])
>  if 'groupby' in s:
>   for j in range(max(0,i-1),min(len(n['cells']),i+7)):
>    print('CELL',j,n['cells'][j]['cell_type']);print(''.join(n['cells'][j]['source']))
> PY`
>
> </details>
</details>

Die nächste Zelle behandelt **`.stack()` und `.unstack()`**. Damit ändern wir die **Anordnung der Daten**, ohne neue Kennzahlen zu berechnen.

Führe die vorhandene Zelle aus:

```python
df_sub = df3[['bfs_name', 'rooms', 'price', 'area']][:5]

print('Original shape')
print(df_sub, '\n')

df_sub_stacked = df_sub.stack()

print('Stacked')
print(df_sub_stacked, '\n')

print('Unstacked (= back to original shape)')
print(df_sub_stacked.unstack())
```

Zuerst erstellen wir eine kleine Beispieltabelle:

```python
df_sub = df3[['bfs_name', 'rooms', 'price', 'area']][:5]
```

- Die doppelten Klammern wählen **vier Spalten** aus.
- **`[:5]`** nimmt die ersten fünf Zeilen.
- **`df_sub`** speichert diesen Ausschnitt.

**`.stack()` stapelt die Spaltenwerte untereinander.** Aus einer breiten Tabelle wie:

```text
   bfs_name  rooms  price  area
0  Zürich      3.0   2400  75.0
```

wird eine Series in dieser Form:

```text
0  bfs_name    Zürich
   rooms          3.0
   price         2400
   area          75.0
```

Jeder Wert erhält dabei einen **zweistufigen Index**, auch **MultiIndex** genannt:

1. ursprünglicher Zeilenindex, hier `0`;
2. ursprünglicher Spaltenname, beispielsweise `price`.

So bleibt erkennbar, zu welcher Wohnung und welchem Merkmal ein Wert gehört.

**`.unstack()` macht die letzte Indexebene wieder zu Spalten.** In diesem Beispiel entsteht dadurch wieder die ursprüngliche Tabellenanordnung.

Merke dir:

- **`groupby().mean()`** fasst Werte rechnerisch zusammen.
- **`stack()` und `unstack()`** ordnen Werte anders an.

**Führe die Zelle aus.** Siehst du zuerst die Tabelle, dann die untereinander angeordneten Werte und zum Schluss wieder die Tabellenform?

> ja

Als Nächstes folgt **„Reshaping data using `.melt()`“**. Auch damit werden Daten von einer breiten in eine lange Form gebracht.

Die vorhandene Zelle lautet:

```python
df_sub = df3[['rooms', 'price', 'area']][:5]

print('Original shape')
print(df_sub, '\n')

print('Reshaped using .melt()')
print(pd.melt(
    df,
    id_vars=['rooms'],
    value_vars=['price', 'area']
))
```

Der zentrale Aufruf ist:

```python
pd.melt(df, id_vars=['rooms'], value_vars=['price', 'area'])
```

- **`df`** ist die Tabelle, die umgeformt wird.
- **`id_vars=['rooms']`** behält die Zimmerzahl als Spalte bei.
- **`value_vars=['price', 'area']`** ordnet die Werte dieser beiden Spalten untereinander an.

Aus dieser beispielhaften Zeile:

| rooms | price | area |
|---:|---:|---:|
| 3.0 | 2400 | 75 |

werden zwei Zeilen:

| rooms | variable | value |
|---:|---|---:|
| 3.0 | price | 2400 |
| 3.0 | area | 75 |

**`variable`** enthält den ursprünglichen Spaltennamen, **`value`** den dazugehörigen Wert. Die Zimmerzahl wird wiederholt. Da zwei Spalten umgeformt werden, entstehen hier pro ursprünglicher Zeile zwei Ergebniszeilen.

Im Unterschied zu `.stack()` schreibt `.melt()` die Merkmalsnamen also in eine eigene Spalte statt in eine zusätzliche Indexebene.

**Ein Detail im vorgegebenen Code:** Oben wird `df_sub` aus den ersten fünf Zeilen von `df3` angezeigt. Der anschliessende `.melt()`-Aufruf verwendet aber **das gesamte `df`**, nicht `df_sub`. Deshalb ist die Ausgabe deutlich länger und basiert auf dem früheren Tabellenstand. Wir lassen das Beispiel wie vorgegeben.

**Führe die Zelle aus.** Danach kommen wir zur Pivot-Tabelle und den Ergänzungen aus Aufgabe 3.

> weiter

<details><summary>2 previous messages</summary>

> Ich prüfe das vorgegebene Pivot-Beispiel. Darauf bauen wir anschliessend die Teilaufgaben von Aufgabe 3 auf.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> p='/Users/leyla.erikci/Desktop/data_analytics/Week_03/combining_and_organizing_data.ipynb'
> with open(p) as f:n=json.load(f)
> for i,c in enumerate(n['cells'][25:],25):
>  print('CELL',i,c['cell_type']);print(''.join(c['source']))
> PY`
>
> </details>
</details>

Jetzt beginnen wir **Aufgabe 3a–b**: Wir verwenden das vorbereitete Notebook aus Aufgabe 2 und verstehen das vorhandene **Pivot-Beispiel**.

Eine **Pivot-Tabelle** fasst Daten nach Gruppen zusammen. Hier berechnen wir Durchschnittswerte je Zimmerzahl – ähnlich wie zuvor mit `.groupby()`.

Führe die vorhandene Zelle aus:

```python
pd.pivot_table(
    df3[['rooms', 'price', 'area']],
    index=['rooms'],
    values=['price', 'area', 'rooms'],
    aggfunc=(np.mean)
)
```

Die Bestandteile:

| Bestandteil | Bedeutung |
|---|---|
| `df3[['rooms', 'price', 'area']]` | Wählt die Daten für die Berechnung aus |
| `index=['rooms']` | Erstellt eine Ergebniszeile je Zimmerzahl |
| `values=[...]` | Gibt die auszuwertenden Spalten an |
| `aggfunc=np.mean` | Berechnet den arithmetischen Mittelwert |

Für jede Zimmergruppe werden also die **durchschnittliche Fläche und der durchschnittliche Mietpreis** berechnet.

`rooms` steht im vorgegebenen Code zusätzlich in `values`. Da diese Spalte bereits zum Gruppieren dient, ist die zusätzliche Angabe hier überflüssig; sie erscheint nicht als eigene Mittelwertspalte.

Der Unterschied zur vorherigen Auswertung:

```python
df3[['rooms', 'price']].groupby(['rooms']).mean()
```

Wir betrachten nun zusätzlich die **Fläche**. So können wir später besser verstehen, weshalb sich die Mietpreise zwischen den Gruppen unterscheiden.

**Führe zunächst das unveränderte Beispiel aus und schicke mir die Ausgabe.** Danach ergänzen wir gemäss **Aufgabe 3c** den Quadratmeterpreis.

> |           |   **area** |   **price** |
> | --------: | ---------: | ----------: |
> | **rooms** |            |             |
> |       1.0 |  32.057692 | 1306.346154 |
> |       1.5 |  35.972973 | 2092.054054 |
> |       2.0 |  54.475000 | 2138.775000 |
> |       2.5 |  67.340278 | 2414.993056 |
> |       3.0 |  67.956522 | 1950.434783 |
> |       3.5 |  89.500000 | 2664.813084 |
> |       4.0 |  96.900000 | 2798.200000 |
> |       4.5 | 114.670588 | 3065.211765 |
> |       5.0 | 103.500000 | 2773.750000 |
> |       5.5 | 153.811321 | 3523.094340 |
> |       6.0 | 667.666667 | 3833.333333 |
> |       6.5 | 248.375000 | 3623.625000 |
> |       7.0 | 175.000000 | 6350.000000 |
> |       7.5 | 205.000000 | 4765.000000 |
> |       8.0 | 160.000000 | 5500.000000 |
> |       8.5 | 210.000000 | 8500.000000 |

Die Pivot-Tabelle zeigt nun je Zimmerzahl die **durchschnittliche Fläche** und den **durchschnittlichen Mietpreis**. Dreizimmerwohnungen haben beispielsweise im Mittel rund **68 m²** und kosten **1’950 CHF**.

Auffällig sind die **667,67 m² bei sechs Zimmern**. Das könnte durch besonders grosse Wohnungen oder fehlerhafte Flächenangaben entstehen. Aus dieser Zusammenfassung allein können wir die Ursache nicht bestimmen.

Jetzt lösen wir **Aufgabe 3c**: den Quadratmeterpreis zur bestehenden Pivot-Tabelle hinzufügen.

Ergänze die Zelle so:

```python
pd.pivot_table(
    df3[['rooms', 'price', 'area', 'price_per_m2']],
    index=['rooms'],
    values=['price', 'area', 'rooms', 'price_per_m2'],
    aggfunc=(np.mean)
)
```

**`price_per_m2` muss an zwei Stellen ergänzt werden:**

- In der ersten Spaltenauswahl, damit die Daten der Funktion zur Verfügung stehen.
- In `values`, damit der Mittelwert dieser Spalte berechnet wird.

Die neue Ergebnisspalte zeigt dann den **Durchschnitt der einzelnen Quadratmeterpreise** innerhalb jeder Zimmergruppe.

**Wichtig:** Das ist nicht zwingend dasselbe wie „durchschnittlicher Mietpreis geteilt durch durchschnittliche Fläche“. Hier zählt jede Wohnung gleich stark zum Mittelwert ihrer Quadratmeterpreise.

**Führe die ergänzte Zelle aus und schicke mir die Tabelle.** Damit vergleichen wir anschliessend gemäss Aufgabe 3d–e Mietpreis, Fläche und Quadratmeterpreis.

> |           |   **area** |   **price** | **price_per_m2** |
> | --------: | ---------: | ----------: | ---------------: |
> | **rooms** |            |             |                  |
> |       1.0 |  32.057692 | 1306.346154 |        50.168077 |
> |       1.5 |  35.972973 | 2092.054054 |        64.345676 |
> |       2.0 |  54.475000 | 2138.775000 |        42.201750 |
> |       2.5 |  67.340278 | 2414.993056 |        37.184861 |
> |       3.0 |  67.956522 | 1950.434783 |        28.567609 |
> |       3.5 |  89.500000 | 2664.813084 |        29.711355 |
> |       4.0 |  96.900000 | 2798.200000 |        29.482000 |
> |       4.5 | 114.670588 | 3065.211765 |        26.399941 |
> |       5.0 | 103.500000 | 2773.750000 |        26.587500 |
> |       5.5 | 153.811321 | 3523.094340 |        23.143396 |
> |       6.0 | 667.666667 | 3833.333333 |        15.706667 |
> |       6.5 | 248.375000 | 3623.625000 |        19.385625 |
> |       7.0 | 175.000000 | 6350.000000 |        36.325000 |
> |       7.5 | 205.000000 | 4765.000000 |        23.273333 |
> |       8.0 | 160.000000 | 5500.000000 |        34.380000 |
> |       8.5 | 210.000000 | 8500.000000 |        40.480000 |

Damit ist **Aufgabe 3c erledigt**. Jetzt interpretieren wir die Tabelle für **3d–e**.

**3d: Mietpreis und Quadratmeterpreis vergleichen**

Wohnungen mit mehr Zimmern kosten insgesamt meist mehr. Ihr Preis pro Quadratmeter ist aber häufig niedriger:

| Zimmer | Durchschnittliche Fläche | Durchschnittlicher Mietpreis | Durchschnittlicher Preis/m² |
|---:|---:|---:|---:|
| 1,5 | 35,97 m² | 2’092 CHF | 64,35 CHF |
| 3,5 | 89,50 m² | 2’665 CHF | 29,71 CHF |
| 5,5 | 153,81 m² | 3’523 CHF | 23,14 CHF |

Eine grössere Wohnung kann also **insgesamt teurer**, aber **pro Quadratmeter günstiger** sein.

**3e: Zusammenhang zwischen Fläche und Quadratmeterpreis**

Die Gruppenmittelwerte deuten darauf hin: **Mit zunehmender Fläche sinkt der Quadratmeterpreis häufig.** Der Verlauf ist allerdings nicht durchgehend; beispielsweise liegen die Werte bei 7 bis 8,5 Zimmern wieder höher.

Eine mögliche Erklärung: Kleine Wohnungen benötigen ebenfalls Küche und Bad. Deren Kosten verteilen sich auf weniger Quadratmeter. Auch Lage, Ausstattung und die Zusammensetzung der angebotenen Wohnungen können die Unterschiede beeinflussen. Die Tabelle allein beweist keine Ursache.

Die auffällige Durchschnittsfläche von **667,67 m² bei sechs Zimmern** sollten wir bei der Interpretation im Hinterkopf behalten.

Füge **direkt unter der Pivot-Tabelle eine Markdown-Zelle** mit dieser geforderten kurzen Erklärung ein:

```markdown
Die Pivot-Tabelle zeigt, dass der durchschnittliche Mietpreis mit
zunehmender Zimmerzahl überwiegend steigt. Der durchschnittliche
Quadratmeterpreis sinkt dagegen bei vielen Gruppen mit zunehmender
Wohnfläche, allerdings nicht durchgehend.

Eine mögliche Erklärung ist, dass sich die Kosten für Küche und Bad
bei grösseren Wohnungen auf mehr Quadratmeter verteilen. Auch Lage
und Ausstattung können die Unterschiede beeinflussen. Die gruppierten
Mittelwerte belegen keinen ursächlichen Zusammenhang. Auffällige
Flächenwerte können die Ergebnisse zusätzlich beeinflussen.
```

Speichere das Notebook mit **Cmd + S**. Danach folgt **3f: die Anzahl der Inserate je Gruppe mit `aggfunc='count'` untersuchen**.

> weiter

Jetzt lösen wir **Aufgabe 3f**: eine neue Pivot-Tabelle mit **`aggfunc='count'`** erstellen und die Anzahl der Wohnungen je Zimmergruppe untersuchen.

Füge unter deiner Erklärung eine neue **Codezelle** ein:

```python
# Anzahl der Inserate je Zimmerzahl
pd.pivot_table(
    df3,
    index=['rooms'],
    values=['price'],
    aggfunc='count'
)
```

Die Gruppierung bleibt gleich, aber die Berechnung ändert sich:

- **`index=['rooms']`** bildet eine Gruppe je Zimmerzahl.
- **`values=['price']`** wählt die Spalte aus, deren vorhandene Werte gezählt werden.
- **`aggfunc='count'`** zählt diese Werte, statt ihren Durchschnitt zu berechnen.

**Warum zählen wir `price`?** In unserer bereinigten Tabelle hat jedes Inserat einen Preis. Deshalb entspricht die Anzahl der Preiswerte der Anzahl der Inserate in der Gruppe.

Die Ergebnisspalte heisst weiterhin **`price`**, enthält nun aber **Anzahlen, keine Mietpreise**. Das ist wichtig beim Lesen der Tabelle.

Mit diesen Häufigkeiten können wir auch die vorherigen Mittelwerte besser beurteilen: Ein Durchschnitt aus zwei Inseraten ist stärker von einzelnen Angeboten abhängig als einer aus hundert Inseraten.

**Führe die Zelle aus und schicke mir die Tabelle.** Daraus formulieren wir die von der Aufgabe verlangte kurze Beschreibung fürs Notebook.

> |           | **price** |
> | --------: | --------: |
> | **rooms** |           |
> |       1.0 |        52 |
> |       1.5 |        37 |
> |       2.0 |        40 |
> |       2.5 |       144 |
> |       3.0 |        46 |
> |       3.5 |       214 |
> |       4.0 |        30 |
> |       4.5 |       170 |
> |       5.0 |         4 |
> |       5.5 |        53 |
> |       6.0 |         3 |
> |       6.5 |        16 |
> |       7.0 |         2 |
> |       7.5 |         3 |
> |       8.0 |         1 |
> |       8.5 |         1 |

Am häufigsten sind **3,5-Zimmer-Wohnungen mit 214 Inseraten**, gefolgt von **4,5 Zimmern mit 170** und **2,5 Zimmern mit 144 Inseraten**.

Zusammen sind das **528 von 816 Inseraten**, also rund **64,7 %**.

Die grossen Zimmergruppen enthalten dagegen teilweise nur ein bis drei Inserate. Deshalb müssen wir ihre Durchschnittspreise vorsichtig interpretieren: Bei **8,5 Zimmern** sind die zuvor angezeigten **8’500 CHF** beispielsweise der Preis **einer einzigen Wohnung**.

Füge unter der Häufigkeitstabelle diese **Markdown-Zelle** ein:

```markdown
Am häufigsten sind Wohnungen mit 3,5 Zimmern (214 Inserate),
4,5 Zimmern (170) und 2,5 Zimmern (144). Diese drei Gruppen machen
zusammen rund 64,7 % der 816 Inserate aus.

Wohnungen mit vielen Zimmern sind deutlich seltener vertreten.
Die Gruppen mit 8 und 8,5 Zimmern enthalten jeweils nur ein Inserat.
Ihre Durchschnittswerte sind daher wenig aussagekräftig für das
allgemeine Angebot.
```

Damit ist **Aufgabe 3f erledigt**.

Nun folgt **3g**: Durchschnittswerte **pro Gemeinde** berechnen und nach Mietpreis und Fläche absteigend sortieren.

Füge eine neue **Codezelle** ein:

```python
# Durchschnittswerte pro Gemeinde berechnen
pivot_municipality = pd.pivot_table(
    df3,
    index=['bfs_name'],
    values=['rooms', 'area', 'price', 'price_per_m2'],
    aggfunc='mean'
)

# Zuerst nach Mietpreis, bei gleichem Mietpreis nach Fläche sortieren
pivot_municipality = pivot_municipality.sort_values(
    by=['price', 'area'],
    ascending=False
)

pivot_municipality
```

Hier ändern wir den Gruppenschlüssel von **`rooms`** zu **`bfs_name`**. Jede Ergebniszeile beschreibt jetzt eine Gemeinde und enthält die Durchschnittswerte ihrer inserierten Wohnungen.

**Die Gemeinde mit dem höchsten durchschnittlichen Mietpreis steht oben.** Nur bei gleichem Durchschnittspreis entscheidet zusätzlich die durchschnittliche Fläche.

Führe die Zelle aus und schicke mir die ersten Zeilen.

> |                |   **area** |   **price** | **price_per_m2** | **rooms** |
> | -------------: | ---------: | ----------: | ---------------: | --------: |
> |   **bfs_name** |            |             |                  |           |
> |     Rüschlikon | 144.000000 | 6660.000000 |        46.250000 |       4.5 |
> |  Küsnacht (ZH) | 136.333333 | 4891.666667 |        35.476667 |       4.5 |
> |     Nürensdorf | 506.500000 | 4500.000000 |        17.605000 |       6.0 |
> |           Maur | 138.500000 | 4250.000000 |        30.445000 |       4.5 |
> |       Obfelden | 127.500000 | 4095.000000 |        31.910000 |       5.5 |
> |            ... |        ... |         ... |              ... |       ... |
> | Weiningen (ZH) |  73.333333 | 1606.666667 |        20.716667 |       3.0 |
> |      Dättlikon |  90.000000 | 1480.000000 |        16.440000 |       4.0 |
> |         Weiach |  46.000000 | 1420.000000 |        30.870000 |       1.5 |
> |     Herrliberg |  18.000000 | 1150.000000 |        63.890000 |       1.0 |
> | Uetikon am See | 300.000000 |   11.000000 |         0.040000 |       6.5 |
>
> 108 rows × 4 columns

**Aufgabe 3g ist korrekt umgesetzt:** Die Tabelle enthält **108 Gemeinden**, sortiert nach dem durchschnittlichen Mietpreis absteigend. Bei gleichem Preis würde die durchschnittliche Fläche entscheiden.

**Rüschlikon steht mit durchschnittlich 6’660 CHF oben.** Das gilt für die Inserate in unserem Datensatz, nicht automatisch für den gesamten Wohnungsmarkt der Gemeinde.

Auffällig ist **Uetikon am See**:

- durchschnittliche Fläche: **300 m²**
- durchschnittlicher Preis: **11 CHF**
- durchschnittlicher Quadratmeterpreis: **0,04 CHF**

Das ist für eine Wohnung sehr unplausibel und deutet auf einen Fehler in den Ausgangsdaten oder der Preisextraktion hin. **Ein vorhandener Zahlenwert kann trotzdem falsch sein** – `.dropna()` erkennt solche Probleme nicht. Wir ändern jetzt nichts zusätzlich, da die Aufgabe das nicht verlangt.

Damit sind die **inhaltlichen Teilaufgaben von Week_03 abgeschlossen**. Zum Abschluss:

1. Führe die letzte **Footer-Infozelle** aus.
2. Speichere das Notebook mit **Cmd + S**, damit Code, Erklärungen und Ausgaben im Projekt erhalten bleiben.

Ein wichtiger Lernpunkt aus der letzten Tabelle: **Eine technisch korrekte Auswertung braucht zusätzlich eine Plausibilitätsprüfung der Ergebnisse.**
