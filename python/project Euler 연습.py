largestPrimeFactor = 0
n = 600851475143

for i in range(2, n+1):
    # 먼저 n의 약수인지 확인하고,
    if n % i == 0:
        # n의 약수가 맞으면 소수인지 확인함
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                largestPrimeFactor = j


print(largestPrimeFactor)