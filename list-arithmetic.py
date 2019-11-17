#arithmetic_list = [ 14, 7, 14 ]
#arithmetic_list = [ 4, 4, 4, 2/3, 1/3, 5, 13 ]
arithmetic_list = [-5, -5, 5, 5, -15]


for index in range (2, len(arithmetic_list)):
    print 'the index is %s' %(index)
    final_right_total = 0

    
    for right_index in range (index + 1, len(arithmetic_list)):
        final_right_total = final_right_total + arithmetic_list[right_index]
        print 'the right total so far from index %s to index %s is %s'%(right_index, len(arithmetic_list), final_right_total)


    final_left_total = 0 

        
    for left_index in range (0, index):
        final_left_total = final_left_total + arithmetic_list[left_index]
        print ' the left total so far from index 0 to index %s is %s'% (left_index, final_left_total)
    print 'comparing %s to %s to see if they are the same'%(final_right_total, final_left_total)
    if final_left_total == final_right_total:
        print ' the artihmetic medium is at the index %s'%(index)
            

