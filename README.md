idMotion

Templates and screens for cpmu6 and later devices

This module was created for IDs using the ether_ip protocol.

The idea is to *not* use module 'insertionDevice'
because insertionDevice assumes the PLC will use the FINS protocol.


Gap demand records

| PV                            | purpose                            |
|-------------------------------|------------------------------------|
| $(prefix)SERVC-01:GAPD        | Demand for gap move                |
| $(prefix)SERVC-01:GAPSET.PROC | Execute move by writing to this PV |
|                               |                                    |

Single axis demand records

| PV                           | purpose                            |
|------------------------------|------------------------------------|
| $(prefix)SERVO-01:1AXISD     | Demand for axis 1 move             |
| $(prefix)SERVO-02:1AXISD     | Demand for axis 2 move             |
| $(prefix)SERVO-03:1AXISD     | Demand for axis 3 move             |
| $(prefix)SERVO-04:1AXISD     | Demand for axis 4 move             |
| $(prefix)SERVC-01:1AXIS.PROC | Execute move by writing to this PV |

Example prefix: for cpmu6 prefix=TS02K-MO-
