class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
    s = -120
    s1 = list(reversed(str(abs(s))))
    print(int("-" + "".join(s1)))

    # str[::-1]로 문자열 역순 정렬 가능
    # 음수일 경우 str[1:][::-1]
    #  "-"를 안붙이고 결과값에 -1을 곱해주기