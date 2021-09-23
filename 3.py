n=input().split()
razi=0
khos=0
for item in n:
    if int(item) >= 80:
        khos+=1
        razi+=1
if khos>=3:
    print("Mamma mia!")
elif razi>=1 and razi<=2:
    print("Mamma mia!!")
else:print("Mamma mia!!!")
# 70 80 90 10 95  Mamma mia!


  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
