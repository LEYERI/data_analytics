# Week_02-Aufgaben lösen

> Ich muss die Aufgaben in "Week_01" lösen. Ich verstehe aber nichts, hilf mir!

<details><summary>1 previous message</summary>

> Ich schaue mir die Aufgaben in „Week_01“ an. Dann gehen wir sie Schritt für Schritt durch und klären die Grundlagen direkt an den Beispielen.
</details>

Wir gehen das gemeinsam Schritt für Schritt durch. Ich habe [die Aufgabenstellung in Week_01](./Week_01/Excercises_Week_01.pdf) gelesen. **Du musst hier noch kein Vorhersagemodell bauen.** Zuerst geht es darum, eine Untersuchung zu planen und Daten zu beschaffen.

Die Woche besteht aus drei Aufgaben:

| Aufgabe | Was du machen sollst |
|---|---|
| 1 | Für zwei Beispiele festlegen: Welches Problem wollen wir untersuchen? |
| 2 | Überlegen: Welche Daten brauchen wir dafür? |
| 3 | Daten abrufen: Supermärkte mit Python, Wohnungen mit einer Browser-Erweiterung. |

**Beginnen wir mit Aufgabe 1.** Du brauchst für jedes Beispiel fünf kurze Punkte. Hier ist ein Lösungsvorschlag mit Erklärung.

**Beispiel 1: Wohnungsmieten im Kanton Zürich vorhersagen**

1. **Problem:** Für Wohnungssuchende ist schwer einzuschätzen, ob die verlangte Miete im Vergleich zu ähnlichen Wohnungen hoch ist.
2. **Ziel:** Die monatliche Angebotsmiete anhand von Wohnungsmerkmalen und Lage schätzen.
3. **Forschungsfrage:** Wie hängen Wohnfläche, Zimmerzahl und Lage mit der monatlichen Angebotsmiete zusammen?
4. **Hypothese:** Wohnungen mit grösserer Wohnfläche haben im Durchschnitt eine höhere monatliche Angebotsmiete.
5. **Mehrwert:** Wohnungssuchende können Angebote besser vergleichen; Vermieter erhalten eine Orientierung für die Preisfestlegung.

Der Unterschied ist: Die **Forschungsfrage** fragt nach einem Zusammenhang. Die **Hypothese** ist eine konkrete Vermutung, die wir später mit Daten überprüfen. Sie ist noch kein bewiesenes Ergebnis.

**Beispiel 2: Supermärkte in Schweizer Gemeinden**

1. **Problem:** Es ist unklar, welche Gemeinden im Verhältnis zu ihrer Bevölkerung wenige Supermärkte haben.
2. **Ziel:** Das Supermarktangebot zwischen Gemeinden vergleichen und mögliche Versorgungslücken erkennen.
3. **Forschungsfrage:** Wie hängt die Einwohnerzahl einer Gemeinde mit der Anzahl ihrer Supermärkte zusammen?
4. **Hypothese:** Gemeinden mit mehr Einwohnern haben im Durchschnitt mehr Supermärkte.
5. **Mehrwert:** Die Analyse liefert Hinweise für die Standortplanung von Supermarktketten und die Versorgungsplanung von Gemeinden.

Dabei ist die Einwohnerzahl ein **grober Hinweis auf Nachfrage**. Wie viel Menschen tatsächlich einkaufen, wissen wir dadurch noch nicht.

Damit hast du bereits einen brauchbaren Entwurf für Aufgabe 1. Für Aufgabe 2 folgt daraus fast automatisch: Wenn wir untersuchen wollen, ob grössere Wohnungen mehr kosten, brauchen wir mindestens **Wohnfläche und Mietpreis pro Wohnung**.

Ist dir der Unterschied zwischen **Ziel, Forschungsfrage und Hypothese** schon klar, oder sollen wir diese drei Begriffe zuerst an einem einfacheren Alltagsbeispiel üben?

> wir müssen jetzt die aufgaben in "Week_02" lösen, bitte gemeinsam lösen, sag mir was ich machen muss und erkläre es kurz aber veständlich, damit ich ready für die prüfung bin

<details><summary>1 previous message</summary>

> Ich lese die Aufgaben in „Week_02“. Danach lösen wir sie gemeinsam in kleinen Schritten – jeweils mit einer kurzen Erklärung für die Prüfung.
</details>

Wir lösen **Week_02 gemeinsam, eine Aufgabe nach der anderen**. Du führst die Schritte aus, und ich erkläre kurz, was dahintersteckt.

Es gibt vier Themen: **Regex → Daten bereinigen → Daten filtern → SQL**. Die benötigten Dateien sind vorhanden.

**Wir starten mit Aufgabe 1: Zahlen aus Text herauslesen.**

Aus diesem Text sollst du den Mietpreis `3160` herausholen:

```text
4,5 Zimmer, 108 m², CHF 3160.—
```

Ein **regulärer Ausdruck (Regex)** ist ein Suchmuster. Damit findet Python zum Beispiel Zahlen innerhalb eines Textes.

**Was du jetzt machen musst:**

1. Öffne **regex101.com**.
2. Kopiere den obigen Text in **TEST STRING**.
3. Trage bei **REGULAR EXPRESSION** nacheinander diese Muster ein:

| Muster | Bedeutung | Treffer im Beispiel |
|---|---|---|
| `[0-9]` | Eine einzelne Ziffer | z. B. `4` |
| `[0-9]+` | Eine oder mehrere Ziffern hintereinander | `4`, `5`, `108`, `3160` |
| `\d+` | Hier dasselbe wie `[0-9]+` | `4`, `5`, `108`, `3160` |
| `[0-9]{4}` | Genau vier aufeinanderfolgende Ziffern | **`3160`** |

Aktiviere die Option **`g` (global)**, damit du alle Treffer siehst.

**Prüfungswissen:** `+` bedeutet „mindestens einmal“, `{4}` bedeutet „genau viermal“. `[0-9]{4}` findet hier den Preis, weil nur der Preis vier Ziffern hat. Bei einem dreistelligen Mietpreis würde dieses Muster nicht passen.

