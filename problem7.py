lines = []

while True:
    line = input("Enter a line (or 'q' to quit): ")
    if line == 'q':
        break
    lines.append(line.upper())

print("\n".join(lines))