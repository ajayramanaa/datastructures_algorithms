from typing import List

class Solution:
    def rescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        left= 0
        right = len(people)-1

        while (left <= right):
            if (left == right):
                boats+=1
                break
            if(people[left] + people[right] <= limit):
                left+= 1
            boats+=1
            right-= 1
        return boats


people = [1,2,3]
limit = 4
obj = Solution()
result =  obj.rescueBoats(people, limit)
print("Number of boats required is %d" % result)








