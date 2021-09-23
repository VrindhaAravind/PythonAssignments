import requests


r=requests.get('https://jsonplaceholder.typicode.com/posts')
data=r.json()

comment=requests.get('https://jsonplaceholder.typicode.com/comments')
comments=comment.json()

def print_posts():
    for i in data:
        print(i)


def user_posts(userid):
    for i in data:
        if i['userId']==userid:
            print(i)
            # print("\nUser Id:", i.get('userId'), "\nPost Id :", i.get('id'), "\nTitle :", i.get('title'), '\nPost :',
            #       i.get('body'))



def post_details(postid):
    for i in data:
        if i['id']==postid:
            # print(i)
            print("\nUser Id:",i.get('userId'),"\nPost Id :",i.get('id'),"\nTitle :",i.get('title'),'\nPost :',i.get('body'))



def print_comments():
    for i in comments:
        print("postId:",i['postId'],"\nid:",i['id'],'\nname:',i['name'],"\nemail:",i['email'],"\nbody",i['body'],"\n")



def comment_details(postid):
    for i in comments:
        if i['postId']==postid:
            print("postId:", i['postId'], "\nid:", i['id'], '\nname:', i['name'], "\nemail:", i['email'], "\nbody",
                  i['body'], "\n")


