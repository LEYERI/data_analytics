# Weiter mit Week_04

> Nun gehts weiter mit Aufgabe Week_04

<details><summary>4 previous messages</summary>

> Ich schaue im Projekt nach den Unterlagen zu Week_04 und dem bisherigen Stand.
>
> <details><summary>Explored a file, ran a command</summary>
>
> - Ran `pwd; rg --files -g 'AGENTS.md' -g '*Week*' -g '*week*' -g '*.ipynb' -g 'README*' -g '*.pdf' -g '*.md'`
>
> <details><summary>Explored 2 files</summary>
>
> - Read `~/.codex/plugins/cache/openai-primary-runtime/pdf/26.1112.11217/skills/pdf/SKILL.md`
> - Read `./Week_03/Chatverlauf_Week_03.md`
>
> </details>
>
> </details>
>
> Wir machen wie bei Week_03 Schritt für Schritt weiter, mit Erklärungen zum Code und zu den Ergebnissen. Ich nutze den PDF-Skill, um die Aufgabenstellung zu lesen.
>
> <details><summary>Ran 6 commands</summary>
>
> - Ran `python3 - <<'PY'
> import json
> from pypdf import PdfReader
> for p in PdfReader('Week_04/Excercises_Week_04.pdf').pages:
>  print(p.extract_text())
> for name in ['graphics_with_matplotlib','exploratory_data_analysis_apartment_data']:
>  print('\nNOTEBOOK:',name)
>  n=json.load(open('Week_04/'+name+'.ipynb'))
>  for i,c in enumerate(n['cells'][:9]):
>   print(i,c['cell_type'],''.join(c['source'])[:2500])
> PY`
> - Ran `ls -a; command -v pdftotext; python3 - <<'PY'
> import json,importlib.util
> for m in ['pdfplumber','fitz','PyPDF2']:
>  print(m, bool(importlib.util.find_spec(m)))
> for name in ['graphics_with_matplotlib','exploratory_data_analysis_apartment_data']:
>  print('\nNOTEBOOK:',name)
>  n=json.load(open('Week_04/'+name+'.ipynb'))
>  for i,c in enumerate(n['cells'][:7]):
>   print(i,c['cell_type'],''.join(c['source'])[:1800])
> PY`
> - Ran `ls /Users/leyla.erikci/.codex; ls /usr/bin/*pdf* /opt/homebrew/bin/*pdf* 2>/dev/null; ls Week_04; ls /Users/leyla.erikci/.local/share/uv/tools 2>/dev/null`
> - Ran `python3 -m pip install --target /tmp/week04_pdf_reader pypdf`
> - Ran `python3 -m pip install --target /tmp/week04_pdf_reader pypdf`
> - Ran `PYTHONPATH=/tmp/week04_pdf_reader python3 - <<'PY'
> from pypdf import PdfReader
> for p in PdfReader('Week_04/Excercises_Week_04.pdf').pages:
>  print(p.extract_text())
> PY`
>
> </details>
</details>

Wir machen **Week_04 wieder Schritt für Schritt**, damit du den Code verstehst und die Ergebnisse selbst erklären kannst.

Die Aufgaben behandeln **explorative Datenanalyse (EDA)**: Wir untersuchen Daten mit Kennzahlen und Grafiken, um Muster und auffällige Werte zu entdecken. Zuerst lernen wir Matplotlib kennen, danach untersuchen wir Wohnungsdaten und Supermärkte. Die Aufgaben stehen hier: :codex-file-citation{path="/Users/leyla.erikci/Desktop/data_analytics/Week_04/Excercises_Week_04.pdf" purpose="source"}

Wir beginnen mit **Aufgabe 1a: Bibliotheken laden**.

Öffne [graphics_with_matplotlib.ipynb](./Week_04/graphics_with_matplotlib.ipynb) in VS Code. Die erste Codezelle enthält:

```python
# Libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle
```

| Code | Bedeutung |
|---|---|
| `import os` | Ermöglicht den Zugriff auf den aktuellen Arbeitsordner. |
| `import numpy as np` | Lädt Funktionen für Zahlen und Zahlenreihen. |
| `import matplotlib.pyplot as plt` | Lädt Funktionen zum Erstellen und Gestalten von Diagrammen. |
| `import matplotlib.colors as mcolors` | Stellt Werkzeuge für Farben bereit. |
| `from matplotlib.patches import Rectangle` | Importiert gezielt `Rectangle`, um Rechtecke zu zeichnen. |

**`as plt` ist ein Kurzname.** Statt `matplotlib.pyplot.plot(...)` schreiben wir später einfach `plt.plot(...)`.

Danach folgt:

```python
import warnings
warnings.filterwarnings("ignore")
```

Das blendet Warnungen aus. Fehlermeldungen werden weiterhin angezeigt. Zum Lernen kannst du die zweite Zeile mit `#` auskommentieren, damit Warnungen sichtbar bleiben.

```python
print(os.getcwd())
```

`os.getcwd()` ermittelt den aktuellen Arbeitsordner; `print(...)` zeigt ihn an. **Diese Zelle erstellt noch kein Diagramm**, sondern bereitet die benötigten Werkzeuge vor.

**Führe die erste Codezelle mit Shift + Enter aus und schicke mir die Ausgabe.** Anschliessend schauen wir uns die Bestandteile eines Diagramms an.

> /Users/leyla.erikci/Desktop/data_analytics/Week_04

Das ist der erwartete Arbeitsordner: **`Week_04`**. Damit wurde die erste Zelle erfolgreich ausgeführt.

Im Notebook folgt **„Parts of a graphic in matplotlib“** mit einer Abbildung der Diagrammbestandteile. Die wichtigsten Begriffe sind:

| Begriff | Bedeutung |
|---|---|
| **Figure** | Die gesamte Zeichenfläche, die auch mehrere Diagramme enthalten kann. |
| **Axes** | Ein einzelner Diagrammbereich mit Daten und Koordinatensystem. |
| **Axis** | Eine einzelne Achse, beispielsweise die x- oder y-Achse. |
| **Title** | Der Titel des Diagramms. |
| **Label** | Die Beschriftung einer Achse, etwa „Fläche in m²“. |
| **Ticks** | Die Markierungen auf den Achsen, etwa bei 0, 10 und 20. |
| **Legend** | Die Legende, die Farben oder Symbole erklärt. |
| **Marker** | Ein Symbol für einen Datenpunkt, beispielsweise ein Kreis. |

**Merke dir besonders den Unterschied zwischen `Figure` und `Axes`:** Die Figure ist wie ein Blatt Papier. Die Axes sind die einzelnen Diagramme auf diesem Blatt.

Später begegnet uns:

```python
fig, ax = plt.subplots()
```

Damit erzeugen wir eine **Figure** namens `fig` und einen **Diagrammbereich** namens `ax`. Über diese Namen können wir beide gezielt gestalten.

Schau dir jetzt die Abbildung im Notebook an und ordne die Begriffe zu. **Falls das Bild nicht angezeigt wird, sag kurz Bescheid.** Danach gehen wir zum Abschnitt **„Named colors supported in matplotlib“** weiter.

> Habe "**## Named colors supported in matplotlib" ausgeführt**

<details><summary>2 previous messages</summary>

> Ich schaue kurz in die ausgeführte Zelle, damit ich dir den Code und die Farbübersicht genau erklären kann.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/graphics_with_matplotlib.ipynb'))
> for i,c in enumerate(n['cells'][6:13],6):
>  print(i,c['cell_type'],''.join(c['source']))
> PY`
>
> </details>
</details>

Jetzt solltest du drei Farbübersichten sehen: **Base Colors**, **Tableau Palette** und **CSS Colors**.

Der Zweck dieser Zelle ist: **Du kannst Farben auswählen und ihre Namen später im Diagramm verwenden**, zum Beispiel:

```python
color='orangered'
```

Die lange Zelle baut diese Übersicht selbst auf. Die wichtigsten Teile:

```python
def plot_colortable(colors, title, sort_colors=True, emptycols=0):
```

Mit **`def`** definieren wir eine eigene Funktion namens `plot_colortable`. Sie erhält eine Farbsammlung und einen Titel. `sort_colors=True` legt fest, dass die Farben standardmässig sortiert werden.

Innerhalb der Funktion passiert Folgendes:

| Code | Zweck |
|---|---|
| `plt.subplots(...)` | Erstellt Zeichenfläche und Diagrammbereich. |
| `ax.set_axis_off()` | Blendet die Achsen aus, weil eine Farbtabelle keine benötigt. |
| `ax.set_title(...)` | Setzt die Überschrift. |
| `for i, name in enumerate(names):` | Durchläuft alle Farbnamen mit ihrer jeweiligen Positionsnummer. |
| `ax.text(...)` | Schreibt einen Farbnamen in die Übersicht. |
| `Rectangle(..., facecolor=colors[name], ...)` | Erstellt das dazugehörige farbige Rechteck. |
| `ax.add_patch(...)` | Fügt das Rechteck zum Diagrammbereich hinzu. |
| `return fig` | Gibt die erstellte Figure zurück. |

**Die Definition allein zeichnet noch nichts.** Erst diese Aufrufe führen die Funktion für die drei Farbsammlungen aus:

```python
plot_colortable(mcolors.BASE_COLORS, "Base Colors",
                sort_colors=False, emptycols=1)

plot_colortable(mcolors.TABLEAU_COLORS, "Tableau Palette",
                sort_colors=False, emptycols=2)

plot_colortable(mcolors.CSS4_COLORS, "CSS Colors")
```

Beim letzten Aufruf fehlt `sort_colors`. Deshalb gilt dort der Standardwert **`True`**: Die CSS-Farben werden nach Farbton, Sättigung und Helligkeit sortiert.

Für die kommenden Aufgaben musst du diese aufwendige Farbtabelle noch nicht selbst programmieren können. Entscheidend ist, dass du **Farbnamen als Text angeben kannst**, etwa `'green'`, `'orange'` oder `'deepskyblue'`.

**Führe jetzt die nächste Codezelle unter „Marker symbols“ aus.** Dort sehen wir, wie sich die Symbole der Datenpunkte verändern lassen.

> ja

Die Grafik unter **„Marker symbols“** zeigt verschiedene Symbole für Datenpunkte. Die Legende ordnet jedem Symbol seinen Code zu.

Gehen wir die Zelle durch:

```python
rng = np.random.RandomState(0)
```

Erstellt einen **Zufallszahlengenerator**. Die `0` ist der Startwert (*Seed*). Mit demselben Startwert entsteht bei jedem erneuten Ausführen dieselbe Zahlenfolge – die Grafik bleibt dadurch reproduzierbar.

```python
plt.figure(figsize=(7, 4))
```

Erstellt eine Zeichenfläche mit **7 Zoll Breite und 4 Zoll Höhe**.

```python
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
```

Die Schleife durchläuft die Symbole nacheinander. Bei jedem Durchlauf bekommt die Variable `marker` einen anderen Wert:

| Code | Symbol |
|---|---|
| `'o'` | Kreis |
| `'.'` | Punkt |
| `'x'` | Kreuz |
| `'+'` | Plus |
| `'v'`, `'^'`, `'<'`, `'>'` | Dreiecke in verschiedene Richtungen |
| `'s'` | Quadrat |
| `'d'` | Schmale Raute |

Innerhalb der Schleife steht:

```python
plt.plot(
    rng.rand(5),
    rng.rand(5),
    marker,
    label="marker='{0}'".format(marker),
    markersize=10
)
```

- Das erste **`rng.rand(5)`** erzeugt fünf zufällige x-Werte zwischen 0 und 1.
- Das zweite erzeugt die fünf zugehörigen y-Werte.
- **`marker`** bestimmt das Symbol dieser fünf Punkte.
- **`label`** legt den Text für die Legende fest. `.format(marker)` ersetzt `{0}` durch den aktuellen Symbolcode.
- **`markersize=10`** bestimmt die Symbolgrösse.

**Jeder Schleifendurchlauf zeichnet also fünf neue Punkte mit einem anderen Symbol.**

Zum Schluss:

```python
plt.legend(numpoints=1, fontsize=10)
plt.xlim(0, 1.5)
```

`plt.legend(...)` zeigt die Legende mit Schriftgrösse 10 und einem Beispielmarker pro Eintrag. `plt.xlim(0, 1.5)` setzt den sichtbaren Bereich der x-Achse auf 0 bis 1,5. Die Daten liegen nur zwischen 0 und 1; rechts bleibt dadurch Platz für die Legende.

**Kleine Übung:** Ändere `markersize=10` auf `markersize=15` und führe die Zelle erneut aus. Die Punkte sollten grösser werden, während ihre Positionen wegen des festen Seeds gleich bleiben.

> ja genau ist grösser geworden

Genau: **`markersize` verändert die Symbolgrösse**, während die Datenwerte und damit die Positionen gleich bleiben.

Weiter geht’s mit **„Scatterplot with individual marker symbols“**. Ein **Scatterplot (Streudiagramm)** zeigt Wertepaare als Punkte: Jeder Punkt hat einen x- und einen y-Wert.

Zuerst werden die Daten definiert:

```python
x = [10, 12, 15, 18, 20, 24, 28, 32, 38, 42]
y = [8, 9, 11, 14, 16, 18, 22, 25, 32, 34]
```

Die Werte werden nach ihrer Position gepaart: Der erste Punkt liegt bei **(10, 8)**, der zweite bei **(12, 9)** usw.

Danach entstehen drei weitere Datenreihen:

```python
z = list(map(lambda x : x*1.2, y))
g = list(map(lambda x : x*0.8, y))
e = list(map(lambda x : x*0.6, y))
```

Die erste Zeile bedeutet: **Multipliziere jeden Wert aus `y` mit 1,2 und speichere die Ergebnisse als Liste `z`.**

- **`lambda x: x*1.2`** ist eine kleine Funktion.
- **`map(..., y)`** wendet sie auf jeden Wert von `y` an.
- **`list(...)`** sammelt die Ergebnisse in einer Liste.

Das `x` innerhalb von `lambda` ist nur ein lokaler Platzhalter und unabhängig von unserer Liste `x`. Verständlicher könnte dieselbe Zeile so aussehen:

```python
z = list(map(lambda wert: wert * 1.2, y))
```

Damit sind die Werte in `z` **20 % höher**, in `g` **20 % niedriger** und in `e` **40 % niedriger** als in `y`.

Die Punkte werden anschliessend gezeichnet:

```python
plt.figure(figsize=(7, 4))

scatter_01 = plt.scatter(x, y, s=100, marker='o', color='orangered')
scatter_02 = plt.scatter(x, z, s=100, marker='+', color='green')
scatter_03 = plt.scatter(x, g, s=100, marker='*', color='deepskyblue')
scatter_04 = plt.scatter(x, e, s=100, marker='^', color='orange')

plt.show()
```

Alle vier Reihen verwenden **dieselben x-Werte**, aber unterschiedliche y-Werte, Symbole und Farben.

**Achtung bei der Grösse:** Bei `plt.scatter()` bezeichnet **`s` die Markerfläche in Punkten²**. Bei `plt.plot()` haben wir dagegen `markersize` verwendet. Die Zahlen sind deshalb nicht direkt vergleichbar.

**Führe diese Zelle aus.** Du solltest vier Punktreihen sehen; die grünen Pluszeichen liegen jeweils am höchsten, die orangefarbenen Dreiecke am tiefsten.

> ja

<details><summary>2 previous messages</summary>

> Ich schaue mir die nächste Zelle zur Achsenformatierung an.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/graphics_with_matplotlib.ipynb'))
> for i,c in enumerate(n['cells'][12:16],12):
>  print(i,c['cell_type'],''.join(c['source']))
> PY`
>
> </details>
</details>

Jetzt folgt **„Formatting axes and setting limits and ticks“**. Die Daten bleiben gleich; wir ergänzen Titel, Achsenbeschriftungen und eine passende Skalierung.

**1. Titel und Achsen beschriften**

```python
plt.title('Scatterplot', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.xlabel('x-axis', fontsize=12)
```

- `title()` setzt den Diagrammtitel.
- `ylabel()` beschriftet die senkrechte y-Achse.
- `xlabel()` beschriftet die waagrechte x-Achse.
- `fontsize=12` bestimmt die Schriftgrösse.

In einer echten Analyse sollten die Beschriftungen das Merkmal und seine Einheit nennen, beispielsweise **„Wohnfläche (m²)“**.

**2. Positionen der Achsenmarkierungen festlegen**

```python
plt.xticks(np.arange(0, 60, step=2))
plt.yticks(np.arange(0, 60, step=5))
```

**Ticks** sind die Markierungen auf den Achsen. `np.arange()` erzeugt dafür eine Zahlenfolge:

| Aufruf | Erzeugte Werte |
|---|---|
| `np.arange(0, 60, step=2)` | 0, 2, 4, …, 58 |
| `np.arange(0, 60, step=5)` | 0, 5, 10, …, 55 |

Der Startwert `0` ist enthalten, der Endwert `60` **nicht**.

Anschliessend wird die Schriftgrösse der Tick-Beschriftungen gesetzt:

```python
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
```

Die zuvor festgelegten Positionen bleiben dabei erhalten.

**3. Den sichtbaren Bereich festlegen**

```python
plt.xlim(0, 50)
plt.ylim(0, 45)
```

Die x-Achse zeigt den Bereich **0 bis 50**, die y-Achse **0 bis 45**. Tick-Markierungen ausserhalb dieser Bereiche sind nicht sichtbar.

**Der wichtige Unterschied:** `ticks` legt die Markierungen fest, `lim` den sichtbaren Ausschnitt. Die zugrunde liegenden Daten werden dadurch nicht verändert.

**Führe die Zelle aus.** Ändere danach testweise bei `plt.xticks(...)` den Wert `step=2` auf `step=10` und führe sie nochmals aus. Die x-Achse sollte weniger Beschriftungen zeigen, während die Punkte an denselben Positionen bleiben.

> weiter

Als Nächstes folgt **„Adding a legend“**: Wir ergänzen eine Legende, damit man die vier Punktreihen unterscheiden kann.

