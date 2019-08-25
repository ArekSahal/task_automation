from subprocess import run
import sys
from connect_github import create_github_rep

#Get user for correct path. Probably a really bad way of doing it but it works for me
response = run("who", capture_output=True)
user = str(response.stdout).replace("b'", "").split(" ")[0]

cred_path = sys.argv[2]
cred = []
with open(cred_path, "r") as file:
    for line in file:
        cred.append(line.replace("\n", ""))

path_to_dir = "/Users/" + user + "/projects"
project_name = sys.argv[1]
path = path_to_dir + "/" + project_name


#Create github repository
clone_link = create_github_rep(project_name, cred)

#Push README file and check if everything is OK
run(["git", "clone", clone_link], cwd=path_to_dir)
run(["touch", "README.md"], cwd=path)
run(["echo", " # " + project_name, ">", "README.md"], cwd=path) #This does not work. The file is just empty
run(["git", "add", "*"], cwd=path)
run(["git", "commit", "-a", "-m", "'first commit'"], cwd=path)
run(["git", "push"], cwd=path)



print(" \n \n Project is now initialized. Here, have a cookie. \n")