s = input("Enter a string: ")
freq = [0] * 26
# print(freq)

for i in s:
    freq[ord(i) - 97] += 1

# print(freq)
x = freq.index(max(freq))
print(chr(97+x))
