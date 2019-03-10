##def leftRotate(arr, d, n):  
##    if(d == 0 or d == n):  
##        return;  
##    i = d  
##    j = n - d  
##    while (i != j):  
##          
##        if(i < j): 
##            swap(arr, d - i, d + j - i, i)  
##            j -= i  
##          
##        else:  
##            swap(arr, d - i, d, j)  
##            i -= j  
##      
##    swap(arr, d - i, d, i) 



def rotate(arr,n):
    x=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=x;
