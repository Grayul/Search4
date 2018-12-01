RED="\033[31m"
YELLOW="\033[33m"
BLUE='\033[1;34m'


echo -e $RED Installing required python modules
sudo pip install json
sudo pip install sys
sudo pip install time
sudo pip install argparse
sudo pip install requests
clear
sleep 2 
sudo chmod +x search4.py
sudo cp search4.py /user/bin/search4
echo -e $YELLOW use search4 coomand on the terminal to use the tool.
