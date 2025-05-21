# Attributes
class User:
    # __init_ constructuor thats set the initial values of that class attribute 
    #  whenever we create specific object for that class
    def __init__(self, usr_email, usr_name, password, current_job_title):
        self.email = usr_email
        self.name= usr_name
        self.password = password
        self.current_job_title = current_job_title

    # Then in this constructed object we can change password or job title
    # Functions that belongs to an object called methods
    
    def change_pwd(self, user_new_password): # Method #1
        self.password = user_new_password
    def change_job_title(self, user_new_job_title): # Method #2
        self.current_job_title = user_new_job_title
    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")



