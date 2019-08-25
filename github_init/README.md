# Automatic Github Initiation

Simple script that allows you to create a new project with one command.

First create an auth.txt in the root directory of this repository.
The first row of this text file should be you github username and the second row your password.


You will also need to install a driver fo a browser and put it in your PATH. If you are not using chrome then you will need to tinker a bit with the connect_github.py file. Info on this can be found on https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium

Once the auth.txt file is done and the drivers are downloaded simply run the ./install.sh in the terminal and it will place an exe file called create in /usr/local/bin/.
If it bothers you then just put the file it creates somewhere in your PATH.

After the installation go ahead and typ the command "create my_first_project" 


If you are working in intellij IDEA then go ahead and remove the "#" at line 10 in "install.sh" as it will allow you to automatically open up the project in idea.
