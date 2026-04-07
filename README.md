# Spezifikation: Peter Impossible Markup Language (PIML) v1.2

## 1. Einleitung
Die **Peter Impossible Markup Language (PIML)** ist ein minimalistisches, aber hochgradig striktes Serialisierungsformat. Es wurde entwickelt, um die visuelle Mehrdeutigkeit klassischer Formate durch eine mathematisch präzise Differenzierung von Whitespace-Typen zu eliminieren.

---

## 2. Strukturregeln

Die Hierarchie wird in PIML durch eine Kombination aus Tabulatoren und Leerzeichen definiert.

### 2.1 Sektionen (Nodes)
Sektionen dienen als Container für weitere Sektionen oder Datenpaare.
* **Einrückung:** Eine Sektion auf der Ebene $n$ wird mit exakt $n$ Tabulatoren (`\t`) eingeleitet.
* **Abschluss:** Der Sektionsname muss mit einem **Em-Dash** (`—`, Unicode `U+2014`) enden.

### 2.2 Datenzeilen (Leafs)
Datenzeilen enthalten die eigentlichen Informationen in Form von Schlüssel-Wert-Paaren.
* **Einrückung:** Eine Datenzeile erbt die $n$ Tabulatoren ihrer Elternsektion und fügt exakt **drei Leerzeichen** (`U+0020`) hinzu.
* **Trennzeichen:** Key und Value werden durch ein einzelnes **geschütztes Leerzeichen** (`NBSP`, Unicode `U+00A0`) getrennt.

---

## 3. Formale Syntax (BNF-Stil)

Die Syntax folgt dieser strikten Logik:

$$
\begin{aligned}
\text{PIML\_Doc} & \rightarrow \{ \text{Section} \mid \text{DataLine} \} \\
\text{Section} & \rightarrow \text{Tab}^n + \text{Name} + \text{"—"} + \text{LF} \\
\text{DataLine} & \rightarrow \text{Tab}^n + \text{"   "} + \text{Key} + \text{"\u00A0"} + \text{Value} + \text{LF}
\end{aligned}
$$

---

## 4. Referenzbeispiel

In der folgenden Darstellung sind die unsichtbaren Zeichen zur Verdeutlichung markiert:
`\t` = Tabulator | `_` = Leerzeichen | `·` = Non-breaking Space (NBSP)

```text
Projekt-Alpha—
   Status Aktiv
	Meilensteine—
	   Phase_1 Abgeschlossen
	   Phase_2 Laufend
		Details—
		   Budget Überschritten
