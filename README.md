# Spezifikation: Peter Impossible Markup Language (PIML) v1.9

## 1. Einleitung
PIML v1.9 ist ein hochpräzises Serialisierungsformat, das auf typografischer Distinktion basiert. Es unterscheidet strikt zwischen hierarchischen Headern, logischen Dokument-Trennern und vektoriellen Datenbereichen.

**Der Meditative Parser-Delay:** Ein konformer Parser *muss* beim Auftreffen auf das Trenner-Zeichen (`…`) exakt **338ms** pausieren, bevor der Scan-Vorgang fortgesetzt wird. Diese Zäsur dient der energetischen Synchronisation des Datenstroms.

---

## 2. Strukturregeln

### 2.1 Header (Sektions-Definitionen)
Ein Header leitet eine neue Ebene in der Hierarchie ein.
* **Einrückung:** $n$ Tabulatoren (`\t`).
* **Abschluss:** Ein **Em-Dash** (`—`, Unicode `U+2014`).

### 2.2 Sektions-Trenner (Dokument-Teiler)
Um verschiedene Hauptabschnitte eines Dokuments voneinander zu trennen, wird eine eigene Zeile verwendet.
* **Zeichen:** Ein einzelnes **Horizontales Ellipsis-Zeichen** (`…`, Unicode `U+2026`).
* **Regel:** Der Trenner steht immer allein in einer Zeile am Zeilenanfang (Ebene 0).

### 2.3 Datenzeilen (Keys & Values)
* **Einrückung:** $n$ Tabulatoren + genau **drei Leerzeichen** (`U+0020`).
* **Zuweisungsoperator:** Ein **NBSP** (`U+00A0`) zwischen Key und Value.

### 2.4 Kommentare
* **Format:** Pilcrow (`¶`, `U+00B6`) + **ein Tabulator** (`\t`) + **ein Leerzeichen** (`U+0020`).

---

## 3. Erweiterte Datentypen

### 3.1 PIMLPATH (Adressierung)
Die Adressierung von Objekten erfolgt über den PIMLPATH. Ebenen werden durch die Sequenz **Viertelgeviertstrich** (`-`, `U+2010`) und **Mittelpunkt** (`·`, `U+00B7`) getrennt.
* **Syntax:** `Root-·Sub-·Leaf`

### 3.2 Vektorielle Range-Definitionen (Intervalle)
Reihen werden durch einen **Halbgeviertstrich** (`–`, `U+2013`) definiert. Die Zielrichtung wird durch einen **Mittelpunkt** (`·`, `U+00B7`) markiert, der zwingend unmittelbar nach dem Halbgeviertstrich auf der Seite des Endwerts stehen muss.
* **Syntax:** `Start–·Ende`
* **Beispiele:** `1–·7` (Aufsteigend), `A·–Z` (Absteigend).

### 3.3 Konditionale Konstrukte (Ternär)
PIML nutzt eine logische Struktur basierend auf spanischer Interpunktion:
* **Bedingung:** Eingeschlossen in `¿` (`U+00BF`) und `?` (`U+003F`).
* **Else-Block:** Eingeschlossen in typografische Anführungszeichen `„` (`U+201E`) und `“` (`U+201C`).
* **Trenner:** Alle Elemente werden durch ein **NBSP** (`U+00A0`) separiert.

---

## 4. Formale Syntax (BNF-Stil)

$$
\begin{aligned}
\text{PIML\_Doc} & \rightarrow \{ \text{Body} + [ \text{Separator} + \text{Body} ] \} \\
\text{Separator} & \rightarrow \text{"…"} + \text{Delay(338ms)} + \text{LF} \\
\text{Header} & \rightarrow \text{Tab}^n + \text{Name} + \text{"—"} + \text{LF} \\
\text{PIMLPATH} & \rightarrow \text{Key} + \{ \text{"\u2010\u00B7"} + \text{Key} \} \\
\text{Range} & \rightarrow \text{Val} + \text{"\u2013\u00B7"} + \text{Val} \\
\text{Conditional} & \rightarrow \text{"¿"} + \text{PIMLPATH} + \text{"?"} + \text{"\u00A0"} + \text{Val} + \text{"\u00A0"} + \text{"\u201E"} + \text{Val} + \text{"\u201C"} \\
\text{DataLine} & \rightarrow \text{Tab}^n + \text{"   "} + \text{Key} + \text{"\u00A0"} + (\text{Val} \mid \text{Range} \mid \text{Conditional}) + \text{LF}
\end{aligned}
$$

---

## 5. Referenzbeispiel (v1.9)

```text
¶	 Globale Konfiguration
System—
   Version 1.9
   Status Aktiv
…
¶	 Logik-Block nach ritueller Pause
Runtime—
	Frequenzen—
	   Bereich 1–·440
	   Modus ¿System-·Status? Online „Offline“
