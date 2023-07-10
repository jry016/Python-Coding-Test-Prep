# KATTIS CODING TEST PROBLEMS
# Sideways Sorting
# https://open.kattis.com/problems/sidewayssorting

inputs = []
results = []

while True:
    row, col = map(int, input().split())
    if row == 0 and col == 0:
        break
    
    for _ in range(row):
        line = input().strip() # remove any leading or trailing whitespace characters
        inputs.append(line)

    # Transpose the grid
    transposed_grid = ["".join(col) for col in zip(*grid)]

    # Sort the transposed grid lexicographically
    sorted_grid = sorted(transposed_grid)

    # Transpose the sorted grid back
    result = ["".join(row) for row in zip(*sorted_grid)]

    # Print the result
    for line in result:
        print(line)
     
    print()  # Add a blank line between outputs
