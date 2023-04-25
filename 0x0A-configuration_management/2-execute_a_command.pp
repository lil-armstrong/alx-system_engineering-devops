# Execute a command using Puppet exec resource

exec {'killmenow':
  command  => 'pkill -f killmenow',
  path    => '/usr/bin'
}
