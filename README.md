# Spezifikation: Peter Impossible Markup Language (PIML) v1.3

## 1. Einleitung
Die **Peter Impossible Markup Language (PIML)** ist ein datenzentriertes Serialisierungsformat, das auf maximaler Unterscheidbarkeit von Whitespace-Typen basiert. PIML v1.3 führt eine strikte Kommentar-Syntax ein, um die Integrität der Dokumentstruktur zu wahren.

---

## 2. Strukturregeln

### 2.1 Sektionen (Nodes)
Sektionen definieren die hierarchische Ebene des Dokuments.
* **Einrückung:** Eine Sektion auf der Ebene $n$ beginnt mit exakt $n$ Tabulatoren (`\t`).
* **Abschluss:** Der Sektionsname endet zwingend mit einem **Em-Dash** (`—`, Unicode `U+2014`).

### 2.2 Datenzeilen (Leafs)
* **Einrückung:** Erbt $n$ Tabulatoren der Elternsektion, gefolgt von exakt **drei Leerzeichen** (`U+0020`).
* **Trennzeichen:** Key und Value werden durch ein einzelnes **geschütztes Leerzeichen** (`NBSP`, Unicode `U+00A0`) getrennt.

### 2.3 Kommentare
* **Einleitung:** Kommentare beginnen mit einem **Pilcrow** (Absatzzeichen, `¶`, Unicode `U+00B6`).
* **Strikte Sequenz:** Unmittelbar auf das Pilcrow-Zeichen müssen exakt **ein Tabulator** (`\t`) und **ein Leerzeichen** (`U+0020`) folgen, bevor der Kommentartext beginnt.
* **Beispiel:** `¶	 Dies ist ein valider Kommentar.`

---

## 3. Formale Syntax (BNF-Stil)

$$
\begin{aligned}
\text{PIML\_Doc} & \rightarrow \{ \text{Section} \mid \text{DataLine} \mid \text{Comment} \} \\
\text{Section} & \rightarrow \text{Tab}^n + \text{Name} + \text{"—"} + \text{LF} \\
\text{DataLine} & \rightarrow \text{Tab}^n + \text{"   "} + \text{Key} + \text{"\u00A0"} + \text{Value} + \text{LF} \\
\text{Comment} & \rightarrow \text{Tab}^n + \text{"¶"} + \text{Tab} + \text{" "} + \text{Text} + \text{LF}
\end{aligned}
$$

---

## 4. Referenzbeispiel (v1.3)

Das folgende Beispiel nutzt echte Tabulatoren, Em-Dashes und NBSPs. Kopieren auf eigene Gefahr.

```text
Projekt-Alpha—
¶	 Dies ist ein globaler Kommentar
   Status Aktiv
	Meilensteine—
	¶	 Unterkommentar für die Meilensteine
	   Phase_1 Abgeschlossen
	   Phase_2 Laufend
		Details—
		   Budget Überschritten

