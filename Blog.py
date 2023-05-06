from datetime import datetime
import os

class Session:
    def __init__(self , username , password , blog):
        self.username = username
        self.password = password
        self.blog = blog
    
    def post(self , title , body):
        self.blog.post_list.append((title , body , self.username , datetime.now().strftime("%Y-%m-%d %H:%M")))
    
    def add_user(self , user , password):
        if (self.username , self.password) == self.blog.user_list[0]:
            self.blog.user_list.append((user , password))
            print("Added Successfully.")
        else:
            print("You Are Not Admin.")

class Blog:
    def __init__(self  , name , username , password):
        self.admin = username
        self.name = name
        self.password = password
        self.date = datetime.now()
        self.post_list = []
        self.user_list = [(username , password)]

    def __str__(self):
        return "This Blog Made In {} By {}.".format(self.date.strftime("%Y-%m-%d %H:%M") , self.admin)
    
    def get_session(self , username , password):
        if (username , password) in self.user_list:
            print("Logged In Successfully.")
            return Session(username , password , self)
        else:
            print("Invalid Information.")
    def show_posts(self):
        for post in self.post_list:
            print(post[0] , "\t" , post[2] , "  " , post[3])
            print("\n" , post[1] , sep = "")
            print("\n" + "__" * 50 + "\n" , sep = "")
    def posts_to_file(self):
        os.mkdir(self.name)
        os.chdir(self.name)
        for i in self.user_list:
            os.mkdir(i[0])
        for i in self.post_list:
            with open(os.getcwd() + os.path.sep + i[2] + os.path.sep + i[0] + " " + i[3].replace(":" , "-") + ".txt" , "w") as file:
                file.write(i[1])