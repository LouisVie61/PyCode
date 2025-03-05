# after make some experiments, I observed that the new outline follow some rules that suitable for me to exploit
# then do the thing below

def numberOfCeils(n: int) -> int:
    if n == 1:
        return 1

    noOfCeils = 1
    for i in range(1, n):
        noOfCeils += (4 * i)

    return noOfCeils

test = 4
expectedOutput = 25

result = numberOfCeils(test)
if result != expectedOutput:
    print("Fail")
else:
    print("Pass")