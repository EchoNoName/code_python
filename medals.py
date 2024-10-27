def min_medals(n):
    if n % 4 == 2 and n % 3 == 0 and n <= 18:
        silver = n / 3
        return(0, silver, 0)
    gold = n // 4
    n = n - gold * 4
    silver = n // 3
    n = n - silver * 3
    return(gold, silver, n)

medals = min_medals(6)
print(f"{medals[0]} gold medals, {medals[1]} silver medals, {medals[2]} bronze medals")