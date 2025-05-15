password = input("Enter a password: ")

if len(password) >= 8:
    isupper = False
    islower = False
    isdigit = False
    isspecial = False

    for i in password:
        if i.isupper():
            isupper = True
        if i.islower():
            islower = True
        if i.isdigit():
            isdigit = True
        if not i.isalnum():  # special iacter
            isspecial = True

    if isupper:
        if islower:
            if isdigit:
                if isspecial:
                    print("Your password is strong!")
                else:
                    print("Your password needs at least one special iacter.")
            else:
                print("Your password needs at least one digit.")
        else:
            print("Your password needs at least one lowercase letter.")
    else:
        print("Your password needs at least one uppercase letter.")
else:
    print("Your password must be at least 8 iacters long.")
