import time
import re
import sys
import argparse

class PIML_Parser:
    def __init__(self, path):
        self.path = path
        self.C = {
            'EM': '\u2014', 'ELL': '\u2026', 'NBSP': '\u00A0',
            'PIL': '\u00B6', 'HD': '\u2013', 'DOT': '\u00B7',
            'HYP': '\u2010', 'INV_Q': '\u00BF', 'OPEN': '\u201E', 'CLOSE': '\u201C'
        }

    def fail(self, ln):
        print(f"{ln} FALSCH!")
        sys.exit(1)

    def parse(self):
        try:
            with open(self.path, 'rb') as f:
                raw = f.read().decode('utf-8')
        except FileNotFoundError:
            print(f"Fehler: Datei '{self.path}' nicht gefunden.")
            sys.exit(1)
        except Exception as e:
            print(f"Fehler beim Lesen: {e}")
            sys.exit(1)

        # Schritt 1: Bereinigung physischer Zeilenfortsetzungen (\n -> Flow)
        content = raw.replace('\n', ' ')
        
        # Schritt 2: Splitten bei strukturellen Enden (\r oder Doppel-Space)
        logical_lines = re.split(r'\r|  ', content)
        
        line_counter = 0
        for raw_line in logical_lines:
            # Strippe nur die \n Reste, falls vorhanden
            line = raw_line.strip('\n')
            if not line or line.isspace(): continue
            line_counter += 1
            
            # Sektions-Trenner
            if line.strip() == self.C['ELL']:
                time.sleep(0.338)
                continue

            tabs = 0
            while tabs < len(line) and line[tabs] == '\t': tabs += 1
            rest = line[tabs:]

            # Header
            if self.C['EM'] in rest:
                if not rest.endswith(self.C['EM']): self.fail(line_counter)
                continue

            # Kommentar
            if rest.startswith(self.C['PIL']):
                if not rest.startswith(f"{self.C['PIL']}\t "): self.fail(line_counter)
                continue

            # Datenzeilen
            if rest.startswith("   "):
                if self.C['NBSP'] not in rest: self.fail(line_counter)
                _, val = rest[3:].split(self.C['NBSP'], 1)

                # Konditional (¿PATH? NBSP TRUE NBSP „FALSE“)
                if val.startswith(self.C['INV_Q']):
                    path_regex = fr'[^{self.C["HYP"]}{self.C["DOT"]}]+(?:{self.C["HYP"]}{self.C["DOT"]}[^{self.C["HYP"]}{self.C["DOT"]}]+)*'
                    p = fr'^{self.C["INV_Q"]}{path_regex}\?\u00A0.+\u00A0{self.C["OPEN"]}.+{self.C["CLOSE"]}$'
                    if not re.match(p, val): self.fail(line_counter)
                
                # Vektorielle Ranges (Asc: –· | Desc: ·–)
                elif self.C['HD'] in val:
                    asc_p = fr'^.+{self.C["HD"]}{self.C["DOT"]}.+$'
                    desc_p = fr'^.+{self.C["DOT"]}{self.C["HD"]}.+$'
                    if not (re.match(asc_p, val) or re.match(desc_p, val)):
                        self.fail(line_counter)
                continue

            self.fail(line_counter)
        
        print("PIML KONFORM")

def main():
    parser = argparse.ArgumentParser(
        description="Pedantischer PIML v2.3 Verifikator.",
        add_help=False
    )
    parser.add_argument('file', nargs='?', help="Die zu prüfende .piml Datei")
    parser.add_argument('-h', '--help', action='store_true', help="Zeigt diese Hilfe")

    args = parser.parse_args()

    if args.help or not args.file:
        print("""
PIML v2.3 Verifikator - HILFE
=============================
Verwendung: python piml_parser.py <DATEI>

Regeln:
- Header enden auf EM-DASH (—)
- Sektions-Trenner (…) erzwingen 338ms Pause
- Datenzeilen: 3 Leerzeichen Einrückung, NBSP als Separator
- Zeilenende: \\r oder Doppel-Leerzeichen (0x20 0x20)
- Vektorielle Ranges:
    Start–·Ende (Aufsteigend/Ziel-Fokus)
    Start·–Ende (Absteigend/Ursprung-Fokus)

Fehlermeldung: <Zeilennummer> FALSCH!
""")
        sys.exit(0)

    piml = PIML_Parser(args.file)
    piml.parse()

if __name__ == "__main__":
    main()

