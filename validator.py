import time
import re
import sys

class PIML_Parser:
    def __init__(self, datei_pfad):
        self.pfad = datei_pfad
        self.C = {
            'EM': '\u2014', 'ELL': '\u2026', 'NBSP': '\u00A0',
            'PIL': '\u00B6', 'HD': '\u2013', 'DOT': '\u00B7',
            'HYP': '\u2010', 'INV_Q': '\u00BF', 'OPEN': '\u201E', 'CLOSE': '\u201C'
        }

    def fail(self, ln):
        """Einziger zulässiger Fehler-Output."""
        print(f"{ln} FALSCH!")
        sys.exit(1)

    def parse(self):
        try:
            with open(self.pfad, 'rb') as f:
                lines = f.read().decode('utf-8').splitlines()
        except Exception:
            sys.exit(1)

        for i, line in enumerate(lines, 1):
            if not line.strip() and not line.startswith('\t'):
                continue
            
            # 1. Meditativer Trenner
            if line == self.C['ELL']:
                time.sleep(0.338)
                continue

            # 2. Hierarchie (Tabs)
            tabs = 0
            while tabs < len(line) and line[tabs] == '\t':
                tabs += 1
            rest = line[tabs:]

            # 3. Header
            if self.C['EM'] in rest:
                if not rest.endswith(self.C['EM']): self.fail(i)
                continue

            # 4. Kommentar
            if rest.startswith(self.C['PIL']):
                if not rest.startswith(f"{self.C['PIL']}\t "): self.fail(i)
                continue

            # 5. Datenzeilen
            if rest.startswith("   "):
                if self.C['NBSP'] not in rest: self.fail(i)
                _, val = rest[3:].split(self.C['NBSP'], 1)

                # A: Konditionale
                if val.startswith(self.C['INV_Q']):
                    path_regex = fr'[^{self.C["HYP"]}{self.C["DOT"]}]+(?:{self.C["HYP"]}{self.C["DOT"]}[^{self.C["HYP"]}{self.C["DOT"]}]+)*'
                    p = fr'^{self.C["INV_Q"]}{path_regex}\?\u00A0.+\u00A0{self.C["OPEN"]}.+{self.C["CLOSE"]}$'
                    if not re.match(p, val): self.fail(i)
                
                # B: Vektorielle Ranges (v2.2 Logik)
                elif self.C['HD'] in val:
                    # Asc: –· (Ziel-Fokus) | Desc: ·– (Ursprung-Fokus)
                    asc_p = fr'^.+{self.C["HD"]}{self.C["DOT"]}.+$'
                    desc_p = fr'^.+{self.C["DOT"]}{self.C["HD"]}.+$'
                    if not (re.match(asc_p, val) or re.match(desc_p, val)):
                        self.fail(i)
                continue

            # Alles andere
            self.fail(i)

        print("PIML KONFORM")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        PIML_Parser(sys.argv[1]).parse()
    else:
        sys.exit(1)
