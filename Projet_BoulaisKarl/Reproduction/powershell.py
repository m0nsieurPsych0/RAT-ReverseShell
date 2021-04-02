#!/usr/bin/env python

from enum import Enum
import subprocess

class Powershell(Enum):
    """Donnes accès à un enum de commandes powershell"""

    # Get user data
    GETLOCALIP   = "(Get-NetIPAddress -AddressFamily IPV4 -InterfaceAlias 'Ethernet *').IPAddress"
    GETMAC       = "((Out-String -InputObject (Get-NetAdapter -Physical | Format-List -Property MacAddress)).split(':')[1]).Trim()"
    GETUSERS     = "(Out-String -InputObject (Get-LocalUser | Where-object { $_.Enabled -like 'True' } | Format-List -Property Name)).Replace('Name : ', '').Split([Environment]::NewLine, [StringSplitOptions]::RemoveEmptyEntries)"
    GETHOSTNAME  = "[System.Net.Dns]::GetHostName()"
    
    # Open Port and services
    OPENSSHPORT  = ""
    ALLOWRDP     = ""
    ALLOWPING    = ""
    PERSIST      = ""

    # TODO: OPTIONNEL
    # GETADMINPASS = ""
    # GETPUBLICIP  = ""

    


    