class Course:
    def __init__(self, course_id, name, capacity):
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_students = []  
        self.instructor = None 
        
    def is_full(self):
        #Check if the course is full
        return len(self.enrolled_students) >= self.capacity


    
    def __str__(self):
        instructor_name = self.instructor.name if self.instructor else "None"
        return f"Course ID: {self.course_id}, Name: {self.name}, Capacity: {self.capacity}, Instructor: {instructor_name}"