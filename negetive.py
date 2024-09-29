arr1 = [-5,3,-2,-7,5,-7,-3,-1,4,3]
arr2 = [5,2,6,3,9,7,5,2,9]
arr3 = [-3,-4,-2,4,5,-6,-1,-2,4,-6,-7,8]
def fn(arr1):
    st = []
    sum = 0
    for i in arr1:
        if i<0:
            sum += i
        else:
            if sum !=0:
                st.append(sum)
            sum=0
    if sum !=0:
        st.append(sum)

    return min(st) if st else -1

print(fn(arr1))
print(fn(arr2))
print(fn(arr3))
