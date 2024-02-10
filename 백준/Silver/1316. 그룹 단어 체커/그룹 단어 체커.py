n = int(input())

for i in range(n):
    word = input()
    
    for i in range(len(word)-1):
        if word.find(word[i]) > word.find(word[i+1]):
            n -= 1
            break
print(n)