# This Puppet manifest updates file descriptor limits for the holberton user to avoid "Too many open files" errors.

exec { 'update-file-limits-for-holberton':
  command => '/usr/bin/env bash -c "sed -i \'/holberton hard/s/5/50000/\' /etc/security/limits.conf && sed -i \'/holberton soft/s/4/50000/\' /etc/security/limits.conf"',
  path    => ['/usr/bin', '/bin'],
}
