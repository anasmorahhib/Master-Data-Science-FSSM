u = input('Enter a number:')
encien = 0
encien2 = 1
for i in range (0, int(u)+1):
    # you can use
    '''nouveau =  encien + encien2
    encien2 = encien
    encien = nouveau'''
    # or
    encien2, encien = encien, (encien + encien2)
    print("u(%d)=%d"%(i,encien2))