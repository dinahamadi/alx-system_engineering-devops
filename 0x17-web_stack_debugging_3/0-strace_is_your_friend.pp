# fix_wordpress.pp
# This Puppet manifest fixes the 'phpp' to 'php' issue in the WordPress wp-settings.php file.

# Execute the sed command to replace 'phpp' with 'php' in the wp-settings.php file
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin'],
  onlyif  => 'grep -q phpp /var/www/html/wp-settings.php',
  notify  => Exec['restart-apache'],
}

# Restart Apache if the file is changed
exec { 'restart-apache':
  command     => '/usr/sbin/service apache2 restart',
  path        => ['/usr/local/bin', '/bin'],
  refreshonly => true,
}
