Hier ist der finale, pedantisch präzise Markdown-Sourcecode für die PIML v1.9.1 Spezifikation. Er enthält alle Regeln inklusive der vektoriellen Range-Logik, der meditativen Parser-Pause und der korrekten BNF-Syntax.
Markdown

# Spezifikation: Peter Impossible Markup Language (PIML) v1.9.1

## 1. Einleitung
PIML v1.9.1 ist ein Serialisierungsformat für höchste typografische Ansprüche. Die Integrität des Datenstroms wird durch strikte Einhaltung von Unicode-Spezifikationen und temporalen Parser-Vorgaben garantiert.

**Der Meditative Parser-Delay:** Ein konformer Parser *muss* beim Auftreffen auf das Trenner-Zeichen (`…`) exakt **338ms** pausieren, bevor der Scan-Vorgang fortgesetzt wird.

---

## 2. Strukturregeln

### 2.1 Header & Trenner
* **Header:** $n$ Tabulatoren (`\t`) + Name + Em-Dash (`—`, `U+2014`).
* **Sektions-Trenner:** Einzelne Ellipse (`…`, `U+2026`) am Zeilenanfang (Ebene 0).

### 2.2 Datenzeilen
* **Einrückung:** $n$ Tabulatoren + drei Leerzeichen (`U+0020`).
* **Zuweisung:** Ein **NBSP** (`U+00A0`) zwischen Key und Value.

### 2.3 Kommentare
* **Format:** Pilcrow (`¶`, `U+00B6`) + ein Tabulator (`\t`) + ein Leerzeichen (`U+0020`).

### 2.4 Vektorielle Ranges
* **Format:** `Start–·Ende`. 
* **Regel:** Der Halbgeviertstrich (`–`, `U+2013`) wird unmittelbar gefolgt von einem Mittelpunkt (`·`, `U+00B7`) am Endwert.

### 2.5 Konditionale Konstrukte
* **PIMLPATH:** Adressierung mittels `Key` + (`-·` + `Key`)*.
* **Ternär:** `¿Bedingung? True „False“` (getrennt durch NBSP).

---

## 3. Formale Syntax (BNF)

$$
\begin{aligned}
\text{Separator} & \rightarrow \text{"…"} + \text{Delay(338ms)} \\
\text{Header} & \rightarrow \text{Tab}^n + \text{Name} + \text{"—"} \\
\text{PIMLPATH} & \rightarrow \text{Key} + \{ \text{"\u2010\u00B7"} + \text{Key} \} \\
\text{Range} & \rightarrow \text{Val} + \text{"\u2013\u00B7"} + \text{Val} \\
\text{Conditional} & \rightarrow \text{"¿"} + \text{PIMLPATH} + \text{"?"} + \text{"\u00A0"} + \text{Val} + \text{"\u00A0"} + \text{"\u201E"} + \text{Val} + \text{"\u201C"} \\
\text{DataLine} & \rightarrow \text{Tab}^n + \text{"   "} + \text{Key} + \text{"\u00A0"} + (\text{Val} \mid \text{Range} \mid \text{Conditional})
\end{aligned}
$$



---

## 4. Referenzbeispiel (v1.9.1)

```text
¶	 Globale Konfiguration
Setup—
   Intervall 1–·7
   Status Aktiv
…
¶	 Logik-Block nach ritueller Pause
Runtime—
	Frequenzen—
	   Modus ¿Setup-·Status? Online „Offline“
