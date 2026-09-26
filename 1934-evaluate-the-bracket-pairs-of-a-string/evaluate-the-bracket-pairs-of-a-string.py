class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        ans= []
        i=0
        know_dict = dict(knowledge)

        while i < len(s):

            if s[i] != '(':
                ans.append(s[i])
                i = i+1
            
            else:
                j = i+1
                
                while s[j] != ')':
                    j = j+1

                key = s[i+1 : j]

                ans.append(know_dict.get(key, '?'))
                i = j+1

        return ''.join(ans) 


