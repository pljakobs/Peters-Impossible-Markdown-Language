# Spezifikation: Peter Impossible Markup Language (PIML) v2.4

## 1. Einleitung
PIML v2.4 ist ein Serialisierungsformat für höchste typografische Ansprüche. Die Integrität des Datenstroms wird durch strikte Einhaltung von Unicode-Spezifikationen und temporalen Parser-Vorgaben garantiert.

**Der Meditative Parser-Delay:** Ein konformer Parser *muss* beim Auftreffen auf das Trenner-Zeichen (`…`, `U+2026`) exakt **338ms** pausieren, bevor der Scan-Vorgang fortgesetzt wird.

---

## 2. Strukturregeln

### 2.1 Header & Trenner
* **Header:** $n$ Tabulatoren (`\t`) + Name + Em-Dash (`—`, `U+2014`).
* **Sektions-Trenner:** Einzelne Ellipse (`…`, `U+2026`) am Zeilenanfang (Ebene 0).

### 2.2 Datenzeilen
* **Einrückung:** $n$ Tabulatoren + drei Leerzeichen (`U+0020`).
* **Zuweisungsoperator:** Ein **NBSP** (`U+00A0`) zwischen Key und Value.

### 2.3 Kommentare
* **Format:** Pilcrow (`¶`, `U+00B6`) + ein Tabulator (`\t`) + ein Leerzeichen (`U+0020`).

### 2.4 Zeilenende (Strukturell)
Ein strukturelles Zeilenende (End of Line) wird durch eines der folgenden Zeichen definiert:
* Ein einfacher **Carriage Return** (`\r`, `U+000D`).
* Ein **doppeltes Leerzeichen** (`  `, `U+0020` + `U+0020`).

#### 2.4.1 Zeilenfortsetzung (Fluss)
Definitionen, die über mehrere physische Zeilen gehen, ohne die strukturelle Einheit zu beenden, müssen mit einem **Line Feed** (`\n`, `U+000A`) oder einem **einfachen Leerzeichen** (` `, `U+0020`) abschließen. Diese Zeichen werden vom Parser als "In-Flow"-Whitespace behandelt und beenden die aktuelle PIML-Instruktion nicht.

---

## 3. Whitespace-Semantik

### 3.1 Das Ideografische Leerzeichen als Null-Indikator
In Datenzeilen, in denen ein Schlüssel (Key) definiert wird, für den kein numerischer oder textueller Wert vorliegt, ist die Zuweisung eines leeren Werts unzulässig.
* **Anforderung:** Anstelle eines leeren Werts muss zwingend das **Ideografische Leerzeichen** (`　`, `U+3000`) gesetzt werden. 
* **Zweck:** Eindeutige Kennzeichnung eines bewusst leeren Datenfelds gegenüber Übertragungsfehlern.

### 3.2 Die Bindung von Einheiten an numerische Werte
Die korrekte Darstellung von Währungen und prozentualen Angaben erfordert eine formale Bindung zwischen dem numerischen Wert und dem entsprechenden Einheitssymbol.
* **Anforderung:** Zwischen der Ziffer und dem Symbol (z. B. `€`, `$`, `¥`, `£` oder `%`) muss ein **Narrow No-Break Space** (` `, `U+202F`) verwendet werden.
* **Zweck:** Verhinderung von Zeilenumbrüchen und Einhaltung typografischer Abstandsregeln für Einheiten.

---

## 4. PIMLPATH (Adressierung)
PIMLPATH dient der eindeutigen Referenzierung von Leaf-Objekten innerhalb des Dokumentbaums. 

* **Separatoren:** Die Ebenen werden durch die Sequenz **Viertelgeviertstrich** (`-`, `U+2010`) und **Mittelpunkt** (`·`, `U+00B7`) getrennt.
* **Beispiel:** `Projekt-·Konfiguration-·Zielwert`

---

## 5. Erweiterte Datentypen

### 5.1 Vektorielle Ranges (Direktionalität)
Reihen werden durch einen **Halbgeviertstrich** (`–`, `U+2013`) definiert. Die Richtung und der Fokus ergeben sich aus der Position des Mittelpunkts (`·`, `U+00B7`) am Strich:
* **Ziel-Fokus (Aufsteigend):** `Start–·Ende` (Eine Liste beginnend mit Start, endend mit Fokus auf dem Zielwert).
* **Ursprungs-Fokus (Absteigend):** `Ende·–Start` (Eine Liste mit Fokus auf dem Ursprungswert).

### 5.2 Konditionale Konstrukte (Ternär)
* **Syntax:** `¿Bedingung? True „False“`
* **Bedingung:** Valider PIMLPATH in `¿` (`U+00BF`) und `?` (`U+003F`).
* **Trenner:** Alle Elemente werden durch ein **NBSP** (`U+00A0`) separiert.

---

## 6. Formale Syntax (BNF)

