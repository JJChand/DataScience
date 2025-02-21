from __future__ import division
from collections import Counter
from collections import defaultdict

users = [{"id": 0, "name": "Hero"},
         {"id": 1, "name": "Dunn"},
         {"id": 2, "name": "Sue"},
         {"id": 3, "name": "Chi"},
         {"id": 4, "name": "Thor"},
         {"id": 5, "name": "Clive"},
         {"id": 6, "name": "Hicks"},
         {"id": 7, "name": "Devin"},
         {"id": 8, "name": "Kate"},
         {"id": 9, "name": "Klein"},]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(z):
    return len(z["friends"])

'''for user in users:
    print(user["id"], user["name"], number_of_friends(user))''' # This is to find the number of friends for each user

total_connections = sum(number_of_friends(user) for user in users) # This is to find the total number of connections
num_users = len(users)
avg_connections = total_connections / num_users
'''print(avg_connections)'''

num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]
sorted(num_friends_by_id,
       key=lambda x: x[1],
       reverse=True)

print(num_friends_by_id)

def friends_of_friends_ids_bad(user):
    return[foaf["id"]
           for friend in user["friends"]
           for foaf in friend["friends"]
           ]
#print(friends_of_friends_ids_bad(users[0]))


def not_the_same(user1, other_user):
    return user1["id"] != other_user["id"]
def not_friends(user, other_user):
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])

def friends_of_friends_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf)
                   and not_friends(user, foaf))

'''id = int(input())
print(friends_of_friends_ids(users[id]))'''

interests = [(0, "Hadoop"), (0, "Big data"), (0,"HBase"), (0, "Java"),
            (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
            (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
            (1, "Postgres"), (2, "Python"), (2, "Scikit-learn"),(2, "scipy"),
            (2, "numpy"), (2, "statsmodels"), (2, "pandas"),(3, "R"), (3, "Python"),
            (3, "statistics"), (3, "regression"), (3, "probability"),
            (4, "machine learning"), (4, "regression"), (4, "decision trees"),
            (4, "libsvm"), (5, "Python"), (5, "R"),(5, "Hava"),(5, "C++"),
            (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
            (6, "probability"), (6, "mathematics"), (6, "theory"),
            (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
            (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
            (8, "Big data"), (8, "artificial intelligence"), (9, "Hadoop"),
            (9, "Java"), (9, "Mapreduce"), (9, "Big data")]

def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
#print(user_ids_by_interest)
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
#print(interests_by_user_id)

def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])
#print(most_common_interests_with(users[0]))

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
#print(salary_by_tenure)

average_salary_by_tenure = {
    tenure : sum(salary) / len(salary)
    for tenure, salary in salary_by_tenure.items()
}













