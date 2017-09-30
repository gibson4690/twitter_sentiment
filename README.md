## twitter_sentiment

# references
https://kenophobio.github.io/2017-01-10/deep-learning-jupyter-ec2/
https://www.youtube.com/watch?v=o_OZdbCzHUA
https://www.youtube.com/watch?v=si8zZHkufRY

# setup
source src/anaconda3/bin/activate root

jupyter notebook --generate-config
key=$(python -c "from notebook.auth import passwd; print(passwd())")

cd ~
mkdir certs
cd certs
certdir=$(pwd)
openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.key -out mycert.pem

cd ~
sed -i "1 a\
c = get_config()\\
c.NotebookApp.certfile = u'$certdir/mycert.pem'\\
c.NotebookApp.keyfile = u'$certdir/mycert.key'\\
c.NotebookApp.ip = '*'\\
c.NotebookApp.open_browser = False\\
c.NotebookApp.password = u'$key'\\
c.NotebookApp.port = 8888" .jupyter/jupyter_notebook_config.py

screen -S jupyter
mkdir notebook
cd notebook
jupyter notebook


pip install tweepy
pip install textblob
