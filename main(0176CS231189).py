import os
import random
import datetime

StudentRecords_File = "students_db.txt"
Score_File = "scores.txt"
Feedback_File = "feedback.txt"
from register import register
from login import login
from showprofile import show_profile
from updateprofile import update_profile
from about_us import about_us
from feedback import feedback
from Announcements import announcements
from logout import logout
from FileHandling import load_students, save_students,save_score
from QuizSection import quiz_menu,attempt_quiz,view_scores
import session

is_admin = False

def main():
  load_students()
  while True:
    print("Welcome in LNCTE")
    print("1. Register")
    print("2. Login")
    print("3. Show Profile")
    print("4. Update Profile")
    print("5. Quiz Section")
    print("6. About us")
    print("7. Feedback")
    print("8. Announcements")
    print("9. Logout")
    print("10. Exit")
    response = input("Enter your choice (1-10): ").strip()

    if response == '1':
        register()
    elif response == '2':
        username = login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        quiz_menu()
    elif response == '6':
        about_us()
    elif response == '7':
        feedback()
    elif response == '8':
        announcements()
    elif response == '9':
        logout()
    elif response == '10':
        print("Exiting the system... Goodbye!".center(50))
        break

    else:
        print("Invalid Choice, Please select correct option")
if __name__ == "__main__":
    main()



''' SYNTAX FROM REGISTER FILE
students_db = {}
current_user = None
def register():
    print("\n---Student Registration---")
    username = input("Enter Username: ").strip()
    if username in students_db:
        print("Username already exists. Try a diffrent one.")
        return
    for user, details in students_db.items():
        if details["roll_no"] == roll_no:
            print(" A student with this Roll Number is already registered.")
            return
        if details["email"] == email:
            print(" A student with this Email is already registered.")
            return

    password = input("Enter Password: ").strip()
    full_name = input("Enter Full Name: ").strip()
    roll_no = input("Enter Roll Number: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    dob = input("Enter Date of Birth (DD/MM/YYYY): ").strip()
    gender = input("Enter Gender: ").strip()
    address = input("Enter Address: ").strip()
    course = input("Enter Course: ").strip()
    year = input("Enter Year (e.g. 1st, 2nd): ").strip()

    students_db[username] = {
        "password": password,
        "full_name": full_name,
        "roll_no": roll_no,
        "email": email,
        "phone": phone,
        "dob": dob,
        "gender": gender,
        "address": address,
        "course": course,
        "year": year
    }
    print(f" Registration successful for {full_name}!\n")'''


''' SYNTAX FROM LOGIN FILE
students_db = {}
current_user = None
def login():
    global current_user
    print("\n--- Student Login ---")
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    if username in students_db and students_db[username]["password"] == password:
        current_user = username
        print(f" Login successful. Welcome, {students_db[username]['full_name']}!\n")
    else:
        print(" Invalid username or password.\n")'''

'''SYNTAX FROM SHOWFILE FILE
students_db = {}
current_user = None
def show_profile():
    if not current_user:
        print("Please login first.\n")
        return

    print("\n--- Student Profile ---")
    profile = students_db[current_user]
    for key, value in profile.items():
        if key != "password":
            print(f"{key.capitalize():15}: {value}")
    print()'''

'''SYNTAX FROM UPDATE PROFILE FILE
students_db = {}
current_user = None

def update_profile():
    if not current_user:
        print(" Please login first.\n")
        return

    print("\n--- Update Profile ---")
    profile = students_db[current_user]
    for key in profile:
        if key == "password":
            continue
        new_value = input(f"Enter new {key.capitalize()} (leave blank to keep '{profile[key]}'): ").strip()
        if new_value:
            profile[key] = new_value

    change_pass = input("Do you want to change password? (y/n): ").lower()
    if change_pass == 'y':
        new_pass = input("Enter new password: ").strip()
        profile["password"] = new_pass
    print("Profile updated successfully!\n")'''

