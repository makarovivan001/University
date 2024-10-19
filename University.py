import sqlite3
db_connection = sqlite3.connect('university.db') 
cursor = db_connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")



def InputDate():
    date = input("Введите дату в формате 'YYYY-MM-DD': ")
    if len(date) == 10 and (date[:4]).isdigit() and (date[5:7]).isdigit() and (date[8:]).isdigit() and date[4] == '-' and date[7] == '-':
            return date
    else:
        print("Введите дату в правильном формате.")
        return InputDate()
    
def InputId():
    id = input("Введите ID: ")
    if id.isdigit():
        return int(id)
    else:
        print("Введите ID правильно, числом.")
        return InputId()
    
def InputScore():
    while True:
        try:
            score = int(input("Введите оценку экзамена (от 0 до 100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Оценка должна быть в диапазоне от 0 до 100.")
        except ValueError:
            print("Введите целое число.")



def clear_db():
    try:
        delete_table = """DROP TABLE IF EXISTS Students"""
        cursor.execute(delete_table)
        delete_table = """DROP TABLE IF EXISTS Teachers"""
        cursor.execute(delete_table)
        delete_table = """DROP TABLE IF EXISTS Courses"""
        cursor.execute(delete_table)
        delete_table = """DROP TABLE IF EXISTS Exams"""
        cursor.execute(delete_table)
        delete_table = """DROP TABLE IF EXISTS Grades"""
        cursor.execute(delete_table)
    except:
        print("Не удалось удалить базу данных")

    
    
    

def create_tables():
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            Student_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Name TEXT NOT NULL,         
            Surname TEXT NOT NULL,  
            Department TEXT NOT NULL,
            Date_Of_Birth DATE NOT NULL
        )
        """)
        print("Таблица 'Students' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Students': {err}")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Teachers (
            Teacher_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Name TEXT NOT NULL,         
            Surname TEXT NOT NULL,  
            Department TEXT NOT NULL
        )
        """)
        print("Таблица 'Teachers' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Teachers': {err}")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            Course_ID INTEGER PRIMARY KEY AUTOINCREMENT,         
            Title TEXT NOT NULL,  
            Description TEXT,
            Teacher_ID INTEGER,
            FOREIGN KEY (Teacher_ID) REFERENCES Teachers(Teacher_ID) ON DELETE CASCADE
        )
        """)
        print("Таблица 'Courses' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Courses': {err}")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Exams (
            Exam_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Exam_Date DATE NOT NULL,
            Max_Score INTEGER NOT NULL,
            Course_ID INTEGER,
            FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID) ON DELETE CASCADE
        )
        """)
        print("Таблица 'Exams' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Exams': {err}")
    
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Grades (
            Grade_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            Student_ID INTEGER,
            Exam_ID INTEGER,
            Score INTEGER NOT NULL,
            FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID) ON DELETE CASCADE,
            FOREIGN KEY (Exam_ID) REFERENCES Exams(Exam_ID) ON DELETE CASCADE
        )
        """)
        print("Таблица 'Grades' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Grades': {err}")


def Count_Of_Lines(table_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cursor.fetchone()[0]
    return row_count



def ADD_New_Student():
    insert_query = "INSERT INTO Students(Name,Surname,Department,Date_of_Birth) VALUES (?,?,?,?)"
    users_to_insert = [(input("Введите имя студента: "), 
                  input("Введите фамилию студента: "), 
                  input("Введите факультет студента: "), 
                  InputDate())]
    try:
        cursor.executemany(insert_query,users_to_insert)
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Students'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Students': {err}"))

def ADD_New_Teacher():
    insert = "INSERT INTO Teachers (Name, Surname, Department) VALUES (?, ?, ?)"
    teachers_to_insert = [(input("Введите имя преподавателя: "), 
                  input("Введите фамилию преподавателя: "), 
                  input("Введите кафедру преподавателя: "))]
    try:
        cursor.executemany(insert, teachers_to_insert)
        db_connection.commit()
        print(f"Запись успешно добавлена в таблицу 'Teachers'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Teachers': {err}")


def ADD_New_Course():
    insert = "INSERT INTO Courses (Title, Description, Teacher_ID) VALUES (?, ?, ?)"
    courses_to_insert = [(input("Введите название курса: "), 
                          input("Введите описание курса: "),
                          InputId())]
                            
    try:
        cursor.executemany(insert, courses_to_insert)
        db_connection.commit()
        print(f"Запись успешно добавлена в таблицу 'Courses'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Courses': {err}")


def ADD_New_Exam():
    insert = "INSERT INTO Exams (Exam_Date, Course_ID, Max_Score) VALUES (?, ?, ?)"
    exams_to_insert = [(InputDate(),
                        InputId(),
                        int(input("Введите максимальный балл экзамена: ")))]
    try:
        cursor.executemany(insert, exams_to_insert)
        db_connection.commit()
        print(f"Запись успешно добавлена в таблицу 'Exams'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Exams': {err}")
    
def ADD_New_Grade():
    insert = "INSERT INTO Grades (Student_ID, Exam_ID, Score) VALUES (?,?,?)"
    to_insert = [(print("Введите ID студента: ") + InputId(),
                  print("Введите ID экзамена: ") + InputId(),
                  print("Введите оценку экзамена: ") + InputScore())]
    try:
        cursor.executemany(insert, to_insert)
        db_connection.commit()
        print(f"Запись успешно добавлена в таблицу 'Grades'.")
    except sqlite3.Error as err:
        print(f"Ошибка при вставке данных в 'Grades': {err}")

def Update_Student():
    student_id = InputId()
    if student_id > Count_Of_Lines("Students"):
        print("Студент с таким ID не найден.")
        return
    new_name = input("Введите новое имя, если не хотите менять - ничего не вводите: ")
    new_surname = input("Введите новую фамилию, если не хотите менять - ничего не вводите: ")
    new_department = input("Введите новый факультет, если не хотите менять - ничего не вводите: ")
    print("Введите новую дату рождения, если не хотите менять - ничего не вводите: ")
    new_date_of_birth = InputDate()

    updates = []
    values = []
    
    if new_name:
        updates.append("Name = ?")
        values.append(new_name)
    if new_surname:
        updates.append("Surname = ?")
        values.append(new_surname)
    if new_department:
        updates.append("Department = ?")
        values.append(new_department)
    if new_date_of_birth:
        updates.append("Date_Of_Birth = ?")
        values.append(new_date_of_birth)

    if updates:
        update_query = f"UPDATE Students SET {', '.join(updates)} WHERE Student_ID = ?"
        values.append(student_id)

        try:
            cursor.execute(update_query, values)
            db_connection.commit()
            print(f"Студент с ID {student_id} успешно обновлен.")
        except sqlite3.Error as err:
            print(f"Ошибка при обновлении студента: {err}")
    else:
        print("Нет данных для обновления.")

def Update_Teacher():
    teacher_id = InputId()
    if teacher_id > Count_Of_Lines("Teachers"):
        print("Преподавателя с таким ID не существует.")
        return
    New_Name = input("Введите новое имя (чтобы не менять - ничего не вводите): ")
    New_Surname = input("Введите новую фамилию (чтобы не менять - ничего не вводите): ")
    New_Department = input("Введите новую кафедру (чтобы не менять - ничего не вводите): ")

    updates = []
    values = []

    if New_Name:
        updates.append("Name = ?")
        values.append(New_Name)
    if New_Surname:
        updates.append("Surname = ?")
        values.append(New_Surname)
    if New_Department:
        updates.append("Department = ?")
        values.append(New_Department)
    if updates:
        update_query = f"UPDATE Teachers SET {"".join(updates)} WHERE Teacher_ID = ?"
        values.append(teacher_id)

        try:
            cursor.execute(update_query, values)
            db_connection.commit()
            print(f"Данные преподавателя с ID {teacher_id} успешно обновлены.")
        except sqlite3.Error as err:
            print(f"Ошибка при обновлении данных преподавателя: {err}")
    else:
        print("Нет данных для обновления.")
def Update_Course():
    course_id = InputId()
    if course_id > Count_Of_Lines("Courses"):
        print("Курса с таким ID не существует.")
        return
    New_Title = input("Введите новое название (чтобы не менять - ничего не вводите): ")
    New_Description = input("Введите новое описание (чтобы не менять - ничего не вводите): ")
    New_Teacher_id = input("Введите ID преподавателя (чтобы не менять - ничего не вводите): ")

    updates = []
    values = []

    if New_Title:
        updates.append("Title = ?")
        values.append(New_Title)
    if New_Description:
        updates.append("Description = ?")
        values.append(New_Description)
    if New_Teacher_id:
        updates.append("Teacher_ID = ?")
        values.append(New_Teacher_id)
    if updates:
        update_query = f"UPDATE Courses SET {"".join(updates)} WHERE Course_ID = ?"
        values.append(course_id)

        try:
            cursor.execute(update_query, values)
            db_connection.commit()
            print(f"Данные курса с ID {course_id} успешно обновлены.")
        except sqlite3.Error as err:
            print(f"Ошибка при обновлении данных курса: {err}")
    else:
        print("Нет данных для обновления.")

def Delete_Student():
    student_id = InputId()
    if student_id > Count_Of_Lines("Students"):
        print("Студента с таким ID не существует.")
        return
    try:
        cursor.execute("DELETE FROM Students WHERE Student_ID = ?", (student_id,))
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Студент с ID {student_id} успешно удален.")
        else:
            print(f"Студент с ID {student_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении студента: {err}")

def Delete_Teacher():
    teacher_id = InputId()
    if teacher_id > Count_Of_Lines("Teachers"):
        print("Учителя с таким ID не существует.")
        return
    try:
        cursor.execute("DELETE FROM Teachers WHERE Teacher_ID = ?", (teacher_id,))
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Преподаватель с ID {teacher_id} успешно удален.")
        else:
            print(f"Преподаватель с ID {teacher_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении преподавателя: {err}")

def Delete_Course():
    course_id = InputId()
    if course_id > Count_Of_Lines("Courses"):
        print("Курса с таким ID не существует.")
        return
    try:
        cursor.execute("DELETE FROM Courses WHERE Course_ID = ?", (course_id,))
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Курс с ID {course_id} успешно удален.")
        else:
            print(f"Курс с ID {course_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении курса: {err}")

def Delete_Exam():
    exam_id = InputId()
    if exam_id > Count_Of_Lines("Exams"):
        print("Экзамена с таким ID не существует.")
        return 
    try:
        cursor.execute("DELETE FROM Exams WHERE Exam_ID = ?", (exam_id,))
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Экзамен с ID {exam_id} успешно удален.")
        else:
            print(f"Экзамен с ID {exam_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении экзамена: {err}")

def Get_Students_By_Department():
    department = input("Введите название факультета для получения списка студентов: ")
    try:
        select_query = "SELECT * FROM Students WHERE Department = ?"
        cursor.execute(select_query,(department,))
        listofstudent = cursor.fetchall()
        if listofstudent:
            print(f"Список студентов факультета '{department}': ")
            for row in listofstudent:
                print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Дата рождения: {row[4]}")
        else:
            print(f"Нет студентов на факультете '{department}'.")
    except sqlite3.Error as err:
        print(f"Ошибка при поиске студентов: {err}")

def Get_Courses_Taught_By_Teacher():
    teacher_id = InputId()
    if teacher_id > Count_Of_Lines("Teachers"):
        print("Преподавателя с таким ID не существует.")
        return
    try:
        cursor.execute("SELECT * FROM Courses WHERE Teacher_ID = ?", (teacher_id,))
        courses = cursor.fetchall()

        if courses:
            print(f"Курсы, читаемые преподавателем с ID {teacher_id}:")
            for row in courses:
                print(f"ID: {row[0]}, Название: {row[1]}, Описание: {row[2]}")
        else:
            print(f"Нет курсов, читаемых преподавателем с ID {teacher_id}.")
    except sqlite3.Error as err:
        print(f"Ошибка при получении курсов преподавателем: {err}")


def Get_Students_By_Course():
    course_id = InputId()
    if course_id > Count_Of_Lines("Courses"):
        print("Курса с таким ID не существует.")
        return
    try:
        cursor.execute("""
        SELECT Students.Student_ID, Students.Name, Students.Surname, Students.Date_Of_Birth
        FROM Students 
        JOIN Grades ON Students.Student_ID = Grades.Student_ID 
        JOIN Exams ON Grades.Exam_ID = Exams.Exam_ID
        JOIN Courses ON Exams.Course_ID = Courses.Course_ID
        WHERE Courses.Course_ID =?""", (course_id,))
        students = cursor.fetchall()

        if students:
            print(f"Студенты, изучающие курс с ID {course_id}:")
            for row in students:
                print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Дата рождения: {row[3]}")
        else:
            print(f"Нет студентов, изучающих курс с ID {course_id}.")
    except sqlite3.Error as err:
        print(f"Ошибка при получении студентов из курса: {err}")

def Get_Grades_On_Course():
    course_id = InputId()
    if course_id > Count_Of_Lines("Courses"):
        print("Курс с таким ID не найден.")
        return
    try:
        cursor.execute("""
        SELECT Students.Student_ID, Students.Name, Students.Surname, Students.Date_Of_Birth, Grades.Score 
        FROM Students 
        JOIN Grades ON Students.Student_ID = Grades.Student_ID 
        JOIN Exams ON Grades.Exam_ID = Exams.Exam_ID
        WHERE Exams.Course_ID =?""", (course_id,))
        students = cursor.fetchall()

        if students:
            print(f"Студенты, изучающие курс с ID {course_id} с баллами:")
            for row in students:
                print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Дата рождения: {row[3]}, Балл: {row[4]}")
        else:
            print(f"Нет студентов, изучающих курс с ID {course_id}.")
    except sqlite3.Error as err:
        print(f"Ошибка при получении баллов студентов: {err}")

def Get_AVG_Course_Grade():
    print("ID студента для получения среднего балла: ")
    student_id = InputId()
    if student_id > Count_Of_Lines("Students"):
        print("Студента с таким ID не существует.")
        return
    print("ID курса для получения среднего балла: ")
    course_id = InputId()
    if course_id > Count_Of_Lines("Courses"):
        print("Курсa c таким ID не существует.")
        return
    try:
        cursor.execute("""
        SELECT AVG(Score) AS Average_Course_Grade
        FROM Grades 
        JOIN Exams ON Grades.Exam_ID = Exams.Exam_ID
        JOIN Courses ON Exams.Course_ID = Courses.Course_ID
        WHERE Grades.Student_ID = ? AND Courses.Course_ID = ?""", (student_id, course_id))
        result = cursor.fetchone()
        average_score = result[0] if result[0] is not None else 0
        print(f"Средний балл студента с ID {student_id} по курсу с ID {course_id}: {average_score}")
    except sqlite3.Error as err:
        print(f"Ошибка при получении среднего балла: {err}")
            
def Get_AVG_Grade():
    student_id = InputId()
    try:
        cursor.execute("""
        SELECT AVG(Score) AS Average_Grade_In_Whole
        FROM Grades
        WHERE Student_ID = ?""", (student_id,)) 
        result = cursor.fetchone()
        whole_average = result[0] if result[0] is not None else 0
        print(f"Средний балл студента с ID {student_id} в целом: {whole_average:.2f}")
    except sqlite3.Error as err:
        print(f"Ошибка при получении среднего балла: {err}")

def Get_AVG_Department_Grade():
    department = input("Введите название факультета для получения среднего балла: ")
    try:
        cursor.execute("""
        SELECT AVG(Score) AS Average_Department_Grade
        FROM Grades
        JOIN Students ON Grades.Student_ID = Students.Student_ID
        JOIN Exams ON Grades.Exam_ID = Exams.Exam_ID
        JOIN Courses ON Exams.Course_ID = Courses.Course_ID
        WHERE Students.Department = ?""", (department,))
        
        result = cursor.fetchone()
        department_average = result[0] if result[0] is not None else 0
        print(f"Средний балл в целом по факультету '{department}': {department_average:.2f}")
    except sqlite3.Error as err:
        print(f"Ошибка при получении среднего балла: {err}")



def ADD_SMTH():
    while True:
        request = input("Введите что вы хотите добавить: (студент, преподаватель, курс, экзамен или оценка/exit)")
        if request == "студент" or request == "Студент":
            ADD_New_Student()
        elif request == "преподаватель" or request == "Преподаватель":
            ADD_New_Teacher()
        elif request == "курс" or request == "Курс":
            ADD_New_Course()
        elif request == "экзамен" or request == "Экзамен":
            ADD_New_Exam()
        elif request == "оценка" or request == "Оценка":
            ADD_New_Grade()
        elif request == "exit" or request == "Exit":
            break
            

        
        else:
            print("Некорректный запрос")
        
def Delete_SMTH():
    while True:
        request = input("Введите что вы хотите удалить: (студент, преподаватель, курс или экзамен/exit)")
        if request == "студент" or request == "Студент":
            Delete_Student()
        elif request == "преподаватель" or request == "Преподаватель":
            Delete_Teacher()
        elif request == "курс" or request == "Курс":
            Delete_Course()
        elif request == "экзамен" or request == "Экзамен":
            Delete_Exam()
        elif request == "exit" or request == "Exit":
            break
        else:
            print("Некорректный запрос")
def Update_SMTH():
    while True:
        request = input("Введите что вы хотите обновить: (студент, преподаватель или курс /exit)")
        if request == "студент" or request == "Студент":
            Update_Student()
        elif request == "преподаватель" or request == "Преподаватель":
            Update_Teacher()
        elif request == "курс" or request == "Курс":
            Update_Course()
        elif request == "exit" or request == "Exit":
            break
        else:
            print("Некорректный запрос")
        

create_tables()







    
def Input():
    while True:
        print("\n Меню (Введите 1/2/3/4/5/6/7/8/9/10/11/exit): ")
        print("1. Добавление нового студента, преподавателя, курса, экзамена и оценки.")
        print("2. Изменение информации о студентах, преподавателях и курсах.")
        print("3. Удаление студентов, преподавателей, курсов и экзаменов.")
        print("4. Получение списка студентов по факультету.")
        print("5. Получение списка курсов, читаемых определенным преподавателем.")
        print("6. Получение списка студентов, зачисленных на конкретный курс.")
        print("7. Получение оценок студентов по определенному курсу.")
        print("8. Средний балл студента по определенному курсу.")
        print("9. Средний балл студента в целом.")
        print("10. Средний балл по факультету.")
        print("11. очистить базу данных")
        while True:
            user_answer = input("")
            if user_answer == "1":
                ADD_SMTH()
            elif user_answer == "2":
                Update_SMTH()
            elif user_answer == "3":
                Delete_SMTH()
            elif user_answer == "4":
                Get_Students_By_Department()
            elif user_answer == "5":
                Get_Courses_Taught_By_Teacher()
            elif user_answer == "6":
                Get_Students_By_Course()
            elif user_answer == "7":
                Get_Grades_On_Course()
            elif user_answer == "8":
                Get_AVG_Course_Grade()
            elif user_answer == "9":
                Get_AVG_Grade()
            elif user_answer == "10":
                Get_AVG_Department_Grade()
            elif user_answer == "11":
                clear_db()
                
            elif user_answer == "exit":
                break
Input()

cursor.close()
db_connection.close()

        