Teste danach das Muster aus der Aufgabe:

```regex
CHF (.*).{2}$
```

Hier bedeutet:

- `CHF `: Suche diese Zeichen inklusive Leerzeichen.
- `(.*)`: Speichere den folgenden Text in **Gruppe 1**.
- `.{2}$`: Die letzten zwei Zeichen gehören zum Ende des Textes.

Der **gesamte Treffer** ist `CHF 3160.—`, aber **Gruppe 1 enthält nur `3160`**. So erhältst du den Preis mit einer Gruppe.

**Dein nächster Schritt:** Teste `[0-9]+` und `[0-9]{4}`. Siehst du beim ersten Muster die vier Treffer `4`, `5`, `108`, `3160` und beim zweiten nur `3160`?


Ja, das funktioniert! Auf deinem Screenshot siehst du:

- **Match 1 (blau):** den gesamten Treffer `CHF 3160.—`
- **Group 1 (grün):** nur den gewünschten Preis `3160`

**Für die Prüfung:** Runde Klammern `(...)` bilden eine Gruppe. Damit kannst du einen Teil des gesamten Treffers separat herauslesen.

Zum Abschluss von Aufgabe 1 teste noch diese beiden Muster:

```regex
(.*) Zimmer
```

Gruppe 1 liefert **`4,5`**, also die Zimmerzahl.

```regex
Zimmer, (.*) m²
```

Gruppe 1 liefert **`108`**, also die Wohnfläche.

Damit kannst du die drei wichtigen Angaben aus dem Text extrahieren: **Zimmerzahl, Fläche und Preis**.

**Danach starten wir Aufgabe 2:** Öffne in VS Code die Datei [apartments_data_winterthur.csv](./Week_02/apartments_data_winterthur.csv). Öffne sie als Text, damit du die Trennzeichen siehst.

Schau unten rechts in VS Code nach der **Zeichenkodierung** und in der Datei nach dem **Trennzeichen zwischen den Spalten**. Was siehst du dort?

> dass es mit kommas und utf 8 codiert wurde?

Genau: **Das Trennzeichen ist ein Komma `,`, die Zeichenkodierung ist UTF-8.**

- **Trennzeichen:** trennt die Spalten voneinander.
- **UTF-8:** legt fest, wie Zeichen wie `ü` und `²` gespeichert werden.

Öffne jetzt [apartments_data_preparation_winterthur.ipynb](./Week_02/apartments_data_preparation_winterthur.ipynb) und führe die Zellen bis einschliesslich `df.head()` mit **Shift + Enter** aus.

Die entscheidende Zeile ist:

```python
df = pd.read_csv(
    'apartments_data_winterthur.csv',
    sep=',',
    encoding='utf-8'
)
```

**Kurz erklärt:** `pd.read_csv()` liest die CSV-Datei als Tabelle ein. Diese Tabelle heisst in pandas **DataFrame** und wird hier in `df` gespeichert. `df.head()` zeigt die ersten fünf Zeilen.

Werden dir die fünf Zeilen angezeigt, oder erscheint eine Fehlermeldung?

> kurze frage: was ist denn das python notebook überhaupt? also was haben wir durchgeführt, damit es mir die 5 zeilen gegeben hat?
>

Ein **Jupyter Notebook** (`.ipynb`) ist ein digitales Arbeitsheft mit **Erklärtext, ausführbarem Python-Code und Ergebnissen**. Der Code ist in einzelne **Zellen** aufgeteilt, die du mit ▶ oder **Shift + Enter** ausführst.

In deiner Zelle haben wir drei Dinge gemacht:

**1. Vorhandene CSV-Dateien aufgelistet**
```python
flist = fnmatch.filter(os.listdir('.'), '*.csv')
for i in flist:
    print(i)
```
Das sucht im aktuellen Ordner nach Dateien mit der Endung `.csv` und zeigt ihre Namen an. Es lädt noch keine Daten.

**2. Die Winterthur-Datei eingelesen**
```python
df = pd.read_csv(
    'apartments_data_winterthur.csv',
    sep=',',
    encoding='utf-8'
)
```
`pd` steht für die zuvor importierte Bibliothek **pandas**, ein Werkzeug zum Arbeiten mit Tabellen.

Die **gesamte CSV-Datei** wird als Tabelle in den Arbeitsspeicher geladen. Diese Tabelle nennt man **DataFrame**. Mit `df =` geben wir ihr den Namen `df`, damit wir später darauf zugreifen können.

**3. Die ersten fünf Zeilen angezeigt**
```python
df.head()
```
`head()` zeigt standardmässig die **ersten fünf Zeilen**. Im Notebook wird das Ergebnis der letzten Zeile automatisch dargestellt.

**Merke für die Prüfung:** `read_csv()` lädt die Daten, `df` hält die Tabelle bereit und `head()` zeigt eine Vorschau. Die restlichen Zeilen sind ebenfalls geladen. Die Nummern **0 bis 4** links sind die Zeilenindizes – Python zählt normalerweise ab 0.

Führe jetzt die nächste Zelle mit `df.shape` aus: Damit erfahren wir, **wie viele Zeilen und Spalten die gesamte Tabelle hat**.

> gemacht

`df.shape` liefert zwei Zahlen: **(Anzahl Zeilen, Anzahl Spalten)**.

```python
df.shape[0]  # Anzahl Zeilen → Wohnungsangebote
df.shape[1]  # Anzahl Spalten → gespeicherte Merkmale
```

**Als Nächstes:** Führe die Zelle mit folgendem Inhalt aus:

```python
df.dtypes
```

Das zeigt den **Datentyp jeder Spalte**. Die Rohdaten werden hier vermutlich als `object` angezeigt – bei diesen Spalten bedeutet das Text.

Warum ist das wichtig? Mit `"CHF 3017.—"` als Text können wir keinen Durchschnitt berechnen. Dafür müssen wir zuerst die Zahl `3017` herauslesen und als Zahl speichern.

Welche Ausgabe bekommst du bei `df.dtypes`?

> web-scraper-order        object
> web-scraper-start-url    object
> rooms_area_price_raw     object
> address_raw              object
> price_raw                object
> description_raw          object
> text_raw                 object
> dtype: object

