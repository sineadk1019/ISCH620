import random

#This function randomly generates a list. I have modified with the version in 
# the professors example because my original attempt wasn't random.
def random_gen(seed_val):
    list_a = []
    random.seed(seed_val)  # Set the seed to ensure reproducibility
    while len(list_a) <60:
        val = random.randrange(1, 120)
        if val not in list_a:
            list_a.append(val)
    return list_a

#assign the function to a variable to use in the sorting functions. 
list_a = random_gen(60)

#Merge Sorted
def list_sort_2():
    full_list = list_a.copy()
    def merge(list_1, list_2, compare):
        result= []
        i,j = 0,0
        while i< len(list_1) and j < len(list_2):
            if compare(list_1[i], list_2[j]):
                result.append(list_1[i])
                i+=1
            else:
                result.append(list_2[j])
                j+=1 
        while (i<len(list_1)):
            result.append(list_1[i])
            i+=1
        while (j< len(list_2)):
            result.append(list_2[j])
            j+=1
        return result
      
    def merge_sort(full_list, compare = lambda x, y: x<y):
        if len(full_list)<2:
            return full_list[:]
        else:
            middle = len(full_list)//2
            list_1 = merge_sort (full_list[:middle], compare)
            list_2 = merge_sort(full_list[middle:], compare)
            return merge(list_1, list_2, compare)
    print(merge_sort(full_list))

    
list_sort_2()
# full_merge = merge_sort()
# print(full_merge)

# def merge_sort(list_1, list_2, lambda x,y : x<y):
        
    
    # def merge_sort(): 
    # while len(full_bsort) < len(list_a):
    #    if x in list_1 >= y in list_2:
    #        full_bsort.append(x)
    #    if y in list_2 >= x in list_1:
    #        full_bsort.append(y)
