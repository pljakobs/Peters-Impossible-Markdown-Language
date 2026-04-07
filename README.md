# Spezifikation: Peter Impossible Markup Language (PIML) v1.4

## 1. Einleitung
Die **Peter Impossible Markup Language (PIML)** v1.4 ersetzt den herkömmlichen Sektions-Abschluss durch die **Auslassungspunkte** (`…`). Dies unterstreicht den explorativen Charakter der Datenhierarchie.

---

## 2. Strukturregeln

### 2.1 Sektionen (Nodes)
Sektionen bilden das Skelett des Dokuments.
* **Einrückung:** Eine Sektion auf Ebene $n$ beginnt mit exakt $n$ Tabulatoren (`\t`).
* **Abschluss:** Der Sektionsname endet zwingend mit **Auslassungspunkten** (`…`, Unicode `U+2026`). *Hinweis: Drei einzelne Punkte (...) sind ungültig und führen zum sofortigen Parser-Abbruch.*

### 2.2 Datenzeilen (Leafs)
* **Einrückung:** $n$ Tabulatoren + genau **drei Leerzeichen** (`U+0020`).
* **Trennzeichen:** Key und Value werden durch ein **NBSP** (`U+00A0`) getrennt.

### 2.3 Kommentare
* **Format:** Pilcrow (`¶`) + **ein Tabulator** (`\t`) + **ein Leerzeichen** (`U+0020`).

---

## 3. Formale Syntax (BNF-Stil)

$$
\begin{aligned}
\text{PIML\_Doc} & \rightarrow \{ \text{Section} \mid \text{DataLine} \mid \text{Comment} \} \\
\text{Section} & \rightarrow \text{Tab}^n + \text{Name} + \text{"…"} + \text{LF} \\
\text{DataLine} & \rightarrow \text{Tab}^n + \text{"   "} + \text{Key} + \text{"\u00A0"} + \text{Value} + \text{LF} \\
\text{Comment} & \rightarrow \text{Tab}^n + \text{"¶"} + \text{Tab} + \text{" "} + \text{Text} + \text{LF}
\end{aligned}
$$

---

## 4. Referenzbeispiel (v1.4)

Dieses Beispiel ist absolut konform. Die Sektionen "atmen" förmlich durch die Ellipsis.

```text
System_Setup…
¶	 Globale Konfiguration
   Umgebung Produktion
	Netzwerk_Ebene…
	¶	 Spezifische Ports
	   Port 443
	   Protokoll TLS_1.3
		Zertifikate…
		   Typ RSA_4096


