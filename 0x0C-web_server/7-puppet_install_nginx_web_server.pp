# Install and configure an Nginx server using Puppet instead of Bash
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-get install'],
}

exec { 'apt-get install':
  provider => shell,
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Hello World!',
  require => Package['nginx'],
}

file_line { 'redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen [::]:80 default_server;',
  line   => 'rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
