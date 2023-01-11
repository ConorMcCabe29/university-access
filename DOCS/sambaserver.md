# Introduction
Samba is a popular open-source implementation of the SMB/CIFS networking protocol, which allows Linux and Unix-based systems to share files and directories with Windows-based systems. This guide will walk you through the process of setting up a Samba server on a Linux-based system, which will allow other devices on the local network to access a shared drive.

## Prerequisites
- A Linux-based operating system with administrative access
- A drive that you wish to share, which is connected to the system and formatted with a filesystem that is supported by the operating system
- Basic knowledge of the command line and editing text files

## Step 1: Update the System
Before we begin installing new software, it's a good idea to update the system's package list and upgrade any outdated packages to their latest versions. This ensures that the system is running the most recent version of the software that will be installed.
sudo apt-get update
sudo apt-get dist-upgrade
## Step 2: Install Samba and Additional Utilities
To install the Samba server software, we will use the apt-get package manager. We will also install some additional utilities that are commonly used with Samba.
sudo apt-get install samba samba-common-bin
## Step 3: Install NTFS-3G Driver
If your drive is formatted with NTFS file system, we will install the NTFS-3G driver, which allows the system to read and write to NTFS-formatted drives.
sudo apt-get install ntfs-3g
## Step 4: Get the UUID of the Drive
To configure the drive to be automatically mounted at boot time, we will get the UUID of the NTFS drive that we want to share by running
sudo blkid
## Step 5: Add Entry in the File System Table
Using the UUID obtained in the previous step, we will add the entry of drive in the file system table. This file can be edited using the command
sudo nano -Bw /etc/fstab
and adding the line
UUID=22889F02889ED39F /mnt/USB1 auto defaults,user,nofail 0 2
## Step 6: Configure Samba
We will configure Samba by editing the Samba configuration file using the command
sudo nano /etc/samba/smb.conf
and adding the following section that describes the share.
[Films]
comment = Films
public = yes
writeable = yes
browsable = yes
path = /mnt/USB1/Films
create mask = 0777
directory mask = 0777
guest ok = yes
only guest = no

With the configuration complete, anyone on the local network can access the shared drive by browsing the network and looking for the 'Films' share, and connecting to it using their login credentials.
Please note that the UUID and path may be different on your system and it should be changed accordingly
