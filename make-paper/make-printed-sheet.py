def print_as_grid(ls, row_size:int):
    """Print a list as a grid, with tabs between items."""
    for i in range(0, len(ls), row_size):
        print('\t'.join(ls[i:i+row_size]))

firsts = open('../first3.txt').read().splitlines()
lasts = open('../last3.txt').read().splitlines()

print("FIRSTS")
print_as_grid(firsts, 6 * 6)

print("LASTS")
print_as_grid(lasts, 6 * 6)