Genau: Alle sieben Spalten enthalten hier **Text (`object`)**. Auch `price_raw` ist Text, weil dort beispielsweise `"CHF 3017.—"` steht.

**Jetzt machen wir aus dem Rohtext eine numerische Zimmerzahl.** Führe die nächste Zelle aus, die mit diesem Code beginnt:

```python
rooms = []
for i in df['rooms_area_price_raw']:
```

Die Zelle verarbeitet jede Wohnung so:

```text
"6,5 Zimmer, 143 m², CHF 3017.—"
                 ↓ Regex: (.*)Zimmer
"6,5 "
                 ↓ .strip() entfernt Leerzeichen
"6,5"
                 ↓ .replace(',', '.') ersetzt das Dezimalkomma
"6.5"
                 ↓ Umwandlung in float64
6.5
```

Die Ergebnisse werden in einer neuen Spalte gespeichert:

```python
df['rooms'] = pd.Series(rooms, dtype="float64")
```

**Für die Prüfung:** `float64` ist ein Datentyp für Zahlen mit Nachkommastellen. Die brauchen wir für Zimmerzahlen wie `4.5`.

Falls keine Zimmerzahl gefunden wird, speichert der Code einen fehlenden Wert.

Führe die Zelle aus. Werden unten die Zimmerzahlen **6.5, 1.0, 4.5, 3.5, 3.5** angezeigt?

> 0    6,5 Zimmer, 143 m², CHF 3017.—
> 1      1 Zimmer, 132 m², CHF 3260.—
> 2    4,5 Zimmer, 117 m², CHF 3782.—
> 3     3,5 Zimmer, 88 m², CHF 2244.—
> 4     3,5 Zimmer, 80 m², CHF 1980.—
> Name: rooms_area_price_raw, dtype: object
>
> 0    6.5
> 1    1.0
> 2    4.5
> 3    3.5
> 4    3.5
> Name: rooms, dtype: float64

Das hat funktioniert: Oben siehst du den **ursprünglichen Text**, unten die daraus extrahierten **Zimmerzahlen als `float64`**. Die neue Spalte `rooms` ist jetzt für Berechnungen geeignet.

**Als Nächstes: Wohnfläche extrahieren.** Führe die nächste Zelle aus, die mit `area = []` beginnt.

Sie verwendet dieses Suchmuster:

```python
re.findall('Zimmer, (.*)m²', i)
```

Die Klammer erfasst den Text **zwischen `Zimmer, ` und `m²`**:

```text
"6,5 Zimmer, 143 m², CHF 3017.—"
               ↓
             "143 "
               ↓ .strip()
             "143"
               ↓ Umwandlung in Int64
              143
```

**Prüfungswissen:** `Int64` speichert ganze Zahlen und erlaubt in pandas auch fehlende Werte (`<NA>`). Im Notebook wird die Fläche als ganze Zahl gespeichert.

Erwartete erste Werte: **143, 132, 117, 88, 80**. Werden sie dir angezeigt?

> Ja: 0    6,5 Zimmer, 143 m², CHF 3017.—
> 1      1 Zimmer, 132 m², CHF 3260.—
> 2    4,5 Zimmer, 117 m², CHF 3782.—
> 3     3,5 Zimmer, 88 m², CHF 2244.—
> 4     3,5 Zimmer, 80 m², CHF 1980.—
> Name: rooms_area_price_raw, dtype: object
>
> 0    143
> 1    132
> 2    117
> 3     88
> 4     80
> Name: area, dtype: Int64

Die Wohnfläche steht jetzt als **ganze Zahl in `area`**.

**Jetzt folgt der Mietpreis:** Führe die nächste Zelle aus, die mit `price = []` beginnt.

Sie sucht mit:

```python
re.findall('[0-9]+', i)
```

`[0-9]+` findet **eine zusammenhängende Folge von Ziffern**. Für deine Daten passiert also:

```text
"CHF 3017.—" → "3017" → 3017
```

Das Ergebnis wird als Zahl vom Typ `Int64` in der neuen Spalte `price` gespeichert.

**Für die Prüfung:** Das Muster funktioniert hier, weil der Preis ohne Tausendertrennzeichen geschrieben ist. Bei `"CHF 3'017.—"` würde es zwei Treffer finden: `"3"` und `"017"`.

Erwartete erste Preise: **3017, 3260, 3782, 2244, 1980**.

Führe danach auch `df.dtypes` aus. Jetzt sollten die neuen Spalten so aussehen:

```text
rooms    float64
area       Int64
price      Int64
```

Stimmt das bei dir?

> Ja

Damit sind **Zimmerzahl, Fläche und Preis als Zahlen gespeichert**. Jetzt prüfen wir die Datenqualität.

Führe die nächste Zelle aus:

```python
print(pd.isna(df).sum())
df[df.isna().any(axis=1)].head()
```

Das bedeutet:

- `pd.isna(df)` prüft jede Zelle: **Fehlt hier ein Wert?**
- `.sum()` zählt die fehlenden Werte **pro Spalte**.
- Die zweite Zeile zeigt die ersten fünf Datensätze, bei denen **mindestens ein Wert fehlt**.

**Für die Prüfung:** Ein fehlender Wert (`NaN` oder `<NA>`) bedeutet „unbekannt“ und ist keine `0`. Eine unbekannte Miete darf beispielsweise nicht als kostenlose Wohnung in den Durchschnitt eingehen.

Wie viele fehlende Werte zeigt es bei **`rooms`, `area` und `price`** an?


Du siehst die **ersten fünf Datensätze mit mindestens einem fehlenden Wert**. Im Screenshot erkennt man bereits mögliche Gründe:

- **Zeile 6:** „Preis auf Anfrage“ → keine Zahl vorhanden → `price` fehlt.
- **Zeilen 13, 20, 27 und 34:** keine Fläche angegeben → `area` fehlt.

**Wichtig:** `.head()` zeigt höchstens fünf Zeilen. Es können insgesamt mehr Datensätze betroffen sein.

