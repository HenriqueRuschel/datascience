

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },]

friendships_pairs = [(0, 1), (0, 2), (1 , 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = {user["id"]: [] for user in users}

for i, j in friendships_pairs
    friendships[i].append(j)
    friendships[j].append(i)

def number_of_frieds(user):
    """quantos amigos tem o _user_?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users) 

num_users = len(users)
avg_connections = total_conections / num_users

num_friends_by_id - [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=true)

def foaf_ids_bad(user):
    """foaf significa "friend of a friend" [amigo de um amigo]"""
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

print(friendship[0])
print(friendship[1])
print(friendship[2])

from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
            foaf_id
            for friend_id in friendships[user_id]
            for foaf_id in friendships[friend_id]
            if foaf_id != user_id
            and foaf_id not in friendships[user_id]
    )

print(friends_of_friends(users[3]))

interest = [ (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"), (1, "NoSQL"), (1, "MongoBD"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"), (3, "statistics"), 

]
