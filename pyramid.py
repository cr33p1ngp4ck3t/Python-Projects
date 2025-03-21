def draw_pyramid(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

rows=input("How many Rows do you want in your Pyramid?")
draw_pyramid(rows)
