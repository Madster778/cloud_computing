#!/bin/bash

# Update the packages
sudo apt update -y

# Upgrade the packages
sudo apt upgrade -y

# Install gnupg which is needed to import the MongoDB public GPG Key
sudo apt install -y gnupg

# Download MongoDB's GPG key and add it to a specific keyring file
curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
   sudo gpg --yes -o /usr/share/keyrings/mongodb-server-8.0.gpg --dearmor

# Create a list file for MongoDB
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | \
   sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list

# Reload the local package database again
sudo apt update -y

# Install the MongoDB packages
echo "Installing MongoDB..."
sudo apt install -y mongodb-org

# Although you can specify any available version of MongoDB,
# apt-get will upgrade the packages when a newer version becomes available.
# To prevent unintended upgrades, you can pin the package at the currently installed version:
sudo apt-mark hold mongodb-org mongodb-org-server mongodb-org-shell mongodb-org-mongos mongodb-org-tools

# Start MongoDB
sudo systemctl start mongod

# Path to your mongod.conf file
CONFIG_FILE="/etc/mongod.conf"

# Use sed to replace "bindIp: 127.0.0.1" with "bindIp: 0.0.0.0"
sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/' "$CONFIG_FILE"

# Restart MongoDB
echo "Restarting MongoDB with updated configuration..."
sudo systemctl restart mongod

# Final status message
echo "MongoDB is installed, running, and open for external connections on port 27017"