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
    Info adapter for BladeChassis components.
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

