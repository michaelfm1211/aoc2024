def is_unsafe(levels):
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
    return is_unsafe

safe = 0
for i, report in enumerate(open("2.txt")):
    levels = [int(x) for x in report.strip().split(" ")]
    if not is_unsafe(levels):
        safe += 1
    else:
        for i in range(len(levels)):
            damp_levels = levels[:i] + levels[i+1:]
            if not is_unsafe(damp_levels):
                safe += 1
                break

print(safe)

