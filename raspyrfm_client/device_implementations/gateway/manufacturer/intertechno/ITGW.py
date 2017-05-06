from raspyrfm_client.device_implementations.controlunit.base import Device
from raspyrfm_client.device_implementations.gateway.base import Gateway


class ITGW(Gateway):
    def __init__(self):
        from raspyrfm_client.device_implementations.gateway.manufacturer import gateway_constants
        super(gateway_constants.ITGW)

    def generate_code(self, device: Device, action: str) -> str:
        """
        This method can be implemented by inheriting classes if it does not implement get_pulse_data
        :param device: The device to generate the code for
        :param action: action to execute
        :return: signal code
        """
        if device.get_channel_config() is None:
            raise ValueError("Missing channel configuration :(")
        if action not in device.get_supported_actions():
            raise ValueError("Unsupported action: " + action)

        pulsedata = device.get_pulse_data(action)
        _head_connair = "TXP:0,0,"
        _code = _head_connair
        _code = _code + str(pulsedata[1]) + ','  # add repetitions
        _code = _code + str(5600) + ','
        _code = _code + str(pulsedata[2]) + ','  # add timebase

        _code = _code + str(len(pulsedata[0])) + ','
        for pulse in pulsedata[0]:
            _code = _code + str(pulse[0]) + ','
            _code = _code + str(pulse[1]) + ','
        return _code[:-1]
