from hl7parser import HL7Message
import datetime

class hl7():
    def __init__(self, *args, **kwargs):
        self.hl7Dict = {}
    def getData(self, fileName):
        with open(fileName) as hl7File:
            hl7File =  hl7File.read()
            h = HL7Message(hl7File)
            mshDict = {}
            pidDict = {}
            obxList = h.obx
            obxDict = {}
            hl7Dict = {}
            for obxdata in range(len(obxList)):
                key = obxList[obxdata].observation_identifier[1]
                value  = obxList[obxdata].observation_value[0]
                obxDict[str(key)] = str(value)

            # adding PID and MSH seperately as they do not change and are required as a valid hl7 message
            pidDict['MDC_ATTR_PT_NAME_GIVEN'] = str(h.pid.patient_name[0][1])
            pidDict['MDC_ATTR_PT_NAME_FAMILY'] = str(h.pid.patient_name[0][0])

            mshDict['SEND_DATE'] = str(h.msh[5])
            mshDict['SENDING_FACILITY'] = str(h.msh[2])
            mshDict['RECEIVING_FACILITY'] = str(h.msh[4])
            self.hl7Dict = dict(**pidDict,**mshDict, **obxDict)
            return self.hl7Dict
            #print(self.hl7Dict)

    def data(self):
        data = self.hl7Dict
        # check for device type aand set value to key
        if 'ICD' in data.get('MDC_IDC_DEV_TYPE'):
            MDC_IDC_DEV_TYPE = 'ICD'
        elif 'IPG' in data.get('MDC_IDC_DEV_TYPE'):
            MDC_IDC_DEV_TYPE = 'PPM'
        else:
            MDC_IDC_DEV_TYPE = 'Unkown'
        
        self.bsc_Dict = {'name_given':data.get('MDC_ATTR_PT_NAME_GIVEN', 'Not Given'),
                        'name_family':data.get('MDC_ATTR_PT_NAME_FAMILY', 'Not Given'),
                        'client_id':data.get('', '-'),
                        'followup_physician':data.get('', '-'),
                        'sess_date':data.get('MDC_IDC_SESS_DTM', datetime.datetime.now(tz=None).strftime("%d-%m-%Y %H:%M:%S")),
                        'dev_implant_date': data.get('MDC_IDC_DEV_IMPLANT_DT'),
                        'type': MDC_IDC_DEV_TYPE,
                        'model':data.get('MDC_IDC_DEV_MODEL', '-'),
                        'serial':data.get('MDC_IDC_DEV_SERIAL', '-'),
                        'mfg': data.get('SENDING_FACILITY', '-'),

                        ###### diagnostics
                        'ra_percent_paced':data.get('MDC_IDC_STAT_BRADY_RA_PERCENT_PACED', '0'), # ra pacing percentage
                        'rv_percent_paced':data.get('MDC_IDC_STAT_BRADY_RV_PERCENT_PACED', '0'), # rv pacing percentage
                        'lv_percent_paced':data.get('', '0'), # LV pacing percentage
                        'biv_percent_paced':data.get('', '0'), # biventricular pacing percentage


                        ####### arrhythmia log
                        'at_burden':data.get('', '0'), #at/af burden in pecentage form
                        'ataf_reset':data.get('', '0'),
                        'total_pac_count':data.get('BdyCounterData.Recent.TotalPACCount', '0'),
                        'total_pvc_count':data.get('BdyCounterData.Previous.PVC.TotalPVCCount', '0'),
                        'nsvt_counter_life':data.get('VTachyCounterData.Life.NonSustainedEpsd', '0'),
                        'nsvt_counter_reset':data.get('VTachyCounterData.Reset.NonSustainedEpsd', '0'),
                        'vt_counter_life':data.get('VTachyCounterData.Life.VTEpsdTotal', '0'),
                        'vt1_counter_life':data.get('VTachyCounterData.Life.VT1EpsdTotal', '0'),
                        'vf_counter_life':data.get('VTachyCounterData.Life.VFEpsdTotal', '0'),
                        'vt_counter_reset':data.get('VTachyCounterData.Reset.VTEpsdTotal', '0'),
                        'vt1_counter_reset':data.get('VTachyCounterData.Reset.VT1EpsdTotal', '0'),
                        'vf_counter_reset':data.get('VTachyCounterData.Reset.VFEpsdTotal', '0'),

                        ####### test results
                        # RA
                        'ra_test_sense':data.get('ManualIntrinsicResult.RAMsmt.Msmt', '0'),
                        'ra_test_threshold':data.get('InterPaceThreshResult.RAMsmt.Amplitude', '0'),
                        'ra_test_pulsewidth':data.get('InterPaceThreshResult.RAMsmt.PulseWidth', '0'),
                        'ra_test_impedance':data.get('ManualLeadImpedData.RAMsmt.Msmt', '0'),
                        # RV
                        'rv_test_sense':data.get('MDC_IDC_MSMT_LEADCHNL_RV_SENSING_INTR_AMPL_MEAN', '0'),
                        'rv_test_threshold':data.get('MDC_IDC_MSMT_LEADCHNL_RV_PACING_THRESHOLD_AMPLITUDE', '0'),
                        'rv_test_pulsewidth':data.get('MDC_IDC_MSMT_LEADCHNL_RV_PACING_THRESHOLD_PULSEWIDTH', '0'),
                        'rv_test_impedance':data.get('MDC_IDC_MSMT_LEADCHNL_RV_IMPEDANCE_VALUE', '0'),
                        'hv_test_impedance':data.get('MDC_IDC_MSMT_LEADHVCHNL_IMPEDANCE', '0'),
                        # LV
                        'lv_test_sense':data.get('', '0'),
                        'lv_test_impedance':data.get('ManualLeadImpedData.LVMsmt.Msmt', '0'),
                        'lv_test_threshold':data.get('InterPaceThreshResult.LVMsmt.Amplitude', '0'),                       
                        'lv_test_pulsewidth':data.get('InterPaceThreshResult.LVMsmt.PulseWidth', '0'),

                        ######  Settings
                        'mode':data.get('BdyNormBradyMode', '-'),
                        'lowrate':data.get('MDC_IDC_SET_BRADY_LOWRATE', '0'),
                        'max_tracking':data.get('NormParams.MTRIntvl', '0'),
                        'max_sensor_rate':data.get('', '0'),
                        'paced_AV_delay':data.get('BdyNormAVDelayMax', '0'),
                        'sensed_AV_delay':data.get('BdyNormSensedAVDelayMax', '0'),
                        'ra_amplitude':data.get('BdyNormAAmplitude', '0'),
                        'ra_pulsewidth':data.get('BdyNormAPulseWidth', '0'),
                        'ra_pace_polarity':data.get('PaceVectorsParam.RA', '-'),
                        'ra_sense_polarity':data.get('SenseVectorsParam.RA', '-'),
                        'ra_sensitivity':data.get('CardiacSensingParams.BdyNormRASensitivity', '-'),
                        'rv_amplitude':data.get('BdyNormVAmplitude', '0'),
                        'rv_pulsewidth':data.get('BdyNormVPulseWidth', '0'),
                        'rv_sensitivity':data.get('CardiacSensingParams.BdyNormRVSensitivity', '-'),
                        'rv_pace_polarity':data.get('PaceVectorsParam.RV', '-'),
                        'rv_sense_polarity':data.get('SenseVectorsParam.RV', '-'),
                        'lv_amplitude':data.get('InterPaceThreshResult.LVMsmt.Amplitude', '0'),
                        'lv_pulsewidth':data.get('', '0'),
                        'lv_polarity':data.get('PaceVectorsParam.LV', '-'),
                        'LV Pulse Configuration': data.get('', '-'),

                        ##### Battery
                        'batt_voltage':data.get('', '0'),# not found currently in bnk file
                        'batt_remaining':data.get('DC_IDC_MSMT_BATTERY_REMAINING_PERCENTAGE', '-'), # not found currently in bnk file
                        'batt_status':data.get('BatteryStatus.BatteryPhase', '-'),
                        'batt_chrge_time':data.get('MDC_IDC_MSMT_CAP_CHARGE_TIME', '0')
                        }
        return self.bsc_Dict
        


if __name__ == "__main__":
    #fileName = "examples\\csc_20190416121705_602864789_21.hl7"
    fileName = "examples/BSC/27814701619069872556.hl7"
    dataclass = hl7()
    datamethod = dataclass.getData(fileName)
    dataResult = dataclass.data()
    print(dataResult)

    # def listData():
    #     for k, v in iter(datamethod.items()):
    #         print(k +" : "+ str(v))
    # listData()