Damit du die Anzahl übersichtlich siehst, führe in einer neuen Codezelle Folgendes aus:

```python
df[['rooms', 'area', 'price']].isna().sum()
```

Das wählt nur die drei Zahlenspalten aus und zählt ihre fehlenden Werte. Welche drei Zahlen erhältst du?

> rooms     1
> area     11
> price     1
> dtype: int64

Das bedeutet:

- **1 Angebot** ohne ausgelesene Zimmerzahl.
- **11 Angebote** ohne ausgelesene Wohnfläche.
- **1 Angebot** ohne ausgelesenen Preis.

Das sind nicht zwingend 13 verschiedene Angebote: Bei einem Angebot können mehrere Angaben fehlen. Wir haben die fehlenden Werte bisher **nur erkannt**, noch nichts gelöscht.

**Jetzt prüfen wir auf doppelte Datensätze.** Führe die nächste Zelle aus:

```python
print(df.duplicated().sum())
```

`duplicated()` markiert Zeilen, die mit einer vorherigen Zeile **in allen Spalten übereinstimmen**. `.sum()` zählt diese Wiederholungen.

**Für die Prüfung:** Fehlende Werte betreffen die **Vollständigkeit**, Duplikate die **Mehrfacherfassung** von Daten.

Welche Zahl bekommst du?

> 0

**0 bedeutet: Es gibt keine vollständig identischen Zeilen.**

Allerdings könnte dieselbe Wohnung mehrfach mit unterschiedlicher Scraper-ID vorkommen. Deshalb ist entscheidend, **welche Spalten man beim Duplikatvergleich berücksichtigt**.

**Speichere jetzt die aufbereiteten Winterthur-Daten**, indem du die nächste Zelle ausführst:

```python
df.to_csv(
    'apartments_data_prepared.csv',
    sep=',',
    encoding='utf-8',
    index=False
)
```

- `to_csv()` schreibt die Tabelle in eine Datei.
- `index=False` verhindert, dass die Zeilennummern als zusätzliche Spalte gespeichert werden.

Danach folgt **Aufgabe 2e: dieselbe Verarbeitung für den Kanton Zürich**:

1. Speichere eine **Kopie des Notebooks** im Ordner `Week_02` als `apartments_data_preparation_zuerich.ipynb`.
2. Ändere darin beim Einlesen den Dateinamen zu:
   ```python
   df = pd.read_csv('apartments_data_zuerich.csv', sep=',', encoding='utf-8')
   ```
3. Führe die Kopie **von oben bis einschliesslich der Prüfung auf Duplikate** aus.

Teile mir dann die Anzahl fehlender Werte bei `rooms`, `area`, `price` sowie die Anzahl der Duplikate mit.

> komme nicht raus, muss ich den namen abändern des jetzigen notebooks?

Du sollst **eine Kopie unter neuem Namen speichern**. Das jetzige Winterthur-Notebook bleibt erhalten.

So geht’s in VS Code:

1. Drücke **Strg + Shift + S** (Mac: **Cmd + Shift + S**) für „Speichern unter“.
2. Speichere im Ordner `Week_02` mit diesem Namen:
   ```text
   apartments_data_preparation_zuerich.ipynb
   ```
3. In der jetzt geöffneten Kopie änderst du **in der Codezeile `pd.read_csv(...)`** den Dateinamen:
   ```python
   df = pd.read_csv('apartments_data_zuerich.csv', sep=',', encoding='utf-8')
   ```

Du hast dann zwei Notebooks: eines für **Winterthur**, eines für **Zürich**. Der neue Notebook-Name allein ändert die eingelesenen Daten noch nicht – dafür ist Schritt 3 nötig.

> gemacht
>

Der Dateiname ist jetzt richtig: **`apartments_data_zuerich.csv`**.

Führe im Zürich-Notebook die Zellen **von oben nach unten** erneut aus – bis einschliesslich der Prüfung auf Duplikate. So werden Zimmerzahl, Fläche und Preis für die **Zürich-Daten** neu berechnet.

**Wichtig für die Prüfung:** Eine Änderung am Code wirkt erst, wenn du die Zelle ausführst. Bereits angezeigte Ergebnisse können noch vom vorherigen Durchlauf stammen.

Führe danach diese Zelle aus:

```python
print(df[['rooms', 'area', 'price']].isna().sum())
print('Duplikate:', df.duplicated().sum())
```

Schick mir die Ausgabe. Danach speichern wir die vorbereiteten Zürich-Daten.

> gemacht

Welche Zahlen wurden angezeigt? Kopiere bitte die Ausgabe hier hinein:

```text
rooms      …
area       …
price      …
Duplikate: …
```

Damit prüfen wir die Zürich-Daten, bevor wir sie speichern.

> rooms     45
> area     135
> price     15
> dtype: int64

Bei den Zürich-Daten fehlen nach dem Extrahieren:

- **45-mal** die Zimmerzahl.
- **135-mal** die Wohnfläche.
- **15-mal** der Preis.

**Für die Prüfung:** Das sind fehlende Angaben pro Spalte, nicht zwingend verschiedene Wohnungen.

Prüfe jetzt noch die Duplikate:

```python
print('Duplikate:', df.duplicated().sum())
```

Danach führe die Speicherzelle aus:

```python
df.to_csv(
    'apartments_data_prepared.csv',
    sep=',',
    encoding='utf-8',
    index=False
)
```

Die Datei enthält dann die **aufbereiteten Zürich-Daten** für Aufgabe 4. Eine vorhandene gleichnamige Datei mit Winterthur-Daten wird dabei ersetzt, wie für die nächsten Aufgaben vorgesehen.

Speichere auch das Notebook mit **Strg + S**. Welche Zahl steht bei `Duplikate`?

> 0

**0: Auch bei Zürich gibt es keine vollständig identischen Zeilen.** Wenn du die CSV-Speicherzelle ausgeführt und das Notebook gespeichert hast, ist Aufgabe 2 abgeschlossen.

**Weiter mit Aufgabe 3: Supermarktdaten im JSON-Format.**

