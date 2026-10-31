class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []

        for op in operations:
            l = len(score_stack)
            
            if op.isdigit() or (op.startswith('-') and op[1:].isdigit()):
                score = int(op)
                score_stack.append(score)
                continue
            
            if op == '+':
                score_stack.append(score_stack[l - 1] + score_stack[l - 2])
            elif op == 'D':
                score_stack.append(score_stack[l - 1] * 2)
            elif op == 'C':
                score_stack.pop()

            

        return 0 if not score_stack else sum(score_stack)
        