Der bisherige Code bleibt gleich. Neu ist dieser Abschnitt:

```python
plt.legend(
    handles=[scatter_01, scatter_02, scatter_03, scatter_04],
    labels=['Red points', 'Green points', 'Blue points', 'Orange points'],
    loc="upper left",
    fontsize=10
)
```

Die Parameter bedeuten:

| Parameter | Bedeutung |
|---|---|
| `handles` | Welche gezeichneten Punktreihen in der Legende erscheinen. |
| `labels` | Welche Texte daneben stehen. |
| `loc="upper left"` | Positioniert die Legende oben links. |
| `fontsize=10` | Legt die Schriftgrösse fest. |

**Die Reihenfolge verbindet Symbol und Text:** `scatter_01` erhält den ersten Text, `scatter_02` den zweiten usw.

Woher kommen diese Namen? Beim Zeichnen haben wir die Rückgabe von `plt.scatter()` gespeichert:

```python
scatter_01 = plt.scatter(x, y, s=100, marker='o', color='orangered')
```

`scatter_01` verweist auf die gezeichnete Punktreihe. Dadurch können wir sie gezielt in die Legende aufnehmen.

Für **Aufgabe 1d** sollst du den Legendentext verändern. Ersetze deshalb den Legendenaufruf durch:

```python
plt.legend(
    handles=[scatter_01, scatter_02, scatter_03, scatter_04],
    labels=['Originalwerte', '20 % höher', '20 % niedriger', '40 % niedriger'],
    loc="upper left",
    fontsize=10
)
```

Diese Texte erklären nun die **Bedeutung der Datenreihen**. Die Farben und Datenpunkte bleiben dabei gleich.

**Führe die geänderte Zelle aus.** Die Legende sollte jetzt die vier neuen Beschriftungen anzeigen.

> weiter

<details><summary>2 previous messages</summary>

> Ich schaue nach, welcher Abschnitt im Notebook als Nächstes folgt.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/graphics_with_matplotlib.ipynb'))
> for i,c in enumerate(n['cells'][16:22],16):
>  print(i,c['cell_type'],''.join(c['source']))
> PY`
>
> </details>
</details>

Jetzt folgen zwei kurze Ergänzungen: **Text im Diagramm** und **Gitternetzlinien**.

**1. „Adding a text annotation“**

Neu ist diese Zeile:

```python
plt.text(28, 6, s="Look at the orange dots!", fontsize=12, color="orange")
```

Sie schreibt einen Hinweis direkt in den Diagrammbereich:

| Argument | Bedeutung |
|---|---|
| `28, 6` | Position des Textes bei x = 28 und y = 6. |
| `s="Look at the orange dots!"` | Der angezeigte Text. |
| `fontsize=12` | Schriftgrösse. |
| `color="orange"` | Textfarbe. |

**Die Position verwendet dieselben Koordinaten wie die Datenpunkte.** Wenn du die erste Zahl erhöhst, wandert der Text nach rechts; bei einer höheren zweiten Zahl wandert er nach oben.

Führe die Zelle aus. Du kannst den Hinweis beispielsweise so ändern:

```python
plt.text(28, 6, s="40 % unter den Originalwerten",
         fontsize=10, color="orange")
```

**2. „Adding a grid“**

Führe danach die nächste Zelle aus. Die entscheidende neue Zeile ist:

```python
plt.grid()
```

Sie schaltet hier das **Gitternetz** ein. Die Linien verlaufen an den Tick-Positionen und helfen, Werte abzulesen.

Um das Gitternetz ausdrücklich einzuschalten und dezenter zu gestalten, kannst du schreiben:

```python
plt.grid(True, color='gray', linestyle='--', alpha=0.3)
```

- **`True`** schaltet es ein.
- **`linestyle='--'`** erzeugt gestrichelte Linien.
- **`alpha=0.3`** macht sie relativ durchsichtig: `0` ist unsichtbar, `1` vollständig deckend.

Die Daten ändern sich bei beiden Ergänzungen nicht – wir verbessern die Lesbarkeit. Danach kommen die **Multiplots mit `plt.subplots()`**, die in Aufgabe 1b ausdrücklich verlangt werden.

> weiter

Jetzt kommt **Aufgabe 1b: mehrere Diagramme in einer Figure**, auch **Subplots** genannt.

Führe die Zelle unter **„Creating multiplots with .subplots()“** aus.

Die zentrale Zeile ist:

```python
fig, ax = plt.subplots(
    2, 2,
    figsize=(7, 4),
    sharex=True,
    sharey=True
)
```

| Bestandteil | Bedeutung |
|---|---|
| `2, 2` | Erstellt **2 Zeilen und 2 Spalten**, also vier Diagrammbereiche. |
| `figsize=(7, 4)` | Grösse der gesamten Figure in Zoll. |
| `sharex=True` | Die Diagramme teilen sich die x-Achsenskalierung. |
| `sharey=True` | Die Diagramme teilen sich die y-Achsenskalierung. |
| `fig` | Verweist auf die gesamte Figure. |
| `ax` | Enthält die vier einzelnen Diagrammbereiche. |

Die gemeinsame Skalierung erleichtert den Vergleich: Derselbe Abstand entspricht in jedem Diagramm derselben Wertedifferenz.

**Wie wählen wir ein einzelnes Diagramm aus?**

Mit `ax[Zeile, Spalte]`. Python zählt ab **0**:

| | Linke Spalte | Rechte Spalte |
|---|---|---|
| **Obere Zeile** | `ax[0, 0]` | `ax[0, 1]` |
| **Untere Zeile** | `ax[1, 0]` | `ax[1, 1]` |

Damit zeichnet beispielsweise:

```python
ax[0, 0].scatter(x, y, s=100, marker='o', color='orangered')
```

die Originalwerte **oben links**. Die anderen Aufrufe verteilen die übrigen Datenreihen:

```python
ax[1, 0].scatter(x, z, s=100, marker='+', color='green')
ax[0, 1].scatter(x, g, s=100, marker='*', color='deepskyblue')
ax[1, 1].scatter(x, e, s=100, marker='^', color='orange')
```

**Titel und Beschriftungen setzen**

```python
ax[0, 0].set_title('Figure at [0, 0]', fontsize=12)
ax[1, 0].set_xlabel('x-label', fontsize=10)
ax[0, 0].set_ylabel('y-label', fontsize=10)
```

Wir sprechen jetzt einen bestimmten Diagrammbereich an. Deshalb verwenden wir beispielsweise **`ax[0, 0].set_title(...)`** statt `plt.title(...)`.

Eine leere Zeichenfolge wie `set_xlabel('')` bedeutet: keine Beschriftung anzeigen.

**Abstände einstellen**

Am Ende steht:

```python
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.9,
    top=0.9,
    wspace=0.4,
    hspace=0.4
)
```

`left`, `bottom`, `right` und `top` legen die äusseren Grenzen des Diagrammrasters als Anteile der Figure fest. **`wspace`** steuert den horizontalen Abstand zwischen den Diagrammen, **`hspace`** den vertikalen.

Ändere nun zur Übung den Titel oben links:

```python
ax[0, 0].set_title('Originalwerte', fontsize=12)
```

Und ändere für **Aufgabe 1c** im selben Diagramm Symbol und Farbe:

```python
ax[0, 0].scatter(x, y, s=100, marker='s', color='purple')
```

**Führe die Zelle erneut aus:** Oben links sollten jetzt violette Quadrate mit dem Titel „Originalwerte“ erscheinen.

> ja

<details><summary>2 previous messages</summary>

> Ich prüfe noch den Rest des Notebooks, bevor wir zu den Wohnungsdaten wechseln.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> for f,start in [('graphics_with_matplotlib',22),('exploratory_data_analysis_apartment_data',0)]:
>  n=json.load(open('Week_04/'+f+'.ipynb'))
>  print(f)
>  for i,c in enumerate(n['cells'][start: start+10],start):
>   print(i,c['cell_type'],''.join(c['source']))
> PY`
>
> </details>
</details>

Dann folgt der letzte Abschnitt: **„Saving figure to file“**.

Die Zelle erstellt die vier Diagramme erneut. Neu sind die letzten beiden Zeilen:

```python
plt.savefig('myplot.png')
plt.close()
```

**`plt.savefig('myplot.png')`** speichert die gesamte Figure als PNG-Bild. Weil nur ein Dateiname angegeben ist, landet das Bild im aktuellen Arbeitsordner, also hier:

```text
Week_04/myplot.png
```

**`plt.close()`** schliesst die Figure und gibt die zugehörigen Ressourcen frei. Die gespeicherte Datei bleibt erhalten. Deshalb kann es sein, dass diese Zelle **kein Diagramm direkt im Notebook anzeigt**.

Für eine höhere Bildauflösung und einen passend zugeschnittenen Rand kannst du die Speicherzeile so ändern:

```python
plt.savefig('myplot.png', dpi=300, bbox_inches='tight')
```

- **`dpi=300`** legt die Auflösung auf 300 Bildpunkte pro Zoll fest.
- **`bbox_inches='tight'`** passt den Bildrand an den Inhalt an, einschliesslich der Beschriftungen.

Beachte: Diese Zelle enthält nochmals eigenen Zeichencode. Änderungen aus der vorherigen Zelle, etwa die violetten Quadrate, musst du hier ebenfalls eintragen, wenn sie im gespeicherten Bild erscheinen sollen.

**Führe die Zelle aus und öffne `myplot.png` im VS-Code-Dateibaum.** Führe anschliessend die letzte **Footer-Infozelle** aus und speichere das Notebook mit **Cmd + S**. Danach beginnen wir mit **Aufgabe 2: Wohnungsdaten untersuchen und Ausreisser erkennen**.

> ok

Weiter mit **Aufgabe 2: Wohnungsdaten untersuchen**.

Öffne [exploratory_data_analysis_apartment_data.ipynb](./Week_04/exploratory_data_analysis_apartment_data.ipynb).

Wir beginnen mit der ersten Codezelle unter **„Libraries and settings“**:

```python
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pylab as py
```

Einige Bibliotheken kennst du bereits. Für dieses Notebook sind besonders diese wichtig:

| Bibliothek | Aufgabe |
|---|---|
| `pandas` als `pd` | Wohnungsdaten einlesen und als Tabelle bearbeiten. |
| `numpy` als `np` | Numerische Berechnungen durchführen. |
| `seaborn` als `sns` | Statistische Grafiken erstellen; baut auf Matplotlib auf. |
| `matplotlib.pyplot` als `plt` | Diagramme zeichnen und gestalten. |
| `statsmodels.api` als `sm` | Statistische Verfahren und Diagnosegrafiken bereitstellen. |
| `pylab` als `py` | Eine zusätzliche Schnittstelle zu Funktionen aus NumPy und Matplotlib. |

Danach steht:

```python
sns.set(color_codes=True)
```

Das aktiviert Seaborns Darstellungsstil. Mit `color_codes=True` werden ausserdem Matplotlibs kurze Farbcodes wie `'b'` an Seaborns aktuelle Palette angepasst.

```python
import warnings
warnings.filterwarnings("ignore")
```

Das blendet Warnungen aus. Wie zuvor kannst du die zweite Zeile zum Lernen mit `#` auskommentieren.

```python
print(os.getcwd())
```

Zeigt den Arbeitsordner an. Er sollte wieder auf **`Week_04`** enden, damit die CSV-Datei beim anschliessenden Einlesen gefunden wird.

**Führe zunächst diese erste Codezelle aus.** Falls ein Fehler erscheint, schicke mir die Fehlermeldung; andernfalls lesen wir als Nächstes die Wohnungsdaten ein.

> weiter

Jetzt folgt **„Importing the enriched apartment data“**: Wir lesen die angereicherten Wohnungsdaten ein und bereinigen sie.

**1. CSV-Datei einlesen und Spalten auswählen**

Die Zelle beginnt mit:

```python
df_orig = pd.read_csv("apartments_data_enriched.csv")[[
    'web-scraper-order',
    'address_raw',
    'lat',
    'lon',
    'bfs_number',
    'bfs_name',
    'rooms',
    'area',
    'luxurious',
    'price',
    'price_per_m2',
    'pop',
    'pop_dens',
    'emp',
    'frg_pct',
    'mean_taxable_income'
]]
```

Von innen nach aussen gelesen:

1. **`pd.read_csv(...)`** liest die CSV-Datei als DataFrame ein.
2. **`[['...', '...']]`** wählt die aufgeführten Spalten aus.
3. **`df_orig = ...`** speichert die Tabelle unter dem Namen `df_orig`.

Die doppelten eckigen Klammern entstehen, weil wir **eine Liste von Spaltennamen** an die Spaltenauswahl übergeben.

Die Daten enthalten Wohnungsmerkmale wie `rooms`, `area` und `price` sowie Gemeindemerkmale wie:

| Spalte | Bedeutung |
|---|---|
| `bfs_name` | Gemeindename |
| `pop` | Einwohnerzahl der Gemeinde |
| `pop_dens` | Bevölkerungsdichte der Gemeinde |
| `emp` | Anzahl Beschäftigte der Gemeinde |
| `frg_pct` | Ausländeranteil der Gemeinde |
| `mean_taxable_income` | Durchschnittliches steuerbares Einkommen der Gemeinde |

**Eine Zeile beschreibt weiterhin ein Wohnungsinserat.** Gemeindemerkmale wiederholen sich deshalb bei Wohnungen derselben Gemeinde.

**2. Doppelte Zeilen entfernen**

```python
df_orig = df_orig.drop_duplicates()
df_orig.head(5)
```

`drop_duplicates()` entfernt Zeilen, die **in allen ausgewählten Spalten übereinstimmen**. Durch die Zuweisung wird `df_orig` mit dem bereinigten Ergebnis aktualisiert.

`head(5)` liefert die ersten fünf Zeilen zur Kontrolle.

**3. Zeilen mit fehlenden Werten entfernen**

```python
df_orig = df_orig.dropna()
df_orig.head(5)
```

`dropna()` entfernt hier jede Zeile, bei der **mindestens eine der ausgewählten Spalten einen fehlenden Wert** enthält.

Das vereinfacht die folgenden Auswertungen, kann aber auch viele Inserate ausschliessen. Und: **Unplausible Zahlen wie eine Miete von 11 CHF werden dadurch nicht entfernt**, denn sie sind vorhanden. Solche Auffälligkeiten untersuchen wir später.

Im Notebook wird standardmässig nur das Ergebnis des **letzten** `head(5)` angezeigt. Wenn du zusätzlich sehen möchtest, wie viele Zeilen übrig bleiben, ergänze am Ende:

```python
print("Zeilen und Spalten:", df_orig.shape)
```

**Führe die Zelle aus und schicke mir die angezeigte Form der Tabelle.** Danach gehen wir zu den **Quantilen** – sie helfen uns, die Verteilung und mögliche Ausreisser zu verstehen.

> |    | **web-scraper-order** |                      **address_raw** |   **lat** |  **lon** | **bfs_number** | **bfs_name** | **rooms** | **area** | **luxurious** | **price** | **price_per_m2** | **pop** | **pop_dens** | **emp** | **frg_pct** | **mean_taxable_income** |
> | -: | --------------------: | -----------------------------------: | --------: | -------: | -------------: | -----------: | --------: | -------: | ------------: | --------: | ---------------: | ------: | -----------: | ------: | ----------: | ----------------------: |
> |  0 |          1693998201-1 |    Neuhusstrasse 6, 8630 Rüti ZH, ZH | 47.252171 | 8.845797 |            118 |    Rüti (ZH) |       3.0 |     49.0 |             0 |    1441.0 |            29.41 |   12286 |  1221.272366 |  5053.0 |   24.841283 |            65362.042683 |
> |  1 |        1693998233-172 |  Widacherstrasse 5, 8630 Rüti ZH, ZH | 47.252087 | 8.854919 |            118 |    Rüti (ZH) |       3.0 |    111.0 |             0 |    2600.0 |            23.42 |   12286 |  1221.272366 |  5053.0 |   24.841283 |            65362.042683 |
> |  2 |        1693998256-331 |        Widenweg 14, 8630 Rüti ZH, ZH | 47.253670 | 8.853993 |            118 |    Rüti (ZH) |       3.0 |     58.0 |             0 |    1490.0 |            25.69 |   12286 |  1221.272366 |  5053.0 |   24.841283 |            65362.042683 |
> |  3 |        1693998265-381 |             Rain 1, 8630 Rüti ZH, ZH | 47.259834 | 8.851705 |            118 |    Rüti (ZH) |       4.0 |    118.0 |             0 |    3240.0 |            27.46 |   12286 |  1221.272366 |  5053.0 |   24.841283 |            65362.042683 |
> |  4 |        1693998276-419 | Bachtelstrasse 24b, 8630 Rüti ZH, ZH | 47.266113 | 8.866872 |            118 |    Rüti (ZH) |       3.0 |     66.0 |             0 |    1450.0 |            21.97 |   12286 |  1221.272366 |  5053.0 |   24.841283 |            65362.042683 |

Die Daten wurden eingelesen. Du siehst die **ersten fünf Zeilen**, nicht die gesamte Tabelle.

Die erste Wohnung hat beispielsweise **49 m²** und kostet **1’441 CHF**. Ihr Quadratmeterpreis beträgt:

\[
\frac{1441}{49} \approx 29{,}41\ \text{CHF/m²}
\]

Alle fünf Wohnungen liegen in **Rüti (ZH)**. Deshalb wiederholen sich die Gemeindemerkmale wie Einwohnerzahl und Bevölkerungsdichte. Das sind keine doppelten Wohnungsinserate.

Jetzt folgt **„Quantiles original values“**:

```python
df_orig[
    ['price', 'rooms', 'area', 'price_per_m2', 'pop_dens']
].quantile(
    q=[0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95]
).round(2)
```

Der Code wählt fünf Spalten aus, berechnet deren **Quantile** und rundet die Ergebnisse auf zwei Nachkommastellen.

