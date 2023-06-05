# print(eval('1 + 2 * 3'))
"""
Write a function called eval_loop that iteratively prompts the user, takes the result‐
ing input and evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last
expression it evaluated.
"""


def eval_loop():
    while True:
        inp = input("enter the expression to be evaluated ? ")
        if inp == "done":
            print("Done! end")
            break
        else:
            print("result:", eval(inp))
    print("Done")


eval_loop()