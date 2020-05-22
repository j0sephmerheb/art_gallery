# Temporary file path
filepath = "simple_file.txt"

# Dictionary Containing the frameglasses
my_dict = {}
sorted_dict = {}



#####################################
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
    return(min(tmpList))
    #print(min(tmpList))
#####################################


#####################################
# Write frameglasses into a text file
def write_frameglasses():
    # Number of frameglasses
    frameglasses_count = str(len(sorted_dict))
    f = open("output.txt", "w")
    f.write(frameglasses_count)
    f.write('\n')
    
    for key in sorted_dict:        
        f.write(key)
        f.write('\n')
    f.close()

#####################################


# Read the sorted file of FrameGlasses
def read_file(filepath):
    # Open the new sorted text file by (L) and (P)
    with open(filepath) as my_txt:        
        # For each line
        for line in my_txt: 
            # Remove line break
            line = line.replace("\n","") 
            
            # Get the ids from the start of the line
            fg_ids = line.split(" ", 1)[0].replace(","," ")

            # Get the tags as a list
            new_list = line.split(" ")
            fg_tags = new_list[1:]

            # Insert into dictionary the key and values
            my_dict[fg_ids] = fg_tags
    #print(my_dict)
    iterate_frameglasses()




# Iterate over dictionary of frameglasses to calculate scores
def iterate_frameglasses():
    while len(my_dict) > 0:
        i = 0

        # First key in the dictionary    
        k1 = list(my_dict)[0]

        # Values/List related to the first key
        fg1 = my_dict[k1]

        # Add the first key/value into a new dictionary, as starting point
        sorted_dict[k1] = fg1

        # Itirate over the dictionary starting from the third element
        i = 1
        score0 = 0
        
        for k in list(my_dict)[i:len(my_dict)]:
            i+=1

            # list/value related to each key in dictionary
            fg_new = my_dict[k]

            # score between list 1 and each new list
            score_new = compare_frameglasses(fg1,fg_new)
            # print("Score between 1 and: " + str(i) + ": " + str(score_new))        

            # if this new score is less than the one we got at first, then we keep
            if score_new > score0:
                score0 = score_new
                # Memorize the new lists and keys
                k2 = k
                fg2 = fg_new
            
            
        # print(" ")
        # print("----------------------")
        # print("Best Score is: " + str(score0))
        # print("Between: ")
        # print(fg1,fg2)
        
        if len(my_dict) == 1:
            sorted_dict[k1] = fg1
            if k1 in my_dict:
                del my_dict[k1]
        else:
            sorted_dict[k2] = fg2            
            del my_dict[k1]
            if k2 in my_dict:     
                del my_dict[k2]

        # print(" ")
        # print("----------------------")
        # print("Old List:")
        # print(my_dict)

        # print(" ")
        # print("----------------------")
        # print("New List:")
        # print(sorted_dict)


    # Write the new sorted dictionary into a text file
    # Remove the tags, keep the IDs, and 
    # Put the total number of lines at the begining of the text
    write_frameglasses()


# Read the sorted file of FrameGlasses
read_file(filepath)


