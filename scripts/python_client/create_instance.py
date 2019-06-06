#!/usr/bin/env python
import time
from os import environ as env
import novaclient.v2.client as nvclient

IMAGE_ID = "1b1e4418-b710-4fd0-b143-517ac23d22a9"
FLAVOR_NAME = "m1.small"
DEFAULT_NETWORK_NAME = "gosgene-net"
PUBLIC_NETWORK_NAME = "public_api"
INSTANCE_NAME = "fstest-vm02"
KEY_NAME = "fs-xubu"

try:
    nova_client = nvclient.Client(auth_url=env['OS_AUTH_URL'],
                       username=env['OS_USERNAME'],
                       api_key=env['OS_PASSWORD'],
                       project_id=env['OS_TENANT_NAME'],
                       region_name=env['OS_REGION_NAME'])

    image = nova_client.images.get(IMAGE_ID)
    flavor = nova_client.flavors.find(name=FLAVOR_NAME)
    net1 = nova_client.networks.find(label=DEFAULT_NETWORK_NAME)
    net2 = nova_client.networks.find(label=PUBLIC_NETWORK_NAME)
    #nics = [{'net-id': net1.id},{'net-id': net2.id} ]
    nics = [{'net-id': net1.id}]
    instance = nova_client.servers.create(name=INSTANCE_NAME, image=image,
                                      flavor=flavor, key_name=KEY_NAME, nics=nics)
    print("Sleeping for 5s after create command")
    time.sleep(5)
    print("List of VMs")
    print(nova_client.servers.list())
finally:
    print("Execution Completed")
