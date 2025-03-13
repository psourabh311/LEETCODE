class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        check = 0
        while len(students) and check != len(students):
            if students[0]==sandwiches[0]:
                check=0
                students.pop(0)
                sandwiches.pop(0)
            else:
                check+=1
                students = students[1:] + [students[0]]
        return check        
