# Networking Portfolio - Enterprise Lab

## 🌐 Big Lab: VLANs, IPv6, OSPFv3, DHCP, HSRP

A comprehensive enterprise network design showcasing advanced routing and switching technologies.

---

## 📋 Overview

This lab demonstrates a multi-layer enterprise network with:

- **VLANs** - Segmented network for security and broadcast control
- **IPv6** - Full dual-stack implementation
- **OSPFv3** - Dynamic routing for IPv6
- **DHCP** - Automated IP address assignment (IPv4 & IPv6)
- **HSRP** - First-hop redundancy for high availability

---

## 🏗️ Network Topology

![Network Diagram](https://github.com/avalos010/Networking-Portfolio/blob/main/Lab-VLANs-IPv6-OSPFv3/Topology-Screenshot.png)

### Device Summary

| Device Type | Count | Purpose |
|-------------|-------|---------|
| Routers | 4 | Core routing, HSRP, OSPFv3 |
| Switches | 2 | Multi-layer switching, VLANs |
| End Devices | 6 | DHCP clients, testing |

---

## 📁 Project Structure

```
networking-portfolio/
├── README.md
├── Big-Lab-VLANs-IPv6-OSPFv3/
│   ├── topology-screenshot.png    # Export from Packet Tracer
│   ├── configs/                   # Device configurations
│   │   ├── router-*.txt
│   │   └── switch-*.txt
│   └── design-notes.md            # Design decisions & explanations
├── .pkt                           # Original Packet Tracer file
└── .gitignore
```

---

## 🚀 How to Use

### Open in Packet Tracer

1. Download Cisco Packet Tracer 9.0+
2. Open `Big lab VLANS,IPV6, ospfv3, dhcp ,hsrp.pkt`
3. Explore the topology and device configurations

### View Configurations

All device configs are exported in `/configs`:

```bash
cat Big-Lab-VLANs-IPv6-OSPFv3/configs/<device-name>-config.txt
```

---

## 🔧 Key Technologies Demonstrated

### VLAN Configuration
- Multiple VLANs for departmental segmentation
- Trunk ports between switches and routers
- Native VLAN configuration

### IPv6 Implementation
- Global unicast addressing
- Link-local addresses
- Dual-stack with IPv4

### OSPFv3 Routing
- Multi-area OSPF for IPv6
- Router ID configuration
- Neighbor adjacencies

### DHCP Services
- IPv4 DHCP pools on routers
- IPv6 DHCPv6 for stateful addressing
- Relay agents where needed

### HSRP Redundancy
- Active/standby gateway configuration
- Virtual IP for default gateways
- Preemption and priority settings

---

## 🎯 Learning Objectives

This lab validates skills in:
- ✅ Enterprise network design
- ✅ Layer 2 switching (VLANs, trunks)
- ✅ Layer 3 routing (OSPFv3)
- ✅ IPv6 addressing and migration
- ✅ Network services (DHCP)
- ✅ High availability (HSRP)

---

## 📝 Design Notes

See [design-notes.md](./Big-Lab-VLANs-IPv6-OSPFv3/design-notes.md) for detailed explanations of design decisions, IP addressing schemes, and configuration rationale.

---

## 🛠️ Tools Used

- Cisco Packet Tracer 9.0.0
- Cisco IOS (simulated)

---

## 📬 Contact

**Built by Jose Avalos** — Networking enthusiast aspiring to make an impact!

🔗 GitHub: [@avalos010](https://github.com/avalos010)

---

*Last updated: April 2026*
