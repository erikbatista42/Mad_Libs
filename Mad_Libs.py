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

favColor = input("What's your favorite color? ")
mad_list.append(favColor)

num_of_siblings = input("How many siblings do you have? ")
mad_list.append(num_of_siblings)

what_you_do_for_work = input("What do you do for work? (example: make sandwiches) ")
mad_list.append(what_you_do_for_work)

fav_place_to_be = input("What is your favorite place to be? ")
mad_list.append(fav_place_to_be)

name_of_closest_person = input("What's the name of the closest person to you? ")
mad_list.append(name_of_closest_person)

where_you_from = input("Where are you from? ")
mad_list.append(where_you_from)

where_do_you_live = input("Where do you currently live? ")
mad_list.append(where_do_you_live)

what_type_of_music_you_listen_to = input("What type of music do you listen to? ")
mad_list.append(what_type_of_music_you_listen_to)

one_thing_you_want_to_learn = input("What's one thing you want to learn? (example: drawing) ")
mad_list.append(one_thing_you_want_to_learn)

fav_shoe_brand = input("What's your favorite shoe brand? (example: Adidas)")
mad_list.append(fav_shoe_brand)

shoe_size = float(input("What's your shoe size?"))
mad_list.append(shoe_size)

# print(mad_list)
# myTup = {"erik" : 18}

def test():
    print("Hey, my name is %s . I am %s years old. For fun, I like to %s and %s. My favorite color is %s. I have %s siblings. For work, I %s. My favorite place to be is %s. The closest person to me is %s. I'm from %s and I live in %s. I like to listen to %s. One thing I want to learn is %s. My favorite shoe brand is %s. My shoe size is %s." % (firstName, age, first_thing_you_do_for_fun, second_thing_you_do_for_fun, favColor, num_of_siblings, what_you_do_for_work, fav_place_to_be, name_of_closest_person, where_you_from, where_do_you_live, what_type_of_music_you_listen_to, one_thing_you_want_to_learn, fav_shoe_brand, shoe_size) )   

test()
