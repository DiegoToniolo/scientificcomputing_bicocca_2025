f = open("README.md")
for l in f:
    if "Diego" in l:
        break
else:
    f.close()
    raise ValueError()
f.close()