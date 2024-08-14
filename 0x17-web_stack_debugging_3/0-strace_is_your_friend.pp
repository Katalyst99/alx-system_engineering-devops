# Puppet used to fix Apache returning a 500 error issue,

exec { 'fix php issue':
  provider => shell,
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