Ein **Quantil ist ein Grenzwert innerhalb sortierter Daten**. Stell dir vor, wir sortieren alle Wohnungen nach ihrer Fläche:

| Quantil | Bedeutung |
|---|---|
| `0.10` – 10%-Quantil | Ungefähr 10 % der Wohnungen liegen mit ihrer Fläche bei oder unter diesem Grenzwert. |
| `0.50` – 50%-Quantil | Der **Median**: die Mitte der sortierten Flächenwerte. |
| `0.90` – 90%-Quantil | Ungefähr 90 % liegen bei oder darunter; etwa 10 % darüber. |

**Beispiel:** Wäre das 90%-Quantil der Fläche **150 m²**, wären ungefähr 90 % der Wohnungen höchstens 150 m² gross. Das bedeutet **nicht**, dass 90 % genau 150 m² haben.

Quantile helfen uns, typische Bereiche und extreme Werte einzuordnen. Ein Wert über dem 90%-Quantil ist allerdings **nicht automatisch ein Fehler oder Ausreisser**.

**Führe die Quantil-Zelle aus und schicke mir die Tabelle.** Danach interpretieren wir die konkreten Werte gemeinsam.

> |      | **price** | **rooms** | **area** | **price_per_m2** | **pop_dens** |
> | ---: | --------: | --------: | -------: | ---------------: | -----------: |
> | 0.05 |   1337.00 |      1.00 |    26.00 |            17.90 |       336.03 |
> | 0.10 |   1492.50 |      1.50 |    41.50 |            20.02 |       525.66 |
> | 0.25 |   1842.25 |      2.50 |    63.00 |            23.30 |      1044.63 |
> | 0.50 |   2391.00 |      3.50 |    86.00 |            27.95 |      1662.60 |
> | 0.75 |   3056.75 |      4.50 |   108.75 |            38.12 |      4778.99 |
> | 0.90 |   3960.00 |      4.75 |   140.50 |            52.78 |      4778.99 |
> | 0.95 |   4957.50 |      5.50 |   163.75 |            67.33 |      4778.99 |

Die Tabelle zeigt uns, **wie sich die Werte der Wohnungsinserate verteilen**.

Betrachten wir zuerst die Zeile **`0.50`**, also den Median:

| Merkmal | Median | Interpretation |
|---|---:|---|
| Mietpreis | 2’391 CHF | Etwa die Hälfte der Inserate kostet höchstens 2’391 CHF. |
| Zimmer | 3,5 | Etwa die Hälfte hat höchstens 3,5 Zimmer. |
| Fläche | 86 m² | Etwa die Hälfte ist höchstens 86 m² gross. |
| Quadratmeterpreis | 27,95 CHF/m² | Etwa die Hälfte kostet höchstens 27,95 CHF pro m². |

**Diese Werte werden für jede Spalte separat berechnet.** Sie beschreiben deshalb nicht zwingend eine tatsächlich vorhandene Wohnung mit genau diesen Eigenschaften.

Die **mittleren 50 %** der Mietpreise liegen ungefähr zwischen dem 25%- und dem 75%-Quantil:

\[
1’842{,}25 \text{ CHF bis } 3’056{,}75 \text{ CHF}
\]

Bei der Fläche liegen die mittleren 50 % zwischen **63 und 108,75 m²**. Dieser Bereich hilft uns, die Grössenordnung des Angebots einzuschätzen.

Zwei Besonderheiten sind wichtig:

**Warum steht beim 90%-Quantil der Zimmerzahl `4.75`?**
Pandas interpoliert standardmässig zwischen benachbarten Werten, wenn die Quantilposition zwischen ihnen liegt. Ein Quantil kann deshalb **4,75 Zimmer** betragen, obwohl kein Inserat genau diese Zimmerzahl hat.

**Warum ist `pop_dens` mehrfach `4778.99`?**
Viele Inserate haben dieselbe Bevölkerungsdichte, weil sie in derselben Gemeinde liegen. Dadurch können mehrere Quantile denselben Wert ergeben.

Für **Aufgabe 3** merken wir uns bereits:

- **10%-Quantil:** 525,66 Einwohner/km² → Grenze für die ländlichere Gruppe.
- **90%-Quantil:** 4’778,99 Einwohner/km² → Grenze für die dichter besiedelte Gruppe.

Dabei werden die Quantile **über die Wohnungsinserate** berechnet. Gemeinden mit vielen Inseraten gehen entsprechend häufiger ein. Wegen gleicher Werte an der Grenze müssen die späteren Gruppen auch nicht genau 10 % der Inserate enthalten.

**Die Quantile allein reichen noch nicht aus, um Ausreisser festzulegen.** Dafür betrachten wir anschliessend weitere Kennzahlen und Grafiken.

Gehe jetzt zum Abschnitt **„Filter apartments“**. Dort steht zunächst:

```python
df = df_orig.loc[df_orig['pop_dens'] <= 5000]
```

Das wählt alle Inserate aus, deren Gemeinde eine Bevölkerungsdichte von **höchstens 5’000 Einwohnern/km²** hat, und speichert sie in `df`. `df_orig` bleibt dabei erhalten.

**Führe diese Zelle zunächst unverändert aus.** Die Grenzen für den Land-Stadt-Vergleich setzen wir später in den separaten Notebooks ein.

> ja

<details><summary>2 previous messages</summary>

> Ich schaue in die nächste Zelle, damit wir die Auswertung der gefilterten Daten gemeinsam durchgehen können.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/exploratory_data_analysis_apartment_data.ipynb'))
> for i,c in enumerate(n['cells'][10:18],10):
>  print(i,c['cell_type'],''.join(c['source']))
> PY`
>
> </details>
</details>

Jetzt prüfen wir **Grösse, Datentypen und Kennzahlen** der gefilterten Tabelle `df`.

**1. „Shape (number of rows and columns)“**

```python
print(df.shape)
```

Das Ergebnis hat die Form:

```text
(Anzahl Zeilen, Anzahl Spalten)
```

Die Zeilen entsprechen Wohnungsinseraten, die Spalten ihren Merkmalen. Damit sehen wir, wie viele Inserate nach dem Filter übrig sind.

**2. „Data types“**

```python
df.dtypes
```

Zeigt den Datentyp jeder Spalte:

| Datentyp | Bedeutung | Beispiel |
|---|---|---|
| `int64` | Ganze Zahl | Einwohnerzahl |
| `float64` | Zahl mit möglichen Nachkommastellen | Fläche, Mietpreis |
| `object` | Hier typischerweise Text | Adresse, Gemeindename |

**Ein numerischer Datentyp garantiert keine sinnvolle Berechnung:** Die Gemeindenummer ist beispielsweise eine Kennung. Ihr Durchschnitt hat keine fachliche Bedeutung.

**3. „Summary statistics of numeric variables“**

```python
df.describe()
```

Erstellt eine Übersicht für die numerischen Spalten:

| Zeile | Bedeutung |
|---|---|
| `count` | Anzahl vorhandener Werte |
| `mean` | Arithmetischer Mittelwert |
| `std` | Standardabweichung: Mass dafür, wie stark die Werte um den Mittelwert streuen |
| `min` | Kleinster Wert |
| `25%` | Unteres Quartil |
| `50%` | Median |
| `75%` | Oberes Quartil |
| `max` | Grösster Wert |

**Hier werden besonders `min` und `max` interessant:** Extrem niedrige Mietpreise oder sehr grosse Flächen können Hinweise auf Ausreisser oder Datenfehler sein. Sie müssen anschliessend geprüft werden.

**Führe diese drei Zellen aus und schicke mir die Ausgabe von `df.describe()`.** Dann suchen wir gemeinsam nach auffälligen Werten.

> |       |    **lat** |    **lon** | **bfs_number** |  **rooms** |    **area** | **luxurious** |   **price** | **price_per_m2** |       **pop** | **pop_dens** |       **emp** | **frg_pct** | **mean_taxable_income** |
> | ----: | ---------: | ---------: | -------------: | ---------: | ----------: | ------------: | ----------: | ---------------: | ------------: | -----------: | ------------: | ----------: | ----------------------: |
> | count | 786.000000 | 786.000000 |     786.000000 | 786.000000 |  786.000000 |    786.000000 |  786.000000 |       786.000000 |    786.000000 |   786.000000 |    786.000000 |  786.000000 |              786.000000 |
> |  mean |  47.407331 |   8.600386 |     186.862595 |   3.421756 |   92.426209 |      0.012723 | 2649.339695 |        33.336489 | 161145.898219 |  2503.950703 | 177328.709924 |   27.771168 |            80631.662280 |
> |   std |   0.085343 |   0.117298 |      81.404652 |   1.304543 |   75.786527 |      0.112146 | 1289.074423 |        17.141739 | 186630.497367 |  1748.039181 | 223745.725478 |    7.592012 |            14393.861209 |
> |   min |  47.195290 |   8.367652 |       1.000000 |   1.000000 |    8.000000 |      0.000000 |   10.000000 |         0.040000 |    698.000000 |    87.959866 |    129.000000 |    7.547170 |            62000.541872 |
> |   25% |  47.361061 |   8.518511 |     121.000000 |   2.500000 |   63.000000 |      0.000000 | 1842.250000 |        23.302500 |   8775.000000 |  1044.628957 |   3460.000000 |   24.535004 |            71059.805603 |
> |   50% |  47.395105 |   8.562069 |     230.000000 |   3.500000 |   86.000000 |      0.000000 | 2391.000000 |        27.950000 |  27746.000000 |  1662.597326 |  19226.000000 |   28.059994 |            82404.831614 |
> |   75% |  47.481115 |   8.710458 |     261.000000 |   4.500000 |  108.750000 |      0.000000 | 3056.750000 |        38.125000 | 420217.000000 |  4778.994655 | 491193.000000 |   32.458468 |            82932.737704 |
> |   max |  47.693893 |   8.915933 |     298.000000 |   8.500000 | 1633.000000 |      1.000000 | 9950.000000 |       149.900000 | 420217.000000 |  4778.994655 | 491193.000000 |   46.226483 |           174434.537050 |

Die Tabelle enthält **786 Wohnungsinserate**. Für jede numerische Spalte steht bei `count` ebenfalls 786 – dort fehlen also keine Werte.

**Bei Mietpreis und Fläche fallen mehrere Werte auf:**

| Merkmal | Auffälliger Wert | Erste Einschätzung |
|---|---:|---|
| Kleinster Mietpreis | **10 CHF** | Für eine monatliche Wohnungsmiete sehr unplausibel. |
| Kleinster Quadratmeterpreis | **0,04 CHF/m²** | Ebenfalls sehr unplausibel. |
| Grösste Fläche | **1’633 m²** | Für eine einzelne Wohnung aussergewöhnlich gross; prüfen. |
| Kleinste Fläche | **8 m²** | Sehr klein; könnte etwa ein Zimmer oder ein fehlerhaftes Inserat sein. |
| Höchster Quadratmeterpreis | **149,90 CHF/m²** | Sehr hoch; könnte beispielsweise ein kleines möbliertes Angebot betreffen. |

**Diese Extremwerte müssen nicht zum selben Inserat gehören.** `describe()` betrachtet jede Spalte einzeln. Wir können daraus beispielsweise nicht schliessen, dass die 1’633-m²-Wohnung 10 CHF kostet.

Auch der Unterschied zwischen **Mittelwert und Median** ist interessant:

- Mietpreis: Mittelwert **2’649 CHF**, Median **2’391 CHF**.
- Fläche: Mittelwert **92,43 m²**, Median **86 m²**.

Hohe Werte ziehen den Mittelwert nach oben. Der Median reagiert weniger stark auf einzelne Extremwerte, weil er nur die Mitte der sortierten Werte beschreibt. Das passt zu den auffälligen Maximalwerten, beweist aber noch keinen Datenfehler.

Ein weiterer wichtiger Punkt: Die höchste Bevölkerungsdichte beträgt **4’778,99**, also weniger als unsere Filtergrenze von 5’000. Der bisherige Filter hat deshalb keine Zeile aus `df_orig` ausgeschlossen.

Jetzt folgt **„Statistical measures … for selected variables“**. Die nächste Zelle berechnet gezielt dieselben Kennzahlen für Preis und Fläche, beispielsweise:

```python
df.price.mean()    # Durchschnittlicher Mietpreis
df.price.median()  # Median des Mietpreises
df.price.std()     # Standardabweichung des Mietpreises
```

`df.price` greift hier auf dieselbe Spalte zu wie `df['price']`. Mit `round(..., 1)` werden die Ergebnisse auf eine Nachkommastelle gerundet.

**Führe diese Zelle aus.** Du solltest für den Preis unter anderem `Mean: 2649.3` und `Median: 2391.0` erhalten. Danach untersuchen wir die Verteilungen grafisch.

> ja

<details><summary>2 previous messages</summary>

> Ich schaue nach, welche Auswertung im Notebook als Nächstes folgt.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/exploratory_data_analysis_apartment_data.ipynb'))
> for i,c in enumerate(n['cells'][18:25],18):
>  print(i,c['cell_type'],''.join(c['source']))
> PY`
>
> </details>
</details>

Vor den Grafiken folgen noch zwei Kennzahlen zur **Form einer Verteilung**. Wir beginnen mit **„Skewness“**, auf Deutsch **Schiefe**:

```python
df[['price', 'rooms', 'area']].skew()
```

Der Code berechnet die Schiefe separat für **Mietpreis, Zimmerzahl und Fläche**.

Die Schiefe beschreibt, **in welche Richtung eine Verteilung einen längeren Ausläufer hat**:

| Wert | Bedeutung |
|---|---|
| Ungefähr `0` | Die Verteilung ist hinsichtlich ihrer Schiefe ungefähr ausgeglichen; das beweist keine Symmetrie. |
| Positiv | **Rechtsschief:** Einige besonders hohe Werte bilden einen Ausläufer nach rechts. |
| Negativ | **Linksschief:** Einige besonders niedrige Werte bilden einen Ausläufer nach links. |

Bei Wohnflächen könnte eine rechtsschiefe Verteilung so entstehen: Viele Wohnungen haben moderate Flächen, einzelne sind dagegen sehr gross. Die **1’633 m²** könnten deshalb die Schiefe deutlich beeinflussen.

**„Rechtsschief“ bedeutet nicht, dass die meisten Werte rechts liegen.** Es bezeichnet die Richtung des langen Ausläufers zu den hohen Werten.

Die Schiefe ergänzt unsere bisherigen Kennzahlen: Während der Mittelwert die durchschnittliche Höhe beschreibt, sagt die Schiefe etwas über die **Verteilungsform** aus. Sie kennzeichnet aber keine einzelnen Inserate als fehlerhaft.

**Führe die Zelle unter „Skewness“ aus und schicke mir die drei Werte.** Danach interpretieren wir sie und gehen zur Kurtosis weiter.

> price     2.093405\
> rooms     0.209733\
> area     12.529695\
> dtype: float64

Alle drei Werte sind **positiv**: Die Verteilungen haben einen Ausläufer zu den höheren Werten. Die Stärke unterscheidet sich deutlich:

| Merkmal | Schiefe | Interpretation |
|---|---:|---|
| `price` | **2,09** | Deutlich rechtsschief: Hohe Mietpreise verlängern den rechten Ausläufer. |
| `rooms` | **0,21** | Nur leicht rechtsschief. |
| `area` | **12,53** | Extrem rechtsschief: Sehr grosse Flächen beeinflussen die Verteilung stark. |

Bei **`area`** passt das zur maximalen Fläche von **1’633 m²**, während der Median nur **86 m²** beträgt. Welche Inserate dafür verantwortlich sind, müssen wir noch einzeln prüfen.

`dtype: float64` bedeutet lediglich, dass die ausgegebenen Kennzahlen als Gleitkommazahlen gespeichert sind.

Jetzt folgt **„Kurtosis“**:

```python
df[['price', 'rooms', 'area']].kurtosis()
```

Die Kurtosis hilft uns einzuschätzen, **wie stark extreme Werte in einer Verteilung ins Gewicht fallen**. Sie reagiert besonders empfindlich auf Werte weit ausserhalb des Zentrums.

Pandas berechnet hier die **Exzess-Kurtosis**, bei der die Normalverteilung den Referenzwert **0** hat:

| Ergebnis | Einordnung |
|---|---|
| Positiv | Hinweis auf stärker ausgeprägte Verteilungsschwänze als bei einer Normalverteilung. |
| Ungefähr `0` | Vergleichbare Kurtosis wie bei einer Normalverteilung; beweist keine Normalverteilung. |
| Negativ | Hinweis auf schwächer ausgeprägte Verteilungsschwänze. |

**Unterschied:** Die Schiefe beschreibt die **Asymmetrie**, die Kurtosis die Bedeutung extremer Abweichungen. Keine der beiden Kennzahlen beweist einen Datenfehler.

**Führe die Kurtosis-Zelle aus und schicke mir die Werte.**

> price      6.668070\
> rooms      0.085123\
> area     232.607355\
> dtype: float64

Die Kurtosis zeigt besonders bei der **Fläche einen extrem hohen Wert**:

| Merkmal | Exzess-Kurtosis | Interpretation |
|---|---:|---|
| `price` | **6,67** | Extreme Abweichungen vom Mittelwert fallen deutlich ins Gewicht. |
| `rooms` | **0,09** | Nahe am Referenzwert 0; das beweist aber keine Normalverteilung. |
| `area` | **232,61** | Extremwerte prägen diese Kennzahl sehr stark. |

Für die **Fläche** passen die bisherigen Befunde zusammen:

- Median: **86 m²**
- Maximum: **1’633 m²**
- Schiefe: **12,53**
- Exzess-Kurtosis: **232,61**

Die Schiefe zeigt den ausgeprägten Ausläufer zu hohen Flächenwerten. Die Kurtosis zeigt, wie stark extreme Abweichungen ins Gewicht fallen. **Ob diese Werte fehlerhaft sind, müssen wir anhand der einzelnen Inserate prüfen.**

Genau dazu folgt jetzt **„Extreme values“**. Die erste Zelle lautet:

