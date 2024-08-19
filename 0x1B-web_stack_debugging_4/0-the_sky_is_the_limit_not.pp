# Puppet used to fix our stack so that we get to 0 requests failed

exec { 'modify limit':
  provider => shell,
  command  => "sed -i 's/15/4096/' /etc/default/nginx && sudo service nginx restart",
}
