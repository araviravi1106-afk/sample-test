words="aabbbccccddd" 
count=dict()
for l in words:
    if l in count:
        count[l] += 1
    else:
        count[l] = 1
print(count)
      


