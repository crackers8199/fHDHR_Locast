from . import channels, epg
from .tuners import Tuners
from .watch import WatchStream
from .images import imageHandler
from .station_scan import Station_Scan
from .ssdp import SSDPServer
from .cluster import fHDHR_Cluster


class fHDHR_Device():

    def __init__(self, settings, origin):
        self.config = settings

        self.channels = channels.Channels(settings, origin)

        self.epg = epg.EPG(settings, self.channels)

        self.tuners = Tuners(settings, self.epg)

        self.watch = WatchStream(settings, self.channels, self.tuners)

        self.images = imageHandler(settings, self.epg)

        self.station_scan = Station_Scan(settings, self.channels)

        self.ssdp = SSDPServer(settings)

        self.cluster = fHDHR_Cluster(settings, self.ssdp)
