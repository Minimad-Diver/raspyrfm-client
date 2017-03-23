from raspyrfm_client.device import actions
from raspyrfm_client.device.manufacturer.universal.HX2262Compatible import HX2262Compatible
import re

class RSL366(HX2262Compatible):
    _argchecks = {
        'CODE': '[1-4]$',
        'CH': '[1-4]$'
    }
    
    _h = '0'
    _l = 'f'
		
    from raspyrfm_client.device.manufacturer import manufacturer_constants
    def __init__(self, manufacturer: str = manufacturer_constants.NONAME, model: str = manufacturer_constants.RSL366):
        super().__init__(manufacturer, model)
				
    def get_supported_actions(self) -> [str]:
        return [actions.ON, actions.OFF]
        
    def get_bits(self, action: str):
        cfg = self.get_channel_config()
        bits = []
        
        bits += self.calc_match_bits(int(cfg['CODE']) - 1, 4)
        bits += self.calc_match_bits(int(cfg['CH']) - 1, 4)
        
        bits += [self._l, self._l, self._l] #fixed
        
        if action is actions.ON:
            bits += [self._l]
        elif action is actions.OFF:
            bits += [self._h]
        else:
            raise ValueError("Invalid action")
            
        print("BITS", bits)
        return bits