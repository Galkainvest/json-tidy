#!/usr/bin/env python3
import argparse, json, sys
def read_text(path: str|None) -> str:
    if path:
        with open(path, "r", encoding="utf-8") as f: return f.read()
    if sys.stdin.isatty():
        sys.exit("hint: pass a file or pipe JSON via stdin")
    return sys.stdin.read()

def main(argv=None):
    p = argparse.ArgumentParser(description="Pretty print JSON")
    p.add_argument("file", nargs="?", help="path to JSON file or omit to read stdin")
    p.add_argument("-i", "--indent", type=int, default=2)
    p.add_argument("-s", "--sort-keys", action="store_true")
    args = p.parse_args(argv)
    data = json.loads(read_text(args.file))
    print(json.dumps(data, indent=args.indent, sort_keys=args.sort_keys, ensure_ascii=False))

if __name__ == "__main__":
    main()
