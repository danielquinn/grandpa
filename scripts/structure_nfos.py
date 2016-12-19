#!/usr/bin/env python3

import json
import os

nfos = os.path.join("..", "resources", "nfo")

output = {}
for nfo in os.listdir(nfos):
    with open(os.path.join(nfos, nfo)) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line in output:
                raise Exception("Duplicate line in {}: {}".format(nfo, line))
            output[line] = int(nfo.replace(".nfo", ""))

with open(os.path.join("..", "htdocs", "js", "search.js"), "w") as f:
    f.write('document.grandpa = {{"index": {}}}'.format(
        json.dumps(output, sort_keys=True)
    ))
