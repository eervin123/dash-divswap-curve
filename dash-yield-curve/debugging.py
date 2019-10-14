with open("/Users/ericervin/Documents/Coding/dash-yield-curve/app.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)