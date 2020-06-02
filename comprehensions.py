
my_numbers = [1, 2, 3, 4, 5, 6, 7]

print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

mapped_list = [i*100 for i in my_numbers]

print("--------------")
print("MAPPED LIST:", mapped_list)

filtered_list = [i for i in my_numbers if i > 3]

print("--------------")
print("FILTERED LIST W/ MATCHES:", filtered_list)

no_match = [i for i in my_numbers if i > 7]

print("--------------")
print("FILTERED LIST W/O MATCHES:", no_match)

mapped_filtered = [i*100 for i in my_numbers if i > 3]

print("--------------")
print("MAPPED AND FILTERED LIST:", mapped_filtered)


#--------------
#ORIGINAL LIST: [1, 2, 3, 4, 5, 6, 7]
#--------------
#TOTAL COMPREHENSION...
#--------------
#MAPPED LIST: [100, 200, 300, 400, 500, 600, 700]
#--------------
#FILTERED LIST W/ MATCHES: [4, 5, 6, 7]
#--------------
#FILTERED LIST W/O MATCHES: []
#--------------
#MAPPED AND FILTERED LIST: [400, 500, 600, 700]
