def conv_alliance(a):
    if a == "red":
        return 0
    if a == "blue":
        return 1
    assert False

with open("iri_matches.csv", "r") as f:
    f.readline() # skip headers
    steps = []
    all_steps = []
    meta = []
    match_number = -1
    team_number = -1
    while True:
        line = f.readline()
        if not line:
            break
        x = line.split(",")
        m = int(x[0])
        if m != match_number:
            match_number = m
            team_number = -1
        t = int(x[1])
        if t != team_number:
            team_number = t
            all_steps.append(steps)
            steps = []
            new = (match_number, team_number, conv_alliance(x[2]), int(x[3]), float(x[7]))
            print(new)
            meta.append(new)
        steps.append((float(x[5]), float(x[6]), int(x[8])))

with open("iri_matches.dat", "wb") as f:
    a = bytearray()
    a.append()
    f.write()
