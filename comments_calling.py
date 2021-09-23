import comments

choice=input("Get details of 1.Posts, 2.Comments :")
if choice=='1':
    ans=input("Want to print all posts from user?")
    if ans=='yes':
        comments.print_posts()
    else:
        ans1=input("Want post of a particular user?")
        if ans1=='yes':
            uid=int(input("Enter user id :"))
            comments.user_posts(uid)
        else:
            ans2=input("Want details of a post?")
            if ans2=='yes':
                inp = int(input("Enter post id :"))
                comments.post_details(inp)
            else:
                print("Invalid input")
elif choice=='2':
    ans=input("Want to print all comments?(Y/N)")
    if ans=='Y':
        comments.print_comments()
    else:
        ans2=input("Want comments of particular post?(Y/N)")
        if ans2=='Y':
            inp = int(input("Enter post id :"))
            comments.comment_details(inp)
        else:
            print("invalid input")

else:
    print("Invalid Option")