```python
# Low costs apartments
df[df['price_per_m2'] <= 10]
```

Sie zeigt alle Inserate mit einem Quadratmeterpreis von **höchstens 10 CHF/m²**:

1. `df['price_per_m2'] <= 10` prüft die Bedingung für jede Zeile und liefert `True` oder `False`.
2. Das äussere `df[...]` wählt nur die Zeilen mit `True` aus.

Das ist eine **Auswahl zur Untersuchung**. Es wird nichts gelöscht und `df` bleibt unverändert.

**Führe diese Zelle aus und schicke mir die angezeigten Inserate.** Besonders interessant sind Gemeinde, Fläche, Mietpreis und Quadratmeterpreis.

> |     | **web-scraper-order** |                             **address_raw** |   **lat** |  **lon** | **bfs_number** |   **bfs_name** | **rooms** | **area** | **luxurious** | **price** | **price_per_m2** | **pop** | **pop_dens** |  **emp** | **frg_pct** | **mean_taxable_income** |
> | --: | --------------------: | ------------------------------------------: | --------: | -------: | -------------: | -------------: | --------: | -------: | ------------: | --------: | ---------------: | ------: | -----------: | -------: | ----------: | ----------------------: |
> | 183 |        1693998317-653 |                             8001 Zürich, ZH | 47.374966 | 8.543989 |            261 |         Zürich |       4.5 |    137.0 |             0 |      16.0 |             0.12 |  420217 |  4778.994655 | 491193.0 |   32.458468 |            82932.737704 |
> | 198 |        1693998326-702 |         Hohenbühlstrasse 7, 8032 Zürich, ZH | 47.366306 | 8.551867 |            261 |         Zürich |       5.5 |    183.0 |             0 |      10.0 |             0.05 |  420217 |  4778.994655 | 491193.0 |   32.458468 |            82932.737704 |
> | 404 |         1693998205-39 | Binzigerstrasse 52, 8707 Uetikon am See, ZH | 47.267185 | 8.689932 |            159 | Uetikon am See |       6.5 |    300.0 |             1 |      11.0 |             0.04 |    6201 |  1792.196532 |   1480.0 |   21.270763 |           118977.376698 |
> | 511 |        1693998369-926 |          Dorfstrasse 2, 8309 Nürensdorf, ZH | 47.458389 | 8.638629 |             64 |     Nürensdorf |       6.5 |    863.0 |             0 |    4500.0 |             5.21 |    5602 |   557.968127 |   1031.0 |   16.815423 |            99039.717665 |
> | 584 |        1693998289-482 |       Lärchenstrasse 6, 8442 Hettlingen, ZH | 47.547836 | 8.717198 |            221 |     Hettlingen |       6.0 |   1633.0 |             0 |    3900.0 |             2.39 |    3169 |   537.118644 |    702.0 |    9.056485 |           101569.727626 |
> | 762 |        1693998280-447 |         Grabenwiese 2, 8484 Weisslingen, ZH | 47.426781 | 8.767586 |            180 |    Weisslingen |       6.5 |    585.0 |             0 |    3250.0 |             5.56 |    3364 |   262.607338 |    886.0 |   10.434007 |            84173.291925 |

Hier sehen wir **sechs auffällige Inserate**, bei denen zwei unterschiedliche Ursachen infrage kommen.

**1. Unplausibel niedrige Mietpreise**

| Index | Gemeinde | Fläche | Mietpreis |
|---|---|---:|---:|
| 183 | Zürich | 137 m² | **16 CHF** |
| 198 | Zürich | 183 m² | **10 CHF** |
| 404 | Uetikon am See | 300 m² | **11 CHF** |

Als monatliche Wohnungsmieten sind diese Beträge sehr unplausibel. Möglicherweise wurde der Preis beim Einlesen oder bei der früheren Datenaufbereitung falsch erfasst. **Die korrekten Preise können wir aus dieser Tabelle nicht rekonstruieren.**

**2. Aussergewöhnlich grosse Flächen**

| Index | Gemeinde | Fläche | Mietpreis | Preis/m² |
|---|---|---:|---:|---:|
| 511 | Nürensdorf | **863 m²** | 4’500 CHF | 5,21 CHF |
| 584 | Hettlingen | **1’633 m²** | 3’900 CHF | 2,39 CHF |
| 762 | Weisslingen | **585 m²** | 3’250 CHF | 5,56 CHF |

Hier wirken die Mietpreise eher plausibel, aber die Flächen sind für einzelne Wohnungen aussergewöhnlich gross. Denkbar wäre beispielsweise, dass eine Grundstücksfläche statt der Wohnfläche erfasst wurde. Das bleibt eine Vermutung.

Der Zusammenhang ist wichtig:

\[
\text{Preis pro m²}=\frac{\text{Mietpreis}}{\text{Wohnfläche}}
\]

**Ein zu niedriger Preis oder eine zu grosse Fläche führt zu einem zu niedrigen Quadratmeterpreis.** Derselbe auffällige Quotient kann also unterschiedliche Ursachen haben.

Beim Inserat in Hettlingen stimmt die Rechnung:

\[
3900 \div 1633 \approx 2{,}39
\]

Eine rechnerisch korrekte Kennzahl kann somit auf fragwürdigen Ausgangsdaten beruhen. Die Flächenwerte sind auch mögliche Treiber der hohen Schiefe und Kurtosis.

Wir entfernen zunächst noch nichts, sondern betrachten die andere Seite. Führe die nächste Zelle aus:

```python
# Very expansive apartments
df[df['price_per_m2'] >= 100]
```

Sie zeigt Inserate mit **mindestens 100 CHF/m²**. Schicke mir die Ausgabe, dann prüfen wir, was diese Angebote auffällig macht.

> |     | **web-scraper-order** |                  **address_raw** |   **lat** |  **lon** | **bfs_number** | **bfs_name** | **rooms** | **area** | **luxurious** | **price** | **price_per_m2** | **pop** | **pop_dens** |  **emp** | **frg_pct** | **mean_taxable_income** |
> | --: | --------------------: | -------------------------------: | --------: | -------: | -------------: | -----------: | --------: | -------: | ------------: | --------: | ---------------: | ------: | -----------: | -------: | ----------: | ----------------------: |
> |  11 |         1693998201-16 |  Wolframplatz 1, 8045 Zürich, ZH | 47.362282 | 8.522193 |            261 |       Zürich |       2.0 |     32.0 |             0 |    3515.0 |           109.84 |  420217 |  4778.994655 | 491193.0 |   32.458468 |            82932.737704 |
> |  20 |         1693998214-82 |  Baurstrasse 29, 8008 Zürich, ZH | 47.355923 | 8.554498 |            261 |       Zürich |       1.5 |     30.0 |             0 |    3790.0 |           126.33 |  420217 |  4778.994655 | 491193.0 |   32.458468 |            82932.737704 |
> |  21 |         1693998214-83 |  Baurstrasse 29, 8008 Zürich, ZH | 47.355923 | 8.554498 |            261 |       Zürich |       1.5 |     25.0 |             0 |    3490.0 |           139.60 |  420217 |  4778.994655 | 491193.0 |   32.458468 |            82932.737704 |
> | 107 |        1693998280-434 |     Neugasse 40, 8005 Zürich, ZH | 47.382469 | 8.530180 |            261 |       Zürich |       1.0 |     11.0 |             0 |    1120.0 |           101.82 |  420217 |  4778.994655 | 491193.0 |   32.458468 |            82932.737704 |
> | 154 |        1693998305-585 | Steinstrasse 35, 8003 Zürich, ZH | 47.366997 | 8.520324 |            261 |       Zürich |       1.0 |     15.0 |             0 |    1500.0 |           100.00 |  420217 |  4778.994655 | 491193.0 |   32.458468 |            82932.737704 |
> | 171 |        1693998309-621 |  Baurstrasse 29, 8008 Zürich, ZH | 47.355923 | 8.554498 |            261 |       Zürich |       1.5 |     30.0 |             0 |    3890.0 |           129.67 |  420217 |  4778.994655 | 491193.0 |   32.458468 |            82932.737704 |
> | 185 |        1693998317-658 |                  8004 Zürich, ZH | 47.380417 | 8.525352 |            261 |       Zürich |       1.0 |     10.0 |             0 |    1499.0 |           149.90 |  420217 |  4778.994655 | 491193.0 |   32.458468 |            82932.737704 |

Diese **sieben Inserate liegen alle in Zürich** und haben kleine Flächen zwischen **10 und 32 m²**.

Der hohe Quadratmeterpreis entsteht hier durch die Kombination aus kleiner Fläche und vergleichsweise hoher Miete:

| Beispiel | Rechnung | Preis/m² |
|---|---|---:|
| 10 m² für 1’499 CHF | `1499 / 10` | **149,90 CHF** |
| 25 m² für 3’490 CHF | `3490 / 25` | **139,60 CHF** |
| 32 m² für 3’515 CHF | `3515 / 32` | **109,84 CHF** |

**Ein hoher Quadratmeterpreis bedeutet nicht automatisch die höchste Gesamtmiete.** Das 10-m²-Angebot kostet insgesamt weniger als die beiden anderen, ist aber pro Quadratmeter am teuersten.

Diese Angebote könnten beispielsweise möblierte Apartments, Zimmer oder Unterkünfte mit Zusatzleistungen sein. Das lässt sich aus den gezeigten Spalten jedoch nicht feststellen. **Sie sind auffällig, aber nicht nachweislich falsch.**

Auch die drei Angebote an der **Baurstrasse 29** sind nicht automatisch Duplikate: Fläche oder Preis unterscheiden sich. Eine gleiche Adresse reicht nicht aus, um Inserate als doppelt einzustufen.

Für die spätere Bereinigung halten wir fest:

- **10–16 CHF Gesamtmiete:** stark unplausibel.
- **585–1’633 m² Wohnfläche:** prüfbedürftig.
- **100–149,90 CHF/m²:** sehr hoch, könnte aber ein besonderes Angebotssegment darstellen.

Der wichtige Lernpunkt ist: **Ein statistischer Ausreisser ist nicht automatisch ein Datenfehler.** Ob wir solche Angebote ausschliessen, muss zur Fragestellung passen und begründet werden.

Damit haben wir beide Extreme des Quadratmeterpreises untersucht. Gehe jetzt zur nächsten Zelle im Notebook weiter.

> **### Get a list of categories of categorical variable**

<details><summary>2 previous messages</summary>

> Ich schaue kurz nach, welche kategoriale Variable die nächste Zelle untersucht.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/exploratory_data_analysis_apartment_data.ipynb'))
> for i,c in enumerate(n['cells']):
>  if 'Get a list of categories' in ''.join(c['source']):
>   for cc in n['cells'][i:i+4]: print(cc['cell_type'],''.join(cc['source']))
> PY`
>
> </details>
</details>

Dieser Abschnitt zeigt, **welche Gemeinden in unseren gefilterten Wohnungsdaten vorkommen**.

Die Zelle lautet:

```python
np.array(pd.Categorical(df['bfs_name']).categories)
```

Eine **kategoriale Variable** ordnet Beobachtungen Gruppen zu. Hier ist `bfs_name` kategorial: Jede Wohnung gehört zu einer Gemeinde, beispielsweise Zürich, Rüti oder Hettlingen.

Wir lesen den Code von innen nach aussen:

| Code | Bedeutung |
|---|---|
| `df['bfs_name']` | Wählt die Spalte mit den Gemeindenamen aus. |
| `pd.Categorical(...)` | Erstellt daraus eine kategoriale Darstellung. |
| `.categories` | Liefert die unterschiedlichen Kategorien, hier die Gemeindenamen. |
| `np.array(...)` | Wandelt diese Kategorien in ein NumPy-Array um. |

**Jeder Gemeindename erscheint in der Ausgabe nur einmal**, auch wenn viele Wohnungen in dieser Gemeinde liegen.

Der Unterschied zu einer Häufigkeitsauswertung ist wichtig:

```python
df['bfs_name'].unique()
```

zeigt ebenfalls die vorkommenden Gemeinden, normalerweise in der Reihenfolge ihres ersten Auftretens.

```python
df['bfs_name'].value_counts()
```

zeigt dagegen zusätzlich, **wie viele Inserate je Gemeinde vorhanden sind**.

Die ursprüngliche Zelle erstellt nur eine Übersicht der Kategorien. **Sie verändert `df` nicht und zählt keine Inserate.**

Führe sie aus. Du solltest eine Ausgabe mit Gemeindenamen sehen, etwa `array([...], dtype=object)`. Danach folgt die **Kreuztabelle („Cross-tabulation“)**.

> ok aber nach aufgebnstellung weitermachen bitte

Ja, wir bleiben bei der Aufgabenstellung. **Aufgabe 2a verlangt, das Notebook Schritt für Schritt auszuführen und den Code zu verstehen.** Deshalb gehören auch die Kategorien und die folgende Kreuztabelle dazu.

Dabei behalten wir das Ziel von **2b–c** im Blick: **Ausreisser erkennen, begründet herausfiltern und die Kennzahlen und Grafiken danach vergleichen.**

Wir gehen jetzt im Notebook zum Abschnitt **„Cross-tabulation“**. Schicke mir die dortige Codezelle, dann erkläre ich genau diese und wir führen sie aus.

> pd.crosstab(df['luxurious'], df['rooms'])

```python
pd.crosstab(df['luxurious'], df['rooms'])
```

Erstellt eine **Kreuztabelle**: Sie zählt, wie viele Inserate zu jeder Kombination aus **Luxusmerkmal und Zimmerzahl** gehören.

- **Zeilen:** `luxurious` – `0` bedeutet nicht als luxuriös markiert, `1` bedeutet als luxuriös markiert.
- **Spalten:** die verschiedenen Zimmerzahlen.
- **Zellen:** Anzahl der passenden Inserate.

Steht beispielsweise in Zeile `1` und Spalte `4.5` eine **2**, gibt es **zwei als luxuriös markierte Inserate mit 4,5 Zimmern**.

Die Tabelle enthält **absolute Häufigkeiten**, keine Preise oder Prozentwerte. Dabei beschreibt `luxurious` die Kennzeichnung im Datensatz; sie ist keine unabhängige Bewertung der Wohnungsqualität.

**Führe die Zelle aus und schicke mir die Tabelle.** Dann interpretieren wir das Ergebnis im Rahmen von Aufgabe 2a.

> |     **rooms** | **1.0** | **1.5** | **2.0** | **2.5** | **3.0** | **3.5** | **4.0** | **4.5** | **5.0** | **5.5** | **6.0** | **6.5** | **7.0** | **7.5** | **8.5** |
> | ------------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
> | **luxurious** |         |         |         |         |         |         |         |         |         |         |         |         |         |         |         |
> |             0 |      52 |      36 |      39 |     135 |      44 |     200 |      28 |     164 |       3 |      53 |       3 |      13 |       2 |       3 |       1 |
> |             1 |       0 |       0 |       0 |       6 |       0 |       3 |       0 |       0 |       0 |       0 |       0 |       1 |       0 |       0 |       0 |

Die Kreuztabelle zeigt **10 als luxuriös markierte Inserate**:

- **6** mit 2,5 Zimmern
- **3** mit 3,5 Zimmern
- **1** mit 6,5 Zimmern

Die übrigen **776 Inserate** sind nicht als luxuriös markiert. Insgesamt sind es wieder **786**.

Beispielsweise gibt es bei **2,5 Zimmern** insgesamt `135 + 6 = 141` Inserate. Davon sind sechs als luxuriös markiert.

**Wichtig:** Die Tabelle zählt Inserate. Sie sagt nicht, wie teuer die Wohnungen sind oder ob die Luxuskennzeichnung zuverlässig ist. Für Aufgabe 2a verstehen wir damit, wie zwei kategorial betrachtete Merkmale gemeinsam ausgewertet werden; Ausreisser entfernen wir hier noch nicht.

**Weiter zur nächsten Codezelle im Notebook – schicke mir den Code.**

> schau doch selber alter

<details><summary>2 previous messages</summary>

> Ich lese die nächsten Zellen direkt aus dem Notebook und führe dich in der vorgegebenen Reihenfolge weiter.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/exploratory_data_analysis_apartment_data.ipynb'))
> for i,c in enumerate(n['cells']):
>  if 'pd.crosstab' in ''.join(c['source']):
>   for j in range(i+1,min(i+9,len(n['cells']))):
>    print(j,n['cells'][j]['cell_type'],''.join(n['cells'][j]['source']))
>   break
> PY`
>
> </details>
</details>

Du hast recht, ich kann den Code selbst nachschauen. Als Nächstes folgt **„Pivot tables“**. Die leere Codezelle kannst du überspringen.

```python
pd.pivot_table(
    df[['rooms', 'price', 'price_per_m2', 'area', 'luxurious']],
    index=['rooms', 'luxurious'],
    values=['price', 'price_per_m2', 'area'],
    aggfunc=(np.mean, 'count')
)
```

Diese Pivot-Tabelle **gruppiert die Inserate nach Zimmerzahl und Luxuskennzeichnung**. Für jede Kombination berechnet sie den Durchschnitt und die Anzahl vorhandener Werte.

| Bestandteil | Bedeutung |
|---|---|
| `index=['rooms', 'luxurious']` | Bildet Gruppen, etwa „2,5 Zimmer, luxuriös“. |
| `values=[...]` | Untersucht Mietpreis, Quadratmeterpreis und Fläche. |
| `np.mean` | Berechnet den Mittelwert innerhalb jeder Gruppe. |
| `'count'` | Zählt die vorhandenen Werte innerhalb jeder Gruppe. |

**Der Unterschied zur Kreuztabelle:** Dort haben wir nur Inserate gezählt. Jetzt sehen wir zusätzlich, wie teuer und gross die Wohnungen in den jeweiligen Gruppen durchschnittlich sind.

Da wir fehlende Werte bereits entfernt haben, sollten die Anzahlen für `price`, `price_per_m2` und `area` innerhalb einer Gruppe gleich sein.

