import requests 

class Fetcher:
    def __init__(self):
        self.__students = requests.get("https://cdn.ituring.ir/ex/users.json").json()

    def nerds(self):
        result = set()
        for student in self.__students:
            if student['score'] > 18.5:
                full_name = f"{student['name']} {student['last_name']}"
                result.add(full_name)
        return result
    
    def sultans(self):    
        max_score = max(student['score'] for student in self.__students)
        names = []  
        for student in self.__students:
            if student['score'] == max_score:
                names.append(f"{student['name']} {student['last_name']}")
        return tuple(names) 

    def mean(self):
        total_score = 0 
        for student in self.__students: 
            total_score += student['score'] 
        return total_score / len(self.__students)

    def get_students(self):
        students_list = []  
        for student in self.__students:  
            student_info = {  
                'first_name': student['name'],
                'last_name': student['last_name'],
                'score': student['score']
            }
            students_list.append(student_info)  
        return students_list  

    
fetcher = Fetcher()  

print("Nerds:", fetcher.nerds())
print("Sultans:", fetcher.sultans())
print("Mean Score:", fetcher.mean())
print("\nStudents List:", *fetcher.get_students(), sep="\n")