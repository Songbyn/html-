def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        #set으로 중복 문자열 삭제 후 rfind find로
        # 
        str1 ="abcdafbeg"
        setStr = set(str1)
        result = list()

        for i in setStr :
            if str1.find(i) == str1.rfind(i) : continue
            else :
                result.append(str1[str1.find(i):str1.rfind(i)+1])

        result1 = ""
        length = 0
        for i,v in enumerate(result) :
            if len(v) > length :
                length = len(v)
                result1 = result[i]