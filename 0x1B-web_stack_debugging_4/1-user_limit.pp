# This Puppet manifest updates file descriptor limits for the holberton user to avoid "Too many open files" errors.

exec { 'update-holberton-hard-file-limit':
  command => '/usr/bin/env bash -c "sed -i \'s/holberton hard nofile [0-9]*/holberton hard nofile 50000/\' /etc/security/limits.conf"',
  path    => ['/usr/bin', '/bin'],
  unless  => 'grep -q "holberton hard nofile 50000" /etc/security/limits.conf',
}

exec { 'update-holberton-soft-file-limit':
  command => '/usr/bin/env bash -c "sed -i \'s/holberton soft nofile [0-9]*/holberton soft nofile 50000/\' /etc/security/limits.conf"',
  path    => ['/usr/bin', '/bin'],
  unless  => 'grep -q "holberton soft nofile 50000" /etc/security/limits.conf',
}
