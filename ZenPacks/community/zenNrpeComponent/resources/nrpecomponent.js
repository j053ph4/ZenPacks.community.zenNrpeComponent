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
            {name: 'name'},{name: 'command'},
                {name: 'eventComponent'},
                
            {name: 'usesMonitorAttribute'},
            {name: 'monitor'},
            {name: 'monitored'},
            {name: 'locking'},
            ]
        ,
                        columns:[{
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
            sortable: true,
            width: 70
        },{
                    id: 'command',
                    dataIndex: 'command',
                    header: _t('Plugin Command'),
                    sortable: true,
                    width: 266
                },{
                    id: 'eventComponent',
                    dataIndex: 'eventComponent',
                    header: _t('Alias'),
                    sortable: true,
                    width: 266
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
        }]
                    });
                    ZC.NrpeComponentPanel.superclass.constructor.call(this, config);
                }
            });
            
            Ext.reg('NrpeComponentPanel', ZC.NrpeComponentPanel);
            ZC.registerName('NrpeComponent', _t('Remote Plugin'), _t('Remote Plugins'));
            
            })(); 

