# Tasks

## 0. Block all incoming traffic but

Let’s install the `ufw` firewall and setup a few rules on `web-01`.

**Requirements:**

    - The requirements below must be applied to `web-01` (feel free to do it on `lb-01` and `web-02`, but it won’t be checked)
    - Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
    	- 22 (SSH)
    	- 443 (HTTPS SSL)
    	- 80 (HTTP)
    - Share the ufw commands that you used in your answer file

## 100. Port fowarding

Firewalls can not only filter requests, they can also forward them.

**Requirements:**

    - Configure `web-01` so that its firewall redirects port `8080/TCP` to port `80/TCP`.
    - Your answer file should be a copy of the `ufw` configuration file that you modified to make this happen

```console
sudo ufw allow 8080/tcp
sudo ufw route allow 8080/tcp redirect to 80
# OR
sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
```

You can also add the following to the file `/etc/ufw/before.rules`

```bash
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
```

```

```