Öffne im Ordner `Week_02` die Datei **`supermarkets.json`**. Du musst dafür nichts hochladen; du kannst sie direkt in VS Code anschauen.

**JSON speichert Daten als Schlüssel-Wert-Paare**, beispielsweise:

```json
{
  "id": 123,
  "lat": 47.37,
  "lon": 8.54,
  "tags": {
    "brand": "Migros",
    "addr:city": "Zürich"
  }
}
```

Das ist ein Beispiel:
- `lat` und `lon` geben den Standort an.
- Unter `tags` stehen weitere Merkmale wie Marke und Ort.
- `tags` enthält selbst wieder Schlüssel-Wert-Paare – die Daten sind also **verschachtelt**.

**Dein nächster Schritt:** Öffne `supermarkets_data_preparation.ipynb` und führe die ersten Zellen bis einschliesslich `df1.head(5)` aus.

Damit wird die JSON-Datei eingelesen und als Tabelle angezeigt. Siehst du dort eine Spalte **`tags`**, deren Einträge geschweifte Klammern `{…}` enthalten?

> nein

Was siehst du stattdessen: **eine Tabelle ohne `tags`**, **eine Fehlermeldung** oder **keine Ausgabe**?

Schick mir einen Screenshot oder kopiere die Fehlermeldung hier hinein. Dann schauen wir gezielt, wo es hakt.

> ja sorry sehe ich

In `tags` stecken also noch mehrere Angaben zusammen, zum Beispiel Marke, Strasse und Ort.

**Führe jetzt die nächsten Zellen bis einschliesslich `df2.head()` aus.** Die entscheidende Zeile ist:

```python
df2 = pd.DataFrame.from_records(df1.tags)
```

Sie macht aus den verschachtelten Angaben **einzelne Tabellenspalten**:

```text
tags: {"brand": "Migros", "addr:city": "Zürich"}
                         ↓
          brand     addr:city
          Migros    Zürich
```

Danach wählt der Code bestimmte Spalten aus und benennt sie um, beispielsweise **`addr:city` → `city`**.

**Für die Prüfung:** Verschachtelte JSON-Daten werden in eine flache Tabelle umgewandelt, damit wir sie leichter filtern und analysieren können.

Siehst du jetzt die Spalten **`brand`, `shop`, `city`, `street`, `housenumber`, `postcode`**?

> js

Als Nächstes verbinden wir die **Standortdaten** mit den **Merkmalen aus `tags`**.

Führe die nächste Zelle bis `df.head(5)` aus:

```python
df = pd.merge(
    df1[['type', 'id', 'lat', 'lon']],
    df2[['brand', 'shop', 'city', 'street', 'housenumber', 'postcode']],
    left_index=True,
    right_index=True
)
df.head(5)
```

`pd.merge()` verbindet zwei Tabellen. Hier werden Zeilen mit **dem gleichen Index** zusammengefügt: Zeile 0 mit Zeile 0, Zeile 1 mit Zeile 1 usw.

Das passt hier, weil `df2` direkt aus `df1` entstanden ist und die Zeilenzuordnung erhalten blieb.

**Ergebnis:** In `df` stehen nun Standort, Marke und Adresse zusammen.

Führe danach die vorhandenen Zellen zur Prüfung auf **fehlende Werte und Duplikate** aus. Gibt es fehlende Werte, und wie viele vollständig doppelte Zeilen werden gezählt?

> 0

Falls die **0 aus `df.duplicated().sum()`** stammt: Es gibt keine vollständig identischen Zeilen.

Jetzt ergänzen wir die geforderten Filter. Füge **vor der CSV-Speicherzelle** eine Markdown-Zelle mit diesem Text ein:

```text
## Additional filters on supermarkets
```

Darunter kommt eine neue **Codezelle** für Aufgabe 3f:

```python
migros_zuerich = df.loc[
    (df['brand'] == 'Migros') & (df['city'] == 'Zürich')
]

display(migros_zuerich)
print('Anzahl:', len(migros_zuerich))
```

**Kurz erklärt:**

- `==` prüft auf Gleichheit.
- `&` bedeutet **UND**: Beide Bedingungen müssen zutreffen.
- `.loc[...]` wählt die passenden Zeilen aus.
- `len(...)` zählt diese Zeilen.

**Für die Prüfung:** Bei mehreren Bedingungen mit `&` braucht jede Bedingung eigene Klammern.

Führe die Zelle aus. Welche Anzahl bekommst du?

> 30

Dein Filter findet **30 Migros-Supermärkte in Zürich**.

**Aufgabe 3g:** Jetzt suchen und zählen wir Coop-Supermärkte in **Zürich, Basel und Bern**. Füge eine neue Codezelle ein:

```python
coop_staedte = df.loc[
    (df['brand'] == 'Coop')
    & (df['city'].isin(['Zürich', 'Basel', 'Bern']))
]

print('Insgesamt:', len(coop_staedte))
print(coop_staedte['city'].value_counts())
```

**Kurz erklärt:**

- `.isin([...])` prüft, ob der Ort **einer der drei Städte** entspricht.
- `len(...)` zählt alle gefilterten Supermärkte.
- `.value_counts()` zählt sie zusätzlich **pro Stadt**.

**Für die Prüfung:** `==` vergleicht mit einem Wert, `.isin()` mit mehreren möglichen Werten.

Welche Zahlen erhältst du?

> Insgesamt: 52
> city
> Zürich    37
> Basel     10
> Bern       5
> Name: count, dtype: int64

Damit hast du **52 Coop-Supermärkte** gefunden: 37 in Zürich, 10 in Basel und 5 in Bern.

**Aufgabe 3h:** Wir suchen jetzt Supermärkte, bei denen **Marke, Ort, Hausnummer und Postleitzahl vorhanden** sind.

Füge eine neue Codezelle ein:

```python
vollstaendige_supermaerkte = df.dropna(
    subset=['brand', 'city', 'housenumber', 'postcode']
)

display(vollstaendige_supermaerkte.head())
print('Anzahl:', len(vollstaendige_supermaerkte))
```

