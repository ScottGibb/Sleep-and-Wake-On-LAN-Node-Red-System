# Troubleshooting Wake on LAN (WoL) Issues on Windows 10 with ASUS P9X79 Motherboard

## Problem

Your computer doesn't consistently wake from LAN (WoL). It mostly works, but fails if left idle for an extended period. You are running Windows 10 with an ASUS P9X79 motherboard.

### Troubleshooting Steps

#### 1. BIOS/UEFI Settings

- **Wake on LAN (WoL) Setting**:
  - Ensure WoL is enabled in the BIOS/UEFI settings. Access the BIOS by pressing `Del` during startup.
  - Navigate to the "Power" section to check the WoL settings.

- **ERP Ready**:
  - Check if the "ERP Ready" option is enabled in the BIOS.
  - If enabled, it might limit power to the network card, affecting WoL. Try disabling it.

#### 2. Network Adapter Settings in Windows

- **Device Manager**:
  1. Go to `Device Manager` > `Network adapters`.
  2. Right-click on your network adapter and select `Properties`.
  3. Under the `Power Management` tab, ensure that "Allow this device to wake the computer" is checked.
  4. Ensure "Only allow a magic packet to wake the computer" is checked to avoid accidental wake-ups.

- **Advanced Settings**:
  1. In the same `Properties` window, go to the `Advanced` tab.
  2. Look for settings like "Wake on Magic Packet," "Wake on Pattern Match," or "Shutdown Wake-On-Lan" and ensure they are enabled.

#### 3. Power Plan Settings

- **Balanced Power Plan**:
  1. Go to `Control Panel` > `Power Options`.
  2. Select the `Balanced` power plan, then click on `Change plan settings`.
  3. Click on `Change advanced power settings`.
  4. Expand `PCI Express` > `Link State Power Management`, and set it to `Off`.

#### 4. Driver Update

- **Network Driver**:
  - Ensure that your network adapter drivers are up-to-date.
  - Download the latest drivers from the manufacturer’s website (ASUS or the NIC manufacturer) or use Device Manager to update them.

#### 5. Router Settings

- **ARP Binding**:
  - Some routers have an ARP binding feature that ensures the MAC address of your computer is always recognized.
  - Check your router’s settings to ensure it's correctly configured.

- **Firmware Update**:
  - Ensure your router's firmware is up to date, as some issues with WoL can be related to the router itself.

#### 6. Test with Shorter Sleep Duration

- Sometimes, the longer the PC is in sleep, the more likely it is that it won't wake up via WoL. Test with shorter durations (e.g., 5 minutes) to see if the issue persists.

#### 7. Check for Windows Updates

- Ensure your Windows 10 is up-to-date, as some updates might contain fixes for power management issues.

#### 8. Network Activity and Power Saving

- Check if there's any scheduled task or network activity that's affecting the network adapter's power state while in sleep mode.

#### 9. Energy Efficient Ethernet

- Disable "Energy Efficient Ethernet" in the network adapter's properties under the `Advanced` tab. This setting can interfere with WoL.

#### 10. Disable Fast Startup

- **Fast Startup**:
  - Fast Startup can interfere with WoL.
  - Disable it by going to `Control Panel` > `Power Options` > `Choose what the power buttons do` > `Change settings that are currently unavailable`, and then uncheck "Turn on fast startup."

### Conclusion

If the problem persists after trying these steps, it might be related to specific hardware compatibility or even a potential defect with the network adapter. In that case, consider testing with a different network adapter or using a PCIe network card to see if the issue is resolved.
