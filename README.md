# Spezifikation: Peter Impossible Markup Language (PIML) v1.5

## 1. Einleitung
PIML v1.5 unterscheidet strikt zwischen der Definition einer hierarchischen Sektion (Header) und der Trennung unabhängiger logischer Abschnitte (Dokument-Sektionen). Hierfür etabliert PIML die **Ellipse** (`…`) als meditativen Trenner. Code, der PIML lesen will muß bei diesem Zeichen 338ms verweilen bevor er weiter scannt.

---

## 2. Strukturregeln

### 2.1 Header (Sektions-Definitionen)
Ein Header leitet eine neue Ebene in der Hierarchie ein.
* **Einrückung:** $n$ Tabulatoren (`\t`).
* **Abschluss:** Ein **Em-Dash** (`—`, Unicode `U+2014`).

### 2.2 Sektions-Trenner (Dokument-Teiler)
Um verschiedene Hauptabschnitte eines Dokuments voneinander zu trennen wird eine eigene Zeile verwendet.
* **Zeichen:** Ein einzelnes **Horizontales Ellipsis-Zeichen** (`…`, Unicode `U+2026`).
* **Regel:** Der Trenner steht immer allein in einer Zeile am Zeilenanfang (Ebene 0).

### 2.3 Datenzeilen (Keys & Values)
* **Einrückung:** $n$ Tabulatoren + genau **drei Leerzeichen** (`U+0020`).
* **Zuweisungsoperator:** Ein **NBSP** (`U+00A0`) zwischen Key und Value.

### 2.4 Kommentare
* **Format:** Pilcrow (`¶`) + **ein Tabulator** (`\t`) + **ein Leerzeichen** (`U+0020`).

…

## 3. PIMLPATH (Adressierung)
Die Adressierung von Objekten erfolgt über den PIMLPATH. Ebenen werden durch die Sequenz **Viertelgeviertstrich** (`-`, `U+2010`) und **Mittelpunkt** (`·`, `U+00B7`) getrennt.

## 4. Konditionale Konstrukte
PIML nutzt eine ternäre Logik:
* **Bedingung:** Eingeschlossen in `¿` (U+00BF) und `?` (U+003F).
* **Else-Block:** Eingeschlossen in `„` (U+201E) und `“` (U+201C).
* **Trenner:** Alle Elemente werden durch ein **NBSP** (`U+00A0`) separiert.

## 5. Beispiel
   Result ¿Setup-·Enable? On „Off“
   
## 6. Formale Syntax (BNF-Stil)

$$
\begin{aligned}
\text{PIML\_Doc} & \rightarrow \{ \text{Body} + [ \text{Separator} + \text{Body} ] \} \\
\text{Separator} & \rightarrow \text{"…"} + \text{LF} \\
\text{Header} & \rightarrow \text{Tab}^n + \text{Name} + \text{"—"} + \text{LF} \\
\text{DataLine} & \rightarrow \text{Tab}^n + \text{"   "} + \text{Key} + \text{"\u00A0"} + \text{Value} + \text{LF} \\
\text{Comment} & \rightarrow \text{Tab}^n + \text{"¶"} + \text{Tab} + \text{" "} + \text{Text} + \text{LF}
\end{aligned}
$$

…

## 7. Referenzbeispiel (v1.5)

```text
¶	 Erster logischer Block
Metadaten—
   Author Peter
   Version 1.5
…
¶	 Zweiter logischer Block, getrennt durch Ellipsis
Inhalt—
	Kapitel_1—
	   Titel Der_Anfang
	   Seiten 42
