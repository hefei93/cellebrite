"""
# PROTOCOLS
# UPLOADERS
# DUMPERS
class ChainQualcomm(BaseChain):
        self.dumpers[DumperQCRamDiag.name]                  = DumperQCRamDiag(self.protocols[ProtocolQualcommDiag.name])
        self.uploaders[UploaderQCDownload.name]             = UploaderQCDownload(self.protocols[ProtocolQualcommDownload.name])