'''SYNTAX FROM QUIZ SECTION FILE
import random, os
import session
from FileHandling import save_score,save_students,save_score

def quiz_menu():
    if not session.current_user:
        print(" Please login to attempt quiz.")
        return

    while True:
        print("\n---  Quiz Categories ---")
        print("1. DSA")
        print("2. DBMS")
        print("3. PYTHON")
        print("4. View Score History")
        print("5. Back to Main Menu")

        choice = input("Choose category: ")

        if choice == "1":
            attempt_quiz("DSA", dsa_questions)
        elif choice == "2":
            attempt_quiz("DBMS", dbms_questions)
        elif choice == "3":
            attempt_quiz("PYTHON", python_questions)
        elif choice == "4":
            view_scores()
        elif choice == "5":
            break
        else:
            print(" Invalid choice!")

def attempt_quiz(category, questions):
    score = 0
    total = len(questions)
    random.shuffle(questions)

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}. {q['question']}")
        for opt in q['options']:
            print(f"   {opt}")
        ans = input("Your answer: ").strip().upper()
        if ans == q['answer']:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer: {q['answer']}")

    print(f"\n You scored {score}/{total} in {category} quiz.")
    save_score(session.current_user, category, score, total)

def view_scores():
    if not os.path.exists(Score_File):
        print("No quiz records found.")
        return

    print("\n---  Score History ---")
    with open(Score_File, "r") as f:
        for line in f:
            user, category, marks, dt = line.strip().split("|")
            if user == current_user:
                print(f"{category} -> {marks} on {dt}")

dsa_questions = [
    {"question": "Which data structure is used for implementing recursion?", 
     "options": ["A. Queue", "B. Stack", "C. Array", "D. Linked List"], "answer": "B"},
     
    {"question": "What is the time complexity of inserting an element at the end of an array (amortized)?", 
     "options": ["A. O(1)", "B. O(n)", "C. O(log n)", "D. O(n^2)"], "answer": "A"},
     
    {"question": "Which traversal technique is used in Depth First Search (DFS)?", 
     "options": ["A. Level Order", "B. Breadth First", "C. Preorder", "D. Inorder"], "answer": "C"},
     
    {"question": "Which data structure is used in BFS algorithm?", 
     "options": ["A. Stack", "B. Queue", "C. Tree", "D. Array"], "answer": "B"},
     
    {"question": "Which sorting algorithm has the best average case complexity?", 
     "options": ["A. Bubble Sort", "B. Merge Sort", "C. Insertion Sort", "D. Selection Sort"], "answer": "B"},
     
    {"question": "Which operation in stack removes the top element?", 
     "options": ["A. push()", "B. pop()", "C. top()", "D. peek()"], "answer": "B"},
     
    {"question": "Which data structure is used in implementing a priority queue?", 
     "options": ["A. Array", "B. Linked List", "C. Heap", "D. Stack"], "answer": "C"},
     
    {"question": "In a circular queue, when is the queue full?", 
     "options": ["A. front == rear", "B. rear == front - 1 (mod size)", "C. rear == size", "D. front == size"], "answer": "B"},
]



dbms_questions = [
    {"question": "Which of the following is a valid type of join in SQL?", 
     "options": ["A. Full Join", "B. Cross Join", "C. Inner Join", "D. All of the above"], "answer": "D"},
     
    {"question": "Which key uniquely identifies each row in a table?", 
     "options": ["A. Foreign Key", "B. Primary Key", "C. Super Key", "D. Candidate Key"], "answer": "B"},
     
    {"question": "What does ACID property stand for in databases?", 
     "options": ["A. Atomicity, Consistency, Isolation, Durability", 
                 "B. Accuracy, Clarity, Isolation, Durability", 
                 "C. Atomic, Control, Integrity, Dependency", 
                 "D. None of the above"], "answer": "A"},
     
    {"question": "Which command is used to remove all records from a table but keep the structure?", 
     "options": ["A. DROP", "B. DELETE", "C. TRUNCATE", "D. REMOVE"], "answer": "C"},
     
    {"question": "What does SQL stand for?", 
     "options": ["A. Structured Question Language", "B. Structured Query Language", 
                 "C. Sequential Query Language", "D. None"], "answer": "B"},
     
    {"question": "Which clause is used to filter records in SQL?", 
     "options": ["A. WHERE", "B. ORDER BY", "C. GROUP BY", "D. DISTINCT"], "answer": "A"},
     
    {"question": "Which type of key is used to link two tables?", 
     "options": ["A. Super Key", "B. Foreign Key", "C. Primary Key", "D. Composite Key"], "answer": "B"},
     
    {"question": "What is normalization in DBMS?", 
     "options": ["A. Process of reducing redundancy", 
                 "B. Process of increasing redundancy", 
                 "C. Process of merging tables", 
                 "D. None"], "answer": "A"},
]



python_questions = [
    {"question": "Which keyword is used to define a function in Python?", 
     "options": ["A. func", "B. define", "C. def", "D. function"], "answer": "C"},
     
    {"question": "What is the output of: print(type([])) ?", 
     "options": ["A. <class 'list'>", "B. <class 'tuple'>", "C. <class 'set'>", "D. <class 'dict'>"], "answer": "A"},
     
    {"question": "Which of these is immutable?", 
     "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"], "answer": "D"},
     
    {"question": "Which operator is used for floor division in Python?", 
     "options": ["A. /", "B. //", "C. %", "D. **"], "answer": "B"},
     
    {"question": "What is the output of bool(0)?", 
     "options": ["A. True", "B. False", "C. 0", "D. None"], "answer": "B"},
     
    {"question": "Which method adds an element at the end of a list?", 
     "options": ["A. insert()", "B. append()", "C. add()", "D. extend()"], "answer": "B"},
     
    {"question": "Which keyword is used for exception handling?", 
     "options": ["A. catch", "B. try", "C. except", "D. Both B and C"], "answer": "D"},
     
    {"question": "What is the output of: len({'a':1, 'b':2, 'c':3}) ?", 
     "options": ["A. 6", "B. 3", "C. 2", "D. Error"], "answer": "B"},
]
'''

'''SYNTAX FROM ABOUT US FILE
def about_us():
    print("\n---  About Us ---")
    print("Welcome to the Student Management System".center(70))
    print("This system was developed to manage student data efficiently.")
    print("Version: 1.0")'''

'''SYNTAX FROM FEEDBACK FILE
students_db = {}
current_user = None

def feedback():
    global current_user
    if not current_user:
        print(" You must be logged in to submit feedback.")
        return

    print("\n---  Feedback ---")
    fb = input("Please enter your feedback: ")
    print(" Thank you for your feedback!")'''

'''SYNTAX FROM ANNUNCEMENTS FILE
students_db = {}
current_user = None

def announcements():
    global current_user
    if not current_user:
        print(" Please log in to view announcements.")
        return
    print("\n---  Announcements ---".center(30))
    print("1.  Semester exams will start from 15th October.")
    print("2.  Registration for the Annual Fest is open.")
    print("3.  Library will be open from 8 AM to 8 PM during exams.")'''

'''SYNTAX FROM LOGOUT FILE
students_db = {}
current_user = None
def logout():
    global current_user
    if current_user:
        print(f"{students_db[current_user]['full_name']} logged out successfully.\n")
        current_user = None
    else:
        print("No user is currently logged in.\n")'''





