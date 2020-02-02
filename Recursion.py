def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x - 1)
        
def efun(num):
    if num == 0:
        return 1
    else:
        return num * efun(num - 2)

#countdown(5) 
print(efun(8))
