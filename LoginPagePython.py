import re

emailPattern = "[a-zA-Z0-9]+@[A-Za-z]+\.(com|edu|org)"
phoneNumberPattern = r"^[+][0-9]{2}[1-9]{2}[0-9]{7}$"


def emailChecker(emailInput):
    if re.match(emailPattern, emailInput):
        # print("Valid Email Address")
        pass
    else:
        print("Invalid Email Address")
        exit(0)


def phoneNumberChecker(numberInput):
    if re.search(phoneNumberPattern, numberInput):
        # print("Valid Phone number")
        pass
    else:
        print("Invalid Phone Number")
        exit(0)


def passWordChecker(pswrd1, pswrd2, name,number,email):
    if pswrd1 == pswrd2:
        print("\nLogin Successful!")
        print("Name : " + name + "\nPhoneNumber : " + number + "\nEmail : " + email)
    else:
        print("\nLogin Unsuccessfull\nPasswords not matched")
        exit(0)


if __name__ == '__main__':
    name = input("Input User Name : ")
    phoneNumber = input("Enter your Mobile Number : ")
    phoneNumberChecker(phoneNumber)
    emailAddress = input("Enter your Email : ")
    emailChecker(emailAddress)
    ps1 = input("Enter your password : ")
    ps2 = input("Re-Enter the password : ")
    passWordChecker(ps1,ps2,name,phoneNumber,emailAddress)
