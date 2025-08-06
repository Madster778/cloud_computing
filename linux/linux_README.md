# Linux & AWS Cloud Essentials – Practical Session Notes

This README summarises the key Linux commands, concepts, and setup processes covered in the cloud training session using an Ubuntu EC2 instance on AWS.

---

## System Information and Shell Basics

Before starting any task, it's good practice to check your system and user context:

```bash
whoami            # Shows current user
uname             # Displays system information
uname --help      # Lists uname options
cat /etc/shells   # Shows available login shells
```

---

## File and Directory Navigation

| Command         | Description                                      |
| --------------- | ------------------------------------------------ |
| `ls`            | List files                                       |
| `ls -a`         | List all files, including hidden ones            |
| `ls -la`        | Long-format list including hidden files          |
| `pwd`           | Print current working directory                  |
| `cd ..`         | Go up one directory level                        |
| `cd` or `cd ~`  | Return to the home directory                     |
| `mkdir folder`  | Create a new directory                           |
| `rm -r folder`  | Recursively delete a directory                   |
| `rm -rf folder` | Force delete folder without confirmation (risky) |

---

## File Management and Text Viewing

| Action                 | Command                  |
| ---------------------- | ------------------------ | ------------- |
| Rename a file          | `mv old.txt new.txt`     |
| Copy a file            | `cp file1.txt file2.txt` |
| Delete a file          | `rm file.txt`            |
| View contents          | `cat file.txt`           |
| View first lines       | `head -2 file.txt`       |
| View last lines        | `tail -2 file.txt`       |
| View with line numbers | `nl file.txt`            |
| Search within a file   | `cat file.txt            | grep keyword` |
| Create/edit a file     | `nano file.txt`          |

---

## Downloading Files from the Internet

| Tool   | Example Command                                         |
| ------ | ------------------------------------------------------- |
| `curl` | `curl https://example.com/image.jpg --output image.jpg` |
| `wget` | `wget https://example.com/image.jpg -O image2.jpg`      |
| `file` | `file image.jpg` (checks the type/metadata of a file)   |

---

## Package Management

Linux packages are managed via `apt` on Debian-based systems like Ubuntu:

```bash
sudo apt update -y       # Update list of available packages
sudo apt upgrade -y      # Upgrade all installed packages
sudo apt install tree -y # Install the tree command
tree                     # View a folder as a directory tree
```

---

## Shell Utilities and Superuser Privileges

| Command              | Purpose                                |
| -------------------- | -------------------------------------- |
| `history`            | Show command history                   |
| `history -c`         | Clear command history                  |
| `sudo su`            | Become root user                       |
| `exit`               | Exit from root or a subshell           |
| `chmod +x script.sh` | Make a script executable               |
| `man <command>`      | View manual page for any Linux command |

---

## Bash Scripting: Automated EC2 Setup with NGINX

To speed up provisioning, we created a Bash script that installs and configures NGINX on a fresh Ubuntu EC2 instance.

**Script: `install_nginx.sh`**

```bash
#!/bin/bash

# update
sudo apt update -y

# upgrade
sudo apt upgrade -y

# install nginx
sudo apt install nginx -y

# restart nginx
sudo systemctl restart nginx

# enable nginx
sudo systemctl enable nginx
```

### How to Use:

1. Create the file:

   ```bash
   nano install_nginx.sh
   ```

2. Make it executable:

   ```bash
   sudo chmod +x install_nginx.sh
   ```

3. Run the script:
   ```bash
   ./install_nginx.sh
   ```

Once complete, NGINX will be installed, running, and configured to restart on boot.

---

### Check NGINX Status

```bash
sudo systemctl status nginx
```
