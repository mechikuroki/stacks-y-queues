def solution(s):
    if len(s) == 0:
        return True
    
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs.keys():
            if not stack or stack.pop() != pairs[c]:
                return False
                
    return True if not stack else False

print(solution("{hola[oo(ooooo]"))
print(solution("[290(1)jfvhjh]"))

