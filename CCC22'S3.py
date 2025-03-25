inp = input()
inp = inp.split(' ')
n = int(inp[0])
m = int(inp[1])
k = int(inp[2])

maxK = 0
seq = 1
for i in range(n, n - m, -1):
    maxK += i


result = []
if k < n or k > maxK:
    print('-1')
else:
    if n == k:
        for i in range(n):
            result.append('1')
        result = result
    elif k <= 2 * n - 1:
        for i in range(n):
            result.append('1')
        k -= n
        if k % 2 == 0:
            i = 1
            while k > 0:
                result[i] = '2'
                i += 2
                k -= 2
        else: 
            i = 2
            result[0] = '2'
            k -= 1
            while k > 0:
                result[i] = '2'
                i += 2
                k -= 2
    else:
        sequence = 1
        length = 0
        while True:
            result.append(str(sequence))
            length += 1
            k -= min(length, m)
            sequence += 1
            lockRange = min(length + 1, m)
            if k == n - length:
                sequence -= 1
                break
            elif k - lockRange < n - length - 1:
                difference = k - (n - length - 1)
                sequence = result[-difference]
                result.append(str(sequence))
                length += 1
                break
            else:
                if sequence > m:
                    sequence = 1
        for i in range(n - length):
            result.append(str(sequence))

    s = ' '
    print(s.join(result))