#!/usr/bin/env python3
import json, sys, os

ROOT = os.path.dirname(os.path.dirname(__file__))
GOLDEN = os.path.join(ROOT, "tests", "outputs", "golden")

def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)

def walk_json_files(base):
    for dirpath, _, filenames in os.walk(base):
        for fn in filenames:
            if fn.lower().endswith(".json"):
                yield os.path.join(dirpath, fn)

def main():
    count = 0
    for path in walk_json_files(GOLDEN):
        try:
            with open(path, "r", encoding="utf-8") as f:
                json.load(f)
            count += 1
        except Exception as e:
            fail(f"Invalid JSON: {path}: {e}")
    print(f"SUCCESS: {count} golden JSON files validated OK")

if __name__ == "__main__":
    if not os.path.isdir(GOLDEN):
        print(f"INFO: No golden folder at: {GOLDEN}")
        sys.exit(0)
    main()