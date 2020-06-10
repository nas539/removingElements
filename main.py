import numpy as np

html = ["<h1>", "Some content", "</h1>"]
html2 = ["<h1>", "Some content", "more", "</h1>"]

def remove_first_and_last(some_list):
    index1 = [0]
    some_list = np.delete(some_list, index1).tolist()
    some_list = some_list[::-1] 
    some_list = np.delete(some_list, index1).tolist() 
    return some_list   

print(remove_first_and_last(html))
print(remove_first_and_last(html2))