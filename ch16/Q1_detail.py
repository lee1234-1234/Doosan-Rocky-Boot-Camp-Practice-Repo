# 문제 1: 괄호 짝 검사
# 문자열을 인수로 받아 포함된 괄호의 짝이 올바르게 사용되었는지
# 확인하는 프로그램을 작성하시오
# • 스택 활용
# • 괄호의 짝이 맞으면 True 반환
# • 괄호의 짝이 맞지 않으면 False 반환



# 1. 괄호를 담을 빈 스택을 생성한다.
# 2. 문자열 안의 문자를 하나씩 가져온다.
# 3. 문자가 여는 괄호라면 스택에 push한다.
# 4. 문자가 닫는 괄호라면 먼저 스택이 비어 있는지 확인한다.
#    4-1. 스택이 비어 있다면 짝이 맞지 않으므로 False를 반환한다.
#    4-2. 스택이 비어 있지 않다면 스택에서 pop한다.
# 5. pop한 여는 괄호와 현재 닫는 괄호의 짝이 맞는지 확인한다.
#    5-1. 짝이 맞지 않으면 False를 반환한다.
# 6. 모든 문자를 확인한 뒤 스택이 비어 있으면 True, 남아 있으면 False를 반환한다.


def check_bracket(text):
    stack = []
    
    for char in text:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            
    if (char == ")" and top != "(") or (char == "}" and top != "{") or (char == "]" and top != "[") :
        return False
    
    return len(stack) == 0    

print(check_bracket("(a+b)"))
print(check_bracket("(a+b)]}"))
print(check_bracket("[[{(a+b)} + 3]-4]"))