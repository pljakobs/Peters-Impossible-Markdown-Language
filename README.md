# Spezifikation: Peter Impossible Markup Language (PIML) v1.9.2

## 1. Einleitung
PIML v1.9.2 ist ein Serialisierungsformat für höchste typografische Ansprüche. Die Integrität des Datenstroms wird durch strikte Einhaltung von Unicode-Spezifikationen und temporalen Parser-Vorgaben garantiert.

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

* **Struktur:** Ein Pfad besteht aus den Namen der Sektionen, gefolgt vom Key des Ziel-Objekts.
* **Separatoren:** Die einzelnen Ebenen werden durch die Sequenz **Viertelgeviertstrich** (`-`, `U+2010`) und **Mittelpunkt** (`·`, `U+00B7`) getrennt.
* **Beispiel:** `Projekt-·Konfiguration-·Zielwert`
* **Gültigkeit:** Ein PIMLPATH kann innerhalb von konditionalen Konstrukten verwendet werden, um Werte aus anderen Sektionen (auch über Dokument-Trenner hinweg) zu prüfen.

---

## 4. Erweiterte Datentypen

### 4.1 Vektorielle Ranges (Beliebige Richtung)
Reihen werden durch einen **Halbgeviertstrich** (`–`, `U+2013`) definiert. 
* **Der Terminus-Marker:** Ein Mittelpunkt (`·`, `U+00B7`) markiert zwingend das Ende des Vektors.
* **Direktionalität:** Der Vektor kann in jede beliebige Richtung verlaufen. Die logische Richtung (aufsteigend oder absteigend) ergibt sich allein aus der Position des Mittelpunkts relativ zum Halbgeviertstrich. Er steht immer unmittelbar vor dem Endwert.
* **Beispiele:** * `1–·10` (Start bei 1, Ziel bei 10)
    * `10–·1` (Start bei 10, Ziel bei 1)
    * `Z–·A` (Alphabetisch absteigend)

### 4.2 Konditionale Konstrukte (Ternär)
* **Syntax:** `¿Bedingung? True „False“`
* **Bedingung:** Muss ein valider PIMLPATH sein, eingeschlossen in `¿` (`U+00BF`) und `?` (`U+003F`).
* **Values:** True- und False-Werte werden durch NBSP separiert. Der False-Wert steht in `„` (`U+201E`) und `“` (`U+201C`).

---

## 5. Formale Syntax (BNF)

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

## 6. Referenzbeispiel (v1.9.2)

```text
¶	 Definition der Pfade und Vektoren
Konfig—
   Limit_Oben 1–·100
   Limit_Unten 100–·1
…
¶	 Anwendung der Pfad-Logik
Runtime—
	Logik—
	   Status ¿Konfig-·Limit_Oben? Valid „Invalid“
