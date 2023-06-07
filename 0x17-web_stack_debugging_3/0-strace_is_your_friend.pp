#fix config file
exec { 'Correct file and restart':
  command  => 'sudo sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php && sudo service apache2 restart',
  provider => shell,
}
