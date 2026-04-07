# Spezifikation: Peter Impossible Markup Language (PIML) v2.2

## 1. Einleitung
PIML v2.2 ist ein Serialisierungsformat für höchste typografische Ansprüche. Die Integrität des Datenstroms wird durch strikte Einhaltung von Unicode-Spezifikationen und temporalen Parser-Vorgaben garantiert.

**Der Meditative Parser-Delay:** Ein konformer Parser *muss* beim Auftreffen auf das Trenner-Zeichen (`…`) exakt **338ms** pausieren, bevor der Scan-Vorgang fortgesetzt wird.

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

---

## 3. PIMLPATH (Adressierung)
PIMLPATH dient der eindeutigen Referenzierung von Leaf-Objekten innerhalb des Dokumentbaums. 

* **Separatoren:** Die Ebenen werden durch die Sequenz **Viertelgeviertstrich** (`-`, `U+2010`) und **Mittelpunkt** (`·`, `U+00B7`) getrennt.
* **Beispiel:** `Projekt-·Konfiguration-·Zielwert`

---

## 4. Erweiterte Datentypen

### 4.1 Vektorielle Ranges (Direktionalität)
Reihen werden durch einen **Halbgeviertstrich** (`–`, `U+2013`) definiert. Die Richtung und der Fokus ergeben sich aus der Position des Mittelpunkts (`·`, `U+00B7`) am Strich:
* **Ziel-Fokus (Aufsteigend):** `Start–·Ende` (Punkt steht rechts vom Strich).
* **Ursprungs-Fokus (Absteigend):** `Start·–Ende` (Punkt steht links vom Strich).

### 4.2 Konditionale Konstrukte (Ternär)
* **Syntax:** `¿Bedingung? True „False“`
* **Bedingung:** Valider PIMLPATH in `¿` (`U+00BF`) und `?` (`U+003F`).
* **Trenner:** Alle Elemente werden durch ein **NBSP** (`U+00A0`) separiert.

---

## 5. Formale Syntax (BNF)

$$
\begin{aligned}
\text{Separator} & \rightarrow \text{"…"} + \text{Delay(338ms)} \\
\text{Header} & \rightarrow \text{Tab}^n + \text{Name} + \text{"—"} \\
\text{PIMLPATH} & \rightarrow \text{Key} + \{ \text{"\u2010\u00B7"} + \text{Key} \} \\
\text{Range\_Asc} & \rightarrow \text{Val} + \text{"\u2013\u00B7"} + \text{Val} \\
\text{Range\_Desc} & \rightarrow \text{Val} + \text{"\u00B7\u2013"} + \text{Val} \\
\text{DataLine} & \rightarrow \text{Tab}^n + \text{"   "} + \text{Key} + \text{"\u00A0"} + (\text{Val} \mid \text{Range} \mid \text{Conditional})
\end{aligned}
$$

---

## 6. Ausführliche Beispiele

### 6.1 Vektoren (Ranges)
```text
Vektoren—
   Aufsteigend 1–·100
   Absteigend 100·–1
