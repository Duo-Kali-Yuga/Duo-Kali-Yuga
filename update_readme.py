import random

# Define your projects list
projects = [
    {
        "title": "Hello World Project",
        "link": "http://example.com",
        "description": "This is a basic Hello World project.",
    },
    {
        "title": "Advanced Project",
        "link": "http://example2.com",
        "description": "This project does something advanced.",
    },
]

# Pick a random project
project = random.choice(projects)

# Define the content for the random project section
random_project_section = f"""
## 🔹Random Project:

**[{project['title']}]({project['link']})**

{project['description']}
"""
project = random.choice(projects)

random_project_section = f"""
## 🔹Random Project:

**[{project['title']}]({project['link']})**

{project['description']}
"""

# Read the README file
with open("README.md", "r") as file:
    lines = file.readlines()

# Write to README and replace the "Random Project" section
with open("README.md", "w") as file:
    for line in lines:
        if line.strip() == "## 🔹Random Project:":
            break
        file.write(line)
    file.write(random_project_section)
