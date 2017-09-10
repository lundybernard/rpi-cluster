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
- TEST: ensure you can ping all the nodes `ansible -i hosts all -m ping`

