#Code passed test excep optimization tests
#Optimized, only focuse on outputing the output no extra diccionaries
#With these method we are counting each occurrance, iterating all over the string, so adding an extra letter ath the end will increase two extra points.

def minion_game(string):
    # your code goes here
    vowels = ["A","E","I","O","U"]
    i=0
    count_k =0
    count_s = 0
    for letter in string:
        
        Kevin = False
        Stuart = False
        if (letter in vowels):
            Kevin = True
           
        elif (letter not in vowels):
            Stuart = True

        for other_string in string[i:]: #We take only the resting part of string
            if Kevin == True:
                count_k = count_k +1
    
            elif Stuart == True:
                
                count_s = count_s +1
        i+=1
    if count_k > count_s:
        print("Kevin " + str(count_k))
    elif count_s > count_k:
        print("Stuart " + str(count_s))
    else:
        print("Draw")
            

if __name__ == '__main__':
    s = "BANANAS"
    minion_game(s)
