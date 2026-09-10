arr = "cabd"
print("Inside the first loop")

ans = []
for i in range(1, len(arr) + 1):
    for j in range(len(arr) - i + 1): 
        ans.append(arr[j:j + i])

 

print("Inside the second loop")

answer = []
for i in range(len(arr)):
    for j in range(i + 1,(len(arr)) + 1):
        answer.append(arr[i:j])
        
        
        

