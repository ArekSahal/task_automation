#!/bin/bash

path_to_cur=${PWD}

cd src
path_to_run=${PWD}
cd ..
echo "#!/bin/bash" > create
echo "python3 ${path_to_run}/main.py \$1 ${path_to_cur}/auth.txt" >> create
#echo "idea /Users/areksahal/projects/\$1" >> create
echo "cd /Users/areksahal/projects/\$1" >> create
mv create /usr/local/bin/
cd /usr/local/bin/
chmod u+x create
mkdir ~/projects
cd $path_to_cur
python3 -m pip install subprocess , selenium

echo "You can now write 'create <project name>' to init a github project in you projects folder"


