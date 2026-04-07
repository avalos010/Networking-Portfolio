# pyright: reportMissingImports=false
from datetime import datetime
from netmiko import ConnectHandler
import os

devices = [{
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'ccnalab123',
    'secret': 'ccnalab123',
    'device_type': 'cisco_ios',
    'name': 'Core-Router-1',
},
{
    'host': '192.168.1.2',
    'username': 'admin',
    'password': 'ccnalab123',
    'secret': 'ccnalab123',
    'device_type': 'cisco_ios',
    'name': 'Core-Router-2',
}
]

def backup_config(device):
    try:
        conn = ConnectHandler(**device)
        conn.enable()
        output = conn.send_command('show running-config')
        os.makedirs('backups', exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"backups/{device['name']}_{timestamp}.txt"

        with open(filename, 'w') as f:
            f.write(output)
            print(f"backup config saved to {filename}")
        conn.disconnect()
        return True
    except Exception as e:
        print(f"Backup failed for {device['host']}: {e}")
        return False

def configure_vlan(device,vlan):
    try:
        conn = ConnectHandler(**device)
        conn.enable()

        commands = ['configure terminal']
        for vlan_id,vlan_name in vlan.items():
            commands.append(f'vlan {vlan_id}')
            commands.append(f'name {vlan_name}')
            print(f"Configuring VLAN {vlan_id} on {device['name']}")

        commands.append('end')
        commands.append('copy running-config startup-config')
        output = conn.send_config_set(commands)
        print(output)
        conn.disconnect()
        return True
    except Exception as e:
        print(f"Failed to configure VLAN {vlan_id} on {device['host']}: {e}")
        return False


if __name__ == "__main__":
    print("Starting network configuration automation...");
    #vlans to create 
    vlans_to_create = {
        10: 'Employees',
        20: 'Guests',
        30: "Voice",
        99: "Management"
    }

    for device in devices:
        print(f"Processing device: {device['name']}")
        print("Backing up configuration...")
        backup_config(device)
        print("Configuring VLANs...")
        configure_vlan(device, vlans_to_create)
    print("Network configuration automation completed successfully.")