**Kurz erklärt:** `dropna(subset=[...])` behält nur Zeilen, bei denen in **keiner der genannten Spalten** ein fehlender Wert steht. Das Ergebnis speichern wir in einer neuen Variable; `df` bleibt erhalten.

**Für die Prüfung:** Entscheidend sind hier nur diese vier Spalten. Eine fehlende Strasse würde eine Zeile beispielsweise nicht ausschliessen.

Welche Anzahl bekommst du?

> 1148

**1148 Supermärkte** haben in allen vier ausgewählten Spalten einen Wert.

**Aufgabe 3i: Öffnungszeiten ergänzen.** Dafür müssen wir weiter oben zwei Stellen im Notebook ändern.

**1. Ergänze `opening_hours` bei der Spaltenauswahl von `df2`:**

```python
df2 = df2[['brand', 'shop', 'addr:city', 'addr:street',
           'addr:housenumber', 'addr:postcode', 'opening_hours']]
```

Die anschliessende Umbenennung der Adressspalten bleibt bestehen.

**2. Ergänze die Spalte auch beim Zusammenführen:**

```python
df = pd.merge(
    df1[['type', 'id', 'lat', 'lon']],
    df2[['brand', 'shop', 'city', 'street',
         'housenumber', 'postcode', 'opening_hours']],
    left_index=True,
    right_index=True
)
```

Führe danach die Zellen **ab `pd.DataFrame.from_records(df1.tags)` bis einschliesslich der Zusammenführung erneut von oben nach unten aus**.

**Warum beide Stellen?** Zuerst übernehmen wir die Öffnungszeiten aus `tags` in `df2`, danach aus `df2` in die gemeinsame Tabelle `df`.

**Aufgabe 3j:** Füge unten eine neue Codezelle ein:

```python
mit_oeffnungszeiten = df.loc[df['opening_hours'].notna()]

display(mit_oeffnungszeiten[['brand', 'city', 'opening_hours']].head())
print('Anzahl:', len(mit_oeffnungszeiten))
```

`.notna()` prüft: **Ist ein Wert vorhanden?**

Welche Anzahl erhältst du?

> wo muss ich die neue codezeile hinzuügen?

Du meinst die **neue Codezelle für Aufgabe 3j**: Füge sie **direkt unter deiner letzten Filterzelle** ein – also unter der Zelle, die `1148` ausgegeben hat.

1. Bewege die Maus an den unteren Rand dieser Zelle.
2. Klicke auf **„+ Code“**.
3. Füge dort ein:

```python
mit_oeffnungszeiten = df.loc[df['opening_hours'].notna()]

display(mit_oeffnungszeiten[['brand', 'city', 'opening_hours']].head())
print('Anzahl:', len(mit_oeffnungszeiten))
```

**Vor dem Ausführen** musst du weiter oben `opening_hours` an den zwei beschriebenen Stellen ergänzen und die betroffenen Zellen erneut ausführen. Sonst kennt `df` diese Spalte noch nicht.

Hast du diese beiden Änderungen oben bereits gemacht?

> gemacht, erhalte Anzahl 2031

**2031 Supermärkte haben einen vorhandenen Wert für die Öffnungszeiten.** Das sind mehr als die 1148 von vorher, weil wir jetzt nur `opening_hours` prüfen – Marke oder Adresse dürfen dabei fehlen.

Speichere das Notebook über **„Speichern unter“** als:

```text
supermarkets_data.ipynb
```

Führe darin auch die vorhandene CSV-Speicherzelle erneut aus, damit die Öffnungszeiten mitgespeichert werden:

```python
df.to_csv(
    'supermarkets_data_prepared.csv',
    sep=',',
    encoding='utf-8',
    index=False
)
```

Damit ist **Aufgabe 3 abgeschlossen**.

**Jetzt Aufgabe 4: Datenbanken und SQL.** Öffne `apartments_database_Python.ipynb` und führe zunächst nur die ersten beiden Codezellen aus, bis einschliesslich:

```python
conn = sqlite3.connect('apartment_database.db')
cursor = conn.cursor()
```

**Kurz erklärt:**

- **SQLite** speichert eine Datenbank in einer Datei.
- `conn` ist die Verbindung zur Datenbank.
- `cursor` führt später SQL-Befehle aus.

Die Verbindung wird geöffnet; falls die Datei noch nicht existiert, wird sie erstellt. Läuft das ohne Fehlermeldung?

> keine fehlermeldung

Die Verbindung steht. **Jetzt erstellen und befüllen wir die Wohnungstabelle.**

Führe die nächsten drei Zellen aus:

1. **`CREATE TABLE ...`** erstellt die Tabelle, falls sie noch nicht existiert. `conn.commit()` bestätigt die Änderung.
2. **`pd.read_csv(...)`** lädt deine vorbereiteten Zürich-Daten und wählt ID, Adresse, Zimmerzahl, Fläche und Preis aus.
3. **`df.to_sql(...)`** schreibt diese Daten in die Datenbank:

```python
df.to_sql(
    name='apartments_table',
    con=conn,
    index=False,
    if_exists='replace'
)
```

**Für die Prüfung:** `if_exists='replace'` ersetzt eine vorhandene Tabelle vollständig durch den DataFrame.

Führe danach die vorhandene Abfrage aus:

```sql
SELECT *
FROM apartments_table
WHERE rooms >= 1
```

Das bedeutet: **Zeige alle Spalten (`*`) aller Wohnungen mit mindestens einem Zimmer.**

Führe die Zelle zum Schliessen der Verbindung noch nicht aus – wir brauchen sie für die nächsten Abfragen.

Wird dir eine Tabelle angezeigt?

> ja

Jetzt **Aufgabe 4c:** Wohnungen mit **mindestens 4 Zimmern UND mindestens 100 m²** auswählen.

Füge direkt unter der bisherigen Abfrage eine neue Codezelle ein:

```python
query = """
SELECT *
FROM apartments_table
WHERE rooms >= 4.0 AND area >= 100
"""

ergebnis = pd.read_sql_query(query, conn)
display(ergebnis)
```

**Kurz erklärt:**

