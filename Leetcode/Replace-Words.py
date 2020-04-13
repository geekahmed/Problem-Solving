/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution(object):
    
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        rootList = set(dict)
        def replace(w):
            for i in range(len(w)):
                if w[:i] in rootList:
                    return w[:i]
            return w
        return " ".join(map(replace, sentence.split()))
