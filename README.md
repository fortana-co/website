# Fortana's website

## Development
`npm install`, then `npm run dev`. Then open `index.html` in your browser.

## Lead form
Using [formspree](https://formspree.io/).

## NGINX and SSL
Files are served from `/var/www/public`. Dependencies: `sudo mkdir /var/www/public/`, then `sudo chown ubuntu:ubuntu /var/www/public/`.

`sudo service nginx stop|start|restart|reload`.

### Certbot automatic renewal
Test by running `sudo certbot renew --dry-run`.

## Deployment
Run `npm run deploy`.
