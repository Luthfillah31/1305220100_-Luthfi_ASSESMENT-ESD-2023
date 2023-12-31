inp = input()

def isDuplicate(li):
    it = 0
    for i in li:
        if i in li[it+1:]:
            return True
        it += 1
    return False

print(isDuplicate(inp))