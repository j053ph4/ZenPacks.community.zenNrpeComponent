Developed by
============
Joseph Anderson

Description:
===========
This ZenPack wraps the "check_nrpe" Nagios plugin such that it is treated as 
a device component, using standard GUI component management methods. 

The component properties specify the remote command plugin to be called.  The 
"arglist" is a newline-delimited list of arguments to be passed to the remote NRPE
daemon (assuming it is configured properly to receive them).

Components
==========
  Component and Datasource class properties are specified in the provided "Definition.py" file.
	A basic RRD Template is also provided that executes the check_nrpe plugin

Installation
============
Describe the install process if anything is needed before or after standard
ZenPack installation.

Requirements
============
    Zenoss Versions Supported: 3.x, 4.x
    External Dependencies: None
    ZenPack Dependencies: ZenPacks.community.ConstructionKit
    Installation Notes: zopectl restart; zenhub restart after installation
    Configuration: None

History
=======
Change History:

1.0 initial release

2.0
    added Zenoss 4.X support
    new dependency on "ConstructionKit" ZenPack to simplify current/future development
    <https://github.com/j053ph4/ZenPacks.community.ConstructionKit>

Tested
======
This ZenPack was tested with versions 3.2.1, 4.2.3

Source
======
https://github.com/j053ph4/ZenPacks.community.zenNrpeComponent

Known issues
============
None  
