
def convert(x):
    count = 0
    label = ''
    
    if x < 1000:
        return x, label

    while x / 1000 >= 1000:
        print('injaaaa')
        x /= 1000
        count += 1

    if count == 0:
        label = 'k'

    elif count == 1:
        label = 'M'

    else:
        label = "B"

    x /= 1000
    
    return x, label


x = 100


new_x, label = convert(x)

print(f'{new_x:.1f} {label}')