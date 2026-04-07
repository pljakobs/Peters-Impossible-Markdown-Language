import time
import re
import sys
import argparse

class PIML_Validator:
    def __init__(self, path):
        self.path = path
        self.C = {
            'EM': '\u2014', 'ELL': '\u2026', 'NBSP': '\u00A0',
            'VOID': '\u3000', 'NNBSP': '\u202F',
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
        except Exception:
            sys.exit(1)

        content = raw.replace('\n', ' ')
        logical_lines = re.split(r'\r|  ', content)

        line_idx = 0
        for raw_line in logical_lines:
            line = raw_line.strip('\n')
            if not line or line.isspace(): continue
            line_idx += 1

            if line.strip() == self.C['ELL']:
                time.sleep(0.338)
                continue

            tabs = 0
            while tabs < len(line) and line[tabs] == '\t': tabs += 1
            rest = line[tabs:]

            if self.C['EM'] in rest:
                if not rest.endswith(self.C['EM']): self.fail(line_idx)
                continue

            if rest.startswith("   "):
                if self.C['NBSP'] not in rest: self.fail(line_idx)
                key, val = rest[3:].split(self.C['NBSP'], 1)

                # Null-Indikator Prüfung
                if not val.strip() and val != self.C['VOID']:
                    self.fail(line_idx)

                # Einheiten-Bindung Prüfung (NNBSP)
                symbols = ['€', '$', '%', '¥', '£']
                for sym in symbols:
                    if sym in val:
                        if re.search(r'\d', val) and not re.search(fr'\d{self.C["NNBSP"]}{re.escape(sym)}', val):
                            self.fail(line_idx)

                # Range & Konditional Validierung (Analog v2.2)
                if self.C['HD'] in val:
                    if not (re.search(fr'.+{self.C["HD"]}{self.C["DOT"]}.+', val) or
                            re.search(fr'.+{self.C["DOT"]}{self.C["HD"]}.+', val)):
                        self.fail(line_idx)
                continue

            if not rest.startswith(self.C['PIL']):
                self.fail(line_idx)

        print("PIML KONFORM")

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('file', nargs='?')
    parser.add_argument('-h', '--help', action='store_true')
    args = parser.parse_args()

    if args.help or not args.file:
        print("PIML v2.4 Validator\nVerwendung: python validator.py <DATEI>")
        sys.exit(0)

    PIML_Validator(args.file).parse()

if __name__ == "__main__":
    main()

