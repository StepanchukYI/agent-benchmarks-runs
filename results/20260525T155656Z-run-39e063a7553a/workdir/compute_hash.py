import hashlib

# The 5 confirmed pairs from the regional verification panel
pairs = [
    ("Northhollow", "1992-04-17"),
    ("Otherwick", "1995-09-22"),
    ("Penrith", "2001-02-08"),
    ("Quenwick", "2014-11-30"),
    ("Riverstone", "2020-06-14")
]

# Sort alphabetically by entity name
pairs.sort(key=lambda x: x[0])

# Join with | separator
joined = "|".join([f"{entity}={value}" for entity, value in pairs])

print(f"Joined string: {joined}")
print(f"SHA-1: {hashlib.sha1(joined.encode('utf-8')).hexdigest()}")
