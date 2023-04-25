# Install a package using Puppet exec and package resource
  package { 'python3-pip':
    ensure => installed
  }

  exec { 'install_flask_with_pip3':
    command => 'pip3 install flask==2.1.0',
    path    => ['/usr/bin', '/usr/sbin',],
    unless  => 'pip3 show flask | grep "Version: 2.1.0"',
    require => Package['python3-pip']
  }
