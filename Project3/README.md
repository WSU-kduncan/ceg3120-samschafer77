**Project 3**
**Sam Schafer**

**PART 1**

**VPC**
- A VPC stands for a virtual private cloud and is a virtual network through AWS. It allows for instances of AWS resources into a VPC.

**Subet**
- A subnet is a smaller piece of a larger network, this allows for an ip address to be divided into multiple parts, one as a host and the other part is the network.

**Internet Gateway**
- An internet gateway allows for traffic to be routed from a computer to an outside network, in this scenario using AWS an internet gateway uses the VPC routing tables to route traffic.

**Route Table**
- A routing table is a set of rules to determine where data packets go traveling over the internet will be directed. A routing table is attached to the VPC and is linked to the subnet. Finally a routing table rule was added to redirect all traffic to the internet gateway.

**Security Group**
- Security groups act as virtual firewalls for the VPC and control incoming and outgoing traffic. In this project we add inbound rules to only allow for incoming traffic into the VPC to be from our personal IP, Wright State University, and instances inside of the VPC. 

**PART 2**

**EC2 Instance**
- I created a new instance using a Centos7 AMI since it is the Linux distro that I am most familiar with and the default username is centos.
- I attached this instance to my VPC, I did this through the manual creation menu.
- I associated my security group with this instance through the manual creation menu.
- I allocated an Elastic IP address through the elastic ip addresses menu which associated an ip address with my instance.

- Was unable to ssh into my instance, was getting a weird error "remote host identification has changed".