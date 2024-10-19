import sqlite3
db_connection = sqlite3.connect('university.db') 
cursor = db_connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

def create_tables():
    try:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Students (
            Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Surname TEXT NOT NULL,
            Department TEXT NOT NULL,
            Date_of_Birth DATE NOT NULL
        )
        """
        cursor.execute(create_table_query)
        print("Таблица 'Students' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Students': {err} ")
    
    try:
        create_table_query1 = """
        CREATE TABLE IF NOT EXISTS Teachers (
            Teacher_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Surname TEXT NOT NULL,
            Department TEXT NOT NULL
        )
        """
        cursor.execute(create_table_query1)
        print("Таблица 'Teachers' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Teachers': {err} ")

    try:
        create_table_query2 = """
        CREATE TABLE IF NOT EXISTS Courses (
            Course_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Description TEXT NOT NULL,
            Teacher_ID INTEGER NOT NULL,
            FOREIGN KEY (Teacher_ID) REFERENCES Teachers(Teacher_ID) ON DELETE CASCADE 
        )
        """
        cursor.execute(create_table_query2)
        print("Таблица 'Courses' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Courses': {err} ")

    try:
        create_table_query3 = """
        CREATE TABLE IF NOT EXISTS Exams(
            Exam_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Exam_Date DATE NOT NULL,
            Course_ID INTEGER NOT NULL,
            Max_Score INTEGER NOT NULL,
            FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID)  
        )
        """
        cursor.execute(create_table_query3)
        print("Таблица 'Exams' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Exams': {err} ")

    try:
        create_table_query4 = """
        CREATE TABLE IF NOT EXISTS Grades(
            Grade_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Student_ID INTEGER NOT NULL,
            Exam_ID INTEGER NOT NULL,
            Score INTEGER NOT NULL,
            FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID) 
            FOREIGN KEY (Exam_ID) REFERENCES Exams(Exam_ID) ON DELETE CASCADE 
        )
        """
        cursor.execute(create_table_query4)
        print("Таблица 'Grades' успешно создана.")
    except sqlite3.Error as err:
        print(f"Ошибка при создании таблицы 'Grades': {err} ")
create_tables()

def Filling_Students():
    insert_query = "INSERT INTO Students (Name,Surname,Department,Date_of_Birth) VALUES (?,?,?,?)"
    users_to_insert =[
        ("Игорь","Акунин","Программирование",2002-4-6),
        ("Иван","Обляков","Программирование",2003-6-12),
        ("Игорь","Дивеев","Машиностроение",2002-1-2),
        ("Антон","Макаров","Экономика",2004-12-22),
        ("Егор","Афанасьев","Машиностроение",2004-9-23),
        ("Дмитрий","Иванов","Экономика",2005-3-16)
    ]
    try:
        cursor.executemany(insert_query,users_to_insert)
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Students'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Students': {err}"))

Filling_Students()

def Filling_Teachers():
    insert_query = "INSERT INTO Teachers (Name,Surname,Department) VALUES (?,?,?)"
    users_to_insert =[
        ("Борис","Акунин","Математика"),
        ("Иван","Андреев","Физика"),
        ("Игорь","Шамуродов","Химия"),
        ("Антон","Григоренко","Экономика"),
        ("Егор","Нестеров","Машиностроение"),
        ("Дмитрий","Васильченко","Программирование")
    ]
    try:
        cursor.executemany(insert_query,users_to_insert)
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Teachers'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Teachers': {err}"))

Filling_Teachers()

def Filling_Courses():
    insert_query = "INSERT INTO Courses (Title,Description,Teacher_ID) VALUES (?,?,?)"
    users_to_insert =[
        ("Первый","Описание для 1",1),
        ("Второй","Описание для 2",2),
        ("Третий","Описание для 3",3),
        ("Четвертый","Описание для 4",4),
        ("2 Первый","Описание первого",5),
        ("2 Третий","Описание третьего",6)
    ]
    try:
        cursor.executemany(insert_query,users_to_insert)
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Courses'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Courses': {err}"))

Filling_Courses()

def Filling_Exams():
    insert_query = "INSERT INTO Exams(Exam_Date,Course_ID,Max_Score) VALUES (?,?,?)"
    users_to_insert =[
        (2023-3-12,1,100),
        (2023-3-13,2,90),
        (2023-3-14,3,100),
        (2023-3-15,4,95),
        (2023-3-16,5,50),
        (2023-3-17,6,110)
    ]
    try:
        cursor.executemany(insert_query,users_to_insert)
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Exams'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Exams': {err}"))

Filling_Exams()

def Filling_Grades():
    insert_query = "INSERT INTO Exams(Student_ID,Exam_ID,Score) VALUES (?,?,?)"
    users_to_insert =[
        (1,1,98),
        (2,2,90),
        (3,3,75),
        (4,4,90),
        (5,5,50),
        (6,6,100)
    ]
    try:
        cursor.executemany(insert_query,users_to_insert)
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Grades'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Grades': {err}"))

Filling_Grades()

def ADD_New_Student():
    insert_query = "INSERT INTO Students(Name,Surname,Department,Date_of_Birth) VALUES (?,?,?,?)"
    users_to_insert = [
        (input("Введите имя нового студента: "), input("Введите фамилию нового студента: "), input("Введите факультет нового студента: "), input("Введите дату рождения студента: "))
    ]
    try:
        cursor.executemany(insert_query,users_to_insert)
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Students'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Students': {err}"))

def ADD_New_Teacher():
    insert_query = "INSERT INTO Teachers(Name,Surname,Department) VALUES (?,?,?)"
    users_to_insert = [
        (input("Введите имя нового преподавателя: "), input("Введите фамилию нового преподавателя: "), input("Введите кафедру нового преподавателя: "))
    ]
    try:
        cursor.executemany(insert_query,users_to_insert)
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Teachers'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Teachers': {err}"))

def ADD_New_Course():
    insert_query = "INSERT INTO Courses(Title, Description, Teacher_ID) VALUES (?,?,?)"
    users_to_insert = [
        (input("Введите название нового курса: "), input("Введите описание курса: "), int(input("Введите ID преподавателя: ")))
    ]
    try:
        cursor.executemany(insert_query,users_to_insert) 
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Courses'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Courses': {err}"))

def ADD_New_Exam():
    insert_query = "INSERT INTO Exams(Exam_Date, Course_ID, Max_Score) VALUES (?,?,?)"
    users_to_insert = [
        (input("Введите дату экзамена: "), int(input("Введите ID курса: ")), int(input("Введите максимальный балл экзамена: ")))
    ]
    try:
        cursor.executemany(insert_query,users_to_insert)
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Exams'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Exams': {err}"))
    
def ADD_New_Grade():
    insert_query = "INSERT INTO Grades(Student_ID, Exam_ID, Score) VALUES (?,?,?)"
    users_to_insert = [
        (int(input("Введите ID студента: ")), int(input("Введите ID экзамена: ")), int(input("Введите оценку: ")))
    ]
    try:
        cursor.executemany(insert_query,users_to_insert)
        db_connection.commit()
        print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Exams'.")
    except sqlite3.Error as err:
        print(print(f"Ошибка при вставке данных в 'Exams': {err}"))

def Update_Student():
    Student_id = int(input("Введите ID студента для обновления: "))
    New_Name = input("Введите новое имя (чтобы не менять - ничего не вводите): ")
    New_Surname = input("Введите новую фамилию (чтобы не менять - ничего не вводите): ")
    New_Department = input("Введите новый факультет (чтобы не менять - ничего не вводите): ")
    New_Date_Of_Birth = input("Введите новую дату рождения (чтобы не менять - ничего не вводите): ")

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
    if New_Date_Of_Birth:
        updates.append("Date_of_Birth = ?")
        values.append(New_Date_Of_Birth)
    if updates:
        update_query = "UPDATE Students SET {"".join(updates)} WHERE Student_ID = ?"
        values.append(Student_id)

        try:
            cursor.execute(update_query, values)
            db_connection.commit()
            print(f"Данные студента с ID {Student_id} успешно обновлены.")
        except sqlite3.Error as err:
            print(f"Ошибка при обновлении данных студента: {err}")
    else:
        print("Нет данных для обновления.")

def Update_Teacher():
    Teacher_id = int(input("Введите ID преподавателя для обновления: "))
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
        update_query = "UPDATE Teachers SET {"".join(updates)} WHERE Teacher_ID = ?"
        values.append(Teacher_id)

        try:
            cursor.execute(update_query, values)
            db_connection.commit()
            print(f"Данные преподавателя с ID {Teacher_id} успешно обновлены.")
        except sqlite3.Error as err:
            print(f"Ошибка при обновлении данных преподавателя: {err}")
    else:
        print("Нет данных для обновления.")
def Update_Course():
    Course_id = int(input("Введите ID курса для обновления: "))
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
        update_query = "UPDATE Courses SET {"".join(updates)} WHERE Course_ID = ?"
        values.append(Course_id)

        try:
            cursor.execute(update_query, values)
            db_connection.commit()
            print(f"Данные студента с ID {Course_id} успешно обновлены.")
        except sqlite3.Error as err:
            print(f"Ошибка при обновлении данных студента: {err}")
    else:
        print("Нет данных для обновления.")

def Delete_Student():
    Student_id = int(input("Введите ID студента, которого вы хотите удалить: "))
    try:
        delete_query = "DELETE FROM Students WHERE Student_ID = ?"
        student_to_delete = Student_id
        cursor.execute(delete_query, student_to_delete)
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Студент с ID {Student_id} успешно удален.")
        else:
            print(f"Студент с ID {Student_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении студента: {err}")

def Delete_Teacher():
    Teacher_id = int(input("Введите ID преподавателя, которого вы хотите удалить: "))
    try:
        delete_query = "DELETE FROM Teachers WHERE Teacher_ID = ?"
        teacher_to_delete = Teacher_id
        cursor.execute(delete_query, teacher_to_delete)
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Преподаватель с ID {Teacher_id} успешно удален.")
        else:
            print(f"Преподаватель с ID {Teacher_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении Преподавателя: {err}")

def Delete_Course():
    Course_id = int(input("Введите ID курса, которого вы хотите удалить: "))
    try:
        delete_query = "DELETE FROM Courses WHERE Course_ID = ?"
        course_to_delete = Course_id
        cursor.execute(delete_query, course_to_delete)
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Курс с ID {Course_id} успешно удален.")
        else:
            print(f"Курс с ID {Course_id} не найден.")
    except sqlite3.Error as err:
        print(f"Ошибка при удалении курса: {err}")

def Delete_Exam():
    Exam_id = int(input("Введите ID экзамена, которого вы хотите удалить: "))
    try:
        delete_query = "DELETE FROM Exams WHERE Exam_ID = ?"
        exam_to_delete = Exam_id
        cursor.execute(delete_query, exam_to_delete)
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Экзамен с ID {Exam_id} успешно удален.")
        else:
            print(f"Экзамен с ID {Exam_id} не найден.")
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
    teacher_id = int(input("Введите ID учителя для поиска курсов: "))
    try:
        select_query = "SELECT * FROM Courses WHERE Teacher_ID = ?"
        cursor.execute(select_query, teacher_id)
        listofcourses = cursor.fetchall()
        if listofcourses:
            print(f"Список курсов,читаемых преподавателем с ID '{teacher_id}'.")
            for row in listofcourses:
                print(f"ID курса: {row[0]}, Название: {row[1]}, Описание: {row[2]}") 
        else:
            print(f"Нет курсов, читаемых преподавателем с ID '{teacher_id}'.")
    except sqlite3.Error as err:
        print(f"Ошибка при поиске курсов: {err}")

def Get_Students_By_Course():
    course_id = int(input("Введите ID курса для поиска студентов: "))
    try:
        select_query = """
        SELECT Students.Student_ID , Students.Name, Students.Surname, Students.Date_of_Birth
        FROM Students
        INNER JOIN Grades ON Students.Student_ID = Grades.Student_ID
        INNER JOIN Exams ON Grades.Exam_ID = Exams.Exam_ID
        INNER JOIN Courses ON Exams.Course_ID = Courses.Course_ID
        WHERE Courses.Course_ID = ?
        """
        cursor.execute(select_query,course_id)
        getstudents = cursor.fetchall()
        if getstudents:
            print(f"Студенты, зачисленные на курс с ID '{course_id}': ")
            for row in getstudents:
                print(f"ID студента: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Дата рождения: {row[3]}")
        else:
            print(f"Нет студентов, зачисленных на курс с ID '{course_id}'.")
    except sqlite3.Error as err:
        print(f"Ошибка при поиске студентов: {err}")

def Get_Grades_On_Course():
    course_id = int(input("Введите ID курса для вывода оценок: "))
    try:
        select_query = """
        SELECT Grades.Student_ID , Grades.Score 
        FROM Grades
        INNER JOIN Exams ON Grades.Exam_ID = Exams.Exam_ID
        INNER JOIN Courses ON Exams.Course_ID = Courses.Course_ID
        WHERE Courses.Course_ID = ?
        """
        cursor.execute(select_query,course_id)
        getgrades = cursor.fetchall()
        if getgrades:
            print(f"Оценки студентов по курсу с ID '{course_id}': ")
            for row in getgrades:
                print(f"ID студента: {row[0]}, Оценка: {row[1]}")
        else:
            print(f"Нет оценок по курсу с ID '{course_id}'.")
    except sqlite3.Error as err:
        print(f"Ошибка при поиске оценок: {err}")

def Get_AVG_Course_Grade():
    student_id = int(input("Введите ID студента для получения среднего балла: "))
    course_id = int(input("Введите ID курса для получения среднего балла: "))
    try:
        select_query = """
        SELECT Grades.Student_ID ,AVG(Grades.Score) AS AverageScore
        FROM Grades 
        JOIN Exams ON Grades.ExamID = Exams.ExamID
        JOIN Courses ON Exams.CourseID = Courses.CourseID
        WHERE Grades.StudentID = ? AND Courses.CourseID = ?
        """
        cursor.execute(select_query,(student_id,course_id))
        getavg = cursor.fetchall()
        if getavg:
            print(f"Средний балл студента с ID '{student_id}' по курсу с ID '{course_id}': ")
            for row in getavg:
                print(f"ID студента: {row[0]}, Средний балл: {row[1]}")
        else:
            print(f"Нет данных по среднему баллу студента с ID '{student_id}' по курсу с ID '{course_id}'.")
    except sqlite3.Error as err:
        print(f"Ошибка при поиске среднего балла: {err}")
            
def Get_AVG_Grade():
    student_id = int(input("Введите ID студента для получения общего среднего балла: "))
    try:
        select_query = """
        SELECT Grades.Student_ID ,AVG(Grades.Score) AS AverageScoreInWhole
        FROM Grades
        WHERE Grades.StudentID = ? 
        """
        cursor.execute(select_query,student_id)
        getavg = cursor.fetchall()
        if getavg:
            print(f"Средний балл студента с ID '{student_id}': ")
            for row in getavg:
                print(f"ID студента: {row[0]}, Средний балл: {row[1]}")
        else:
            print(f"Нет данных по среднему баллу студента с ID '{student_id}'.")
    except sqlite3.Error as err:
        print(f"Ошибка при поиске среднего балла: {err}")

def Get_AVG_Department_Grade():
    department = input("Введите название факультета для получения среднего балла: ")
    try:
        select_query = """
        SELECT Grades.Student_ID ,AVG(Grades.Score) AS AverageScoreOnDepartment
        FROM Grades 
        JOIN Students ON Grades.Student_ID = Students.ExamID
        WHERE Students.Department = ?
        """
        cursor.execute(select_query,department)
        getavg = cursor.fetchall()
        if getavg:
            print(f"Средний балл студента по факультету '{department}': ")
            for row in getavg:
                print(f"ID студента: {row[0]}, Средний балл: {row[1]}")
        else:
            print(f"Нет данных по среднему баллу студента по факультету '{department}'.")
    except sqlite3.Error as err:
        print(f"Ошибка при поиске среднего балла: {err}")

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


    
def Input():
    while True:
        print("\n Меню (Введите 1/2/3/4/5/6/7/8/9/10/exit): ")
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
            elif user_answer == "exit":
                break
Input()

cursor.close()
db_connection.close()

        










