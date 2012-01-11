/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an ExampleDevice in the web interface.
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

ZC.NrpeComponentPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NrpeComponent',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'name'},
                {name: 'nrpeHost'},
                {name: 'nrpeSSL'},
                {name: 'nrpeCommand'},
                {name: 'nrpeFlag'},
                {name: 'nrpeArgs'},
                {name: 'nrpeEventComponent'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'nrpeHost',
                dataIndex: 'nrpeHost',
                header: _t('Host'),
                sortable: true,
                width: 150
            },{
                id: 'nrpeSSL',
                dataIndex: 'nrpeSSL',
                header: _t('SSL'),
                sortable: true,
                width: 70
            },{
                id: 'nrpeCommand',
                dataIndex: 'nrpeCommand',
                header: _t('Plugin'),
                sortable: true,
                width: 70
            },{
                id: 'nrpeFlag',
                dataIndex: 'nrpeFlag',
                header: _t('Flags'),
                sortable: true,
                width: 150
            },{
                id: 'nrpeArgs',
                dataIndex: 'nrpeArgs',
                header: _t('Args'),
                sortable: true,
                width: 120
            },{
                id: 'nrpeEventComponent',
                dataIndex: 'nrpeEventComponent',
                header: _t('Component'),
                sortable: true,
                width: 120
            },{
                id: 'status',
                dataIndex: 'status',
                header: _t('Status'),
                width: 70
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                sortable: true,
                width: 65
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                sortable: true,
                width: 65
            }
			]
        });
        ZC.NrpeComponentPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NrpeComponentPanel', ZC.NrpeComponentPanel);
ZC.registerName('NrpeComponent', _t('Remote Plugin'), _t('Remote Plugins'));

})();

