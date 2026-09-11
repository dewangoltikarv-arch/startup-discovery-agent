"""Startup Discovery Agent - Find emerging startups from Japan and South Korea"""

__version__ = "1.0.0"
__author__ = "Startup Discovery Contributors"

from startup_discovery.discovery import StartupDiscovery
from startup_discovery.models import Startup

__all__ = ["StartupDiscovery", "Startup"]
