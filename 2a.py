safe = 0
for i, report in enumerate(open("2.txt")):
    levels = [int(x) for x in report.strip().split(" ")]
    
    direction = "down" if levels[0] > levels[1] else "up"

    prev = levels[0]
    is_unsafe = False
    for level in levels[1:]:
        if direction == "down" and prev <= level:
            is_unsafe = True
            break
        elif direction == "up" and prev >= level:
            is_unsafe = True
            break
        if abs(prev - level) > 3:
            is_unsafe = True
            break
        prev = level

    if not is_unsafe:
        safe += 1

print(safe)
