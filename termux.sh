
echo Installing requirements ...

apt update -y
apt upgrade -y
pkg install python -y
pip install --upgrade pip
pip install requests
clear

cd $HOME/Search4

chmod +x search4.py

echo use python search4.py to run the script.
