class Solution:
    def totalMoney(self, n: int) -> int:
        whole, rem = n//7, n%7
        num = [28]*whole
        part = whole*rem
        while rem>0:
            part += rem
            rem -=1
        answer = part
        for i in range(len(num)):
            answer += num[i] +7*i
        return answer
