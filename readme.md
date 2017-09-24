# Raspberry Pi Cluster

## Physical Setup

[cluster hardware example](https://www.youtube.com/watch?v=KJKhRLKXr-Q)


## Install the OS

[raspbian install guide](https://www.raspberrypi.org/documentation/installation/installing-images/)

[headless install guide](https://www.raspberrypi.org/forums/viewtopic.php?t=74176)

### Write the image to the microSD
`unzip -p ~/Downloads/2017-09-07-raspbian-stretch.zip | sudo dd bs=4M conv=fsync of={/dev/sd_card}`

or use [Etcher](https://github.com/resin-io/etcher)

### Enable SSH access
Add an empy file named 'ssh' to the boot partition

`sudo touch /media/{usr}/boot/ssh`


## Configure the Network
- Assign static IP's to the nodes


## Setup Ansible
Now, with a totally fresh raspbian install, use ansible to configure all the nodes.
- Add each nodes IP to the ansible hosts file.
- TEST: ensure you can ping all the nodes `ansible -i ansible/hosts --ask-pass all -m ping`
- Issue: deal with host-key-checking one way or another
  - add host keys to known hosts file maybe?
- Install 3rd party ansible roles `ansible-galaxy install -r requirements.yaml`
- create an ansible.cfg file, to avoid having to use `-i hosts` when running commands
- add `# ansible-playbook -i hosts <playbook file name>` to your playbooks so they can be run with `ansible-playbook <playbook name>.yaml`


## Configure Devices
Initial config:
1. change the default pi user password to something random

`ansible-playbook set_pi_usr_pas.yaml --ask-pass`

2. Initial new raspberry pi configuration

`ansible-playbook raspberrypi.yaml --ask-pass --verbose -f 10`

once our ssh key has been copied up, we dont need to --ask-pass again.

`ansible-playbook raspberrypi.yaml --verbose -f 10`


## Install Miniconda

### manual install notes:

```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
/bin/bash Miniconda3-latest-Linux-armv7l.sh -b -p miniconda
echo 'export PATH="/home/pi/miniconda/bin:$PATH"' >> .bashrc

conda update --yes conda
conda create --yes --name dask --channel rpi dask


```
