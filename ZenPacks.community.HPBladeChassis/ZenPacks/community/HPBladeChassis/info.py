################################################################################
#
# This program is part of the HP Blade Chassis Zenpack for Zenoss.
# Copyright (C) 2011 Simon Helson.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of modules.

$Id: info.py,v 1.1 2010/12/14 21:57:58 egor Exp $"""

__version__ = "$Revision: 1.1 $"[11:-2]

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import ThresholdInfo
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from ZenPacks.community.HPBladeChassis import interfaces


class BladeChassisInfo(ComponentInfo):
    implements(interfaces.IBladeChassisInfo)

    bcEnclosureName = ProxyProperty("bcEnclosureName")
    bcEnclosureType = ProxyProperty("bcEnclosureType")
    bcPartNumber = ProxyProperty("bcPartNumber")
    bcSerialNumber = ProxyProperty("bcSerialNumber")
    bcUUID = ProxyProperty("bcUUID")
    bcAssetTag = ProxyProperty("bcAssetTag")
    bcMidplaneSparePartNumber = ProxyProperty("bcMidplaneSparePartNumber")
    bcPduType = ProxyProperty("bcPduType")
    bcPduSparePartNumber = ProxyProperty("bcPduSparePartNumber")
    bcOATrayType = ProxyProperty("bcOATrayType")
    bcOATraySparePartNumber = ProxyProperty("bcOATraySparePartNumber")
    bcOATraySerialNumber = ProxyProperty("bcOATraySerialNumber")



class BladeServerInfo(ComponentInfo):
    implements(interfaces.IBladeServerInfo)

    bsDisplayName = ProxyProperty("bsDisplayName")
    bsPosition = ProxyProperty("bsPosition")
    bsSerialNum = ProxyProperty("bsSerialNum")
    bsProductId = ProxyProperty("bsProductId")
    bsPartNumber = ProxyProperty("bsPartNumber")
    bsSystemBoardPartNum = ProxyProperty("bsSystemBoardPartNum")
    bsCPUType = ProxyProperty("bsCPUType")
    bsCPUCount = ProxyProperty("bsCPUCount")
    bsNic1Mac = ProxyProperty("bsNic1Mac")
    bsNic2Mac = ProxyProperty("bsNic2Mac")
    bsIloIp = ProxyProperty("bsIloIp")
    bsInstalledRam = ProxyProperty("bsInstalledRam")
    bsIloFirmwareVersion = ProxyProperty("bsIloFirmwareVersion")

class BladeChassisFanInfo(ComponentInfo):
    implements(interfaces.IBladeChassisFanInfo)

    bcfNumber = ProxyProperty("bcfNumber")
    bcfProductName = ProxyProperty("bcfProductName")
    bcfPartNumber = ProxyProperty("bcfPartNumber")
    bcfSparePartNumber = ProxyProperty("bcfSparePartNumber")

