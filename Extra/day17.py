class User:

    def __init__(self, name, id, number):
        self.name = name
        self.id = id
        self.followers = 0
        self.following = 0
        # print(f"This is object {number}")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("User 1","u1",1)
print("user 1 followers:", user1.followers)
print("user 1 following:", user1.following)
print()

user2 = User("User 2","u2",2)
user2.follow(user1)
print("user 1 followers:", user1.followers)
print("user 1 following:", user1.following)
print()

print("user 2 followers:", user2.followers)
print("user 2 following:", user2.following)

=