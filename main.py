from user import User
from post import Post
# Create object from the class
app_user_one = User("arno@example.com", "Arno", "password", "Dance Teacher")
app_user_one.get_user_info()

app_user_one.change_job_title("Junior Devops")
app_user_one.get_user_info()

app_user_two = User("Peter@example.com", "Peter Griffin", "Drunking Clam", "Chill guy")
app_user_two.get_user_info()

new_post = Post("Teach Megan how to be a real man!", app_user_two.name)
new_post.get_post_info()