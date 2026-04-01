# Design Notes - Enterprise Network Lab

## 🎯 Network Design Goals

This lab was designed to demonstrate enterprise-grade networking with focus on:

1. **Scalability** - Hierarchical design that can grow
2. **Redundancy** - No single point of failure
3. **Security** - Segmentation through VLANs
4. **Modern protocols** - IPv6 and OSPFv3 ready for the future

---

## 📐 Topology Overview

### Core Layer
- Routers handling inter-VLAN routing
- OSPFv3 for dynamic routing
- HSRP for gateway redundancy

### Distribution Layer
- Layer 3 switches (if applicable)
- VLAN aggregation
- Route summarization

### Access Layer
- Layer 2 switches
- Port security
- VLAN assignment

---

## 🌐 VLAN Design

| VLAN ID | Name | Purpose | Subnet |
|---------|------|---------|--------|
| 10 | Management | Network device management | TBD |
| 20 | Users | End-user devices | TBD |
| 30 | Servers | Server farm | TBD |
| 40 | Voice | VoIP phones | TBD |
| 99 | Native | Trunk native VLAN | TBD |

**Design Decisions:**
- Separate VLANs for security boundaries
- Native VLAN changed from default (VLAN 1) for security
- Management VLAN isolated for device access

---

## 🔢 IPv6 Addressing Scheme

Using ULA (Unique Local Addresses) or Global Unicast:

```
Format: 2001:DB8:<VLAN>::/64 per VLAN
Example:
- VLAN 10: 2001:DB8:10::/64
- VLAN 20: 2001:DB8:20::/64
- VLAN 30: 2001:DB8:30::/64
```

**Why IPv6?**
- Future-proofing
- Larger address space
- Built-in features (no NAT needed)
- Industry trend

---

## 🔄 OSPFv3 Configuration

### Areas
- **Area 0** - Backbone (core routers)
- **Area 1** - Distribution/Access (if multi-area)

### Key Configurations
```
ipv6 router ospf 1
 router-id X.X.X.X

interface GigabitEthernet0/0
 ipv6 ospf 1 area 0
```

**Design Decisions:**
- OSPFv3 chosen for IPv6 native support
- Router IDs use IPv4 format for stability
- Passive interfaces on user-facing ports

---

## 🔌 DHCP Services

### IPv4 DHCP
```
ip dhcp pool VLAN20
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
 dns-server 8.8.8.8
```

### IPv6 DHCPv6
```
ipv6 dhcp pool VLAN20
 address-prefix 2001:DB8:20::/64
 dns-server 2001:4860:4860::8888
```

**Why DHCP?**
- Automated client configuration
- Centralized management
- Reduced human error

---

## 🛡️ HSRP Redundancy

### Configuration Example
```
interface Vlan20
 standby 20 ip 192.168.20.1
 standby 20 priority 110
 standby 20 preempt
```

**Active Router:** Higher priority (110)
**Standby Router:** Default priority (100)

**Benefits:**
- Seamless failover (< 10 seconds)
- Virtual IP as default gateway
- No client reconfiguration needed

---

## 🔒 Security Considerations

- ✅ Native VLAN changed from VLAN 1
- ✅ Unused ports shut down
- ✅ Management VLAN isolated
- ✅ Password encryption enabled
- ✅ SSH preferred over Telnet (if configured)

---

## 🧪 Testing & Verification

### Commands Used to Validate

```bash
# VLAN verification
show vlan brief
show interfaces trunk

# IPv6 verification
show ipv6 interface brief
show ipv6 route

# OSPFv3 verification
show ipv6 ospf neighbor
show ipv6 ospf database

# DHCP verification
show ip dhcp binding
show ipv6 dhcp binding

# HSRP verification
show standby brief
```

---

## 📈 Future Improvements

Potential enhancements for next iteration:

- [ ] Add ACLs for traffic filtering
- [ ] Implement port security on access switches
- [ ] Add NAT for internet connectivity
- [ ] Configure EtherChannel for link aggregation
- [ ] Add wireless components
- [ ] Implement QoS for voice VLAN

---

*Document created: April 2026*

---

**Lab Author:** Jose Avalos  
**GitHub:** [@avalos010](https://github.com/avalos010)
