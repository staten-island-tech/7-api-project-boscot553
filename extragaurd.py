def isvalid(email, password):
    ats = 0
    ints = 0
    caps = 0
    integer =["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    captials =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
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
        if char in captials:
            caps += 1
    if ints < 1:
        print("Password must have at least one integer")
        return
    if caps < 1:
        print("Password must have at least one captial letter")
        return
    print(f"Email: {email}, Password: {password}")
isvalid("J@.net", "2025Jiscool")