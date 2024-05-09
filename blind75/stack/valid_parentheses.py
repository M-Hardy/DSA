# couple mistakes that caused incorrect answer:
# - else condition (we found a closed bracket): check that there are brackets
#   in the stack before checking last bracket in stack; if there's nothing in
#   the stack then that means the input parentheses are also invalid
# - after loop is complete, return whether the stack is empty or not, not just
#   True; this will be incorrect if all open/close pairs are resolved but there
#   are extra open brackets in the stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        parentheses = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        
        for p in s:
            if p not in parentheses:
                stack.append(p)
            
            else:
                if not stack or parentheses[p] != stack.pop():
                    return False
                
        return not stack