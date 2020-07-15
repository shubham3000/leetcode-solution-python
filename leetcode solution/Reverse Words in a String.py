class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")         #Split the string where there is a space. NOTE: If there are extra spaces, elements for each will be created
        string =[] 
        for word in words:
            if word.strip():        #Remove excess white space. NOTE: "strip" removes whitespaces before and after the word
			    string.append(word)
        return(" ".join(string[::-1]))