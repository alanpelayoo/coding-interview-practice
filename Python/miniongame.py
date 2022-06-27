#Code passed test excep optimization tests

def minion_game(string):
    # your code goes here
    vowels = ["A","E","I","O","U"]
    i=0
    kevin_w ={}
    stuart_w ={}

    count_k =0
    count_s = 0

    for letter in string:
        Kevin = False
        Stuart = False
        subs=""
        
        if (letter in vowels):
            Kevin = True
           
        elif (letter not in vowels):
            Stuart = True

        for other_string in string[i:]: #We take only the resting part of string
            subs = subs+other_string
            
            if Kevin == True:
                if subs not in kevin_w:
                    kevin_w[subs]=1
                elif subs in kevin_w:
                    kevin_w[subs]=1 +kevin_w[subs]

            elif Stuart == True:
                if subs not in stuart_w:
                    stuart_w[subs] = 1
                elif subs in stuart_w:
                    stuart_w[subs] = 1 +stuart_w[subs]

            
        i+=1
    for kevin in kevin_w:
        count_k = count_k +kevin_w[kevin]

    for stuart in stuart_w:
        count_s = count_s +stuart_w[stuart]
    
    if count_k > count_s:
        print("Kevin " + str(count_k))
    elif count_s > count_k:
        print("Stuart " + str(count_s))
    else:
        print("Draw")
            

if __name__ == '__main__':
    s = input()
    minion_game(s)