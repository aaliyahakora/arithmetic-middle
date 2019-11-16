arithmetic_list = [ 4, 7, 5, 1, 9, 3, 11 ]

index = 2
left_index = 0
left_total = 0


while index < 7:
    for left_index in range (0, index-1):
        left_total = left_total + arithmetic_list[left_index]
        print left_total
        
    index = index + 1

    

