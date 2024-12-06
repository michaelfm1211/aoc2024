rules, updates = open("5.txt").read().split("\n\n")

g = {} # g[pg] contains all dependents of pg
for rule in rules.split("\n"):
    a, b = rule.split("|")
    if a not in g:
        g[a] = set([b])
    else:
        g[a].add(b)

middle_sum = 0
for update in updates.split("\n")[:-1]: # :-1 to get rid of blank line
    pages = update.split(",")

    is_ordered = True
    unprinted = set(pages)
    for page in pages:
        if page in g and not g[page].intersection(pages).issubset(unprinted):
            is_ordered = False
            break
        unprinted.remove(page)
    if not is_ordered:
        continue

    # find middle
    middle_sum += int(pages[len(pages) // 2])

print(middle_sum)
