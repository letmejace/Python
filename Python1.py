# Q1

a = 80
b = 75
c = 55

answer = round((a + b + c) / 3)
print(answer)

# Q2

n = 13

if (n % 2):
    print('Even number: 짝수')
else :
    print('Odd number: 홀수')

# Q3

id = '881120-1068234'

result = int(id[:6])
print(result)

# Q4

pin = "881120-1068234"

num = pin[7]

print(num)

# Q5
a = "a:b:c:d"
add = a.replace(':','#')
print(add)

# Q6
num = [1, 3, 5, 4, 2]
num.sort()
num.reverse()
print(num)

# Q7
words = ['Life', 'is', 'too', 'short']
x = " ".join(words)
print(x)

# Q8

a = (1,2,3)
b = 4
new = a + (b,)
print(new)

# Q9

# Q10

a = {'A':90, 'B':80, 'C':70}
element = a.pop('B')
print(element)

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
n = set(a)

print(n)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b) 

