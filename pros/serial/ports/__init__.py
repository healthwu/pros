from functools import lru_cache

from serial.tools import list_ports as list_ports

from pros.common import logger
from .base_port import BasePort, PortConnectionException, PortException
from .direct_port import DirectPort


@lru_cache()
def list_all_comports():
    ports = list_ports.comports()
    logger(__name__).debug('Connected: {}'.format(';'.join([str(p.__dict__) for p in ports])))
    return ports