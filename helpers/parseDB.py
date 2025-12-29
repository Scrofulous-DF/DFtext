import json

out = 10000000

line = 1

dict = {}

with open("helpers\\db.json", "r", encoding="utf-8") as f:

    j = json.load(f)

    for codeblock in j["codeblocks"]:
        dict[codeblock["name"]] = []

    for action in j["actions"]:
        dict[action["codeblockName"].strip()].append(action["name"].strip())

    print(json.dumps(dict, indent=4))

    # for i in range(out):
    #     char = f.read(1)

    #     print(char, end="")

    #     if char == "\n":
    #         line += 1
    #         print("|",line,"|", end="")
            

