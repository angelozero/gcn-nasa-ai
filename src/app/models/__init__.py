from pydantic import BaseModel

from app.models.base import GCNBase
from app.models.gcn_circulars import GCNCircular
from app.models.gcn_heartbeat import GCNHeartbeat
from app.models.gcn_notices_chime_frb import CHIMEFRBNotice
from app.models.gcn_notices_dsa110_frb import DSA110FRBNotice
from app.models.gcn_notices_einstein_probe_wxt_alert import EinsteinProbeWXTAlert
from app.models.gcn_notices_icecube_lvk_nu_track_search import IceCubeLVKNuTrackSearch
from app.models.igwn_gwalert import GWAlert

__all__ = [
    "GCNBase",
    "GCNCircular",
    "GCNHeartbeat",
    "CHIMEFRBNotice",
    "DSA110FRBNotice",
    "EinsteinProbeWXTAlert",
    "IceCubeLVKNuTrackSearch",
    "GWAlert",
    "TOPIC_MODEL_MAP",
]

TOPIC_MODEL_MAP: dict[str, type[BaseModel]] = {
    "gcn.heartbeat": GCNHeartbeat,
    "gcn.circulars": GCNCircular,
    "gcn.notices.chime.frb": CHIMEFRBNotice,
    "gcn.notices.dsa110.frb": DSA110FRBNotice,
    "gcn.notices.einstein_probe.wxt.alert": EinsteinProbeWXTAlert,
    "gcn.notices.icecube.lvk_nu_track_search": IceCubeLVKNuTrackSearch,
    "igwn.gwalert": GWAlert,
}
