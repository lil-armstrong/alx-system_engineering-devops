# Script fixes Apache missing index.html file

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => '
    <!DOCTYPE html>
    <html>
    <head>
      <title>Holberton &#8211; Just another WordPress site</title>
      <link rel="alternate" 
      type="application/rss+xml" 
      title="Holberton &raquo; Feed" 
      href="http://127.0.0.1/?feed=rss2" />
      <link rel="alternate" 
      type="application/rss+xml" 
      title="Holberton &raquo; Comments Feed" 
      href="http://127.0.0.1/?feed=comments-rss2" />
    </head>
    <body>
      <h1 class="site-title">
        <a href="http://127.0.0.1/" rel="home">Holberton</a>
      </h1>
      <p>Yet another bug by a Holberton student</p>
      <div>
        <div id="wp-custom-header" 
        class="wp-custom-header">
          <img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" 
          width="2000" 
          height="1200" 
          alt="Holberton" />
        </div>
      </div>
    </body>
    </html>
  ',
}