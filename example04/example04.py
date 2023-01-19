# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('text1.txt', 'r', encoding= 'utf-8') as text:
    s = text.readline()
print(s)

def encode(s):
 
    encoding = "" 
 
    i = 0
    while i < len(s):
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding  

print(encode(s))

data = open('text2.txt', 'w')
data.writelines(encode(s))
data.close()