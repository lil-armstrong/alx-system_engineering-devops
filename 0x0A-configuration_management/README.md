# 0x0A. Configuration management

# Tasks
## Install Puppet

	```bash
	apt install -y ruby=1.:2.7+1 --allow-downgrades
	apt install -y ruby-augeas
	apt install -y ruby-shadow
	apt install -y puppet

	# install puppet lint
	gem install puppet-lint
	```

## 0. Create a file
	Using Puppet, create a file in /tmp
	- File path is `/tmp/school`
	- File permission is `0744`
	- File owner is `www-data`
	- File group is `www-data`
	- File contains `I love Puppet`

## 1. install a package
	Using Puppet, install `flask` from `pip3`.
	- install `flask`
	- Version must be `2.1.0`

## 2. Execute a command
	Using Puppet, create a manifest that kills process named `killmenow`
	- Must use `exec` Puppet resource
	- Must use `pkill`
