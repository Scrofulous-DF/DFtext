import json
import sys
import gzip
import base64

# How to use in vscode if you have your gzipped text.

# Press play it will fail because of wrong args.
# Click in the terminal and press uparrow to get what it runned.
# Add the filename you want, and then past in your gzipped text.

# WhateverVScodeSpitOout test1 H4sIAAAAAAAA/...

def CreateJsonFilefromGzip(filename, gzipped):
    base64_bytes = base64.b64decode(gzipped)
    decompressed_bytes = gzip.decompress(base64_bytes)
    decompressed_text = decompressed_bytes.decode("utf-8")

    jsontext = json.loads(decompressed_text)

    jsontext = json.dumps(jsontext, indent=4)

    with open("JsonForTesting\\" + filename + ".json", "w") as f:
        f.write(jsontext)

if __name__ == "__main__":

    filename = sys.argv[1]
    gzipped = sys.argv[2]

    CreateJsonFilefromGzip(filename, gzipped)