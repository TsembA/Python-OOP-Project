# 🧑‍💻 Python OOP Project – User & Post Classes

This is a Python project that demonstrates the fundamentals of **Object-Oriented Programming (OOP)** using two simple classes: `User` and `Post`.

---

## 📚 Overview

This project simulates a basic system where users can be created and assigned roles. Each user can create posts, and each post is linked to the user who authored it.

---

## 🏗️ Structure

- `User`: Represents a person with email, name, password, and job title.
- `Post`: Represents a simple message created by a user.

---

## 📁 File Layout

```
.
├── user.py     # Contains the User class
├── post.py     # Contains the Post class
└── main.py     # Demonstrates how the classes are used
```

---

## 🔍 Features

### ✅ User Class

- Create a user with:
  - Email
  - Name
  - Password
  - Job title
- Change password: `change_pwd(new_password)`
- Change job title: `change_job_title(new_title)`
- Display info: `get_user_info()`

### 📝 Post Class

- Create a post with:
  - Message
  - Author (a user)
- Display post info: `get_post_info()`

---

## 🧪 Example Usage

```python
from user import User
from post import Post

app_user_one = User("arno@example.com", "Arno", "password", "Dance Teacher")
app_user_one.get_user_info()

app_user_one.change_job_title("Junior Devops")
app_user_one.get_user_info()

app_user_two = User("Peter@example.com", "Peter Griffin", "Drunking Clam", "Chill guy")
app_user_two.get_user_info()

new_post = Post("Teach Megan how to be a real man!", app_user_two.name)
new_post.get_post_info()
```

### ✅ Output

```
User Arno currently works as a Dance Teacher. You can contact them at arno@example.com
User Arno currently works as a Junior Devops. You can contact them at arno@example.com
User Peter Griffin currently works as a Chill guy. You can contact them at Peter@example.com
Post: Teach Megan how to be a real man! Written by Peter Griffin
```
