from urllib.request import urlopen

import json

url_post = 'https://jsonplaceholder.typicode.com/posts'
url_comment = 'https://jsonplaceholder.typicode.com/comments'


def post_detail():
    global post_data
    return list(post_data[0].keys())



def post_get():
    global post_data
    return post_data


def post_bsd_user(x):
    global post_data
    # User ID should be a number between 1 and 10 both included
    temp=[]
    for i in post_data:
        if i['userId'] == x:
            temp.append(i)
    return temp

def comment_get():
    global comment_data
    # print('Comment data contains: ', comment_data[0].keys(), '\n')
    return comment_data



def comment_bsd_post(x):
    global comment_data
    # Post ID should be between 1 and 100 both included
    temp=[]
    for i in comment_data:
        if i['postId'] == x:
            temp.append(i)
    return temp

# Fetching Post Data
response_post = urlopen(url_post)
post_data = json.loads(response_post.read())

# Fetching comment Data
response_comment = urlopen(url_comment)
comment_data = json.loads(response_comment.read())

# Post Functions
print('The Post data contains :', post_detail(),'\n')
[print(i) for i in post_get()]
[print(i) for i in post_bsd_user(int(input('\nEnter the required UserId :')))]

# Comment Functions
[print(i) for i in comment_get()]
[print(i) for i in  comment_bsd_post(int(input('\nEnter the required postId :')))]