Achte beim Interpretieren besonders auf die **Gruppengrösse**: Die luxuriöse 6,5-Zimmer-Gruppe enthält laut Kreuztabelle nur **ein Inserat**. Ihr „Durchschnitt“ entspricht deshalb genau diesem einen Angebot und lässt sich kaum verallgemeinern.

**Führe die Pivot-Zelle aus und schicke mir die Ausgabe.** Wir prüfen daran auch, wie sich die zuvor entdeckten auffälligen Inserate auf die Gruppenmittelwerte auswirken.

> |           |               | **area**   | **price**  | **price_per_m2** |             |           |           |
> | :-------- | :------------ | :--------- | :--------- | :--------------- | ----------- | --------- | --------- |
> |           |               | **count**  | **mean**   | **count**        | **mean**    | **count** | **mean**  |
> | **rooms** | **luxurious** |            |            |                  |             |           |           |
> | 1.0       | 0             | 52         | 32.057692  | 52               | 1306.346154 | 52        | 50.168077 |
> | 1.5       | 0             | 36         | 35.333333  | 36               | 2110.166667 | 36        | 65.455000 |
> | 2.0       | 0             | 39         | 54.589744  | 39               | 2155.846154 | 39        | 42.528462 |
> | 2.5       | 0             | 135        | 66.800000  | 135              | 2382.755556 | 135       | 37.010000 |
> | 1         | 6             | 72.166667  | 6          | 3339.500000      | 6           | 45.978333 |           |
> | 3.0       | 0             | 44         | 68.159091  | 44               | 1964.022727 | 44        | 28.677955 |
> | 3.5       | 0             | 200        | 89.770000  | 200              | 2648.980000 | 200       | 29.494700 |
> | 1         | 3             | 101.666667 | 3          | 6036.666667      | 3           | 59.826667 |           |
> | 4.0       | 0             | 28         | 98.464286  | 28               | 2852.357143 | 28        | 29.646429 |
> | 4.5       | 0             | 164        | 115.060976 | 164              | 3067.847561 | 164       | 26.332622 |
> | 5.0       | 0             | 3          | 108.000000 | 3                | 2881.666667 | 3         | 26.376667 |
> | 5.5       | 0             | 53         | 153.811321 | 53               | 3523.094340 | 53        | 23.143396 |
> | 6.0       | 0             | 3          | 667.666667 | 3                | 3833.333333 | 3         | 15.706667 |
> | 6.5       | 0             | 13         | 253.000000 | 13               | 4077.461538 | 13        | 21.676154 |
> | 1         | 1             | 300.000000 | 1          | 11.000000        | 1           | 0.040000  |           |
> | 7.0       | 0             | 2          | 175.000000 | 2                | 6350.000000 | 2         | 36.325000 |
> | 7.5       | 0             | 3          | 205.000000 | 3                | 4765.000000 | 3         | 23.273333 |
> | 8.5       | 0             | 1          | 210.000000 | 1                | 8500.000000 | 1         | 40.480000 |

Die Pivot-Tabelle zeigt, **wie stark einzelne auffällige Inserate die Mittelwerte beeinflussen können**.

Beim Kopieren sind die mehrstufigen Überschriften etwas verrutscht. Die sechs Ergebnisspalten gehören so zusammen:

| `area` | | `price` | | `price_per_m2` | |
|---|---|---|---|---|---|
| count | mean | count | mean | count | mean |

Die Zimmerzahl wird im Notebook bei aufeinanderfolgenden Gruppen nicht wiederholt. Die Zeile mit `luxurious = 1` direkt unter **2,5 Zimmern** gehört deshalb ebenfalls zu **2,5 Zimmern**.

**Vergleich der Luxuskennzeichnung**

| Zimmer | Luxuriös | Anzahl | Ø Mietpreis | Ø Preis/m² |
|---|---|---:|---:|---:|
| 2,5 | Nein | 135 | 2’382,76 CHF | 37,01 CHF |
| 2,5 | Ja | 6 | 3’339,50 CHF | 45,98 CHF |
| 3,5 | Nein | 200 | 2’648,98 CHF | 29,49 CHF |
| 3,5 | Ja | 3 | 6’036,67 CHF | 59,83 CHF |

Die als luxuriös markierten Angebote sind in diesen Gruppen durchschnittlich teurer. **Das beweist keinen ursächlichen Effekt der Luxuskennzeichnung**: Die Gruppen sind unterschiedlich gross und können sich auch bei Lage, Fläche oder Ausstattung unterscheiden.

Für unsere **Ausreisseranalyse in Aufgabe 2b** sind besonders zwei Ergebnisse wichtig:

- **6 Zimmer, nicht luxuriös:** Nur drei Inserate ergeben eine Durchschnittsfläche von **667,67 m²**. Das zuvor entdeckte Inserat mit **1’633 m²** zieht diesen Mittelwert stark nach oben.
- **6,5 Zimmer, luxuriös:** Die Gruppe enthält genau **ein Inserat** mit **11 CHF Miete** und **0,04 CHF/m²**. Der Mittelwert übernimmt vollständig dessen unplausiblen Preis.

**Merksatz:** Ein Mittelwert sollte immer zusammen mit der Anzahl der Beobachtungen und möglichen Extremwerten betrachtet werden.

Als Nächstes folgt **„Correlation matrix“**. Im Notebook enthält diese Zelle allerdings eine fachliche Ungenauigkeit:

```python
corr = df[[
    'rooms', 'area', 'price',
    'price_per_m2', 'pop_dens', 'frg_pct'
]].cov().corr()
```

**`.cov().corr()` berechnet Korrelationen zwischen den Spalten der Kovarianzmatrix.** Für die üblichen Korrelationen zwischen unseren ursprünglichen Merkmalen muss `.cov()` entfallen.

Ändere die Zelle deshalb zu:

```python
corr = df[[
    'rooms', 'area', 'price',
    'price_per_m2', 'pop_dens', 'frg_pct'
]].corr()

corr
```

Die Werte liegen zwischen **−1 und +1**:

- **Positiv:** Höhere Werte eines Merkmals gehen tendenziell mit höheren Werten des anderen einher.
- **Negativ:** Höhere Werte gehen tendenziell mit niedrigeren Werten des anderen einher.
- **Nahe 0:** Kaum linearer Zusammenhang; andere Zusammenhänge können trotzdem bestehen.

**Führe die korrigierte Zelle aus und schicke mir die Matrix.**

> weiter

Weiter mit **„Covariance matrix“**. Die Zelle lautet:

```python
cov = df[[
    'rooms',
    'area',
    'price',
    'price_per_m2',
    'pop_dens',
    'frg_pct'
]].cov()

cov
```

Sie berechnet die **Kovarianz** zwischen jedem Paar der ausgewählten Merkmale.

Wie bei der Korrelation zeigt das Vorzeichen die Richtung des gemeinsamen Verlaufs:

| Kovarianz | Bedeutung |
|---|---|
| Positiv | Höhere Werte eines Merkmals gehen tendenziell mit höheren Werten des anderen einher. |
| Negativ | Höhere Werte gehen tendenziell mit niedrigeren Werten des anderen einher. |
| Nahe 0 | Wenig gemeinsamer linearer Verlauf. |

Der entscheidende Unterschied: **Die Kovarianz hängt von den Einheiten ab und ist nicht auf −1 bis +1 begrenzt.**

Wenn wir die Fläche statt in m² in cm² ausdrücken, ändern sich ihre Kovarianzen, obwohl die Wohnungen dieselben bleiben. Deshalb können wir anhand der grössten Zahl in dieser Matrix **nicht einfach den stärksten Zusammenhang bestimmen**.

Die **Korrelation** normiert die Kovarianz mithilfe der Standardabweichungen:

\[
r_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{s_X\cdot s_Y}
\]

Dadurch wird sie einheitenlos und besser zwischen verschiedenen Merkmalspaaren vergleichbar.

Auf der **Diagonale** der Kovarianzmatrix steht jeweils die **Varianz** eines Merkmals:

\[
\operatorname{Cov}(X,X)=s_X^2
\]

Das ist das Quadrat seiner Standardabweichung und beschreibt seine Streuung.

**Führe die Kovarianz-Zelle aus.** Für unsere Aufgabe behalten wir im Kopf: Sowohl Kovarianz als auch Pearson-Korrelation können stark von Extremwerten beeinflusst werden. Nach dem Herausfiltern der auffälligen Inserate können sich deshalb auch diese Matrizen verändern.

> warte was ist kovarianz und korrelation?

Beide beschreiben, **wie zwei Merkmale gemeinsam variieren** – beispielsweise Wohnfläche und Mietpreis.

Stell dir drei Wohnungen vor:

| Wohnfläche | Miete |
|---:|---:|
| 40 m² | 1’200 CHF |
| 80 m² | 2’000 CHF |
| 120 m² | 2’800 CHF |

Hier gilt: **Je grösser die Wohnung, desto höher die Miete.** Beide Merkmale steigen gemeinsam.

**Kovarianz: Gehen die Abweichungen in dieselbe Richtung?**

Wir vergleichen jede Wohnung mit den Durchschnittswerten. In unserem Beispiel sind das **80 m²** und **2’000 CHF**.

- Die kleine Wohnung liegt bei Fläche **und** Miete unter dem Durchschnitt.
- Die grosse Wohnung liegt bei beiden darüber.

Die Kovarianz fasst diese gemeinsamen Abweichungen zusammen:

| Vorzeichen | Aussage |
|---|---|
| **Positiv** | Überdurchschnittliche Fläche geht tendenziell mit überdurchschnittlicher Miete einher. |
| **Negativ** | Überdurchschnittliche Fläche geht tendenziell mit unterdurchschnittlicher Miete einher. |
| **Null** | Die gemeinsamen Abweichungen gleichen sich aus; kein linearer Zusammenhang. |

Das Problem: **Die Grösse der Kovarianz hängt von den Einheiten ab.** Messen wir die Fläche in cm² statt m², wird die Zahl viel grösser. Der Zusammenhang selbst bleibt aber gleich.

**Korrelation: Wie stark ist der lineare Zusammenhang auf einer einheitlichen Skala?**

Die **Pearson-Korrelation** ist die normierte Kovarianz. Sie liegt immer zwischen **−1 und +1**:

| Korrelation | Bedeutung |
|---:|---|
| **+1** | Alle Punkte liegen exakt auf einer steigenden Geraden. |
| **+0,8** | Starker positiver linearer Zusammenhang. |
| **0** | Kein linearer Zusammenhang. |
| **−0,8** | Starker negativer linearer Zusammenhang. |
| **−1** | Alle Punkte liegen exakt auf einer fallenden Geraden. |

Unser Beispiel hat **Korrelation +1**, weil pro zusätzlichen 40 m² die Miete immer um genau 800 CHF steigt. Echte Wohnungsdaten streuen stärker, etwa wegen unterschiedlicher Lagen und Ausstattungen.

**Zum Merken:**

- **Kovarianz:** Zeigt die Richtung des gemeinsamen Verlaufs; ihre Grösse hängt von den Einheiten ab.
- **Korrelation:** Macht Richtung und Stärke des **linearen** Zusammenhangs auf einer vergleichbaren Skala sichtbar.

Wichtig: Eine Korrelation von **0,8 bedeutet nicht „80 % höhere Miete“**. Sie beschreibt einen Zusammenhang, keine Preissteigerung. Und sie beweist keine Ursache.

**Kurze Verständnisfrage:** Wenn der Quadratmeterpreis mit zunehmender Wohnfläche tendenziell sinkt – erwartest du eine positive oder negative Korrelation?

> negativ

Genau, **negativ**: Wenn die Wohnfläche steigt und der Quadratmeterpreis tendenziell sinkt, bewegen sich die beiden Merkmale in entgegengesetzte Richtungen.

Je näher die Korrelation an **−1** liegt, desto enger folgen die Punkte einer fallenden Geraden. Bei beispielsweise **−0,2** wäre der negative lineare Zusammenhang eher schwach.

Eine Besonderheit unserer Daten: **Die Fläche steckt bereits in der Berechnung des Quadratmeterpreises**:

\[
\text{Preis pro m²}=\frac{\text{Mietpreis}}{\text{Fläche}}
\]

Die beiden Merkmale sind dadurch rechnerisch miteinander verbunden. Das sollten wir bei der Interpretation berücksichtigen.

Führe jetzt die korrigierte Korrelationszelle aus, falls noch nicht geschehen:

```python
corr = df[[
    'rooms', 'area', 'price',
    'price_per_m2', 'pop_dens', 'frg_pct'
]].corr()

corr
```

**Schicke mir die Matrix.** Dann lesen wir die tatsächlichen Zusammenhänge unserer Wohnungsdaten gemeinsam ab.

> |              | **rooms** |  **area** | **price** | **price_per_m2** | **pop_dens** | **frg_pct** |
> | -----------: | --------: | --------: | --------: | ---------------: | -----------: | ----------: |
> |        rooms |  1.000000 |  0.546018 |  0.448113 |        -0.488242 |    -0.325442 |   -0.287241 |
> |         area |  0.546018 |  1.000000 |  0.347605 |        -0.332813 |    -0.195720 |   -0.240144 |
> |        price |  0.448113 |  0.347605 |  1.000000 |         0.261341 |     0.273259 |    0.081137 |
> | price_per_m2 | -0.488242 | -0.332813 |  0.261341 |         1.000000 |     0.584032 |    0.337679 |
> |     pop_dens | -0.325442 | -0.195720 |  0.273259 |         0.584032 |     1.000000 |    0.658301 |
> |      frg_pct | -0.287241 | -0.240144 |  0.081137 |         0.337679 |     0.658301 |    1.000000 |

Deine Vermutung bestätigt sich: **Wohnfläche und Quadratmeterpreis korrelieren negativ**, mit **−0,33**. Grössere Wohnungen haben in diesem Datensatz tendenziell einen niedrigeren Preis pro m². Der lineare Zusammenhang ist allerdings nicht besonders eng.

So liest du die Matrix: Suche die **Zeile des einen Merkmals** und die **Spalte des anderen**. Am Schnittpunkt steht ihre Korrelation.

Die wichtigsten Ergebnisse:

| Merkmale | Korrelation | Bedeutung im Datensatz |
|---|---:|---|
| Zimmerzahl ↔ Fläche | **+0,55** | Wohnungen mit mehr Zimmern haben tendenziell mehr Fläche. |
| Zimmerzahl ↔ Mietpreis | **+0,45** | Mehr Zimmer gehen tendenziell mit höherer Gesamtmiete einher. |
| Zimmerzahl ↔ Preis/m² | **−0,49** | Mehr Zimmer gehen tendenziell mit niedrigerem Quadratmeterpreis einher. |
| Bevölkerungsdichte ↔ Preis/m² | **+0,58** | Inserate in dichter besiedelten Gemeinden haben tendenziell höhere Quadratmeterpreise. |
| Fläche ↔ Mietpreis | **+0,35** | Grössere Wohnungen kosten tendenziell mehr, aber der lineare Zusammenhang ist hier eher mässig. |

**Warum ist Fläche ↔ Mietpreis nicht stärker?** Lage und Ausstattung können eine Rolle spielen. Zudem könnten die auffälligen Flächen und falschen Mietpreise den Wert beeinflussen. Welche Wirkung die Bereinigung tatsächlich hat, prüfen wir später durch den Vergleich.

Zwei Eigenschaften der Matrix:

- **Auf der Diagonale steht immer 1:** Jedes dieser Merkmale korreliert perfekt mit sich selbst.
- **Die Matrix ist spiegelbildlich:** Fläche ↔ Preis ist dasselbe wie Preis ↔ Fläche. Du musst jedes Paar nur einmal betrachten.

Bei Gemeindemerkmalen wie `pop_dens` und `frg_pct` gilt ausserdem: **Eine Gemeinde kommt für jedes ihrer Inserate erneut vor.** Die Korrelation von **+0,66** zwischen diesen beiden Merkmalen ist daher durch die Anzahl der Inserate je Gemeinde mitgeprägt. Sie beschreibt keine Ursache und keinen Zusammenhang auf Ebene einzelner Personen.

Damit ist die Korrelationsmatrix für **Aufgabe 2a** interpretiert. Führe anschliessend die bereits besprochene **Kovarianz-Zelle** aus; danach gehen wir zu den grafischen Auswertungen weiter.

> weiter

<details><summary>2 previous messages</summary>

