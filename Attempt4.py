
def vaildation():
    ans = None
    while ans != "Y" or ans != "N":
        ans = input("""Hello User. Today I have a very simple question for you.
         Are you smart? If the answer is Yes, then type the upper letter Y. If it is No, then type the upper letter N.""")
        if ans == "Y":
            print ("Hmm, okay then. Sure I guess. Narcissist.")
        elif ans == "N":
            print ("WOW, talk about low-self esteem, sheesh. Get a therapist or something, I don't know. I'm just a disembodied voice.")
        else:
            print ("That is NOT a valid response. Try again.")

vaildation()