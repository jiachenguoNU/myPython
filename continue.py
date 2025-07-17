nodes = [1, None, 3, None, 5]

for node in nodes:
    if not node:
        continue                    # Skips the rest of the iteration
    print(f'hahaha, {node}')