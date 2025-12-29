s = "hey there how are you! Hope you'r Doing great stuff in your life"

print(s.capitalize())

count=0

for i in range(0,len(s)):
    if s[i]==' ':
        count=count+1

print(count)