from installclass import BaseInstallClass
import rhpl
from rhpl.translate import N_
from constants import *
from flags import flags
import os
import iutil
import types
import yuminstall
try:
    import instnum
except ImportError:
    instnum = None

import logging
log = logging.getLogger("anaconda")

# custom installs are easy :-)
class InstallClass(BaseInstallClass):
    # name has underscore used for mnemonics, strip if you dont need it
    id = "pld"
    name = N_("PLD Linux")
    pixmap = "custom.png"
    _description = N_("Select this installation type to gain complete "
		     "control over the installation process, including "
		     "software package selection and partitioning.")
    _descriptionFields = (productName,)
    sortPriority = 10000
    allowExtraRepos = True

    repopaths = { "base": ["PLD/i686/RPMS", "PLD/noarch/RPMS"], }
    tasks = [
        (N_("GNOME Desktop"), [
            "gnome",
            "gnome_complete",
            "gnome_games",
            "gnome_themes",
        ]),
        (N_("KDE Desktop"), [
            "kde_kdepim",
            "kde_kdeedu",
            "kde_multimedia",
            "kde_koffice",
            "kde_network",
            "kde_graphics",
            "kde_admin",
            "kde_games",
            "kde_look"
        ]),
        (N_("Basic IceWM"), [
            "icewm",
        ]),
        (N_("WindowMaker"), [
            "wmaker",
        ]),
        (N_("General Development Tools"), [
            "devel"
        ]),
        (N_("Java Development Tools"), [
            "java"
        ]),
    ]

    def setInstallData(self, anaconda):
	BaseInstallClass.setInstallData(self, anaconda)
        if not anaconda.isKickstart:
            BaseInstallClass.setDefaultPartitioning(self, 
                                                    anaconda.id.partitions,
                                                    CLEARPART_TYPE_LINUX)

    def setGroupSelection(self, anaconda):
        grps = anaconda.backend.getDefaultGroups(anaconda)
        map(lambda x: anaconda.backend.selectGroup(x), grps)

    def setSteps(self, anaconda):
        dispatch = anaconda.dispatch
	BaseInstallClass.setSteps(self, anaconda);
	dispatch.skipStep("partition")
	dispatch.skipStep("regkey")

    # for rhel, we're putting the metadata under productpath
    def getPackagePaths(self, uri):
        rc = {}
        for (name, path) in self.repopaths.items():
            if not type(uri) == types.ListType:
                uri = [uri,]
            if not type(path) == types.ListType:
                path = [path,]

            lst = []
            for i in uri:
                for p in path:
                    lst.append("%s/%s" % (i, p))

            rc[name] = lst

        log.info("package paths is %s" %(rc,))
        return rc

    def handleRegKey(self, key, intf, interactive = True):
        self.repopaths = { "base": "%s" %(productPath,) }
        self.tasks = self.taskMap[productPath.lower()]
        self.installkey = key

        try:
            inum = instnum.InstNum(key)
        except Exception, e:
            if True or not BETANAG: # disable hack keys for non-beta
                # make sure the log is consistent
                log.info("repopaths is %s" %(self.repopaths,))
                raise
            else:
                inum = None

        if inum is not None:
            # make sure the base products match
            if inum.get_product_string().lower() != productPath.lower():
                raise ValueError, "Installation number incompatible with media"

            for name, path in inum.get_repos_dict().items():
                # virt is only supported on i386/x86_64.  so, let's nuke it
                # from our repo list on other arches unless you boot with
                # 'linux debug'
                if name.lower() == "virt" and ( \
                        rhpl.getArch() not in ("x86_64","i386")
                        and not flags.debug):
                    continue
                self.repopaths[name.lower()] = path
                log.info("Adding %s repo" % (name,))

        else:
            key = key.upper()
            # simple and stupid for now... if C is in the key, add Clustering
            # if V is in the key, add Virtualization. etc
            if key.find("C") != -1:
                self.repopaths["cluster"] = "Cluster"
                log.info("Adding Cluster option")
            if key.find("S") != -1:
                self.repopaths["clusterstorage"] = "ClusterStorage"
                log.info("Adding ClusterStorage option")
            if key.find("W") != -1:
                self.repopaths["workstation"] = "Workstation"
                log.info("Adding Workstation option")
            if key.find("V") != -1:
                self.repopaths["virt"] = "VT"
                log.info("Adding Virtualization option")

        for repo in self.repopaths.values():
            if not self.taskMap.has_key(repo.lower()):
                continue

            for task in self.taskMap[repo.lower()]:
                if task not in self.tasks:
                    self.tasks.append(task)
        self.tasks.sort()

        log.info("repopaths is %s" %(self.repopaths,))

    def getBackend(self, methodstr):
        return yuminstall.YumBackend

    def __init__(self, expert):
	BaseInstallClass.__init__(self, expert)

        self.repopaths = { "base": "%s" %(productPath,) }

        # minimally set up tasks in case no key is provided
        self.tasks = self.taskMap[productPath.lower()]