> Ich lese die nächste Grafikzelle direkt aus dem Notebook.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/exploratory_data_analysis_apartment_data.ipynb'))
> for i,c in enumerate(n['cells'][37:44],37):
>  print(i,c['cell_type'],''.join(c['source']))
> PY`
>
> </details>
</details>

Jetzt beginnt der grafische Teil mit **„Line chart (matplotlib)“**, einem Liniendiagramm.

```python
x = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025]
y = [100, 125, 156, 167, 175, 215, 230, 255]
```

**Das sind vorgegebene Beispieldaten**, keine Auswertung unserer Wohnungsinserate:

- `x` enthält die Jahre.
- `y` enthält einen beispielhaften Mietpreisindex.

Ein **Index** beschreibt Veränderungen gegenüber einem Basiswert. Hier gilt **1990 = 100**:

| Jahr | Index | Bedeutung gegenüber 1990 |
|---|---:|---|
| 1990 | 100 | Basiswert |
| 1995 | 125 | 25 % höher |
| 2025 | 255 | 155 % höher |

**255 bedeutet also nicht 255 CHF**, sondern das 2,55-Fache des Ausgangsniveaus.

Gezeichnet wird mit:

```python
fig = plt.figure(figsize=(7, 4))
plt.plot(x, y, color="green")
```

`plt.plot()` verbindet die aufeinanderfolgenden Wertepaare mit einer grünen Linie. Die übrigen Zeilen setzen Titel, Achsenbeschriftungen und Schriftgrössen; `plt.show()` zeigt die Grafik an.

**Wofür eignet sich ein Liniendiagramm?** Für Entwicklungen mit einer sinnvollen Reihenfolge, insbesondere über die Zeit. Die Verbindungslinien erleichtern das Erkennen des Verlaufs.

Führe die Zelle aus. Du solltest einen steigenden Verlauf sehen. **Für unsere Ausreissersuche liefert dieses Beispiel noch keine Erkenntnis**, weil es `df` nicht verwendet. Als Nächstes folgt der Boxplot der tatsächlichen Wohnflächen.

> weizet

Jetzt folgt **„Boxplot (seaborn)“**. Damit untersuchen wir die tatsächlichen **Wohnflächen** auf auffällige Werte.

```python
plt.figure(figsize=(8, 1.2))
plt.ticklabel_format(style='plain')
sns.boxplot(x=df['area'], color="greenyellow")
```

- `figsize=(8, 1.2)` erstellt eine breite, flache Zeichenfläche.
- `style='plain'` verwendet normale Zahlendarstellung statt wissenschaftlicher Schreibweise.
- `sns.boxplot(...)` zeichnet einen horizontalen Boxplot der Spalte `area`.

**So liest du den Boxplot:**

| Bestandteil | Bedeutung |
|---|---|
| Linker Rand der Box | 25%-Quantil: **63 m²** |
| Linie innerhalb der Box | Median: **86 m²** |
| Rechter Rand der Box | 75%-Quantil: **108,75 m²** |
| „Antennen“ (*Whisker*) | Reichen bis zu den äussersten beobachteten Werten innerhalb der üblichen Grenzen. |
| Einzelne Punkte ausserhalb | Nach der Boxplot-Regel auffällige Werte. |

Die **Box enthält die mittleren 50 %** der Flächenwerte. Ihre Breite ist der Interquartilsabstand, kurz **IQR**:

\[
IQR = 108{,}75-63=45{,}75\ \text{m²}
\]

Die obere Grenze der üblichen Boxplot-Regel beträgt:

\[
Q_3+1{,}5\cdot IQR
=108{,}75+1{,}5\cdot45{,}75
=177{,}375\ \text{m²}
\]

Flächen **über rund 177,38 m²** werden daher als einzelne Punkte dargestellt. Die rechte Antenne endet beim grössten tatsächlich vorhandenen Wert, der diese Grenze nicht überschreitet.

**Wichtig für Aufgabe 2b:** Ein solcher Punkt ist ein statistisch auffälliger Wert, aber nicht automatisch ein Datenfehler. Eine Wohnung mit 180 m² kann plausibel sein; die **1’633 m²** verdienen deutlich genauere Prüfung.

**Führe die Zelle aus.** Wegen der extrem grossen Flächen könnte die Box links stark zusammengedrückt erscheinen. Schicke mir die Grafik oder beschreibe kurz, was du siehst.

> ja, ist stark links

Genau: Die Fläche von **1’633 m²** zieht die x-Achse weit nach rechts. Dadurch wirkt die Box mit den mittleren 50 % der Wohnungen klein und links zusammengedrückt. **Das ist ein sichtbarer Einfluss der Extremwerte auf die Darstellung.**

Weiter mit **„Histogram (matplotlib)“**. Hier betrachten wir den **Quadratmeterpreis**:

```python
n, bins, patches = plt.hist(
    x=df['price_per_m2'],
    bins=25,
    color='#42AD12',
    alpha=0.5,
    rwidth=0.95
)
```

Ein **Histogramm** teilt Zahlenwerte in Intervalle ein und zählt, wie viele Beobachtungen in jedes Intervall fallen.

- **x-Achse:** Quadratmeterpreis in CHF/m².
- **y-Achse:** Anzahl der Inserate im jeweiligen Preisintervall.
- **`bins=25`:** Teilt den Wertebereich in 25 gleich breite Intervalle.
- **`color='#42AD12'`:** Legt die Farbe mit einem Hex-Farbcode fest.
- **`alpha=0.5`:** Macht die Balken halbtransparent.
- **`rwidth=0.95`:** Lässt kleine Lücken zwischen den Balken.

Die drei Rückgaben werden gespeichert:

| Variable | Inhalt |
|---|---|
| `n` | Anzahl der Inserate pro Intervall |
| `bins` | Grenzen der Intervalle |
| `patches` | Die gezeichneten Balkenobjekte |

**Unterschied zum Balkendiagramm:** Ein Histogramm zeigt Intervalle eines numerischen Merkmals. Ein Balkendiagramm vergleicht Kategorien, etwa Gemeinden oder Supermarktmarken.

**Führe die gesamte Histogramm-Zelle aus.** Achte darauf, in welchem Preisbereich die meisten Inserate liegen und ob ein langer Ausläufer zu hohen Preisen erkennbar ist. Die zuvor gefundenen Werte nahe **0 CHF/m²** sollten ganz links liegen.

> ja

<details><summary>2 previous messages</summary>

> Ich schaue mir die nächste Zelle zum Dichteplot an.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/exploratory_data_analysis_apartment_data.ipynb'))
> for i,c in enumerate(n['cells'][43:49],43):
>  print(i,c['cell_type'],''.join(c['source']))
> PY`
>
> </details>
</details>

Weiter mit **„Density plot (seaborn)“**. Diese Grafik kombiniert das Histogramm mit einer **geglätteten Dichtekurve** des Quadratmeterpreises.

Der zentrale Aufruf lautet:

```python
sns.distplot(
    df['price_per_m2'],
    hist=True,
    kde=True,
    bins=20,
    color='green',
    hist_kws={'edgecolor': 'black'},
    kde_kws={'linewidth': 2}
)
```

| Parameter | Bedeutung |
|---|---|
| `hist=True` | Zeigt die Histogrammbalken. |
| `kde=True` | Ergänzt eine geglättete Dichtekurve. |
| `bins=20` | Verwendet 20 Preisintervalle. |
| `hist_kws={'edgecolor': 'black'}` | Zeichnet schwarze Balkenränder. |
| `kde_kws={'linewidth': 2}` | Legt die Linienstärke der Kurve fest. |

**Was bedeutet „Dichte“?**

Anders als im vorherigen Histogramm zeigt die y-Achse hier **keine Anzahl von Wohnungen**. Die Darstellung ist so normiert, dass die gesamte Histogrammfläche 1 ergibt.

Die Kurve schätzt, **in welchen Preisbereichen sich die Inserate konzentrieren**:

- Ein hoher Kurvenbereich bedeutet eine hohe Konzentration von Werten.
- Ein niedriger Bereich bedeutet eine geringe Konzentration.
- Die Kurvenhöhe selbst ist **kein Prozentanteil**. Dafür müsste man die Fläche über einem Preisintervall betrachten.

**Die Kurve ist eine geglättete Schätzung.** Sie zeigt keine zeitliche Entwicklung und verbindet auch keine einzelnen Inserate.

Führe die Zelle aus. Achte auf den Hauptgipfel und den Ausläufer zu hohen Quadratmeterpreisen. Falls `sns.distplot` eine Fehlermeldung auslöst, schicke sie mir; ansonsten gehen wir danach zum **QQ-Plot der Wohnfläche**.

> weiter

Jetzt folgt **„Quantile-Quantile (QQ-) plot“**. Damit prüfen wir, **wie stark die Verteilung der Wohnflächen von einer Normalverteilung abweicht**.

Zuerst werden die Flächen standardisiert:

```python
x = 'area'
df_qq = df
df_qq['var'] = (df[x] - df[x].mean()) / df[x].std()
```

Ändere dabei die zweite Zeile zu:

```python
df_qq = df.copy()
```

**`df_qq = df` erstellt keine unabhängige Kopie.** Die neue Spalte würde dadurch auch in `df` landen. Mit `.copy()` arbeiten wir auf einer separaten Tabelle.

Die vollständige Berechnung lautet dann:

```python
x = 'area'
df_qq = df.copy()
df_qq['var'] = (df[x] - df[x].mean()) / df[x].std()
```

Die Formel berechnet für jede Fläche einen **z-Wert**:

\[
z=\frac{\text{Fläche}-\text{mittlere Fläche}}{\text{Standardabweichung der Fläche}}
\]

| z-Wert | Bedeutung |
|---:|---|
| `0` | Die Fläche entspricht dem Mittelwert. |
| `1` | Eine Standardabweichung über dem Mittelwert. |
| `−1` | Eine Standardabweichung darunter. |

**Standardisieren macht die Daten nicht normalverteilt.** Es verändert nur ihren Massstab.

Danach:

```python
print(df_qq.sort_values('var')[['area', 'var']])
```

Das zeigt Fläche und z-Wert, sortiert von klein nach gross.

```python
sm.qqplot(df_qq['var'], line='45')
py.show()
```

Der QQ-Plot vergleicht:

- **x-Achse:** theoretische Quantile einer Standardnormalverteilung.
- **y-Achse:** Quantile unserer standardisierten Wohnflächen.

**So liest du die Grafik:** Liegen die Punkte ungefähr auf der diagonalen Referenzlinie, passt die Verteilung näherungsweise zur Normalverteilung. Deutliche systematische Abweichungen sprechen dagegen.

Bei unseren Flächen erwarten wir besonders rechts starke Abweichungen nach oben: Die extrem grossen Wohnungen sind viel grösser, als es zu einer Normalverteilung passen würde.

**Führe die Zelle mit `.copy()` aus.** Schau besonders auf die Punkte ganz rechts und darauf, wie weit sie von der Diagonalen entfernt liegen.

> wird das in aufgabe verlangt die änderung?

**Nein, die Änderung zu `.copy()` wird nicht ausdrücklich verlangt.** Sie war eine technische Empfehlung von mir.

Für **Aufgabe 2a** kannst du die Originalzelle unverändert ausführen:

```python
df_qq = df
```

Du solltest dabei nur verstehen: `df_qq` und `df` verweisen dann auf dieselbe Tabelle. Die folgende Zuweisung fügt deshalb die Spalte `var` auch zu `df` hinzu.

Wir bleiben ab jetzt beim vorgegebenen Code und kennzeichnen optionale Änderungen klar. **Die frühere Korrektur von `.cov().corr()` zu `.corr()` war dagegen fachlich nötig, um die Korrelationen der ursprünglichen Merkmale zu berechnen.**

> aj einfach weiter und aufgabe lösen

<details><summary>2 previous messages</summary>

> Wir gehen mit dem vorgegebenen Notebook weiter und setzen danach den geforderten Ausreisserfilter um.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/exploratory_data_analysis_apartment_data.ipynb'))
> for i,c in enumerate(n['cells'][47:],47):
>  print(i,c['cell_type'],''.join(c['source']))
> PY`
>
> </details>
</details>

Weiter mit **„Barchart (matplotlib)“**. Führe die **beiden Codezellen** unter dieser Überschrift aus.

Zuerst werden die Inserate je Zimmerzahl gezählt:

```python
df_bar = df['rooms'].value_counts().nlargest(15).sort_values(ascending=True)
```

Von links nach rechts:

- **`value_counts()`** zählt die Inserate je Zimmerzahl.
- **`nlargest(15)`** behält die 15 häufigsten Zimmerkategorien.
- **`sort_values(ascending=True)`** sortiert diese nach Anzahl aufsteigend.

Danach bereitet der Code die Balken vor:

```python
napart = list(df_bar.values)
index = list(df_bar.index.values)
y_pos = np.arange(len(index))
```

`napart` enthält die **Anzahlen**, `index` die zugehörigen **Zimmerzahlen**. `y_pos` erzeugt die Positionen für die Balken.

Gezeichnet wird mit:

```python
ax.barh(y_pos, napart, align='center', color='g', alpha=0.8)
ax.set_yticks(y_pos, index)
```

**`barh()` erstellt horizontale Balken.** Ihre Länge zeigt die Anzahl der Inserate; die Beschriftung links zeigt die Zimmerzahl.

Aus unserer Kreuztabelle erwarten wir die längsten Balken bei:

| Zimmer | Anzahl Inserate |
|---:|---:|
| 3,5 | **203** |
| 4,5 | **164** |
| 2,5 | **141** |

Damit erkennen wir, **welche Wohnungsgrössen im Datensatz besonders häufig angeboten werden**. Die Grafik sagt nichts darüber aus, welche Wohnungen besonders gefragt sind – dafür bräuchten wir Nachfragedaten.

**Führe beide Zellen aus.** Danach folgt direkt das Kreisdiagramm derselben Häufigkeiten.

> weiter

Jetzt folgt **„Piechart (matplotlib)“**, das Kreisdiagramm.

```python
df_bar = df.rooms.value_counts().nlargest(8).sort_values(ascending=True)
```

Das zählt die Inserate je Zimmerzahl und wählt die **acht häufigsten Zimmerkategorien** aus.

```python
sizes = list(df_bar.values)
labels = list(df_bar.index.values)
```

- `sizes` enthält die Anzahlen und bestimmt die Grösse der Kreissektoren.
- `labels` enthält die zugehörigen Zimmerzahlen.

```python
explode = (0, 0, 0, 0, 0.0, 0, 0, 0.1)
```

Der letzte Sektor wird etwas nach aussen verschoben. Da die Anzahlen aufsteigend sortiert wurden, ist das die **häufigste Zimmerkategorie**.

Der eigentliche Zeichenbefehl lautet:

```python
ax1.pie(
    sizes,
    labels=labels,
    explode=explode,
    autopct='%1.1f%%',
    shadow=False,
    startangle=90
)
```

| Parameter | Bedeutung |
|---|---|
| `autopct='%1.1f%%'` | Zeigt Prozentwerte mit einer Nachkommastelle. |
| `shadow=False` | Zeichnet keinen Schatten. |
| `startangle=90` | Dreht den Beginn des ersten Sektors auf 90°. |

```python
ax1.axis('equal')
```

Sorgt dafür, dass der Kreis rund dargestellt wird.

**Wichtig beim Interpretieren:** Die Prozentwerte beziehen sich nur auf die **acht ausgewählten Kategorien**, nicht auf alle 786 Inserate. Die übrigen Zimmerkategorien fehlen im Diagramm.

**Führe die Zelle aus.** Danach folgt das Streudiagramm von Wohnfläche und Mietpreis – dort werden die auffälligen Inserate wieder besonders relevant.

> weiter

Jetzt folgt **„Scatterplot (matplotlib)“**. Wir betrachten den Zusammenhang zwischen **Wohnfläche und Mietpreis**:

```python
plt.figure(figsize=(7,4))

plt.scatter(
    df['area'],
    df['price'],
    color="green",
    alpha=1.0,
    s=10
)

plt.title('Scatterplot', fontsize=12)
plt.xlabel('area (m2)')
plt.ylabel('price (CHF)')
plt.show()
```

**Jeder Punkt steht für ein Wohnungsinserat:**

- Die **x-Position** zeigt die Wohnfläche in m².
- Die **y-Position** zeigt den Mietpreis in CHF.
- `s=10` legt die Markerfläche fest.
- `alpha=1.0` bedeutet vollständig deckende Punkte.

Eine Wohnung mit **100 m² und 2’500 CHF Miete** liegt beispielsweise am Punkt **(100, 2500)**.

Für **Aufgabe 2b – Ausreisser erkennen** achtest du auf:

- **Punkte weit rechts:** besonders grosse Flächen, etwa 585, 863 und 1’633 m².
- **Punkte nahe dem unteren Rand:** die unplausiblen Mietpreise von 10, 11 und 16 CHF.
- **Die übrige Punktwolke:** Steigen die Mietpreise tendenziell mit der Fläche? Wie stark streuen sie bei ähnlicher Fläche?

Anders als der Boxplot zeigt dieses Diagramm **zwei Merkmale gleichzeitig**. Dadurch sehen wir beispielsweise, dass eine extrem grosse Fläche nicht unbedingt mit einer entsprechend hohen Miete verbunden ist.

**Führe die Zelle aus.** Die grossen Flächen dürften die meisten anderen Punkte wieder links zusammendrücken. Danach ergänzen wir im nächsten Abschnitt die Regressionsgerade.

> ja weiter

Jetzt folgt **„Scatterplot (matplotlib) with regression line“**. Eine Regressionsgerade fasst den **linearen Zusammenhang zwischen Fläche und Mietpreis** zusammen.

Zuerst bildet der Code eine Teilmenge:

```python
df_sub = df.loc[df.price >= 1000]
print(df_sub.shape)
```

Es bleiben nur Inserate mit **mindestens 1’000 CHF Miete**. Damit werden unter anderem die unplausiblen Preise von 10, 11 und 16 CHF ausgeschlossen. **Die extrem grossen Flächen bleiben jedoch enthalten.** `df` wird dabei nicht verändert.

Danach zeichnet der Code die ausgewählten Inserate als grüne Punkte.

Die Gerade wird hier berechnet:

```python
b, a = np.polyfit(df_sub.area, df_sub.price, 1)
print(b)
print(a)
```

**`np.polyfit(..., 1)`** passt eine Gerade an die Daten an. Sie wählt die Gerade so, dass die Summe der quadrierten vertikalen Abstände zwischen Punkten und Gerade möglichst klein wird.

Ihre Gleichung lautet:

\[
\widehat{\text{Mietpreis}} = b \cdot \text{Fläche} + a
\]

| Wert | Bedeutung |
|---|---|
| `b` – Steigung | Um wie viele CHF sich der geschätzte Mietpreis pro zusätzlichem m² verändert. |
| `a` – Achsenabschnitt | Geschätzter Mietpreis bei 0 m²; hier vor allem ein mathematischer Parameter. |

**Beispiel:** Bei `b = 15` und `a = 1000` würde die Gerade für 80 m² schätzen:

\[
15 \cdot 80 + 1000 = 2’200\ \text{CHF}
\]

Das sind nur Beispielwerte – deine tatsächlichen Werte werden ausgegeben.

Gezeichnet wird die Gerade mit:

```python
plt.plot(
    df_sub.area,
    b * df_sub.area + a,
    linewidth=1,
    linestyle='dashed',
    color='darkred'
)
```

**Für unsere Ausreisseranalyse wichtig:** Die extrem grossen Flächen können die Gerade stark beeinflussen. Die Steigung beschreibt ausserdem einen Zusammenhang im Datensatz und beweist keinen ursächlichen Preiseffekt zusätzlicher Fläche.

**Führe die Zelle aus und schicke mir die beiden ausgegebenen Zahlen für `b` und `a`.**

> (769, 17)\
> 5.842687833767065\
> 2149.0487159317886

Deine geschätzte Gerade lautet:

\[
\widehat{\text{Mietpreis}} = 5{,}84 \cdot \text{Fläche} + 2’149{,}05
\]

- **Steigung `b = 5,84`:** Pro zusätzlichem m² steigt der geschätzte Mietpreis entlang dieser Geraden um rund **5,84 CHF**.
- **Achsenabschnitt `a = 2’149,05`:** Rechnerischer Wert bei 0 m². Als tatsächliche Wohnungsmiete ist er hier nicht sinnvoll interpretierbar.

Für **100 m²** ergibt sich beispielsweise:

\[
5{,}8427 \cdot 100 + 2’149{,}0487 \approx 2’733{,}32\ \text{CHF}
\]

**Die Steigung ist nicht der Quadratmeterpreis!** Die geschätzte Gesamtmiete besteht aus dem Flächenanteil **plus** dem Achsenabschnitt.

Die Ausgabe **`(769, 17)`** bedeutet:

- **769 Inserate** haben mindestens 1’000 CHF Miete. Gegenüber den vorherigen 786 wurden also **17 ausgeschlossen**.
- Die **17. Spalte** ist `var`, die zuvor durch die originale QQ-Plot-Zelle auch zu `df` hinzugefügt wurde.

Die auffälligen grossen Flächen sind weiterhin enthalten und können die Gerade beeinflussen. Ob die Gerade nach deren Ausschluss steiler wird, prüfen wir beim geforderten Vergleich.

Weiter mit **„Scatterplot-matrix (seaborn)“**:

```python
sns.set(style="ticks", font_scale=0.8)

