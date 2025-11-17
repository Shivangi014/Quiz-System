"NAME : Shivangi"
"ENROLLMENT : 0176CS231189"
"BATCH : 6 (3rd year)"
"BATCH TIME : (12:10-1:50)"


"Conditional Statement: IF-ELSE PROBLEM"

"Q1:Write a program to check whether a number is positive, negative, or zero."

age = int(input("Enter your age: "))
if age > 0 :
    print ("Positive")
elif number < 0 :
    print ("Negative")
else:
    print ("Zero")


'Q2:Write a program to check whether a number is even or odd.'


number = int(input("Enter a number: "))
if number % 2 == 0:
    print ("Number is Even.")
else:
    print ("Number is Odd.")



"Q3:Write a program to check if a given year is a leap year or not."

year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("Given year is leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("Given year is leap year")
else:
    print("Given year is not a leap year")


"Q4:Write a program to find the greatest of two numbers"

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if n1 > n2:
    print(f"{n1} is the greatest number. ")
elif n2 > n1:
    print(f"{n2} is the greatest number. ")
else:
    print("Both numbers are equal.")


"Q5:Write a program to check whether a person is eligible to vote (age >= 18)"

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


"Q6:Write a program to check whether a given character is a vowel or consonant"

char = input("Enter a character: ")
if len(char) == 1 and char.isalpha():
   if char.lower() in 'aieou':
       print(f"'{char}' is a Vowel.")
   else:
       print(f"'{char}' is a Consonant.")
else:
    print("Invalid Input.")


"Q7:Write a program to check if a number is divisible by 5"

number = int(input("Enter a number: "))
if number % 5 == 0:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 5.")


'Q8:Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit'
"number."

num = int(input("Enter a number: "))
num_digits = len(str(abs(num)))
if num_digits == 1:
    print(f"{num} is a single-digit number.")
elif num_digits == 2:
    print(f"{num} is a two-digit number.")
else:
    print(f"{num} has more than two digits.")


"Q9:Write a program to check whether a student has passed or failed (passing marks = 40)"

marks = int(input("Enter your marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")


"Q10:Write a program to find whether the entered number is a multiple of both 3 and 7."

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is multiple of 3 and 7.")
else:
    print(f"{num} is not multiple of 3 and 7.")




"Conditional Statement: LADDER IF & NESTED IF"

"Q1:Write a program to find the greatest among three numbers"

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if n1 >= n2 and n1 >= n3:
    print(f"{n1} is greatest.")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} is greatest.")
else:
    print(f"{n3} is greatest.")


"Q2:Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+)"

age = int(input("Enter the age: "))
if age < 0:
    print("Invalid input")
elif age < 13:
    print("The person is a Child.")
elif age <= 19:
    print("The person is a Teenager.")
elif age <= 59:
    print("The person is a Adult.")
else:
    print("The person is a Senior.")


'Q3:Write a program to assign grades based on marks:'
'90-100: A,'
'75-89: B,'
'50-74: C,'
'35-49: D,'
'<35: Fail.'

marks = int(input("Enter the marks (0-100): "))
if marks < 0 or marks > 100:
    print("Invalid marks entered.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Grade: Fail")


'Q4:Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.'

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")


"Q5:Write a program to check if a character is uppercase, lowercase, digit, or special symbol."

char = input("Enter a single character: ")
if len(char) != 1:
    print("Invalid input.")
else:
    if char.isdigit():
        print(f"'{char}' is a Digit.")
    elif char.isupper():
        print(f"'{char}' is an Uppercase letter.")
    elif char.islower():
        print(f"'{char}' is a Lowercase letter.")
    else:
        print(f"'{char}' is a Special symbol.")


'Q6:Write a program to calculate electricity bill based on units:'
'Up to 100 units: ₹5 per unit,'
'101–200 units: ₹7 per unit,'
'Above 200 units: ₹10 per unit'

num_unit = int(input("Enter the number of units: "))
if num_unit < 0:
    print("Invalid input. Units cannot be negative.")
else:
    if num_unit <= 100:
        bill = num_unit * 5
    elif num_unit <= 200:
        bill = (100 * 5) + (num_unit - 100) * 7
    else:
        bill = (100 * 5) + (100 * 7) + (num_unit - 200) * 10

    print(f"Your electricity bill is: ₹{bill}")


"Q7:Write a program to determine the largest of four numbers using nested if"

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))
if n1 >= n2:
    if n1 >= n3:
        if n1 >= n4:
            print(f"{n1} is largest.")
        else:
            print(f"{n4} is largest.")
    else:
        if n3 >= n4:
            print(f"{n3} is largest.")
        else:
            print(f"{n4} is largest.")
