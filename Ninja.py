def solution(tuple_of_test_cases):
    pass
    """ This function returns the number of platforms that need to be moved"""
    final_stones = ""  # to count number of stones being moved
    for k in range(len(tuple_of_test_cases)-1):
        N = tuple_of_test_cases[k][0]
        J = tuple_of_test_cases[k][1]
        D = list(tuple_of_test_cases[k][2])
        S = sum(D)
        stones = 0
        if S > J*(N+1):
            pass

        elif max(D) <= J:
            pass

        else:
        
            
            stones = 0
            i = 1
        
            while i != -1:
                if max(D) > J:
                    if D.index(max(D)) == 0:
                        D_temp = D[:]
                        stones += 1 # counting number of moves
                        D_temp[D_temp.index(max(D_temp))] -= max(D_temp)- J
                        D_temp[D.index(max(D))+1] += max(D)- J 
                        D = D_temp[:]
                        

                    elif  D.index(max(D)) == len(D)-1:
                        D_temp = D[:]
                        stones += 1 # counting number of moves
                        D_temp[D_temp.index(max(D_temp))] -= max(D_temp)- J
                        D_temp[D.index(max(D))-1] += max(D)- J
                        D = D_temp[:]
                        

                    elif   ((D.index(max(D))+i) <= (len(D)-1)) & ((D.index(max(D))-i) >= 0):
                        if D[D.index(max(D))+i] > D[D.index(max(D))-i]:
                            D_temp = D[:]
                            stones += 1 # counting number of moves
                            D_temp[D_temp.index(max(D_temp))] -= max(D_temp)- J
                            D_temp[D.index(max(D))-1] += max(D)- J
                            D = D_temp[:]
                            i -= 1
                            

                        elif D[D.index(max(D))+i] < D[D.index(max(D))-i]:
                            D_temp = D[:]
                            stones += 1 # counting number of moves
                            D_temp[D_temp.index(max(D_temp))] -= max(D_temp)- J
                            D_temp[D.index(max(D))+1] += max(D)- J
                            D = D_temp[:]
                            i -=1
                            
                
                        elif  ((D.index(max(D))+i) <= (len(D)-1)) & ((D.index(max(D))-i) <= 0):
                            D_temp = D[:]
                            stones += 1 # counting number of moves
                            D_temp[D_temp.index(max(D_temp))] -= max(D_temp)- J
                            D_temp[D.index(max(D))+1] += max(D)- J
                            D = D_temp[:]
                            i -= 1
                            
                                   
                        elif  ((D.index(max(D))+i) >= (len(D)-1)) & ((D.index(max(D))-i) >= 0):
                            D_temp = D[:]
                            stones += 1 # counting number of moves
                            D_temp[D_temp.index(max(D_temp))] -= max(D_temp)- J
                            D_temp[D.index(max(D))-1] += max(D)- J
                            D = D_temp[:]
                            i -=1
                            
                                                
                        else:
                            i +=1
                
                    else:
                        i += 1
                    
                else:
                    i = -1
                    
    
            
        final_stones += str(stones)
    return str(final_stones)  # change to return