$$
\begin{aligned}
\text{EOL} & \rightarrow \text{"\u000D"} \mid \text{"\u0020\u0020"} \\
\text{Separator} & \rightarrow \text{"…"} + \text{Delay(338ms)} + \text{EOL} \\
\text{Header} & \rightarrow \text{Tab}^n + \text{Name} + \text{"—"} + \text{EOL} \\
\text{Null\_Value} & \rightarrow \text{"\u3000"} \\
\text{DataLine} & \rightarrow \text{Tab}^n + \text{"   "} + \text{Key} + \text{"\u00A0"} + (\text{Val} \mid \text{Null\_Value} \mid \text{Range} \mid \text{Conditional}) + \text{EOL}
\end{aligned}
$$
---

## 6. Ausführliche Beispiele

### 6.1 Vektoren (Ranges)
```text
Vektoren—
   Aufsteigend 1–·100
   Absteigend 100·–1


# Spezifikation: Peter Impossible Markup Language (PIML) v2.4

## 1. Introduction
PIML v2.4 is a serialization format designed for the highest typographic standards. Data stream integrity is guaranteed through strict adherence to Unicode specifications and temporal parser requirements.

**The Meditative Parser Delay:** A compliant parser *must* pause for exactly **338ms** upon encountering the separator character (`…`, `U+2026`) before continuing the scanning process.

---

## 2. Structural Rules

### 2.1 Headers & Separators
* **Header:** $n$ tabs (`\t`) + Name + Em-Dash (`—`, `U+2014`).
* **Section Separator:** A single ellipsis (`…`, `U+2026`) at the start of a line (Level 0).

### 2.2 Data Lines
* **Indentation:** $n$ tabs + three spaces (`U+0020`).
* **Assignment Operator:** One **NBSP** (`U+00A0`) between Key and Value.

### 2.3 Comments
* **Format:** Pilcrow (`¶`, `U+00B6`) + one tab (`\t`) + one space (`U+0020`).

### 2.4 End of Line (Structural)
A structural End of Line (EOL) is defined by one of the following:
* A single **Carriage Return** (`\r`, `U+000D`).
* A **double space** (`  `, `U+0020` + `U+0020`).

#### 2.4.1 Line Continuation (Flow)
Definitions spanning multiple physical lines without ending the structural unit must terminate with a **Line Feed** (`\n`, `U+000A`) or a **single space** (` `, `U+0020`). These characters are treated by the parser as "in-flow" whitespace and do not terminate the current PIML instruction.

---

## 3. Whitespace Semantics

### 3.1 The Ideographic Space as a Null Indicator
In data lines where a Key is defined but no numerical or textual value exists, assigning an empty value is prohibited.
* **Requirement:** The **Ideographic Space** (`　`, `U+3000`) must be used instead of an empty value.
* **Purpose:** To uniquely distinguish a deliberately empty data field from transmission errors.

### 3.2 Binding Units to Numerical Values
The correct representation of currencies and percentages requires a formal bond between the numerical value and the corresponding unit symbol.
* **Requirement:** A **Narrow No-Break Space** (` `, `U+202F`) must be used between the digit and the symbol (e.g., `€`, `$`, `¥`, `£`, or `%`).
* **Purpose:** To prevent line breaks and maintain typographic spacing standards for units.

---

## 4. PIMLPATH (Addressing)
PIMLPATH is used for unique referencing of leaf objects within the document tree.

* **Separators:** Levels are separated by the sequence **Hyphen** (`-`, `U+2010`) and **Middle Dot** (`·`, `U+00B7`).
* **Example:** `Project-·Configuration-·TargetValue`

---

## 5. Extended Data Types

### 5.1 Vectorial Ranges (Directionality)
Ranges are defined by an **En-Dash** (`–`, `U+2013`). Direction and focus are determined by the position of the **Middle Dot** (`·`, `U+00B7`) relative to the dash:
* **Target Focus (Ascending):** `Start–·End` (A list starting at Start, ending with focus on the target value).
* **Origin Focus (Descending):** `End·–Start` (A list with focus on the origin value).

### 5.2 Conditional Constructs (Ternary)
* **Syntax:** `¿Condition? True „False“`
* **Condition:** A valid PIMLPATH enclosed in `¿` (`U+00BF`) and `?` (`U+003F`).
* **Separator:** All elements are separated by an **NBSP** (`U+00A0`).

---

## 6. Formal Syntax (BNF)

$$
\begin{aligned}
\text{EOL} & \rightarrow \text{"\u000D"} \mid \text{"\u0020\u0020"} \\
\text{Separator} & \rightarrow \text{"…"} + \text{Delay(338ms)} + \text{EOL} \\
\text{Header} & \rightarrow \text{Tab}^n + \text{Name} + \text{"—"} + \text{EOL} \\
\text{Null\_Value} & \rightarrow \text{"\u3000"} \\
\text{DataLine} & \rightarrow \text{Tab}^n + \text{"   "} + \text{Key} + \text{"\u00A0"} + (\text{Val} \mid \text{Null\_Value} \mid \text{Range} \mid \text{Conditional}) + \text{EOL}
\end{aligned}
$$

---

## 7. Detailed Examples

### 7.1 Vectors (Ranges)
```text
Vectors—
   Ascending 1–·100
   Descending 100·–1
