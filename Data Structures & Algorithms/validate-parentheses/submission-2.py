class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack_list = []

        for c in s:
            len_stack_list = len(stack_list)
            if c == '(' or c == '{' or c == '[':
                stack_list.append(c)
            elif (c == ')' or c == '}' or c == ']') and len_stack_list > 0:
                last_bracket = stack_list[len_stack_list - 1]

                if last_bracket == '(' and c == ')':
                    stack_list.pop()
                elif last_bracket == '{' and c == '}':
                    stack_list.pop()
                elif last_bracket == '[' and c == ']':
                    stack_list.pop()
                else:
                    return False
            else:
                return False

        return len(stack_list) == 0 