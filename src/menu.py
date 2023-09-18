# from main import *
#
# def menu():
#     print("1. Add a new student")
#     print("2. Delete a student")
#     print("3. Update a student")
#     print("4. Search a student")
#     print("5. Display all students")
#     print("6. Exit")
#     print("Enter your choice: ", end="")
#     choice = int(input())
#     return choice
#
# def add_student():
#     print("Enter student's id: ", end="")
#     id = int(input())
#     print("Enter student's first name: ", end="")
#     first_name = input()
#     print("Enter student's last name: ", end="")
#     last_name = input()
#     print("Enter student's grade: ", end="")
#     grade = int(input())
#     obj = Estudiante(id, first_name, last_name, grade)
#     obj.save()
#     print("Student added successfully")
#
# def delete_student():
#     print("Enter student's id: ", end="")
#     id = int(input())
#     obj = Estudiante.get(id)
#     obj.delete()
#     print("Student deleted successfully")
#
# def update_student():
#     print("Enter student's id: ", end="")
#     id = int(input())
#     obj = Estudiante.get(id)
#     print("Enter student's first name: ", end="")
#     first_name = input()
#     print("Enter student's last name: ", end="")
#     last_name = input()
#     print("Enter student's grade: ", end="")
#     grade = int(input())
#     obj.first_name = first_name
#     obj.last_name = last_name
#     obj.grade = grade
#     obj.save()
#     print("Student updated successfully")
#
# def search_student():
#     print("Enter student's id: ", end="")
#     id = int(input())
#     obj = Estudiante.get(id)
#     print(obj)
#
# def display_all_students():
#     for obj in Estudiante.all():
#         print(obj)
#
# while True:
#     choice = menu()
#     if choice == 1:
#         add_student()
#     elif choice == 2:
#         delete_student()
#     elif choice == 3:
#         update_student()
#     elif choice == 4:
#         search_student()
#     elif choice == 5:
#         display_all_students()
#     elif choice == 6:
#         break
#     else:
#         print("Invalid choice")
#     input("Press enter to continue...")
#