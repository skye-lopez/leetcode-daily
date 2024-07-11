def reverseParentheses(self, s: str) -> str:
    sol = []
    for i in range(len(s)):
        if s[i] == '(':
            sol.append(s[i])
        elif s[i] == ')':
            reversed = []
            while sol and sol[-1] != '(':
                reversed.append(sol.pop()[::-1])
            sol.pop()
            revStr = "".join(reversed)
            sol.append(revStr)
        else:
            sol.append(s[i])
    return "".join(sol)
