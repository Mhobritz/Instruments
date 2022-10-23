# Courtesy of sdickreuter/python-andor
ERROR_CODES = {
    20001: ["DRV_ERROR_CODES", "None"],
    20002: ["DRV_SUCCESS", "None"],
    20003: ["DRV_VXNOTINSTALLED", "None"],
    20004: ["DRV_ERROR_SCAN", "None"],
    20005: ["DRV_ERROR_CHECK_SUM", "None"],
    20006: ["DRV_ERROR_FILELOAD", "None"],
    20007: ["DRV_ERROR_VXD_INIT", "None"],
    20008: ["DRV_ERROR_VXD_INIT", "None"],
    20009: ["DRV_ERROR_ADDRESS", "None"],
    20010: ["DRV_ERROR_PAGELOCK", "None"],
    20011: ["DRV_ERROR_PAGE_UNLOCK", "None"],
    20012: ["DRV_ERROR_BOARDTEST", "None"],
    20013: ["DRV_ERROR_ACK", "None"],
    20014: ["DRV_ERROR_UP_FIFO", "None"],
    20015: ["DRV_ERROR_PATTERN", "None"],
    20017: ["DRV_ACQUISITION_ERRORS", "None"],
    20018: ["DRV_ACQ_BUFFER", "None"],
    20019: ["DRV_ACQ_DOWNFIFO_FULL", "None"],
    20020: ["DRV_PROC_UNKNOWN_INSTRUCTION", "None"],
    20021: ["DRV_ILLEGAL_OP_CODE", "None"],
    20022: ["DRV_KINETIC_TIME_NOT_MET", "None"],
    20023: ["DRV_ACCUM_TIME_NOT_MET", "None"],
    20024: ["DRV_NO_NEW_DATA", "None"],
    20025: ["PCI_DMA_FAIL", "None"],
    20026: ["DRV_SPOOLERROR", "None"],
    20027: ["DRV_SPOOLSETUPERROR", "None"],
    20029: ["SATURATED", "None"],
    20033: ["DRV_TEMPERATURE_CODES", "None"],
    20034: ["DRV_TEMP_OFF", "None"],
    20035: ["DRV_TEMP_NOT_STABILIZED", "None"],
    20036: ["DRV_TEMP_STABILIZED", "None"],
    20037: ["DRV_TEMP_NOT_REACHED", "None"],
    20038: ["DRV_TEMP_OUT_RANGE", "None"],
    20039: ["DRV_TEMP_NOT_SUPPORTED", "None"],
    20040: ["DRV_TEMP_DRIFT", "None"],
    20049: ["DRV_GENERAL_ERRORS", "None"],
    20050: ["DRV_COF_NOTLOADED", "None"],
    20051: ["DRV_COF_NOTLOADED", "None"],
    20052: ["DRV_FPGAPROG", "None"],
    20053: ["DRV_FLEXERROR", "None"],
    20054: ["DRV_GPIBERROR", "None"],
    20055: ["ERROR_DMA_UPLOAD", "None"],
    20064: ["DRV_DATATYPE", "None"],
    20065: ["DRV_DRIVER_ERRORS", "None"],
    20066: ["DRV_P1INVALID", "None"],
    20067: ["DRV_P2INVALID", "None"],
    20068: ["DRV_P3INVALID", "None"],
    20069: ["DRV_P4INVALID", "None"],
    20070: ["DRV_INIERROR", "None"],
    20071: ["DRV_COERROR", "None"],
    20072: ["DRV_ACQUIRING", "None"],
    20073: ["DRV_IDLE", "None"],
    20074: ["DRV_TEMPCYCLE", "None"],
    20075: ["DRV_NOT_INITIALIZED", "Was andor.initialize() run yet?"],
    20076: ["DRV_P5INVALID", "None"],
    20077: ["DRV_P6INVALID", "None"],
    20078: ["DRV_INVALID_MODE", "None"],
    20079: ["DRV_INVALID_FILTER", "None"],
    20080: ["DRV_I2CERRORS", "None"],
    20081: ["DRV_DRV_I2CDEVNOTFOUND", "None"],
    20082: ["DRV_I2CTIMEOUT", "None"],
    20083: ["P7_INVALID", "None"],
    20089: ["DRV_USBERROR", "None"],
    20090: ["DRV_IOCERROR", "None"],
    20091: ["DRV_NOT_SUPPORTED", "None"],
    20093: ["DRV_USB_INTERRUPT_ENDPOINT_ERROR", "None"],
    20094: ["DRV_RANDOM_TRACK_ERROR", "None"],
    20095: ["DRV_INVALID_TRIGGER_MODE", "None"],
    20096: ["DRV_LOAD_FIRMWARE_ERROR", "None"],
    20097: ["DRV_DIVIDE_BY_ZERO_ERROR", "None"],
    20098: ["DRV_INVALID_RINGEXPOSURES", "None"],
    20099: ["DRV_BINNING_ERROR", "None"],
    20115: ["DRV_ERROR_MAP", "None"],
    20116: ["DRV_ERROR_UNMAP", "None"],
    20117: ["DRV_ERROR_MDL", "None"],
    20118: ["DRV_ERROR_UNMDL", "None"],
    20119: ["DRV_ERROR_BUFFSIZE", "None"],
    20121: ["DRV_ERROR_NOHANDLE", "None"],
    20130: ["DRV_GATING_NOT_AVAILABLE", "None"],
    20131: ["DRV_FPGA_VOLTAGE_ERROR", "None"],
    20099: ["DRV_BINNING_ERROR", "None"],
    20100: ["DRV_INVALID_AMPLIFIER", "None"],
    20101: ["DRV_INVALID_COUNTCONVERT_MODE", "None"],
    # not in newest SDK User Guide (11.02.2016):
    20990: ["DRV_NOCAMERA", "None"],
    20991: ["DRV_NOT_SUPPORTED", "None"],
    20992: ["DRV_NOT_AVAILABLE", "None"]
}

class AndorCameraError(Exception):
    def __init__(self, error_code):
        self.error_code = error_code
        super().__init__(ERROR_CODES[self.error_code])

    def __str__(self):
        error_info = ERROR_CODES[self.error_code]
        return f'({self.error_code}) {error_info[0]}. {error_info[1]}'

