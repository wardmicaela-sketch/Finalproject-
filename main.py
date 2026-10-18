raw_names = ["  john smith  ", "MARY JONES", "", "bob miller", "   ", "SARAH davis", "  amy chen  "]

clean = []

for name in raw_names:
    trimmed_name = name.strip()             # remove leading/trailing spaces
    if trimmed_name != "":                  # skip blank entries
        clean.append(trimmed_name.title())  # add the cleaned, title-cased name

print(clean)