"""
Written By: NirZ

from IDumper import IDumper
class DumperNand(IDumper):
    def dump(self, chipset_version, start = 0, end = 0, name = "", whichflash=0, consequence_size = 1, dma_transfer = True):
        #find flash data in table and print
        nand_csv = NandCsv()
        for i in nand_data.keys():
        if end == 0:
        #init the flash
        #and dump it
        total_page_size = nand_data["PageSize"]+nand_data["SpareSize"]