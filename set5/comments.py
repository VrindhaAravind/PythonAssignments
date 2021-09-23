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

def comment(postid):
    for i in comments:
        if i['postId']==postid:
            print(i)
comment(1)
# print("Select ptions: 1. Print complete posts from all user. 2. Posts from a particular user,given the post")
# ans=input()
# # if ans=='Y':
# print_posts()
choice=input("Get details of 1.Posts, 2.Comments :")
if choice=='1':
    ans=input("Want to print all posts from user?")
    if ans=='yes':
        print_posts()
    else:
        ans1=input("Want post of a particular user?")
        if ans1=='yes':
            uid=int(input("Enter user id :"))
            user_posts(uid)
        else:
            ans2=input("Want details of a post?")
            if ans2=='yes':
                inp = int(input("Enter post id :"))
                post_details(inp)
            else:
                print("Invalid input")
elif choice=='2':
    ans=input("Want to print all comments?(Y/N)")
    if ans=='Y':
        print_comments()
    else:
        ans2=input("Want comments of particular post?(Y/N)")
        if ans2=='Y':
            inp = int(input("Enter post id :"))
            comment_details(inp)
        else:
            print("invalid input")

else:
    print("Invalid Option")