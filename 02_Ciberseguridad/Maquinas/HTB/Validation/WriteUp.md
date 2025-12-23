IP
10.10.11.116

# recon

## nmap

```bash
sudo nmap -p- --min-rate 5000 -sS -n -Pn 10.10.11.116 -oN ports
	PORT     STATE SERVICE
	22/tcp   open  ssh
	80/tcp   open  http
	4566/tcp open  kwtc
	8080/tcp open  http-proxy
```

```bash
 nmap -p22,80,4566,8080 -sCV 10.10.11.116 -oN services
 
	 22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey: 
	|   3072 d8:f5:ef:d2:d3:f9:8d:ad:c6:cf:24:85:94:26:ef:7a (RSA)
	|   256 46:3d:6b:cb:a8:19:eb:6a:d0:68:86:94:86:73:e1:72 (ECDSA)
	|_  256 70:32:d7:e3:77:c1:4a:cf:47:2a:de:e5:08:7a:f8:7a (ED25519)
	80/tcp   open  http    Apache httpd 2.4.48 ((Debian))
	|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
	|_http-server-header: Apache/2.4.48 (Debian)
	4566/tcp open  http    nginx
	|_http-title: 403 Forbidden
	8080/tcp open  http    nginx
	|_http-title: 502 Bad Gateway
	Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
 
```

## FFUF

```bash
ffuf -c -u http://10.10.11.116/FUZZ  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

Nothing

# Exploitation

## BURP SQLi

![[Pasted image 20250920145949.png]]


When we send the request, we get a new cookie

![[Pasted image 20250920150000.png]]

If we use this new cookie to follow the redirection, we can see the SQL error

![[Pasted image 20250920150013.png]]

Database has only 1 column

![[Pasted image 20250920150027.png]]

database name: registration

```
union select database();
```


revershell


![[Pasted image 20250920150038.png]]
![[Pasted image 20250920150053.png]]

Database credentials

![[Pasted image 20250920150101.png]]
# Privec

Password reuse
![[Pasted image 20250920150113.png]]

