# Mad Libs about a person. This program's goal is to get the computer to know who you are.

print("We want to know who you are...")
print("Answer the following questions so we can get to know you! ")

mad_list = []

firstName = input("What is your first name? ")
mad_list.append(firstName)

age = input("How old are you? ")
mad_list.append(age)

    
first_thing_you_do_for_fun = input("What do you do for fun? (say something like 'play video games'")
mad_list.append(first_thing_you_do_for_fun)

second_thing_you_do_for_fun = input("What's another thing you like to do for fun? ")
mad_list.append(second_thing_you_do_for_fun)

# print(mad_list)


def test():
    print("Hey, my name is %s . I am %s years old. For fun, I like to %s and %s." % (firstName, age, first_thing_you_do_for_fun, second_thing_you_do_for_fun) )   

test()
