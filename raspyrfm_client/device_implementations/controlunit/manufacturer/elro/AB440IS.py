from raspyrfm_client.device_implementations.controlunit.manufacturer.elro.AB440ID import AB440ID
from raspyrfm_client.device_implementations.controlunit.manufacturer.elro.AB440S import AB440S


class AB440IS(AB440ID):
    def __init__(self):
        from raspyrfm_client.device_implementations.manufacturer_constants import Manufacturer
        from raspyrfm_client.device_implementations.controlunit.controlunit_constants import ControlUnitModel

        super(AB440S, self).__init__(Manufacturer.ELRO,
                                     ControlUnitModel.AB440IS)
