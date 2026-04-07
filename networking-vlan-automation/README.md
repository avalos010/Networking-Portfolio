# 🤖 VLAN Automation Script

**Python + Netmiko** - Automated VLAN configuration and backup for Cisco IOS devices

---

## 📋 Overview

This Python script automates two critical network operations tasks:

1. **Automated Backups** - Captures running-config from all devices before making changes
2. **Bulk VLAN Configuration** - Deploys VLANs across multiple devices simultaneously

**Why this matters:** Manual VLAN configuration doesn't scale. In a real enterprise with 50+ switches, clicking through Packet Tracer isn't an option. This script shows I can automate real-world tasks.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3** | Scripting language |
| **Netmiko** | SSH library for network devices |
| **Cisco IOS** | Target device OS |
| **datetime** | Timestamped backups |

---

## 📁 Script Features

### ✅ Pre-Change Backups
```python
backup_config(device)
```
- Connects to each device via SSH
- Captures `show running-config`
- Saves to `backups/<device-name>_<timestamp>.txt`
- **Best practice:** Always backup before making changes!

### ✅ Bulk VLAN Deployment
```python
configure_vlan(device, vlans_to_create)
```
- Creates multiple VLANs in a single session
- Assigns meaningful names to each VLAN
- Saves config to startup-config
- Handles errors gracefully

### ✅ VLANs Deployed
| VLAN ID | Name | Purpose |
|---------|------|---------|
| 10 | Employees | Staff devices |
| 20 | Guests | Guest network |
| 30 | Voice | VoIP phones |
| 99 | Management | Network devices |

---

## 🚀 How to Use

### Prerequisites

```bash
# Install netmiko
pip install netmiko

# Verify installation
pip show netmiko
```

### Configure Your Devices

Edit the `devices` list with your actual device info:

```python
devices = [{
    'host': '192.168.1.1',        # Device IP
    'username': 'admin',           # SSH username
    'password': 'your_password',   # SSH password
    'secret': 'your_secret',       # Enable secret
    'device_type': 'cisco_ios',    # Device type
    'name': 'Core-Router-1',       # Friendly name
}]
```

### Run the Script

```bash
python vlan_automation.py
```

### Expected Output

```
Starting network configuration automation...
Processing device: Core-Router-1
Backing up configuration...
backup config saved to backups/Core-Router-1_20260407_112800.txt
Configuring VLANs...
Configuring VLAN 10 on Core-Router-1
Configuring VLAN 20 on Core-Router-1
Configuring VLAN 30 on Core-Router-1
Configuring VLAN 99 on Core-Router-1
[...]
Network configuration automation completed successfully.
```

---

## 📂 Output Structure

```
networking-vlan-automation/
├── README.md                 # This file
├── vlan_automation.py        # Main script
└── backups/                  # Auto-created backup folder
    ├── Core-Router-1_20260407_112800.txt
    ├── Core-Router-2_20260407_112801.txt
    └── ...
```

---

## 🔒 Security Notes

**Current state:** Passwords are hardcoded (fine for lab learning)

**Production improvements:**
- Use environment variables for credentials
- Implement SSH key-based authentication
- Store secrets in a vault (HashiCorp Vault, AWS Secrets Manager)
- Add logging with proper audit trails

Example with environment variables:
```python
import os
password = os.getenv('DEVICE_PASSWORD')
```

---

## 🧪 Testing in Your Lab

1. **Set up devices** in Packet Tracer or GNS3/EVE-NG
2. **Enable SSH** on each device:
   ```
   ip domain-name lab.local
   crypto key generate rsa modulus 2048
   username admin privilege 15 secret ccnalab123
   line vty 0 4
    transport input ssh
    login local
   ```
3. **Ensure reachability** - Ping devices from your machine
4. **Run the script** and verify VLANs are created

---

## 🎯 Skills Demonstrated

- ✅ Python scripting for network automation
- ✅ SSH connectivity to network devices
- ✅ Netmiko library usage
- ✅ Configuration backup strategies
- ✅ Error handling in automation
- ✅ Bulk device management
- ✅ Change management best practices

---

## 📬 Author

**Jose Avalos**  
GitHub: [@avalos010](https://github.com/avalos010)

*Created: April 2026*

---

## 📚 Resources

- [Netmiko Documentation](https://ktbyers.github.io/netmiko/)
- [Python for Network Engineers](https://pynet.twb-tech.com/)
- [Cisco IOS Command Reference](https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-software/products-command-reference-list.html)