g = sns.PairGrid(
    df[['rooms', 'area', 'price',
        'price_per_m2', 'pop_dens', 'frg_pct']],
    height=1.2,
    aspect=1
)

g.map_upper(sns.scatterplot, color='darkgreen', s=10)
g.map_lower(sns.scatterplot, color='darkgreen', s=10)
g.map_diag(plt.hist, color='brown')
```

Die **Streudiagrammmatrix** zeigt viele Merkmalskombinationen gleichzeitig:

- **Auf der Diagonale:** Histogramme der einzelnen Merkmale.
- **Ausserhalb der Diagonale:** Streudiagramme; das Spaltenmerkmal steht auf der x-Achse, das Zeilenmerkmal auf der y-Achse.
- Oberhalb und unterhalb der Diagonale erscheinen dieselben Paare mit vertauschten Achsen.

**Führe die Zelle aus.** Achte besonders auf die Diagramme mit `area`: Die extremen Flächen sollten dort erneut als weit entfernte Punkte auffallen.

> weiter

Weiter mit **„Hexagonal binning plot (matplotlib)“**. Diese Grafik zeigt, **wo besonders viele Inserate dicht beieinanderliegen**.

Zuerst wird eine Teilmenge ausgewählt:

```python
df_sub = df.loc[(df.price <= 6000) & (df.area <= 200)]
print(df_sub.shape)
```

Es bleiben Inserate mit:

- **höchstens 6’000 CHF Miete**
- **höchstens 200 m² Fläche**

**`&` bedeutet „und“:** Beide Bedingungen müssen erfüllt sein. Die Klammern um die einzelnen Bedingungen sind wichtig.

Dieser Filter gilt nur für `df_sub`. **Er ist noch nicht unsere abschliessende Ausreisserbereinigung** und entfernt beispielsweise die unplausibel niedrigen Mietpreise nicht gezielt.

Gezeichnet wird mit:

```python
plt.hexbin(
    df_sub.area,
    df_sub.price,
    gridsize=30,
    cmap='Greens'
)
```

Statt jedes Inserat als Punkt zu zeigen, teilt `hexbin()` die Zeichenfläche in **sechseckige Felder** ein und zählt die Inserate darin.

| Bestandteil | Bedeutung |
|---|---|
| x-Achse | Wohnfläche |
| y-Achse | Mietpreis |
| Farbe eines Sechsecks | Anzahl der Inserate in diesem Bereich |
| `gridsize=30` | Steuert die Feinheit des Rasters. |
| `cmap='Greens'` | Verwendet eine grüne Farbskala. |

Die Farblegende wird hier ergänzt:

```python
cb = plt.colorbar(label='count in bin')
cb.set_label('counts in bin')
```

**Dunklere Felder stehen bei dieser Farbskala für mehr Inserate.** So erkennen wir Häufungen, die im Streudiagramm durch überlagerte Punkte schwer sichtbar sein können.

**Führe die Zelle aus.** Schau, in welchen Kombinationen aus Fläche und Mietpreis die dunkelsten Felder liegen. Danach folgt die Korrelations-Heatmap.

> weiter

Jetzt folgt **„Correlation heatmap (seaborn)“**. Sie stellt die bereits besprochene Korrelationsmatrix **als Farben und Zahlen** dar.

```python
sns.set(font_scale=0.8)

plt.figure(figsize=(7,4))

corr = df[[
    'rooms',
    'area',
    'price',
    'price_per_m2',
    'pop_dens',
    'frg_pct'
]].corr().round(2)

sns.heatmap(
    corr,
    cmap="BrBG",
    annot=True
)
```

Der Code macht Folgendes:

| Code | Bedeutung |
|---|---|
| `.corr()` | Berechnet die Pearson-Korrelationen zwischen den Merkmalen. |
| `.round(2)` | Rundet auf zwei Nachkommastellen. |
| `sns.heatmap(corr, ...)` | Stellt die Matrix als farbige Felder dar. |
| `cmap="BrBG"` | Verwendet eine braun-grünblaue Farbskala. |
| `annot=True` | Schreibt die Korrelationswerte in die Felder. |

**Die Heatmap enthält dieselben Informationen wie die numerische Korrelationsmatrix.** Die Farben erleichtern es, Muster schnell zu erkennen. Lies die Zuordnung der Farben anhand der Farbskala ab.

Du solltest beispielsweise wieder diese Werte finden:

- **Zimmer ↔ Fläche:** etwa **+0,55**
- **Zimmer ↔ Preis/m²:** etwa **−0,49**
- **Bevölkerungsdichte ↔ Preis/m²:** etwa **+0,58**

Die Diagonale enthält überall **1**, weil jedes Merkmal mit sich selbst perfekt korreliert.

**Führe die Zelle aus.** Bei der späteren Bereinigung führen wir sie erneut aus und können prüfen, wie sich die Korrelationen ohne die ausgewählten Ausreisser verändern. Als letzte Grafik folgt danach der Bubble-Plot.

> weizer

Jetzt folgt die letzte Grafik: **„Bubble plot (seaborn)“**.

Zuerst wählt der Code Wohnungen mit **2,5 bis 4,5 Zimmern** aus:

```python
df_sub = df.loc[
    (df['rooms'] >= 2.5) & (df['rooms'] <= 4.5)
]
```

Danach wird gezeichnet:

```python
ax = sns.scatterplot(
    x="area",
    y="price",
    size="rooms",
    hue="pop_dens",
    palette="Set2",
    data=df_sub
)
```

Ein Bubble-Plot ist ein Streudiagramm, das zusätzliche Merkmale über **Punktgrösse und Farbe** darstellt:

| Darstellung | Merkmal |
|---|---|
| Horizontale Position | Wohnfläche |
| Vertikale Position | Mietpreis |
| Punktgrösse | Zimmerzahl |
| Punktfarbe | Bevölkerungsdichte der Gemeinde |

Ein grösserer Punkt bedeutet hier also **mehr Zimmer**, nicht automatisch mehr Fläche.

Diese Zeile am Ende blendet die Legende aus:

```python
ax.legend([], [], frameon=False)
```

Ohne Legende können wir die Farben und Grössen nicht genau zuordnen. Für Aufgabe 2a genügt zunächst, den vorgegebenen Code auszuführen und seine Bedeutung zu verstehen.

**Führe die Bubble-Plot-Zelle und danach die Footer-Zelle aus.** Damit haben wir das Notebook für **Aufgabe 2a** durchgearbeitet und für **2b** auffällige Inserate identifiziert.

Jetzt setzen wir **Aufgabe 2c** um: eine Teilmenge ohne die ausgewählten Ausreisser bilden und die Auswertung wiederholen.

Ersetze im Abschnitt **„Filter apartments“** die bisherige Filterzeile durch:

```python
df = df_orig.loc[
    (df_orig['pop_dens'] <= 5000)
    & (df_orig['area'] <= 500)
    & (df_orig['price_per_m2'] > 10)
].copy()
```

Damit behalten wir:

- den bisherigen Bevölkerungsdichtefilter,
- Wohnflächen bis **500 m²**,
- Quadratmeterpreise über **10 CHF/m²**.

**Die Grenzen sind unsere begründete Entscheidung für diese Übung, keine allgemeingültige Ausreisserdefinition.** Sie entfernen die sechs zuvor untersuchten auffälligen Inserate. Die hohen Quadratmeterpreise behalten wir, weil wir dort keinen eindeutigen Datenfehler festgestellt haben.

Führe die Filterzelle und anschliessend die Zelle mit `print(df.shape)` aus. Erwartet sind **780 Zeilen und 16 Spalten**. Danach führen wir alle nachfolgenden Auswertungen erneut aus und vergleichen die Ergebnisse.

> weiter

Für **Aufgabe 2c** führen wir jetzt die Auswertung mit den gefilterten Daten erneut aus.

**Führe alle Zellen ab „Shape“ bis zur Footer-Zelle der Reihe nach aus.** Die Importzelle und die Filterzelle musst du dafür nicht erneut ändern.

Achte beim Vergleich auf diese Stellen:

| Auswertung | Vor der Bereinigung | Was prüfen wir jetzt? |
|---|---|---|
| Anzahl Inserate | 786 | Erwartet: **780** |
| Durchschnittliche Fläche | 92,43 m² | Wie stark sinkt sie? |
| Maximale Fläche | 1’633 m² | Welcher grösste Wert bleibt übrig? |
| Schiefe der Fläche | 12,53 | Wird sie deutlich kleiner? |
| Kurtosis der Fläche | 232,61 | Wie stark nimmt sie ab? |
| Boxplot und Streudiagramm | Durch grosse Flächen zusammengedrückt | Ist die übrige Verteilung besser sichtbar? |
| Regressionsgerade | Steigung **5,84 CHF/m²** | Wie verändert sich die Steigung? |

Die Bereinigung verändert nicht nur die Grafiken: Die entfernten Inserate gehen auch nicht mehr in Mittelwerte, Korrelationen und die Regressionsrechnung ein.

**Schicke mir danach die neuen Ausgaben von `df.describe()`, Schiefe und Kurtosis.** Daraus formulieren wir den konkreten Vorher-nachher-Vergleich für Aufgabe 2c, bevor wir mit Aufgabe 3 weitermachen.

> gemacht

<details><summary>2 previous messages</summary>

> Ich prüfe die gespeicherten Notebook-Ausgaben, damit wir den Vergleich direkt abschliessen können.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/exploratory_data_analysis_apartment_data.ipynb'))
> for c in n['cells']:
>  s=''.join(c['source'])
>  if any(t in s for t in ['df = df_orig.loc','df.describe()',"].skew()",'].kurtosis()', 'print(df.shape)']):
>   print('CODE',s)
>   for o in c.get('outputs',[]):
>    print(''.join(o.get('text',[])))
>    print(''.join(o.get('data',{}).get('text/plain',[])))
> PY`
>
> </details>
</details>

Die gespeicherten Ausgaben bestätigen: **Der Filter hat sechs Inserate entfernt. Es bleiben 780.**

Besonders die Flächenverteilung verändert sich deutlich:

| Kennzahl der Fläche | Vorher | Nachher |
|---|---:|---:|
| Mittelwert | 92,43 m² | **88,39 m²** |
| Median | 86 m² | **86 m²** |
| Maximum | 1’633 m² | **282 m²** |
| Standardabweichung | 75,79 m² | **39,78 m²** |
| Schiefe | 12,53 | **0,86** |
| Exzess-Kurtosis | 232,61 | **1,90** |

**Die extremen Flächen haben Mittelwert und Streuung stark beeinflusst.** Der Median bleibt hingegen unverändert – er reagiert weniger empfindlich auf einzelne Extremwerte.

Beim Mietpreis steigt die Schiefe leicht von **2,09 auf 2,17**. Eine Bereinigung muss also nicht jede Verteilung symmetrischer machen.

Ausserdem bleibt eine **Mindestmiete von 86 CHF** übrig. Unser Filter entfernt die ausgewählten Auffälligkeiten, garantiert aber keine vollständig fehlerfreien Daten.

Füge für **Aufgabe 2c** eine Markdown-Zelle unter der Filterzelle ein:

```markdown
Mit den Bedingungen area <= 500 und price_per_m2 > 10 wurden
sechs auffällige Inserate ausgeschlossen. Es bleiben 780 Inserate.

Die durchschnittliche Wohnfläche sinkt von 92,43 auf 88,39 m²,
während der Median bei 86 m² bleibt. Die Standardabweichung sinkt
von 75,79 auf 39,78 m². Auch Schiefe und Exzess-Kurtosis der Fläche
nehmen stark ab. Die entfernten Extremwerte haben die ursprüngliche
Flächenverteilung somit deutlich beeinflusst.

Die gewählten Grenzen sind eine begründete Entscheidung für diese
Analyse. Sie garantieren keine vollständige Datenbereinigung:
Beispielsweise bleibt ein Mietpreis von 86 CHF prüfbedürftig.
```

Speichere das Notebook. Dann beginnen wir **Aufgabe 3: ländliche und dicht besiedelte Gebiete vergleichen**.

Erstelle im VS-Code-Dateibaum **zwei Kopien** des gerade bearbeiteten Notebooks und benenne sie:

- `rural_apartments.ipynb`
- `city_apartments.ipynb`

Im nächsten Schritt passen wir jeweils den Bevölkerungsdichtefilter an.

> weiter

Jetzt bearbeiten wir **Aufgabe 3b: Wohnungen in ländlicheren Gemeinden**.

Öffne **`rural_apartments.ipynb`**. Das 10%-Quantil der Bevölkerungsdichte aus Aufgabe 3a beträgt gerundet **525,66 Einwohner/km²**.

Ersetze die Codezelle unter **„Filter apartments“** durch:

```python
# 10%-Quantil anhand der ursprünglichen Daten bestimmen
rural_limit = df_orig['pop_dens'].quantile(0.10)

# Ländlichere Gemeinden auswählen und Ausreisserfilter beibehalten
df = df_orig.loc[
    (df_orig['pop_dens'] <= rural_limit)
    & (df_orig['area'] <= 500)
    & (df_orig['price_per_m2'] > 10)
].copy()

print("Grenzwert:", rural_limit)
print("Zeilen und Spalten:", df.shape)
```

**Was passiert hier?**

- **`.quantile(0.10)`** berechnet die genaue Grenze. So vermeiden wir Rundungsfehler durch die manuell eingetragenen `525.66`.
- **`pop_dens <= rural_limit`** wählt Inserate in Gemeinden mit höchstens dieser Bevölkerungsdichte aus.
- Die beiden Ausreisserbedingungen bleiben für den späteren fairen Vergleich in beiden Notebooks gleich.

„Ländlich“ ist hier also **über die Bevölkerungsdichte definiert**, nicht über eine offizielle Gemeindeklassifikation.

**Führe anschliessend das gesamte Notebook von oben nach unten aus** – in VS Code mit **„Run All / Alle ausführen“**. Damit werden alle Tabellen und Grafiken für diese Teilmenge neu berechnet.

Speichere das Notebook mit **Cmd + S**. Danach exportierst du es über das Notebook-Menü **`…` → Export → HTML** als:

```text
rural_apartments.html
```

Falls der Export einen Fehler meldet, kümmern wir uns darum. Als Nächstes setzen wir den entsprechenden Filter für die dichter besiedelten Gemeinden.

> ich sehe rural nicht

<details><summary>2 previous messages</summary>

> Ich prüfe die Dateien in Week_04 und lege die beiden benötigten Kopien an, falls sie fehlen.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> from pathlib import Path
> import shutil
> folder=Path('Week_04')
> source=folder/'exploratory_data_analysis_apartment_data.ipynb'
> for name in ['rural_apartments.ipynb','city_apartments.ipynb']:
>  target=folder/name
>  if target.exists():
>   print('Bereits vorhanden:',target)
>  else:
>   shutil.copy2(source,target)
>   print('Kopie erstellt:',target)
> PY`
>
> </details>
</details>

Die Kopien fehlten noch. Ich habe beide jetzt erstellt:

- [rural_apartments.ipynb](./Week_04/rural_apartments.ipynb)
- [city_apartments.ipynb](./Week_04/city_apartments.ipynb)

Öffne **rural_apartments.ipynb** über den Link. Falls die Dateien im VS-Code-Dateibaum noch fehlen, aktualisiere dort die Ansicht.

Es sind zunächst Kopien des bisherigen Notebooks; die Filter müssen wir jetzt anpassen.

> ok weiter

Öffne **`rural_apartments.ipynb`** und ersetze die Codezelle unter **„Filter apartments“** durch:

```python
# Grenze für ländlichere Gemeinden
rural_limit = df_orig['pop_dens'].quantile(0.10)

df = df_orig.loc[
    (df_orig['pop_dens'] <= rural_limit)
    & (df_orig['area'] <= 500)
    & (df_orig['price_per_m2'] > 10)
].copy()

