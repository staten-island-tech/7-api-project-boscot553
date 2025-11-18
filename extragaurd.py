def isvalid(email, password):
    ats = 0
    ints = 0
    integer =["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if isinstance(email, str):
        ats = 0
    else:
        print("Email must be a string")
        return
    for char in email:
        if char == "@":
            ats += 1
    if ats != 1:
        print("Email must have one @ sign.")
        return
    if isinstance(password, str):
        ats = 1
    else:
        print("Password must be a string")
        return
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        return
    for char in password:
        if char in integer:
            ints += 1
        if char.isupper():
            print("Password must contain at least one upper case letter")
            return
    if ints < 1:
        print("Password must have at least one integer")
        return
isvalid("jjjjj@", "gGgggggggg")