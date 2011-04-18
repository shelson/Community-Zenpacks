/*
###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
*/

(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.BladeServerPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'BladeServer',
            autoExpandColumn: 'bsDisplayName',
            fields: [
                {name: 'bsDisplayName'},
                {name: 'bsPosition'},
                {name: 'bsSerialNum'},
                {name: 'bsProductId'},
                {name: 'bsCPUCount'},
                {name: 'bsInstalledRam'}
            ],
            columns: [{
                id: 'bsPosition',
                dataIndex: 'bsPosition',
                header: _t('Slot'),
                width: 30
            },{
                id: 'bsDisplayName',
                dataIndex: 'bsDisplayName',
                header: _t('Name')
            },{
                id: 'bsSerialNum',
                dataIndex: 'bsSerialNum',
                header: _t('Serial Number'),
            },{
                id: 'bsProductId',
                dataIndex: 'bsProductId',
                header: _t('Product Id'),
                width: 180
            },{
                id: 'bsCPUCount',
                dataIndex: 'bsCPUCount',
                header: _t('CPU Count'),
                width: 100
            },{
                id: 'bsInstalledRam',
                dataIndex: 'bsInstalledRam',
                header: _t('RAM'),
                width: 60
            }]
        });
        ZC.BladeServerPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('BladeServerPanel', ZC.BladeServerPanel);
ZC.registerName('BladeServer', _t('Blade'), _t('Blades'));


ZC.BladeChassisFanPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'BladeChassisFan',
            autoExpandColumn: 'bcfProductName',
            fields: [
                {name: 'bcfProductName'},
                {name: 'bcfNumber'},
                {name: 'bcfPartNumber'},
                {name: 'bcfSparePartNumber'}
            ],
            columns: [{
                id: 'bcfNumber',
                dataIndex: 'bcfNumber',
                header: _t('Slot'),
                width: 30
            },{
                id: 'bcfProductName',
                dataIndex: 'bcfProductName',
                header: _t('Product Name')
            },{
                id: 'bcfPartNumber',
                dataIndex: 'bcfPartNumber',
                header: _t('Part Number')
            },{
                id: 'bcfSparePartNumber',
                dataIndex: 'bcfSparePartNumber',
                header: _t('Spare Part Number')
            }]
        });
        ZC.BladeChassisFanPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('BladeChassisFanPanel', ZC.BladeChassisFanPanel);
ZC.registerName('BladeChassisFan', _t('Fans'), _t('Fans'));

})();
