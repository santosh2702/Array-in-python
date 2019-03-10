def maxSum(arr):
    arrSum=0
    currVal=0
    n=len(arr)
    for i in range(0,n):
        arrSum=arrSum+arr[i]
        currVal=currVal+(i*arr[i])
    maxVal=currVal

    for j in range(1,n):
        currVal=currVal+arrSum-n*arr[n-j]
        if currVal>maxVal:
            maxVal=currVal

    return maxVal
arr=[1,20,2,10]
print ("MAx sum is:",maxSum(arr))
