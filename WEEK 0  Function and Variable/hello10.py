#Ask user for their name
name = input(" what's your name " ).strip().title()
# Remove Whitespace From str and Capitalize user's name

#Split user.s name into first name and last name
first, last = name.split("")


# Say hello to user
print(f"hello, {first}")
