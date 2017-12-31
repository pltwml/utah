print('if statement')
# x = int(input("Number: "))
x = 0
if x > 0:
    print("Positive")

elif x == 0:
    print('Zero')

else:
    print("Negative")

''' loops '''
print('\n loops \n')

# Iterable list
words = ['one', 'two', 'three']

for i in words:
    print(i)

''' range '''

print("\n range() \n")

for i in range(5):
    print(i)

'''range() returns a referenceable object rather than a list'''
l = range(5)

print(list(range(5)))
print(l[0])

''' break in for '''
print('break in for loop\n')

for i in range(5):
    for k in range(2, 5):
        if i % k == 0:
            print("break: ", i, "%", k, " == 0")
            break
    else:
        print("break:  not occurred")
