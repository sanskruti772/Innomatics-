#Question 1
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

#Question 2
    
    

marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

for m in marks:
    if m >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Total Pass Students:", pass_count)
print("Total Fail Students:", fail_count)