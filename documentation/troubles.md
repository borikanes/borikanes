## nginx on raspbian
I had a few troubles with making nginx work on raspbian. Initially when i did `sudo apt-get install nginx` (even after i did `sudo apt-get update`) it installed an older version so i manually installed nginx1.8.0.....why? because i was having troubles with the older version(1.4.6) and hoped a newer/updated version will help. I manually installed it by doing the following

      curl http://nginx.org/keys/nginx_signing.key | apt-key add -
      # cd into /etc/apt/sources.list.d/
      # if nginx.list doesn't exist then `touch nginx.list`
      echo -e "deb-src http://nginx.org/packages/debian/ squeeze nginx" > /etc/apt/sources.list.d/nginx.list
      # you can cd into ~/.ssh here if you want to keep the key there
      wget http://nginx.org/keys/nginx_signing.key
      sudo apt-key add nginx_signing.key
      sudo apt-get update
      sudo apt-get build-dep nginx
      # you can do this part below in any directory
      mkdir src
      cd src/
      sudo apt-get source nginx
      cd nginx-1.8.0/
      dpkg-buildpackage -uc -b
      cd ..
      sudo dpkg -i nginx_1.8.0-1~squeeze_amd64.deb

If you do `sudo nginx -v` it should say 1.8.0

### Starting nginx
If you run `sudo nginx` and you check `localhost:80` it should show the default welcom to nginx page

#### proxying with nginx ?
Go into your nginx.conf file in `/etc/nginx/` and add this server block

          server / {

            listen 80;
            server_name localhost;

            location / {
                proxy_pass http://localhost:8080/; #obviously change the port number if yours isn't running on 8080
            }
          }
Run `sudo nginx -s reload`
If you get an warning like this

      nginx: [warn] conflicting server name "localhost" on 0.0.0.0:80, ignored

go into `/etc/nginx/conf.d/` and open the default.conf file and comment out the whole file.

Run `sudo nginx -s reload` and you should be good to go

### GitHub Webhook errors
Using GitHub's Webhook seem to be slow. I basically had to create a route that data will be pushed to.  When that route is called with the data it takes the data and saves it locally in a file that i will then parse.  The file seems to be there but after a few minutes which i think is really weird.
