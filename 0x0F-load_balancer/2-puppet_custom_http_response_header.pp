
# create a custom HTTP header response
package { 'nginx':
	ensure => installed
}

exec { 'setup':
	provider => shell,
	command => 'sudo echo "add_header X-Served-By \$hostname;" > /etc/nginx/conf.d/custom_header.conf; sudo sed -i "/^\s*server_name\s*_;/a \\\n\tinclude /etc/nginx/conf.d/custom_header.conf;" "/etc/nginx/sites-available/default"; sudo nginx -t && sudo systemctl restart nginx',
	require => Package['nginx']
}
