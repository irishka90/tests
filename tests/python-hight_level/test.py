import sys
import re

patter = r"\bcat\b"

for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(patter, line)) > 0:
        print(line)
