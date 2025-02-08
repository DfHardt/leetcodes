def isPalindrome(x: int | str) -> bool:
    x = str(x)
    a = range(0, len(x[:len(x)//2]))
    b = range(len(x) - 1, len(x) // 2 - 1, -1)
    auxi, auxj = [], []
    for i,j in zip(a, b):
        auxi.append(x[i])
        auxj.append(x[j])
    if auxi == auxj:
        return True
    return False

print(isPalindrome(-1))
