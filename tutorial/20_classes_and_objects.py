import datetime

class User:
    pass

# user1 is an instance of class User
# user1 is object
# first_name, last_name - fields: Data attached to an object
# "...lowercase with words separated by underscores as necessary to improve readability"
user1 = User()
user1.first_name = "Dave"
user1.last_name = "Bowman"

user2 = User()
user1.first_name = "Frank"
user1.last_name = "Pole"

user1.age = 37
user2.favourite_book = "2001: Space Odyssey"

class Profile:
    # Docstring
    """A member of FriendFace. For now we are 
    only storing their name and birthday.
    But soon we will store an uncomfortable
    amount of user infromation."""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # yyyymmdd
            # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

profile = Profile("Dave Bowman", "19710315")
print(profile.name)
print(profile.first_name)
print(profile.last_name)
print(profile.birthday)
print(profile.age())


