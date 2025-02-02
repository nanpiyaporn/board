def linear_search(list, target):
    """ 
    Return the index postition of the target
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print ( " Target on the list")
    else:
         print ( " Target is noton the list")

X1 = [ 0,1,2,3,4,5,6,7,8,9,10]

result = linear_search(X1, 10)
verify(result)