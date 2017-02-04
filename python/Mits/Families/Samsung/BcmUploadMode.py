from Mits.Families.BaseFamily               import BaseFamilySerial, BaseFamilyUSB
from Mits.Chains.ChainBcmUploadMode         import ChainBcmUploadMode
class FamilyBcmSerial(BaseFamilySerial):        
class FamilyBcmUploadMode(BaseFamilyUSB):
        vid = [0x04e8]
        # Models start with GT-S5xxx or GT-S7xxx, the write_endpoint is 2