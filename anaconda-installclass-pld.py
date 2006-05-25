from installclass import BaseInstallClass
from rhpl.translate import N_
from constants import *
import os
import iutil

# custom installs are easy :-)
class InstallClass(BaseInstallClass):
    # name has underscore used for mnemonics, strip if you dont need it
    id = "pld"
    name = N_("PLD Linux")
    pixmap = "custom.png"
    description = N_("Select this installation type to gain complete "
		     "control over the installation process, including "
		     "software package selection and partitioning.")
    sortPriority = 10000
    showLoginChoice = 1
    showMinimal = 1

    tasks = [
        (N_("Office and Productivity"), ["kde_graphics", "kde_koffice", "kde_multimedia", "gnome_office"]),
        (N_("Software Development"), ["devel", "devel_extras", "java", "kde_devel"]),
        (N_("Web server"), ["apache1_base", "apache_base"])
    ]

    def setInstallData(self, id, intf = None):
        BaseInstallClass.setInstallData(self, id)
        BaseInstallClass.setDefaultPartitioning(self, id.partitions,
                                                CLEARPART_TYPE_LINUX)

    def setGroupSelection(self, backend, intf):
        grps = backend.getDefaultGroups()
        map(lambda x: backend.selectGroup(x), grps)

    def __init__(self, expert):
        BaseInstallClass.__init__(self, expert)
