def pascal_triangle_row(n):
    n = n - 1
    row = [1]
    for _ in range(n):
        row = [x + y for x, y in zip(row + [0], [0] + row)]
    return row


# Example usage
n = 4
print(pascal_triangle_row(n))