- `SELECT *`: alle Spalten anzeigen.
- `FROM`: aus welcher Tabelle?
- `WHERE`: welche Bedingungen müssen gelten?
- `AND`: **beide** Bedingungen müssen erfüllt sein.
- `pd.read_sql_query(...)`: führt SQL aus und liefert einen DataFrame.

**Für die Prüfung:** In SQL schreibst du `AND`; beim pandas-Filter haben wir `&` verwendet.

Führe die Zelle aus. Enthalten die angezeigten Wohnungen jeweils mindestens **4 Zimmer und 100 m²**?

> ja

**Aufgabe 4d:** Jetzt berechnen wir die **durchschnittliche Miete je Zimmerzahl** – beispielsweise für alle 1-Zimmer-, 1,5-Zimmer- und 2-Zimmer-Wohnungen.

Füge eine neue Codezelle ein:

```python
query = """
SELECT rooms, AVG(price) AS durchschnittspreis
FROM apartments_table
GROUP BY rooms
ORDER BY rooms
"""

preise_pro_zimmerzahl = pd.read_sql_query(query, conn)
display(preise_pro_zimmerzahl)
```

**Kurz erklärt:**

- `GROUP BY rooms` fasst Wohnungen mit gleicher Zimmerzahl zusammen.
- `AVG(price)` berechnet für jede Gruppe den durchschnittlichen Mietpreis.
- `AS durchschnittspreis` benennt die Ergebnisspalte.
- `ORDER BY rooms` sortiert nach Zimmerzahl.

**Für die Prüfung:** Gesucht ist hier die durchschnittliche **Wohnungsmiete pro Zimmerkategorie**. Wir teilen den Preis also nicht durch die Zimmerzahl.

Das Ergebnis hat **zwei Spalten**: Zimmerzahl und Durchschnittspreis. Siehst du diese Tabelle?

> ja

**Aufgabe 4e funktioniert fast gleich:** Gesucht ist jetzt die **durchschnittliche Wohnfläche je Zimmerzahl**.

Füge eine neue Codezelle ein:

```python
query = """
SELECT rooms, AVG(area) AS durchschnittsflaeche
FROM apartments_table
GROUP BY rooms
ORDER BY rooms
"""

flaechen_pro_zimmerzahl = pd.read_sql_query(query, conn)
display(flaechen_pro_zimmerzahl)
```

Wir ersetzen nur **`AVG(price)` durch `AVG(area)`**. Jede Zeile zeigt dann beispielsweise: „Wohnungen mit 3,5 Zimmern haben durchschnittlich … m².“

**Für die Prüfung:** `AVG()` ignoriert fehlende Werte. Wohnungen ohne Flächenangabe gehen deshalb nicht in diesen Flächendurchschnitt ein.

Führe die Zelle aus und speichere das Notebook mit **Strg + S**. Danach erstellen wir die Datenbank für die Supermärkte.

> ok

**Jetzt Aufgabe 4f–h: eine Datenbank für Supermärkte erstellen und Winterthur filtern.**

Erstelle in VS Code über **Strg + Shift + P → „Create: New Jupyter Notebook“** ein neues Notebook. Speichere es im Ordner `Week_02` als:

```text
supermarkets_database_Python.ipynb
```

Füge diese **drei Codezellen** ein und führe sie der Reihe nach aus.

**1. Daten laden und Datenbank öffnen**

```python
import pandas as pd
import sqlite3

df = pd.read_csv('supermarkets_data_prepared.csv', encoding='utf-8')
conn = sqlite3.connect('supermarkets_database.db')
```

Die CSV wird als DataFrame geladen; `conn` öffnet die Verbindung zur Supermarkt-Datenbank.

**2. Tabelle speichern**

```python
df.to_sql(
    'supermarkets_table',
    con=conn,
    index=False,
    if_exists='replace'
)
```

`to_sql()` erstellt die Tabelle direkt aus dem DataFrame. Ein separates `CREATE TABLE` ist dafür nicht erforderlich.

**3. Supermärkte in Winterthur abfragen**

```python
query = """
SELECT *
FROM supermarkets_table
WHERE city = 'Winterthur'
"""

winterthur = pd.read_sql_query(query, conn)
display(winterthur)
print('Anzahl:', len(winterthur))
```

**Für die Prüfung:** In SQL prüft **`=`** auf Gleichheit. Textwerte stehen in einfachen Anführungszeichen: **`'Winterthur'`**.

Welche Anzahl erhältst du? Danach schliessen wir die Verbindung und machen einen kurzen Prüfungscheck.


Die Fehlermeldung **`FileNotFoundError`** bedeutet: Python findet `supermarkets_data_prepared.csv` nicht. Im Explorer ist diese Datei ebenfalls noch nicht sichtbar.

**Wir müssen die aufbereiteten Supermarktdaten zuerst als CSV speichern:**

1. Wechsle zum Notebook **`supermarkets_data.ipynb`**.
2. Führe dort die Speicherzelle aus:

   ```python
   df.to_csv(
       'supermarkets_data_prepared.csv',
       sep=',',
       encoding='utf-8',
       index=False
   )
   ```

3. Prüfe, ob **`supermarkets_data_prepared.csv`** links im Ordner `Week_02` erscheint.
4. Wechsle zurück zu **`supermarkets_database_Python.ipynb`** und führe die erste Zelle erneut aus.

**Merke:** Das Speichern des Notebooks speichert deinen **Code und die Ausgaben**. Erst `to_csv()` speichert die **Tabelle als eigene CSV-Datei**.

Erscheint die CSV jetzt im Explorer?


**`NameError: name 'df' is not defined`** bedeutet: Die Tabelle `df` wurde in dieser Python-Sitzung noch nicht erstellt.

**So behebst du das:**

1. Bleibe in **`supermarkets_data.ipynb`**.
2. Klicke oben auf **„Alle ausführen“**. Dadurch werden zuerst die Daten geladen und verarbeitet, danach gespeichert.
3. Falls eine Zelle fehlschlägt, schick mir die **erste Fehlermeldung**.

Wenn alles durchläuft, wechsle zurück zu **`supermarkets_database_Python.ipynb`** und führe dort die drei Zellen von oben nach unten aus.

