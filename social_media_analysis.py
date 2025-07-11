"""
2) Task : Social Media Interaction Analysis

Analyze social media posts and interactions to find top influencers and engagement trends.


posts = [
    {"user": "alice", "likes": 120, "comments": 12, "shares": 8, "topic": "tech"},
    {"user": "bob", "likes": 200, "comments": 22, "shares": 14, "topic": "travel"},
    {"user": "alice", "likes": 90, "comments": 10, "shares": 5, "topic": "tech"},
    {"user": "diana", "likes": 300, "comments": 40, "shares": 25, "topic": "health"},
    {"user": "bob", "likes": 100, "comments": 12, "shares": 7, "topic": "travel"},
]

Calculate total engagement per user (likes + comments + shares).
Identify the top influencer (highest average engagement per post).
Calculate topic-wise engagement.
Find the most engaging topic.

"""

total = {}
topic_total = {}

posts = [
    {"user": "Alice", "likes": 120, "comments": 12, "shares": 8, "topic": "Tech"},
    {"user": "Bob", "likes": 200, "comments": 22, "shares": 14, "topic": "Travel"},
    {"user": "Alice", "likes": 90, "comments": 10, "shares": 5, "topic": "Tech"},
    {"user": "Diana", "likes": 300, "comments": 40, "shares": 25, "topic": "Health"},
    {"user": "Bob", "likes": 100, "comments": 12, "shares": 7, "topic": "Travel"},
]

for i in posts:
    user = i['user']
    likes = i['likes']
    comments = i['comments']
    shares = i['shares']

    if user not in total:
        total[user] = {'engagement': 0, 'posts': 1}
        total[user]['engagement'] = (likes+comments+shares)
        total[user]['eng_per_post'] = total[user]['engagement']/total[user]['posts']
    else:
        total[user]['posts'] += 1
        total[user]['engagement'] += (likes+comments+shares)
        total[user]['eng_per_post'] = total[user]['engagement']/total[user]['posts']

for i in posts:
    user = i['user']
    likes = i['likes']
    comments = i['comments']
    shares = i['shares']
    topic = i['topic']

    if topic not in topic_total:
        topic_total[topic] = {'engagement': 0}
        topic_total[topic]['engagement'] = (likes+comments+shares)
    else:
        topic_total[topic]['engagement'] += (likes+comments+shares)

top = max(total, key = lambda x : total[x]['eng_per_post'])
most_eng_topic = max(topic_total, key = lambda x : topic_total[x]['engagement'])

for i in total:
    print(f"Total engagement of {i} is {total[i]['engagement']}")

print()
print(f"The top influencer (highest average engagement per post) is {top}")
print()

for i in topic_total:
    print(f"Topic-wise engagement for {i} is {topic_total[i]['engagement']}")

print()

print(f"The most engaging topic is {most_eng_topic}")
