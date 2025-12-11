#!/usr/bin/python3

from .Module import Module


class LinkStack(Module):
    def __init__(self, subDomain):
        """A Uptime Kuma instance

        Args:
            subDomain (SubDomain): The subdomain this module is installed on
        """
        self.requiredDirs = ['src']
        super().__init__(subDomain)

    def _getCustomEnvVars(self) -> dict[str, str]:
        self.exposedPort = self.getFreePort()
        return {
            'ADMIN_EMAIL': str(self.exposedPort),
        }
