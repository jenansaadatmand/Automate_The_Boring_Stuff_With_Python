def spam():
    eggs = 'spam local'
    print(eggs)    # Prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)    # prints 'bacon local'
    spam()
    print(eggs)    # prints 'bacon local'
eggs = 'global'
bacon()
print(eggs)        # prints 'global'
