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

## Configure Devices
Initial config:

`ansible-playbook raspberrypi.yaml --ask-pass --verbose -f 10`

once our ssh key has been copied up, we dont need to --ask-pass again.

- change the remote_user in raspberrypi.yaml to the value of  raspi_config_replace_user: name:

`ansible-playbook raspberrypi.yaml --verbose -f 10`
