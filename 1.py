string=input()
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels=vowels+1

print(2**vowels)