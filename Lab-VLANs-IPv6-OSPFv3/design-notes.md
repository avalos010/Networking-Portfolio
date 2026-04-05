# Design Notes - Enterprise Network Lab

## 🎯 Network Design Highlights

This lab demonstrates a production-like enterprise topology with layered security segmentation and redundancy. Key focus areas:

### 🔹 Device Inventory (Complete)
| Device Type | Count | Role |
|-------------|-------|------|
| Routers | 2 | Core routing, HSRP, OSPFv3 |
| Switches | 2 | Layer 2 access, VLAN trunking |
| Sub-interfaces | 6 | 802.1Q trunking + HSRP roles |

### 🔹 VLAN Architecture
- **VLAN 10** - User data (PDs: 192.168.10.0/24)
- **VLAN 20** - Guest network (PDs: 192.168.20.0/24)  
- **VLAN 30** - Server segment (PDs: 192.168.30.0/24)
- **Native VLAN** - Disabled for security

### 🔹 Maintained Protocols
- ✅ **VLANs** - Proper segmentation with trunking
- ✅ **HSRP** - Redundant gateways (active/standby)
- ✅ **OSPFv3** - Dynamic IPv6 routing in area 0
- ✅ **DHCP** - Automated IP assignment for all VLANs
- ✅ **NAT** - Internet connectivity with PAT overload
- ✅ **ACLs** - Basic filtering in place

## 🖍️ Design Decisions

### Why HSRP with Active/Standby?
- Implements true gateway redundancy
- Primary/inactive router election via priority/preeempt
- Eliminates single point of failure for network layer devices

### DHCP Server Configuration
- Excluded ranges prevent IP conflicts
- Separate pools per VLAN match subnet structure
- Global DNS server at 8.8.8.8 for all DHCP clients

### OSPFv3 Implementation
- Dual-stack routing (IPv4 + IPv6)
- Router ID set to 1.1.1.1 for stability
- Area 0 design keeps routing simple

### Layer 2 Design
- Rapid-PVST+ ensures fast convergence
- EtherChannel bundles access port links
- VLAN trunking enables multi-VLAN transport

## 📋 Verification Commands

To validate configuration integrity:
```bash
# HSRP status
show standby brief

# OSPFv3 neighbor relationships  
show ipv6 ospf neighbor

# DHCP leases
show ip dhcp binding

# EtherChannel status
show etherchannel summary

# VLAN assignments
show vlan brief
```

## 📅 Scope & Realism

### Network Size
- **End-to-end** basic forwarding simulation
- **Enterprise pattern** matching real-world deployments
- **Extensible** base for adding security/layer 3 features

### Assumed Environment
- Packet Tracer 9.0 (enterprise topology)
- Extended with DHCP server simulation
- IPv6 addressing using ULA prefixes
- Virtualization-ready design (prepared for VM migration)

## 🧱 Future Enhancements

Potential additions for maturing the design:
- [ ] ACLs for traffic filtering
- [ ] Port-security on access ports (max 2 MACs)
- [ ] Quality of Service (QoS) for VoIP traffic
- [ ] Multiprotocol BGP simulation
- [ ] Wireless access point integration
- [ ] Timer logging for failover performance

---

*Lab Author: Jose Avalos (@avalos010)*  
*Original Build Date: April 2026*
