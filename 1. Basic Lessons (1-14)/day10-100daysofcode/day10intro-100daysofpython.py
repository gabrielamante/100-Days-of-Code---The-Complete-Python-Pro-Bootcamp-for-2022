# Fuctions with outputs

def format_name(f_name,l_name):
    """ Take a first and last last name and format it to return the title case version of the name. """
    firstname = f_name.title()
    lastname = l_name.title()
    return f"{firstname} {lastname}"

print(format_name("gAbrIEl", "AmaNTe"))