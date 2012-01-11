(function() {

/**
* On the device details page the uid is
* Zenoss.env.device_uid and on most other pages it is set with
* the environmental variable PARENT_CONTEXT;
**/
    function getPageContext() {
        return Zenoss.env.device_uid || Zenoss.env.PARENT_CONTEXT;
    }

    Ext.ComponentMgr.onAvailable('component-add-menu', function(config) {
        var menuButton = Ext.getCmp('component-add-menu');
        menuButton.menuItems.push({
			xtype: 'menuitem',
            text: _t('Add Remote Plugin') + '...',
            hidden: Zenoss.Security.doesNotHavePermission('Manage Device'),
            handler: function() {
                var win = new Zenoss.dialog.CloseDialog({
                    width: 300,
                    title: _t('Add Remote Plugin'),
                    items: [{
                        xtype: 'form',
                        buttonAlign: 'left',
                        monitorValid: true,
                        labelAlign: 'top',
                        footerStyle: 'padding-left: 0',
                        border: false,
                        items: [{
                            xtype: 'textfield',
                            name: 'nrpeCommand',
                            fieldLabel: _t('Plugin'),
                            id: "nrpeCommandField",
                            width: 260,
                            allowBlank: false
                        }, {
                            xtype: 'textfield',
                            name: 'nrpeFlag',
                            fieldLabel: _t('Flag'),
                            id: "nrpeFlagField",
                            width: 260,
                            allowBlank: true
                        }, {
                            xtype: 'textarea',
                            name: 'nrpeArgs',
                            fieldLabel: _t('Args'),
                            id: "nrpeArgsField",
                            width: 260,
                            allowBlank: true
                        }, {
                            xtype: 'textfield',
                            name: 'nrpeEventComponent',
                            fieldLabel: _t('Component'),
                            id: "nrpeEventComponentField",
                            width: 260,
                            allowBlank: true
                        }],
                        buttons: [{
                            xtype: 'DialogButton',
                            id: 'zenNrpeComponent-submit',
                            text: _t('Add'),
                            formBind: true,
                            handler: function(b) {
                                var form = b.ownerCt.ownerCt.getForm();
                                var opts = form.getFieldValues();
                                Zenoss.remote.zenNrpeComponentRouter.addNrpeComponentRouter(opts,
                                function(response) {
                                    if (response.success) {
                                        new Zenoss.dialog.SimpleMessageDialog({
                                            title: _t('Plugin Check Added'),
                                            message: response.msg,
                                            buttons: [{
                                                xtype: 'DialogButton',
                                                text: _t('OK')
                                            }]
                                        }).show();
                                    }
                                    else {
                                        new Zenoss.dialog.SimpleMessageDialog({
                                            message: response.msg,
                                            buttons: [{
                                                xtype: 'DialogButton',
                                                text: _t('OK')
                                            }]
                                        }).show();
                                    }
                                });
                            }
                        }, Zenoss.dialog.CANCEL]
                    }]
                });
                win.show();
            }
        });
    });
}());
