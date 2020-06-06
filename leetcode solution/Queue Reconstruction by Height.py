"""Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them,
therefore each guy's index will be just as same as his k value.
For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
E.g.
input: [[5,3],[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
After sorting:
[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [5, 3], [4, 4]]"""



class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        new=[]
        people.sort(key=lambda x: (x[0]*-1 ,x[1]))
        for i,j in people:
            new.insert(j,[i,j])
        return new