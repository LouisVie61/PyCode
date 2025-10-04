def calculate_chicken_and_dog(total: int, totalLegs: int):
    if total < 0 or totalLegs < 0 or totalLegs % 2 != 0:
        return []

    dog = (totalLegs - 2 * total) // 2
    chicken = total - dog

    if dog < 0 or chicken < 0:
        return []
    return [dog, chicken]

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    result = calculate_chicken_and_dog(n, m)

    if not result or (result[0] + result[1] != n or 4 * result[0] + 2 * result[1] != m):
        print("invalid")
    else:
        print(f"dog: {result[0]}, chicken: {result[1]}")
