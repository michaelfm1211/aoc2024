from collections import deque

# rules, updates = open("5test.txt").read().split("\n\n")
rules, updates = open("5.txt").read().split("\n\n")

# construct graph
g = {} # g[pg] contains all dependents of pg
for rule in rules.split("\n"):
    a, b = rule.split("|")
    if a not in g:
        g[a] = set([b])
    else:
        g[a].add(b)

# find topologically unsorted
unsorted = []
for update in updates.split("\n")[:-1]: # :-1 to get rid of blank line
    pages = update.split(",")

    unprinted = set(pages)
    for page in pages:
        if page in g and not g[page].intersection(pages).issubset(unprinted):
            unsorted.append(pages)
            break
        unprinted.remove(page)

# do topological sort
topo_sorted = []
for pages in unsorted:
    g1 = {k: [v for v in g[k] if v in pages] for k in g if k in pages}
    for pg in list(g1.keys()):
        if len(g1[pg]) == 0:
            del g1[pg]

    topo_sorted.append([])
    unseen = set(pages)
    while unseen:
        def visit(n):
            if n not in unseen:
                return
            unseen.remove(n)
            if n in g1:
                for adj in g1[n]:
                    visit(adj)
            topo_sorted[-1].append(n)
        visit(next(iter(unseen)))

middle_sum = 0
for pages in topo_sorted:
    middle_sum += int(pages[len(pages) // 2])
print(middle_sum)