else:
    if n2 >= n3:
        if n2 >= n4:
            print(f"{n2} is largest.")
        else:
            print(f"{n4} is largest.")
    else:
        if n3 >= n4:
            print(f"{n3} is largest.")
        else:
            print(f"{n4} is largest.")


"Q8:Write a program to check if a given year is a century year and also a leap year"

year = int(input("Enter a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a Century and Leap Year.")
    else:
        print(f"{year} is a Century Year but not a Leap Year.")
else:
    print(f"{year} is not a Century Year.")


'Q9:Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9),'
'Obese (30+).'

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")


"Q10:Write a program to display the smallest number among three using nested if"

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if n1 <= n2:
    if n1 <= n3:
        print(f"{n1} is smallest.")
    else:
        print(f"{n3} is smallest.")
else:
    if n2 <= n3:
        print(f"{n2} is smallest.")
    else:
        print(f"{n3} is smallest.")




"Conditional Statement: FOR LOOP PROBLEM"


'Q1:Write a program using a for loop to print all armstrong numbers between 100 and 999.(Armsrong number: sum of cubes of digits equals the number itself.Example: 153=> 1^3+ 5^3+ 3^3)'

for num in range(100,1000):
    hundereds = num // 100
    tens = (num // 10) % 10
    digits = num % 10
    sum_digits = hundereds**3 + tens**3 + digits**3
    if sum_digits == num:
        print(num)


'Q2:Write a program to generate and display the first n prime numbers using a for loop.'

n = int(input("Enter the number:"))
count = 0
num = 2
for num in range(2, 1000000):
    is_prime = True
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
        if count == n:
            break


'Q3:Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.'

for num in range (1,501):
    if num % 3 == 0:
        digit_sum = sum(int(digit) for digit in str(num))
        if digit_sum <= 10:
            print(num)


'Q4:Write a program using a for loop to print a pyramid of stars(*) of height n.Example for n=4:'
'    *     '
'   ***    '
'  *****   '
' *******  '

n = int(input("Enter the height of the pyramid: "))
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ",end = "")
    for j in range(1,2 * i):
        print("*",end = "")
    print()


'Q5:Write a program to accept a string and check whether it is pangram (contains all 26 alphabets at least once) using a for loop.'

str = input("Enter a string: ").lower()
alphabet_set = set()
for char in str:
    if 'a' <= char <= 'z':
        alphabet_set.add(char)
if len(alphabet_set) == 26:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")


'Q6:Write a program using a for loop to print all twin primes between 1 and 100.(Twin primes: pairs of prime numbers with a difference of 2, eg.,(3,5),(11,13))'

for num in range(2,100):
    prime1 = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime1 = False
            break
    prime2 = True
    for j in range(2, int((num+2)**0.5) + 1):
        if (num + 2) % j == 0:
            prime2 = False
            break
    if prime1 and prime2:
        print(f"({num}, {num+2})")


'Q7:Write a program that accepts a number from the user and prints whether it is s Harshad number(number divisible by the sum of its digits) using a for loop.'

num = int(input("Enter a number: "))
str = str(num)
digit_sum = 0
for digit in str:
    digit_sum += int(digit)
if num % digit_sum == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")


'Q8:Write a program to generate Pascal Traiangle up to n rows using a for loop.'

n = int(input("Enter the nuber of rows: "))
triangle = []
for i in range(n):
       row = [1] * (i+1)
       for j in range(1,i):
           row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
       triangle.append(row)
for row in triangle:
    print(' '.join(map(str, row)))


'Q9:Write a program using a for loop to display the sum of the series:1² + 2² + 3² + ... + n²'

n = int(input("Enter the value of n: "))
total_sum = 0
for i in range(1, n+1):
    total_sum += i**2
print("Sum of the series 1^2 + 2^2 + ... + ", n, "^2 =", total_sum)


'Q10:Write a program that accepts a number from the user and prints whether it is a Strong number (sum of'
'factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145.'

num = int(input("Enter a number: "))
temp = num
sum_factorials = 0
while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum_factorials += factorial
    temp //= 10
if sum_factorials == num:
    print(f"{num} is a Strong number. ")
else:
    print(f"{num} is not a Strong number.")


"Conditional Statement: WHILE LOOP PROBLEM"

'Q1:Write a program using a while loop to find the reverse of a number and check if the reversed number is prime. Example: Input = 73 → Reverse = 37 → Prime'

num = int(input("Enter a number: "))
temp = num
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
print("Reversed Number:", reversed_num)
if reversed_num < 2:
    print(f"{reversed_num} is not prime.")
else:
    is_prime = True
    i = 2
    while i * i <= reversed_num:
        if reversed_num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(f"{reversed_num} is prime.")
    else:
        print(f"{reversed_num} is not prime.")


'Q2:Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.'

total_sum = 0
while total_sum <= 100:
    num = input("Enter a number: ")
    digit_sum = 0
    for digit in num:
        if digit.isdigit():
            digit_sum += int(digit)
    total_sum += digit_sum
    print(f"Total sum of digits: {total_sum}")
print("Sum of digits exceeded 100. Program terminated.")


'Q3:Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero, e.g., 202, 1203).'

num_str = input("enter a number: ")
if num_str[0] == '0':
    print("Not a duck number (starts with zero). ")
else:
    i = 0
    contains_zero = False
    while i < len(num_str):
        if num_str[i] == '0':
            contains_zero = True
            break
        i += 1
    if contains_zero:
        print(f"{num_str} is a Duck number.")
    else:
        print(f"{num_str} is not a Duck number.")


'Q4:Write a program using a while loop to accept a number and check if it is a Happy number. (A number is happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a happy number.'

num = int(input("enter a number: "))
visited = set()
while num != 1 and num not in visited:
    visited.add(num)
    sum_of_squares = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_squares += digit * digit
        temp //= 10
    num = sum_of_squares
if num == 1:
    print("The number is a Happy number.")
else:
    print("The number is not a Happy number.")


'Q5:Write a program using a while loop to find the largest prime factor of a given number.'

num = int(input("Enter a number: "))
largest_prime = -1
n = num
while n % 2 == 0:
    largest_prime = 2
    n //= 2
factor = 3
while factor * factor <= n:
    while n % factor == 0:
        largest_prime = factor
        n //= factor
    factor += 2
if n > 2:
    largest_prime = n
print("The largest prime factor of", num, "is", largest_prime)


'Q6:Write a program to repeatedly accept a string from the user until the string entered is a palindrome.'

while True:
    string = input("Enter a string: ")
    i = 0
    j = len(string) - 1
    is_palindrome = True
    while i < j:
        if string[i] != string[j]:
            is_palindrome = False
            break
        i += 1
        j -= 1
    if is_palindrome:
        print("The string is a palindrome.")
        break
    else:
        print("Not a palindrome. Please try again.")


'Q7:Write a program using a while loop to compute the sum of digits of a number until the result becomes a single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2.'

num = int(input("Enter a number: "))
while num >= 10:
    digit_sum = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    num = digit_sum
print("The digital root is:",num)


'Q8:Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even => n/2, if odd => 3n+1. Continue until n=1)'

num = int(input("Enter a number: "))
print("Collatz sequence:")
while num != 1:
    print(num, end=" ")
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1
print(num)


'Q9:Write a program using a while loop to accept a number and check whether it is a Kaprekar number. (Kaprekar number: if square of the number can be split into two parts whose sum equals the number. Example: 45²=2025 => 20+25=45).'

num = int(input("Enter  number: "))
square = num * num
num_str = str(num)
square_str = str(square)
result = False
len_num = len(num_str)
i = 1
while i < len(square_str):
    left = square_str[:len(square_str) - i]
    right = square_str[len(square_str) - i:]
    left_num = int(left) if left else 0
    right_num = int(right) if right else 0
    if left_num + right_num == num and right_num != 0:
        result = True
        break
    i += 1
if result or num == 1:
    print(f"{num} is a Kaprekar number.")
else:
    print(f"{num} is not a Kaprekar number.")


'Q10:Write a program to simulate an ATM machine using a while loop where a user can:'
'• Check balance'
'• Deposit money'
'• Withdraw money (only if balance is sufficient)'
'• Exit'
'Continue until the user chooses to exit.'

balance = int(input("Enter your balance"))
while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your current balance is: ${balance}")
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawl amount.")
        else:
            balance -= amount
            print(f"Please take your cash: ${amount}")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
        
        
