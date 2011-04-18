#
# This program is part of the HP Blade Chassis Zenpack for Zenoss.
# Copyright (C) 2011 Simon Helson.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""interfaces

describes the form field to the user interface.

"""

__version__ = "$Revision: 1.1 $"[11:-2]

from Products.Zuul.interfaces import IThresholdInfo, IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IBladeChassisInfo(IComponentInfo):
    """
    Info adapter for BladeChassis objects, currently unused.
    """
    bcEnclosureName = schema.Text(title=u"Enclosure Name", readonly=True, group='Details')
    bcEnclosureType = schema.Text(title=u"Enclosure Type", readonly=True, group='Details')
    bcPartNumber = schema.Text(title=u"Part Number", readonly=True, group='Details')
    bcSerialNumber = schema.Text(title=u"Serial Number", readonly=True, group='Details')
    bcUUID = schema.Text(title=u"UUID", readonly=True, group='Details')
    bcAssetTag = schema.Text(title=u"Asset Tag", readonly=True, group='Details')
    bcMidplaneSparePartNumber = schema.Text(title=u"Midplane Spare Part #", readonly=True, group='Details')
    bcPduType = schema.Text(title=u"PDU Type", readonly=True, group='Details')
    bcPduSparePartNumber = schema.Text(title=u"PDU Spare Part #", readonly=True, group='Details')
    bcOATrayType = schema.Text(title=u"OA Tray Type", readonly=True, group='Details')
    bcOATraySparePartNumber = schema.Text(title=u"OA Tray Spare Part #", readonly=True, group='Details')
    bcOATraySerialNumber = schema.Text(title=u"OA Tray Serial #", readonly=True, group='Details')

class IBladeServerInfo(IComponentInfo):
    """
    Info adapter for BladeServer components
    """
    bsDisplayName = schema.Text(title=u"Display Name", readonly=True, group='Details')
    bsPosition = schema.Text(title=u"Slot", readonly=True, group='Details')
    bsSerialNum = schema.Text(title=u"Serial Number", readonly=True, group='Details')
    bsProductId = schema.Text(title=u"Product Id", readonly=True, group='Details')
    bsPartNumber = schema.Text(title=u"Part Number", readonly=True, group='Details')
    bsSystemBoardPartNum = schema.Text(title=u"Sys Board Part Number", readonly=True, group='Details')
    bsCPUType = schema.Text(title=u"CPU Type", readonly=True, group='Details')
    bsCPUCount = schema.Text(title=u"CPU Count", readonly=True, group='Details')
    bsNic1Mac = schema.Text(title=u"NIC 1 MAC Address", readonly=True, group='Details')
    bsNic2Mac = schema.Text(title=u"NIC 2 MAC Address", readonly=True, group='Details')
    bsIloIp = schema.Text(title=u"ILO IP Address", readonly=True, group='Details')
    bsInstalledRam = schema.Text(title=u"Installed Ram", readonly=True, group='Details')
    bsIloFirmwareVersion = schema.Text(title=u"ILO Firmware Version", readonly=True, group='Details')

class IBladeChassisFanInfo(IComponentInfo):
    """
    Info adapter for Blade Chassis Fan Components
    """
    bcfNumber = schema.Text(title=u"Fan #", readonly=True, group='Details')
    bcfProductName = schema.Text(title=u"Product Name", readonly=True, group='Details')
    bcfPartNumber = schema.Text(title=u"Part Number", readonly=True, group='Details')
    bcfSparePartNumber = schema.Text(title=u"Spare Part Number", readonly=True, group='Details')


