

set -e

cd /var/www/tictactoe

pip3 install flask
chown -R apache:apache /var/www/tictactoe
chmod -R 755 /var/www/tictactoe