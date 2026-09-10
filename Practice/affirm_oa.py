def windFarms(premium, x, y):
    n = len(premium)
    total_premium = sum(premium)
    half = total_premium / 2
    
    # weighted median for x
    paired_x = sorted(zip(x, premium))
    running = 0
    cx = paired_x[0][0]
    for coord, p in paired_x:
        running += p
        if running >= half:
            cx = coord
            break
    
    # weighted median for y
    paired_y = sorted(zip(y, premium))
    running = 0
    cy = paired_y[0][0]  # ← was [1] before, this was a bug
    for coord, p in paired_y:
        running += p
        if running >= half:
            cy = coord
            break
    
    total = 0
    for j in range(n):
        distance = abs(x[j] - cx) + abs(y[j] - cy)
        total += premium[j] * distance
    
    return total

x = [1, 3, 2, 4] 
y = [1, 2, 3, 4] 
premium = [1, 3, 2, 4]
print(windFarms(premium, x, y))