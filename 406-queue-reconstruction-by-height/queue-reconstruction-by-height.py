class Solution(object):
    def reconstructQueue(self, people):
        # Sort the people array based on height in descending order and then by k in ascending order
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Initialize an empty queue
        queue = []
        
        # Insert each person into the queue at the specified position based on k value
        for person in people:
            queue.insert(person[1], person)
        
        return queue
