# Static list for testing
fg1 = ['sea', 'blue', 'sky', 'water']
fg2 = ['python', 'blue', 'sky']

# Compare FrameGlasses
def compare_frameglasses(fg1, fg2):
    # Number of tags common to fg1 and fg2
    intOfList = list(set(fg1) & set(fg2))
    len3 = len(intOfList)

    # Number of tags in fg1 but not in fg2
    len1 = len(fg1) - len3

    # Number of tags in fg2 but not in fg1
    len2 = len(fg2) - len3
    
    # Temporary List
    tmpList = []
    tmpList.append(len1)
    tmpList.append(len2)
    tmpList.append(len3)
    tmpList.sort()

    # Return the local satisfaction score
    #return(min(tmpList))
    print(min(tmpList))

# To be removed later
compare_frameglasses(fg1, fg2)
