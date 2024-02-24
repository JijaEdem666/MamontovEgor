melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}
s = ""
for elem in melt:
    if elem.find('O') > 0:
        s += str(melt[elem]) + " "
print(s)