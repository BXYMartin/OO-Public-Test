import os, sys

dirs = os.listdir('./runtime/')
comp = {}
error=False
for f in dirs:
    if f[0] == '.':
        continue
    name=os.path.splitext(f)[0]
    if not f.endswith(".res"):
        if f.endswith(".err"):
            with open("./runtime/" + f, "r") as err:
                lines = err.readlines()
            if len(lines) != 0:
                error=True
                print(name + " ERROR: Runtime Error Occurred!")
                for line in lines:
                    print(line, end="")
        continue
    with open("./runtime/" + f, "r") as reader:
        lines = reader.readlines()
    i = 1
    for line in lines:
        if i not in comp:
            comp[i] = {}
        if line not in comp[i]:
            comp[i][line] = []
        comp[i][line].append(name)
        i=i+1

useful=0
for key, value in comp.items():
    if len(value) != 1:
        print("[!] FAILED On Line " + str(key))
        for line, names in value.items():
            print("[!] ERROR: Line " + str(key) + " {" + line.strip() + "} -> " + str(names))
        sys.exit(key)
    for line, names in value.items():
        if not line.startswith("Failed"):
            useful=useful+1
            break

print("[i]  INFO:\t Useful Lines Count " + str(useful) + "/" + str(len(comp)))
if error:
    sys.exit(1)
sys.exit(0)
