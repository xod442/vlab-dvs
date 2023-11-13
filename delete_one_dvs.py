'''
888888888888                                      88              88
         ,88                                      88              88
       ,88"                                       88              88
     ,88"     ,adPPYba,  8b,dPPYba,   ,adPPYba,   88  ,adPPYYba,  88,dPPYba,
   ,88"      a8P_____88  88P'   "Y8  a8"     "8a  88  ""     `Y8  88P'    "8a
 ,88"        8PP"""""""  88          8b       d8  88  ,adPPPPP88  88       d8
88"          "8b,   ,aa  88          "8a,   ,a8"  88  88,    ,88  88b,   ,a8"
888888888888  `"Ybbd8"'  88           `"YbbdP"'   88  `"8bbdP"Y8  8Y"Ybbd8"'

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__status__ = "Alpha"


Usage: This python file adds port groups to vmware distributed virtual switches

'''
from pyVmomi import vim
from pyVim.task import WaitForTask
from pyVim.connect import SmartConnect, Disconnect
import ssl
import datetime
import logging
import time


def delete_dvs(vsphere_ip,vsphere_user,vsphere_pass, lab_group=None):

    sslContext = ssl._create_unverified_context()

    port="443"

    # Create a connector to vsphere
    si = SmartConnect(
        host=vsphere_ip,
        user=vsphere_user,
        pwd=vsphere_pass,
        port=port,
        sslContext=sslContext
    )

    content = si.RetrieveContent()
    dvs_list = content.viewManager.CreateContainerView(content.rootFolder,
                                                     [vim.DistributedVirtualSwitch],
                                                     True)

    for dvs in dvs_list.view:
        if dvs.name == lab_group:
            task = dvs.Destroy_Task()
            response = WaitForTask(task)

    dvs_list.Destroy()

    return
