#!/usr/bin/env python

from enum import Enum

class powershell(Enum):
    """Donnes accès à un enum de commandes powershell"""

    GETLOCALIP   = ""
    GETUSERS     = ""
    GETHOSTNAME  = ""
    GETMAC       = ""
    OPENSSHPORT  = ""
    ALLOWRDP     = ""
    ALLOWPING    = ""
    PERSIST      = ""

    # TODO: OPTIONNEL
    # GETADMINPASS = ""
    # GETPUBLICIP  = ""

    


    