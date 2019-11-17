arithmetic_list = [ 4, 7, 5, 1, 9, 3, 11 ]

index_for_left = 2
index_for_right = 2
left_index = 0
left_total_one = 0
left_total_two = 0
final_left_total = 0
left_amount = 0
right_index = index_for_right+1
right_total_one = 0
right_total_two = 0
final_right_total = 0
right_amount = 0

while index_for_right < 7:
    for right_index in range (index_for_right+1, 7):
        for right_amount in range (index_for_right+1,7):
            final_right_total = final_right_total + arithmetic_list[right_amount]
            print final_right_total
    index_for_right = index_for_right + 1
"""
while index_for_left < 7:
    for left_index in range (0, index_for_left-1):
        for left_amount in range (0, index_for_left-1):
            final_left_total = final_left_total + arithmetic_list[left_amount]
            if final_left_total == final_right_total:
                print arithmetic_list[index]
        
    index_for_left = index_for_left + 1
"""
    

