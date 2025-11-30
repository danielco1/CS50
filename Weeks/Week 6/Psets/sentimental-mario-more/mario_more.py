while True:
    height = input("Height: ")
    if height.isdigit():
        height = int(height)
        if 1 <= height <= 8:
            break
for i in range(1, height + 1):
    spaces = " " * (height - i)
    left = "#" * i
    gap = "  " 
    right = "#" * i
    print(spaces + left + gap + right)