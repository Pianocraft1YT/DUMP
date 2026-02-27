repeat = input("Wanna do it again? [yes/no] ")
        elif randomsize == "no" and repeat == "yes" and randomcolor == "no":
            block.clear()
            usersize()
            usercolors()
            drawfn()
            repeat = input("Wanna do it again? [yes/no] ")
        elif randomcolor == "yes" and randomsize == "yes" and repeat == "yes":
            randcolorfn()
            randsizefn()
            drawfn()
            repeat = input("Wanna do it again? [yes/no] ")
        elif randomcolor == "yes" and randomsize == "no" and repeat == "yes":
#Iterate through the list of possible colors
            randcolorfn()
            usersize()
            drawfn()
            repeat = input("Wanna do it again? [yes/no] ")
#If you don't want to, compliments user
        if repeat == "no":
            print("Have a nice day!")
#To prevent from going to else:
        if repeat == "yes":
            print("Let's go!")
#Invalid ansers get rejected
        else:
            print("Something went wrong. Try again.")