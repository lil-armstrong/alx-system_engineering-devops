
# Installs a Nginx server

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "/^\s*server_name\s*_;/a \\\n\tlocation /redirect_me {\n\t\treturn 301 http://tired.com;\n\t}\n" "/etc/nginx/sites-available/default" ; sudo service nginx start',
}
