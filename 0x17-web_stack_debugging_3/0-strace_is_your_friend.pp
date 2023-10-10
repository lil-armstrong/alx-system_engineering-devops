file { '/var/www/html/index.html':
  ensure  => 'file',
  content => '
    <!DOCTYPE html>
    <html>
    <head>
      <title>My Puppet HTML Page</title>
    </head>
    <body>
      <h1>Welcome to my Puppet-generated HTML page!</h1>
      <p>This is a basic index file created with Puppet.</p>
    </body>
    </html>
  ',
}