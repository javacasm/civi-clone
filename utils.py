v = 0.1
print(f'{__name__} v{v}')

def cartessian_to_isometric(x,y):
    iso_x = x - y
    iso_y = (x + y)/2
    return iso_x, iso_y
