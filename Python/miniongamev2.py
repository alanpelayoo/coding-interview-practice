#Code passed test excep optimization tests
#Optimized, with these code we are not doing the nessting iteration. reducinge time.
#NESTED LOOPS NOT REQUIRED "If you're looping through the string multiple times, think about how you can derive the answer mathematically, rather than checking every possible iteration."

def minion_game(string):
    # your code goes here
    vowels = ["A","E","I","O","U"]
    i=0
    count_k =0
    count_s = 0
    for letter in string:
        if (letter in vowels):
            count_k = len(string)-i + count_k

        elif (letter not in vowels):
            count_s = len(string)-i + count_s
        i+=1
    if count_k > count_s:
        print("Kevin " + str(count_k))
    elif count_s > count_k:
        print("Stuart " + str(count_s))
    else:
        print("Draw")
            

if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)
