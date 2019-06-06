Virrtual Cluster Setup within eMedLab
======================================

This repository provides some helpful guidelines for setting up a virtual cluster in eMedLab infratstucture. 

Summary of Steps
----------------

- Setup a local Linux VM for interacting with eMedLab Openstack cloud
  - Requires: Ansible > 2.0
- Create a VM on eMedLab cloud to act as a cluster generator VM
  - Requires: public_api as the 2nd nic 
- Create cluster
  - Requires: selected version of Python tools


 Tasks for a local control box
-----------------------

- Install python-dev python-virtualenv
- Create a new virtual environment
- Install ansible
- Configure playbook 
- Run the playbook

Check/Test
------------

- Check in the dashboard/ssh  