**Für die Prüfung:** Variablen wie `df` leben im Arbeitsspeicher des **Kernels**, also des laufenden Python-Prozesses. Nach einem Neustart musst du die Zellen erneut ausführen. Gespeicherte Tabellenausgaben können trotzdem noch sichtbar sein.

> hat geklappt, datei supermarkets_data_prepared.csv wurde erstellt

Jetzt kannst du in **`supermarkets_database_Python.ipynb`** die drei Zellen **von oben nach unten** erneut ausführen:

1. CSV laden und Datenbank öffnen.
2. Mit `df.to_sql(...)` die Tabelle speichern.
3. Mit der SQL-Abfrage nach `Winterthur` filtern.

**Damit läuft der Datenfluss so:**

```text
CSV-Datei → pandas-DataFrame → SQL-Tabelle → gefiltertes Ergebnis
```

Welche **Anzahl** zeigt die Winterthur-Abfrage an?

> 3392

**3392 könnte die Anzahl aller gespeicherten Supermärkte sein.** `df.to_sql(...)` gibt nach dem Speichern die Anzahl geschriebener Zeilen zurück.

Für die Anzahl **nur in Winterthur** führe diese Zelle aus:

```python
query = """
SELECT *
FROM supermarkets_table
WHERE city = 'Winterthur'
"""

winterthur = pd.read_sql_query(query, conn)
display(winterthur)
print('Anzahl Winterthur:', len(winterthur))
```

**Für die Prüfung:** `to_sql()` **speichert** Daten; `SELECT ... WHERE` **filtert** sie.

Welche Zahl steht jetzt hinter **„Anzahl Winterthur“**?

> 27

**27 Supermärkte in Winterthur** – damit hat deine SQL-Abfrage funktioniert.

Füge zum Abschluss eine Codezelle ein und führe sie aus:

```python
conn.close()
```

Das schliesst die Datenbankverbindung. Speichere danach das Notebook mit **Strg + S**. Damit sind die inhaltlichen Aufgaben von Week_02 durchgearbeitet.

Für die Prüfung solltest du diese Schritte erklären können:

| Befehl | Zweck |
|---|---|
| `pd.read_csv(...)` | CSV als Tabelle laden |
| `df.head()` | Erste fünf Zeilen anzeigen |
| `df.shape` | Anzahl Zeilen und Spalten ermitteln |
| `df.dtypes` | Datentypen anzeigen |
| `re.findall(...)` | Textteile mit einem Suchmuster extrahieren |
| `df.isna().sum()` | Fehlende Werte pro Spalte zählen |
| `df.duplicated().sum()` | Vollständig doppelte Zeilen zählen |
| `df.loc[...]` | Zeilen nach Bedingungen filtern |
| `df.to_csv(...)` / `df.to_sql(...)` | Tabelle als CSV / in einer Datenbank speichern |
| `GROUP BY` mit `AVG()` | Durchschnitt je Gruppe berechnen |

**Kurzer Prüfungscheck:** Du möchtest alle Coop-Supermärkte in Bern auswählen. Wie würdest du die Lücken ergänzen?

```sql
SELECT *
FROM supermarkets_table
WHERE brand = '___' AND city = '___'
```

> kurze frage, muss ich änderunge nun pushen im github?

**Damit deine Änderungen auf GitHub gespeichert sind: ja.** Falls du über GitHub abgeben musst, gehört das dazu.

In VS Code:

1. **Alle Dateien speichern**.
2. Links **Quellcodeverwaltung** öffnen.
3. Geänderte und neue Dateien prüfen und mit **`+` vormerken** („Stage Changes“).
4. Eine Nachricht eingeben, z. B. `Week_02 Aufgaben gelöst`.
5. **Commit** klicken, danach **Push** oder **Änderungen synchronisieren**.

**Merke:** Speichern sichert die Dateien im Codespace, **Commit** erstellt einen lokalen Versionsstand, **Push** überträgt ihn zu GitHub.

Ob du CSV- und Datenbankdateien mit abgeben sollst, hängt von euren Abgabevorgaben ab.

> help
>

<details><summary>2 previous messages</summary>

> Git wird durch eine Sperrdatei blockiert. Ich prüfe, ob noch ein Git-Vorgang läuft oder ob die Sperre übrig geblieben ist.
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `ps -eo pid,comm,args | rg '[g]it|[i]ndex.lock'; ls -l .git/index.lock; git status --short`
> - Ran `rm .git/index.lock && git status --short`
>
> </details>
</details>

**Die Blockierung ist behoben.** Es lief kein Git-Vorgang mehr; ich habe die übrig gebliebene Sperrdatei entfernt. Deine Aufgaben-Dateien bleiben erhalten.

Jetzt in VS Code:

1. Fehlermeldung mit **„Abbrechen“** schliessen.
2. **Alle Dateien speichern**.
3. Änderungen mit **`+`** vormerken.
4. Nachricht eingeben: `Week_02 Aufgaben gelöst`
5. **Commit** klicken, danach **Änderungen synchronisieren / Push**.

**Kurz erklärt:** Die Sperrdatei verhindert, dass zwei Git-Vorgänge gleichzeitig Änderungen vornehmen. Hier war sie nach einem früheren Vorgang liegen geblieben.

> wuhuuuu

🎉 Geschafft! Wenn die Synchronisierung durchgelaufen ist, sind deine Änderungen jetzt auf GitHub gesichert.

Bereit für einen kurzen Prüfungscheck zu Week_02?

> bitte geb mir den markdown dieses chats an, aber ohne die screenshots bilder von mir, da dies einen fetten text erzeugen

<details><summary>2 previous messages</summary>

> Ich erstelle dir eine Markdown-Datei mit den Textnachrichten dieses Chats. Die Screenshots lasse ich weg.
>
> <details><summary>Ran a command</summary>
>
> - Ran `mkdir -p /tmp/chat_export`
>
> </details>
</details>

> mkdir -p /tmp/chat_export

Der Befehl erstellt den Ordner `/tmp/chat_export`. Er existiert bereits – die Markdown-Datei mit dem Chat ist darin noch nicht erstellt.
