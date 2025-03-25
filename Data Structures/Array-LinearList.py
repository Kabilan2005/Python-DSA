
# Exceptions need to be handled wisely

class array():
    def __init__(own):
        own.length=0
        own.data={}
    
    def __str__(own):
        print(own.data.values())
        return str(own.__dict__)
    
    def get(own,index):
        return own.data[index]
    
    def push(own,key):
        own.data[own.length]=key
        own.length+=1

    def pop(own):
        last_item=own.data[own.length-1]
        del own.data[own.length-1]
        own.length-=1
        return last_item

    def insert(own,index,key):
        for i in range(own.length-1,index,-1):
            own.data[i+1]=own.data[i]
        own.data[index]=key
        own.length+=1

    def delete(own,index):
        for i in range(index,own.length-1,1):
            own.data[i]=own.data[i+1]
        del own.data[own.length-1]
        own.length-=1

    def kadane(own):
        # Maximum Subarray Sum
        sum=own.data[0]
        maxEnding=own.data[0]

        for i in range(1,own.length):
            maxEnding=max(maxEnding+own.data[i],own.data[i])
            sum=max(sum,maxEnding)
        
        return sum

arr=array()
arr.push(2)
arr.push(3)
arr.push(-8)
arr.push(7)
arr.push(0)
arr.push(-1)
arr.push(2)
arr.push(3)
print(arr.kadane())
