def permutation(inputS, result, count, level):
    
    if(level == len(inputS)):
        #print the result
        for i in range(len(result)):
            print(result[i], end = "")
        print()
        return
    else:
        for i in range(len(inputS)):
            if count[i] == 0:
                continue
            else:
                result[level] = inputS[i]
                count[i] -= 1
                permutation(inputS, result, count, level + 1)
                count[i] += 1


inputS = input()
#print(inputS)
result = [0 for i in range(len(inputS))]
#print(result)
##count = []
count = [1 for i in range(len(inputS))]
##for i in range(len(inputS)):
##    count.append(1)
#print(count)

                
##inputS = "abc"
##result = [0,0,0]
##count = [1,1,1]
permutation(inputS, result, count, 0)




##def printPermutationsHelper(s, output):
##    length = len(s)
##    if length==0:
##        print(output)
##        return
##    for i in range(0, length):
##        printPermutationsHelper(s[0:i] + s[i+1:], output + s[i])
##
##def printPermutations(s):
##    printPermutationsHelper(s,"")
##    # Main
##s = input()
##printPermutations(s)









    
