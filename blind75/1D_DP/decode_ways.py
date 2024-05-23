# implementation note: remember to initialize oneStep and twoSteps 
# to 1 in order for incrementation to work; if either are 0 then
# that value (i-1 or i-2) will always be incorrect because its
# incrementation never builds

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        # num decodings @ i-2 and @ i-1
        # num decodings @ i = numDecodings(i-1) + numDecodings(i-2) *if you can make valid 2 digit num with i
        twoSteps = 1
        oneStep = 1

        for i in range(1, len(s)):
            cur = 0
            if s[i] != "0":
                cur += oneStep
            if i-1 >= 0 and (s[i-1] == "1" or s[i-1] == "2" and 0 <= int(s[i]) < 7):
                cur += twoSteps 

            twoSteps = oneStep
            oneStep = cur
        return oneStep