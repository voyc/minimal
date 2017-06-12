# build icon

# compile the js files with google closure compiler
python compilejs.py $1 >min.js

# compress css file with yui
cat normaleyes.css icon/icon.css minimal.css >min.css
java -jar ~/bin/yuicompressor/yuicompressor-2.4.2.jar min.css -o min.css --charset utf-8

# prepare index.php for production use
cp index.html index.php
sed -i -e 's/<!--<remove>//g' index.php
sed -i -e 's/<remove>-->//g' index.php
