
import Globals
import os.path

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

from Acquisition import aq_base
from Products.ZenModel.ZenPack import ZenPackBase
from Products.ZenModel.DeviceClass import manage_addDeviceClass

class ZenPack(ZenPackBase):
    """ WMIPerf_Windows loader
    """

    dcProperties = {
        '/Server/WBEM/Win': {
            'description': ('', 'string'),
            'devtypes': (['WMI', 'WBEM'], 'lines'),
            'zCollectorPlugins': (
                (
                'community.wmi.NewDeviceMap',
                'community.wmi.DeviceMap',
                'community.wmi.ProcessorMap',
                'community.wmi.InterfaceMap',
                'community.wmi.FileSystemMap',
                'community.wmi.ProcessMap',
                'community.wmi.ProductMap',
                'community.wmi.RouteMap',
                'community.wmi.DiskDriveMap',
                'community.wmi.WinServiceMap',
                'zenoss.portscan.IpServiceMap',
                ),
                'lines',
            ),
            'zWmiMonitorIgnore': (False, 'boolean'),
        },
        '/Server/WBEM/Win2K': {
            'description': ('', 'string'),
            'devtypes': (['WMI', 'WBEM'], 'lines'),
            'zCollectorPlugins': (
                (
                'community.wmi.NewDeviceMap',
                'community.wmi.DeviceMap',
                'community.wmi.ProcessorMap',
                'community.wmi.InterfaceMap',
                'community.wmi.FileSystemMap',
                'community.wmi.ProcessMap',
                'community.wmi.ProductMap',
                'community.wmi.DiskDriveMap',
                'community.wmi.WinServiceMap',
                'zenoss.portscan.IpServiceMap',
                ),
                'lines',
            ),
            'zWmiMonitorIgnore': (False, 'boolean'),
        },
    }

    def addDeviceClass(self, app, dcp, properties):
        try:
            dc = app.zport.dmd.Devices.getOrganizer(dcp)
        except:
            dcp, newdcp = dcp.rsplit('/', 1)
            dc = self.addDeviceClass(app, dcp, self.dcProperties.get(dcp, {}))
            manage_addDeviceClass(dc, newdcp)
            dc = app.zport.dmd.Devices.getOrganizer("%s/%s"%(dcp, newdcp))
            dc.description = ''
        for prop, value in properties.iteritems():
            if not hasattr(aq_base(dc), prop):
                dc._setProperty(prop, value[0], type = value[1])
        return dc

    def install(self, app):
        for devClass, properties in self.dcProperties.iteritems():
            self.addDeviceClass(app, devClass, properties)
        ZenPackBase.install(self, app)

    def upgrade(self, app):
        for devClass, properties in self.dcProperties.iteritems():
            self.addDeviceClass(app, devClass, properties)
        ZenPackBase.upgrade(self, app)

    def remove(self, app, leaveObjects=False):
        for dcp in self.dcProperties.keys():
            try:
                dc = app.zport.dmd.Devices.getOrganizer(dcp)
                dc._delProperty('zCollectorPlugins')
            except: continue
        ZenPackBase.remove(self, app, leaveObjects)