print("Grenzwert:", rural_limit)
print("Zeilen und Spalten:", df.shape)
```

**Die erste Zeile berechnet das 10%-Quantil der ursprünglichen Bevölkerungsdichten.** Der Filter behält Inserate aus Gemeinden, deren Dichte höchstens diesem Grenzwert entspricht. Unsere Ausreisserfilter bleiben erhalten.

Klicke danach oben auf **„Run All / Alle ausführen“**. So werden sämtliche Tabellen und Grafiken für die ländlichere Gruppe neu berechnet. Speichere mit **Cmd + S**.

**Gib mir danach kurz Bescheid. Ich lese die Ergebnisse direkt aus der gespeicherten Datei.**

> ausgeführt

<details><summary>2 previous messages</summary>

> Ich lese die gespeicherten Ergebnisse der ländlicheren Gruppe und bereite den nächsten Schritt vor.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> n=json.load(open('Week_04/rural_apartments.ipynb'))
> for c in n['cells']:
>  s=''.join(c['source'])
>  if any(t in s for t in ['rural_limit','print(df.shape)',"# Price",'df.describe()']):
>   print('CODE',s[:400])
>   for o in c.get('outputs',[]):
>    if o.get('output_type')=='error': print('ERROR',o.get('ename'),o.get('evalue'))
>    else: print(''.join(o.get('text',[])) or ''.join(o.get('data',{}).get('text/plain',[])))
> PY`
>
> </details>
</details>

Die gespeicherten Ergebnisse passen: **81 Inserate** liegen in Gemeinden mit höchstens **525,66 Einwohnern/km²** und erfüllen unsere Ausreisserfilter.

| Kennzahl | Ländlichere Gruppe |
|---|---:|
| Durchschnittliche Fläche | **116,77 m²** |
| Durchschnittliche Miete | **2’498,60 CHF** |
| Durchschnittlicher Quadratmeterpreis | **22,49 CHF/m²** |

Jetzt folgt **Aufgabe 3c: dichter besiedelte Gemeinden**.

Öffne [city_apartments.ipynb](./Week_04/city_apartments.ipynb) und ersetze die Zelle unter **„Filter apartments“** durch:

```python
# Grenze für dichter besiedelte Gemeinden
city_limit = df_orig['pop_dens'].quantile(0.90)

df = df_orig.loc[
    (df_orig['pop_dens'] >= city_limit)
    & (df_orig['area'] <= 500)
    & (df_orig['price_per_m2'] > 10)
].copy()

print("Grenzwert:", city_limit)
print("Zeilen und Spalten:", df.shape)
```

Wir verwenden jetzt das **90%-Quantil** und **`>=`**: Es bleiben Inserate aus Gemeinden mit mindestens dieser Bevölkerungsdichte. Die Ausreisserbedingungen sind in beiden Gruppen identisch.

Klicke auf **„Alle ausführen“** und speichere mit **Cmd + S**. Danach lese ich die Ergebnisse direkt aus und wir beantworten **3d: Unterschiede zwischen den Gruppen**.

Die geforderten **HTML-Exporte beider Notebooks** stehen anschliessend noch aus.

> ausgefüjrt

<details><summary>2 previous messages</summary>

> Ich lese die Ergebnisse der dichter besiedelten Gruppe und prüfe, wie wir beide Notebooks als HTML exportieren können.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `python3 - <<'PY'
> import json,importlib.util
> for name in ['city_apartments','rural_apartments']:
>  n=json.load(open('Week_04/'+name+'.ipynb'))
>  print(name)
>  for c in n['cells']:
>   s=''.join(c['source'])
>   if 'city_limit' in s or '# Price' in s or 'df.describe()' in s:
>    for o in c.get('outputs',[]):
>     print(''.join(o.get('text',[])) or ''.join(o.get('data',{}).get('text/plain',[])))
>  print('Errors:',[(o.get('ename'),o.get('evalue')) for c in n['cells'] for o in c.get('outputs',[]) if o.get('output_type')=='error'])
> print('nbconvert',bool(importlib.util.find_spec('nbconvert')))
> PY`
> - Ran `command -v jupyter; ls /opt/homebrew/bin/jupyter* /Users/leyla.erikci/Library/Python/3.*/bin/jupyter* 2>/dev/null`
> - Ran `/opt/anaconda3/bin/jupyter nbconvert --to html Week_04/rural_apartments.ipynb Week_04/city_apartments.ipynb`
>
> </details>
</details>

Beide Notebooks wurden ohne gespeicherte Fehlermeldungen ausgeführt. Ich habe auch die geforderten HTML-Dateien exportiert:

- [rural_apartments.html](./Week_04/rural_apartments.html)
- [city_apartments.html](./Week_04/city_apartments.html)

Jetzt **Aufgabe 3d: Ergebnisse vergleichen**:

| Kennzahl | Ländlichere Gruppe | Dichtere Gruppe |
|---|---:|---:|
| Inserate | 81 | 261 |
| Durchschnittliche Fläche | 116,77 m² | 75,96 m² |
| Durchschnittliche Zimmerzahl | 4,27 | 2,93 |
| Durchschnittliche Miete | 2’498,60 CHF | 3’236,16 CHF |
| Durchschnittlicher Preis/m² | 22,49 CHF | 47,85 CHF |
| Median der Miete | 2’420 CHF | 2’900 CHF |

**In der dichter besiedelten Gruppe sind die Wohnungen durchschnittlich kleiner, aber teurer.** Der durchschnittliche Quadratmeterpreis ist mehr als doppelt so hoch.

Eine Besonderheit: **Die dichtere Gruppe enthält hier ausschliesslich Inserate aus der Stadt Zürich.** Wegen der vielen gleichen Dichtewerte an der Quantilgrenze umfasst sie deutlich mehr als 10 % der Inserate.

Füge diese Erklärung als Markdown-Zelle vor der Footer-Zelle beider Notebooks ein:

```markdown
## Vergleich zwischen ländlicheren und dichter besiedelten Gebieten

Die ländlichere Gruppe umfasst 81 Inserate, die dichter besiedelte
Gruppe 261 Inserate. Letztere enthält ausschliesslich die Stadt Zürich.

In der ländlicheren Gruppe sind die Wohnungen durchschnittlich
116,77 m² gross und kosten 2’498,60 CHF. In der dichter besiedelten
Gruppe sind sie mit 75,96 m² kleiner, kosten aber durchschnittlich
3’236,16 CHF.

Der durchschnittliche Quadratmeterpreis beträgt 22,49 CHF in der
ländlicheren und 47,85 CHF in der dichter besiedelten Gruppe.
Die Stadtzürcher Angebote sind somit im Mittel kleiner und teurer.

Der Vergleich beschreibt die Inserate dieses Datensatzes und beweist
keinen ursächlichen Einfluss der Bevölkerungsdichte. Unterschiede
etwa bei Lage, Ausstattung und Wohnungsgrösse können mitwirken.
```

Speichere danach beide Notebooks. Die HTML-Dateien aktualisieren wir anschliessend mit dieser Erklärung. Dann folgt **Aufgabe 4: EDA der Supermarktdaten**.

> weiter mit task 4

<details><summary>2 previous messages</summary>

> Ich schaue mir die Supermarktdaten an und erstelle das Notebook für Task 4. Wir beginnen mit dem Einlesen und der Anzahl der Supermärkte je Marke.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `python3 - <<'PY'
> import csv
> from pathlib import Path
> p=Path('Week_04/supermarkets_data_enriched.csv')
> with p.open() as f:
>  r=csv.DictReader(f)
>  print('Spalten:',r.fieldnames)
>  rows=list(r)
>  print('Zeilen:',len(rows))
>  print('Erste Zeile:',rows[0])
>  from collections import Counter
>  print('Marken:',Counter(row.get('brand') for row in rows))
> print('Notebook vorhanden:',Path('Week_04/exploratory_data_analysis_supermarket_data.ipynb').exists())
> PY`
> - Ran `python3 - <<'PY'
> import nbformat as nbf
> from pathlib import Path
> p=Path('Week_04/exploratory_data_analysis_supermarket_data.ipynb')
> PY`
> - Ran ``python3 - <<'PY'
> import json
> from pathlib import Path
> cells=[]
> def add(kind,source):
>  c={'cell_type':kind,'metadata':{},'source':source.splitlines(True)}
>  if kind=='code': c.update(execution_count=None,outputs=[])
>  cells.append(c)
> add('markdown','# Task 4: Exploratory data analysis of supermarket data\n\nDie Zellen werden der Reihe nach ausgeführt. Die Markenbezeichnungen bleiben wie in der Quelldatei erhalten.')
> add('markdown','## Task 4b: Bibliotheken und Daten einlesen')
> add('code',"import pandas as pd\nimport seaborn as sns\nimport matplotlib.pyplot as plt\n\ndf = pd.read_csv('supermarkets_data_enriched.csv', index_col=0)\nprint('Zeilen und Spalten:', df.shape)\ndf.head()")
> add('markdown','## Task 4c: Anzahl je Marke\n\n`value_counts()` zählt vorhandene Markenangaben. Fehlende Marken werden separat ausgewiesen. Schreibvarianten wie ALDI und Aldi bleiben hier getrennt.')
> add('code',"brand_counts = df['brand'].value_counts()\nprint('Ohne Markenangabe:', df['brand'].isna().sum())\nbrand_counts")
> add('markdown','## Balkendiagramm der Marken')
> add('code',"fig, ax = plt.subplots(figsize=(10, 6))\nbrand_counts.plot.bar(ax=ax, color='seagreen')\nax.set_xlabel('Marke')\nax.set_ylabel('Anzahl Supermärkte')\nax.set_title('Supermärkte je Marke – vorhandene Markenangaben')\nplt.xticks(rotation=90)\nplt.tight_layout()\nplt.show()")
> add('markdown','## Streudiagrammmatrix der numerischen Merkmale\n\nAuf der Diagonale stehen Histogramme, ausserhalb Streudiagramme. Gemeindemerkmale wiederholen sich für Standorte derselben Gemeinde.')
> add('code',"numeric_vars = ['lat', 'lon', 'pop', 'pop_dens', 'frg_pct', 'emp']\ng = sns.PairGrid(df[numeric_vars], height=1.5)\ng.map_upper(sns.scatterplot, color='darkgreen', s=8, alpha=0.4)\ng.map_lower(sns.scatterplot, color='darkgreen', s=8, alpha=0.4)\ng.map_diag(plt.hist, color='seagreen')\nplt.show()")
> add('markdown','## Standorte von Denner, Volg und Landi\n\nDie x-Achse zeigt den Längengrad, die y-Achse den Breitengrad. Jeder Punkt ist ein Eintrag aus dem Datensatz; die Farbe bezeichnet die Marke. Dies ist eine Koordinatendarstellung ohne Kartenhintergrund.')
> add('code',"brands = ['Denner', 'Volg', 'Landi']\ndf_locations = df.loc[df['brand'].isin(brands)]\n\nfig, ax = plt.subplots(figsize=(9, 7))\nsns.scatterplot(data=df_locations, x='lon', y='lat', hue='brand',\n                hue_order=brands, palette={'Denner': 'red', 'Volg': 'blue', 'Landi': 'green'},\n                s=15, alpha=0.7, ax=ax)\nax.set_xlabel('Längengrad (°)')\nax.set_ylabel('Breitengrad (°)')\nax.set_title('Standorte von Denner, Volg und Landi')\nax.legend(title='Marke')\nplt.tight_layout()\nplt.show()")
> add('markdown','## Footer information')
> add('code',"import os\nimport platform\nfrom datetime import datetime\n\nprint('-----------------------------------')\nprint(os.name.upper())\nprint(platform.system(), '|', platform.release())\nprint('Datetime:', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))\nprint('Python Version:', platform.python_version())\nprint('-----------------------------------')")
> n={'cells':cells,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python'}},'nbformat':4,'nbformat_minor':4}
> p=Path('Week_04/exploratory_data_analysis_supermarket_data.ipynb')
> p.write_text(json.dumps(n,ensure_ascii=False,indent=1)+'\n')
> print('Erstellt:',p)
> PY``
>
> </details>
</details>

Für **Task 4a** habe ich das Notebook erstellt:

[exploratory_data_analysis_supermarket_data.ipynb](./Week_04/exploratory_data_analysis_supermarket_data.ipynb)

Es enthält die geforderten Schritte. Wir führen sie gemeinsam aus.

**Task 4b: Daten einlesen**

Öffne das Notebook und führe die erste Codezelle aus:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('supermarkets_data_enriched.csv', index_col=0)

print('Zeilen und Spalten:', df.shape)
df.head()
```

- **`pd.read_csv(...)`** liest die Supermarktdaten.
- **`index_col=0`** verwendet die erste CSV-Spalte als Zeilenindex. Dort stehen bereits gespeicherte Zeilennummern.
- **`df.shape`** zeigt die Tabellengrösse.
- **`df.head()`** zeigt die ersten fünf Einträge.

Erwartet wird **`(3242, 17)`**.

**Danach Task 4c: Anzahl je Marke**

```python
brand_counts = df['brand'].value_counts()

print('Ohne Markenangabe:', df['brand'].isna().sum())
brand_counts
```

**`value_counts()` zählt die Einträge je Marke.** Fehlende Markenangaben werden dabei standardmässig ausgelassen; deshalb zählen wir sie separat.

In den Quelldaten fehlen bei **1’233 Einträgen** die Markenangaben. Ausserdem kommen Schreibvarianten wie **`ALDI` und `Aldi`** vor. Diese werden zunächst als unterschiedliche Kategorien gezählt – wichtig für die spätere Interpretation.

**Führe diese beiden Zellen aus und speichere das Notebook.** Danach lesen wir die Ergebnisse direkt aus und besprechen das Balkendiagramm.

> weiter

Weiter mit dem **Balkendiagramm: Anzahl Supermärkte je Marke**.

Führe die nächste Zelle aus:

```python
fig, ax = plt.subplots(figsize=(10, 6))

brand_counts.plot.bar(ax=ax, color='seagreen')

ax.set_xlabel('Marke')
ax.set_ylabel('Anzahl Supermärkte')
ax.set_title('Supermärkte je Marke – vorhandene Markenangaben')

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
```

Die entscheidende Zeile ist:

```python
brand_counts.plot.bar(ax=ax, color='seagreen')
```

Sie zeichnet die zuvor berechneten Häufigkeiten als **senkrechte Balken**:

- **x-Achse:** Marken
- **y-Achse:** Anzahl der Einträge je Marke
- **Balkenhöhe:** Häufigkeit der jeweiligen Marke

Da `value_counts()` standardmässig absteigend sortiert, erscheinen die häufigsten Marken links.

Die letzten Formatierungen helfen bei der Lesbarkeit:

| Code | Wirkung |
|---|---|
| `rotation=90` | Dreht die Markennamen senkrecht. |
| `plt.tight_layout()` | Passt die Abstände an, damit Beschriftungen möglichst vollständig sichtbar bleiben. |

**Bei der Interpretation beachten:** Die 1’233 Einträge ohne Markenangabe fehlen in diesem Diagramm. Auch werden beispielsweise `ALDI` und `Aldi` getrennt dargestellt. Die Balken zeigen daher die **Häufigkeiten der gespeicherten Markenbezeichnungen**, keine vollständigen Marktanteile.

Danach folgt die geforderte **Streudiagrammmatrix mit `sns.PairGrid()`**.

> alles ausgeführt

<details><summary>2 previous messages</summary>

> Ich prüfe die gespeicherten Ausgaben auf Fehler und ob alle geforderten Grafiken vorhanden sind.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python3 - <<'PY'
> import json
> p='Week_04/exploratory_data_analysis_supermarket_data.ipynb'
> n=json.load(open(p))
> for i,c in enumerate(n['cells']):
>  if c['cell_type']!='code': continue
>  print('Zelle',i,'Ausgeführt:',c.get('execution_count'),'Grafiken:',sum('image/png' in o.get('data',{}) for o in c.get('outputs',[])))
>  for o in c.get('outputs',[]):
>   if o.get('output_type')=='error':print('FEHLER',o.get('ename'),o.get('evalue'))
>   elif 'text' in o:print(''.join(o['text'])[:600])
>   elif 'text/plain' in o.get('data',{}) and 'brand_counts' in ''.join(c['source']):print(''.join(o['data']['text/plain'])[:1500])
> PY`
>
> </details>
</details>

**Task 4 ist erledigt.** Ich habe die gespeicherten Ausgaben geprüft: Alle Zellen wurden ausgeführt, keine Fehlermeldungen gespeichert und alle drei geforderten Grafiken sind vorhanden.

- **Daten eingelesen:** 3’242 Einträge, 17 Spalten.
- **Marken gezählt und als Balkendiagramm dargestellt:** Coop 497, Migros 495, Denner 423, Volg 210 und Landi 39.
- **Streudiagrammmatrix erstellt:** für `lat`, `lon`, `pop`, `pop_dens`, `frg_pct` und `emp`.
- **Standortdiagramm erstellt:** Denner, Volg und Landi in unterschiedlichen Farben.

Beim Interpretieren bleibt wichtig: **1’233 Einträge haben keine Markenangabe**, und Schreibvarianten wie `ALDI` und `Aldi` werden getrennt gezählt.

Deine Lösung ist in [exploratory_data_analysis_supermarket_data.ipynb](./Week_04/exploratory_data_analysis_supermarket_data.ipynb) gespeichert.

> fertig?

**Ja, die Aufgaben 1–4 von Week_04 sind bearbeitet.**

Nur der letzte Abgabeschritt bleibt: Falls du den Vergleichstext zu Aufgabe 3 nachträglich eingefügt hast, müssen die beiden HTML-Dateien nochmals exportiert werden, damit sie ebenfalls diesen Text enthalten.

> ok

<details><summary>2 previous messages</summary>

> Ich aktualisiere die beiden HTML-Exporte aus den gespeicherten Notebooks.
>
> <details><summary>Ran a command</summary>
>
> - Ran `/opt/anaconda3/bin/jupyter nbconvert --to html Week_04/rural_apartments.ipynb Week_04/city_apartments.ipynb`
>
> </details>
</details>

Die HTML-Dateien sind jetzt auf dem Stand der gespeicherten Notebooks:

- [rural_apartments.html](./Week_04/rural_apartments.html)
- [city_apartments.html](./Week_04/city_apartments.html)
