import netmiko

device = {
    'device_type': 'cisco_ios',
    'host':   '10.0.15.117',
    'username': 'admin',
    'password': 'cisco',
    'port' : 22
}

net_connect = netmiko.ConnectHandler(**device)
net_connect.enable()
config = ["conf t", "int Loopback 61070254", "ip add 192.168.1.1 255.255.255.0"]
net_connect.send_config_set(config)
print(net_connect.find_prompt())
print(net_connect.send_command("show ip int br"))
