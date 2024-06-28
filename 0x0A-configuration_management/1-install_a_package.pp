#install flask from pip3
package { 'python3-pip':
  ensure  => 'installed',
  require => Exec['apt-get install']
}

exec { 'apt-get install':
  command  => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.1.1'
}
