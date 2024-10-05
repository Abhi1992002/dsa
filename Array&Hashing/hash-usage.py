names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

# Creating a map to store the count of each name
counts = {}

for name in names:
    if name in counts: # checking if the name is already exist as key in the map
        counts[name] += 1
    else:
        counts[name] = 1

print(counts)
