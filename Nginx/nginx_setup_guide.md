# 🌐 Task 2: NGINX Setup Instructions (EC2 or Local Linux)

This guide sets up a basic NGINX server to serve your HTML project.

---

## ✅ 1. Launch EC2 (Ubuntu/Debian) or use a local Linux machine

Ensure your instance or VM:
- Has a public IP
- Allows inbound traffic on port 80 (HTTP)

---

## ✅ 2. Install NGINX

```bash
sudo apt update
sudo apt install nginx -y
```

_For Amazon Linux 2, use:_
```bash
sudo yum update -y
sudo amazon-linux-extras enable nginx1
sudo yum install nginx -y
```

---

## ✅ 3. Start and Enable NGINX

```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

---

## ✅ 4. Set Up Web Directory

```bash
sudo mkdir -p /var/www/html
sudo chown -R $USER:$USER /var/www/html
```

---

## ✅ 5. Replace Default NGINX Index Page

You will use the CI/CD pipeline to automatically copy `index.html` here:
```bash
/var/www/html/index.html
```

---

## ✅ 6. Confirm NGINX is Running

Visit your public IP:
```
http://<your-ec2-ip>
```

You should see either the default or your custom HTML page.

---

## 🔒 Security Group Notes (For EC2)

Allow:
- Port 22 (SSH)
- Port 80 (HTTP)

---

## 🧪 Test Deployment (Manual)

You can manually copy your `index.html` once to test:
```bash
scp index.html ubuntu@<your-ec2-ip>:/tmp
ssh ubuntu@<your-ec2-ip>
sudo mv /tmp/index.html /var/www/html/index.html
```

---

Now you're ready for automated deployment via script!