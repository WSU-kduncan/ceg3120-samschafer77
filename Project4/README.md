*Project4*
*Sam Schafer*

1. A template is a declaration of an AWS resource that makes up a stack. The stack used in this project will build a linux VM from a .yml file. The .yml template contains parameters that will edit properties when creating the cloud formation from this template.

2. I selected a Amazon Linux AMI 2018.03 from the US East N. Virginia region.

3. I added a VPC range to 10.0.0.0/16

4. I Added a subnet range to 10.0.0.0/24

5. I added security groups for my home and Wright State University.

6. I added AWS::CloudFormation::Init: to run commands to install git, python, and pip.