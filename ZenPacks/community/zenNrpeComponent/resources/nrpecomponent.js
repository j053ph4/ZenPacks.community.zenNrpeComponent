
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }
    
    function pass_link(ob){ 
        return ob; 
    }
    
    ZC.NrpeComponentPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'NrpeComponent',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "command"
                    }, 
                    {
                        "name": "eventComponent"
                    }, 
                    {
                        "name": "getIpserviceLink"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Plugin Command", 
                        "renderer": "pass_link", 
                        "id": "command", 
                        "dataIndex": "command"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Alias", 
                        "renderer": "pass_link", 
                        "id": "eventComponent", 
                        "dataIndex": "eventComponent"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "IP Service", 
                        "renderer": "pass_link", 
                        "id": "getIpserviceLink", 
                        "dataIndex": "getIpserviceLink"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.NrpeComponentPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('NrpeComponentPanel', ZC.NrpeComponentPanel);
    ZC.registerName('NrpeComponent', _t('Remote Nagios'), _t('Remote Nagios'));
    
    })();

