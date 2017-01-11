installer=''
if ["$(uname)" == "Darwin" ]; then
    installer="brew"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    installer="sudo apt-get"
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    exit(1);
fi
$installer install python-devel
$installer  install python-setuptools
sudo easy_install pdfkit
$installer install gcc -y
sudo easy_install pip
sudo STATIC_DEPS=true pip install readability-lxml
sudo STATIC_DEPS=true pip install tldextract
sudo STATIC_DEPS=true pip install imgurpython
