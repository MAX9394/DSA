a = [1,2,3,4,5,6]

n = len(a)
l, r = 0, n-1

def reversed_array(a,l,r):
    if l < r:
        a[l], a[r] = a[r], a[l]
        return reversed_array(a,l+1,r-1)
    else:
        return a

print(reversed_array(a,l,r))