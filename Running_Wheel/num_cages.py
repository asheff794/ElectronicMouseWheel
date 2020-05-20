def num_cages():
    import sys
    ncages=int(input('Enter the number of cages: '))
    
    if 1<=ncages<=12:
        return ncages
    else:
       print('Please enter a number between 1 and 12 \n')