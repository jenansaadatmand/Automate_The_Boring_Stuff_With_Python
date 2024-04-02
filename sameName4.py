def spam():
    print(eggs)    # Error! first need to assign a value for it
    eggs = 'spam local'
#    print(eggs)   # Need to remove commenting out and delete top print(eggs)
eggs = 'global'
spam()
print(eggs)
