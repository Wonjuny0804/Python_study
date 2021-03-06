"""
DashInsert Function
if there are relays of odd numbers insert "-"
when even numbers "*"

"""
def DashInsert(data):
    numbers = list(map(int, data)) # 숫자 문자열을 숫자 리스트로 변경
    result = []

    for i, num in enumerate(numbers):
        result.append(str(num))
        if i < len(numbers) - 1:
            is_odd = num % 2 == 1
            is_next_odd = numbers[i+1] % 2 == 1 
            if is_odd and is_next_odd:
                result.append("-")
            elif not is_odd and is_next_odd:
                result.append("*")
    
    return "".join(result)

print(DashInsert("4546793"))

"""
이 알고리즘은 왜 먹히는가?
그렇다면 이 알고리즘에서 사용하고 있는 줄을 하나하나 분석해보자.
numbers = list(map(int, data))는 무슨 뜻인가?
map 함수는 어떻게 쓰는 것일까?

"""