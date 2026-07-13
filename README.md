idMotion

Templates and screens for cpmu6 and later devices

This module was created for IDs using the ether_ip protocol.

The idea is to *not* use module 'insertionDevice'
because insertionDevice assumes the PLC will use the FINS protocol.

Gap demand records

| PV                            | purpose                            |
|-------------------------------+------------------------------------|
| TS02K-MO-SERVC-01:GAPD        | Demand for gap move                |
| TS02K-MO-SERVC-01:GAPSET.PROC | Execute move by writing to this PV |
|                               |                                    |


Single axis demand records

