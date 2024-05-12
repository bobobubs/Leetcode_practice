class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unables = 0  # Counter for the number of students unable to take the sandwich
        while sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0) 
                sandwiches.pop(0)  
                unables = 0  # Reset the counter 
            else:
                students.append(students.pop(0))  # Move student to the back of the queue
                unables += 1  
                if unables == len(students):
                    return len(students)  
        return 0  # All students got their sandwiches
