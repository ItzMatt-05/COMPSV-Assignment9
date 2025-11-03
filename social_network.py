class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of Person objects representing this person's friends.
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''
    def __init__(self, name):
        self.name=name
        self.friends=[]
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
class SocialNetwork:
    '''
    A class representing a social network using an adjacency list.
    Attributes:
        people (dict): Maps a person's name to their Person instance.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Connects two people as friends (bidirectional).
        print_network(): Prints out the network of people and their friends.
    '''
    def __init__(self):
        self.people={}
    def add_person(self, name):
        if name not in self.people:
            self.people[name]=Person(name)
        else:
            print(f"{name} already exists in the network.")
    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both people do not exist!")
            return
        person1=self.people[person1_name]
        person2=self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)
    def print_network(self):
        for name, person in self.people.items():
            friend_names=[friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names) if friend_names else 'No friends yet'}")
if __name__=="__main__":
    network=SocialNetwork()
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")
    network.print_network()
"""
A graph is the right choice for showing a social network because it can handle lots of people and connections that go both ways in that each person is a node, and friendships are the lines connecting them. 
Lists and trees don’t work well here. A list only shows items in order, and a tree needs a top or root. 
Friendships aren’t like that, they’re equal and can go in many directions.
Since every person keeps a list of their friends, an adjacency network is a good fit because not everyone is friends with everyone else, so it ultimately saves memory. 
Adding new people or friendships is quick and it’s easy to see who someone’s friends are too. 
The only part that slows it down a bit is when checking if two people are already connected, since the code has to look through their list.
This setup works like real social media apps such as Facebook or LinkedIn, where people add each other over time. 
Printing the network just loops through everyone and lists their friends. 
Overall, using a graph makes sense because it’s simple, flexible, and shows real-world connections the way they actually are, no hierarchy, just people linked together.
"""
