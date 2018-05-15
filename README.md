# Fortana's website

## Development
`npm install`, then `npm run dev`. Then open `index.html` in your browser.

## Lead form
Using [formspree](https://formspree.io/).

## NGINX and SSL
Files are served from `/var/www/public`. Dependencies: `sudo mkdir /var/www/public/`, then `sudo chown ubuntu:ubuntu /var/www/public/`.

`sudo systemctl stop|start|restart|reload nginx`

__DON'T USE THIS SYNTAX__: `sudo service nginx stop|start|restart|reload`. `service` is a wrapper around various init systems, but Ubuntu 16 uses `systemd`. [The main command used to introspect and control systemd is systemctl](https://wiki.archlinux.org/index.php/systemd#Basic_systemctl_usage).

## SSH
`ssh -i ~/.ssh/fortana ubuntu@34.216.168.46`

### Certbot automatic renewal
Test by running `sudo certbot renew --dry-run`.

## Deployment
Run `npm run deploy`.
