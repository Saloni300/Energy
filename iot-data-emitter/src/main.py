"""
This module is to mimic the data generation by SmartSwitches (IoT/SmartDevices)
"""
from enum import Enum
from uuid import uuid4
import time
from loguru import logger
import random

DEVICE_DATA = [
    # format (device_name, device_type)
    
    # two air conditioners on first floor
    ('1F-AC1', 'air-conditioner'),
    ('1F-AC2', 'air-conditioner'),

    # two air conditioners on second floor
    ('2F-AC1', 'air-conditioner'),
    ('2F-AC2', 'air-conditioner'),

    # two sets of street lights on first street
    ('1S-SL1', 'street-light'),
    ('1S-SL2', 'street-light'),

    # one set of street lights on second street
    ('2S-SL1', 'street-light'),

    # one set of street lights on third street
    ('3S-SL1', 'street-light'),
]

class DeviceType(Enum):
    AIR_CONDITIONER = 'air-conditioner'
    STREET_LIGHT = 'street-light'

class DeviceState(Enum):
    ON = 'on'
    OFF = 'off'

class Device:
    def __init__(self, name: str, device_type: DeviceType) -> None:
        self.id = uuid4()
        self.name = name
        self.device_type = device_type
        self.__state = DeviceState.OFF    # newly initiated device is in OFF state
    
    def is_on(self) -> bool:
        return self.__state == DeviceState.ON

    def turn_on(self):
        self.__state = DeviceState.ON
        # logger.debug(f'{self.name} ON')
        self.share_event(self.to_json())

    def turn_off(self):
        self.__state = DeviceState.OFF
        # logger.debug(f'{self.name} OFF')
        self.share_event(self.to_json())
    
    def share_event(self, event: dict):
        event.update(timestamp=time.time())
        logger.debug(f'POST {event}')
        # POST event to api endpoint
    
    def to_json(self) -> dict:
        return {
            'id': str(self.id),
            'name': self.name,
            'device_type': self.device_type.value,
            'state': self.__state.value,
        }

def main():
    # create devices
    devices: list[Device]= []
    
    for device_name, device_type in DEVICE_DATA:
        device = Device(device_name, DeviceType(device_type))
        devices.append(device)
    
    while True:
        for device in devices:
            if device.is_on():
                device.turn_off()
            else:
                device.turn_on()
            seconds = random.choice(range(5,10))
            logger.debug(f'sleep for {seconds}s')
            # time.sleep(seconds)
        time.sleep(1)
    


if __name__ == '__main__':
    main()