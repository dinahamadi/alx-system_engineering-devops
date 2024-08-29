# Ensure the WordPress configuration file is present and has the correct permissions

file { '/var/www/html/wp-config.php':
  ensure  => 'file',
  source  => 'puppet:///modules/wordpress/wp-config.php',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Ensure the necessary directories have the correct permissions
file { '/var/www/html/wp-content':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

file { '/var/www/html/wp-content/uploads':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

# Restart Apache service to apply changes
exec { 'restart_apache':
  command     => '/usr/sbin/apache2ctl restart',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-config.php'],
}
