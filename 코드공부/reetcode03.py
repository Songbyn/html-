class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str1 = ""
        strArr = []
        for i in range(len(s)) :
            if(s[i] in str1) :
                strArr.append(str1)
                str1 = ""
            str1 += s[i] 
        
        strArr.append(str1)
        result = strArr[0]
        for i in strArr :
            if len(result) < len(i) :
                result = i
            
        print(strArr)
        return result
    
c = Solution()
print(c.lengthOfLongestSubstring("bbbbb"))