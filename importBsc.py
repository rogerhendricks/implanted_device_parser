import csv
import datetime

class BscImport():
    def __init__(self, *args, **kwargs):
        self.bscDict= {}
        self.fDict = {}
    def getbscData(self, fileName):
        
        with open(fileName, mode='r') as csvfile:
          reader = csv.reader(filter(lambda row: row[0]!='#', csvfile))
          for row in reader:
                k,v = row
                self.bscDict[k]=v
        return self.bscDict
    
    def mode(self, fileName):
        modeclass = BscImport()
        mode = modeclass.getbscData(fileName)
        implant_day = mode.get('PatientData.ImplantDay')
        implant_month = mode.get('PatientData.ImplantMonth')
        implant_year = mode.get('PatientData.ImplantYear')
        implant_date = f"{implant_day}-{implant_month}-{implant_year}"
        self.bsc_Dict = {'name_given':mode.get('PatientFirstName', 'Not Given'),
                        'name_family':mode.get('PatientLastName', 'Not Given'),
                        'client_id':mode.get('', '-'),
                        'followup_physician':mode.get('', '-'),
                        'sess_date':mode.get('', datetime.datetime.now(tz=None).strftime("%d-%m-%Y %H:%M:%S")),
                        'dev_implant_date': implant_date,
                        'type':mode.get('SystemTypeTierName', '-'),
                        'model':mode.get('SystemName', '-'),
                        'serial':mode.get('SystemSerialNumber', '-'),
                        'mfg':'Boston Scientific',

                        ###### diagnostics
                        'ra_percent_paced':mode.get('', '0'), # ra pacing percentage
                        'rv_percent_paced':mode.get('', '0'), # rv pacing percentage
                        'lv_percent_paced':mode.get('', '0'), # LV pacing percentage
                        'biv_percent_paced':mode.get('', '0'), # biventricular pacing percentage


                        ####### arrhythmia log
                        'at_burden':mode.get('', '0'), #at/af burden in pecentage form
                        'ataf_reset':mode.get('', '0'),
                        'total_pac_count':mode.get('BdyCounterData.Recent.TotalPACCount', '0'),
                        'total_pvc_count':mode.get('BdyCounterData.Previous.PVC.TotalPVCCount', '0'),
                        'nsvt_counter_life':mode.get('VTachyCounterData.Life.NonSustainedEpsd', '0'),
                        'nsvt_counter_reset':mode.get('VTachyCounterData.Reset.NonSustainedEpsd', '0'),
                        'vt_counter_life':mode.get('VTachyCounterData.Life.VTEpsdTotal', '0'),
                        'vt1_counter_life':mode.get('VTachyCounterData.Life.VT1EpsdTotal', '0'),
                        'vf_counter_life':mode.get('VTachyCounterData.Life.VFEpsdTotal', '0'),
                        'vt_counter_reset':mode.get('VTachyCounterData.Reset.VTEpsdTotal', '0'),
                        'vt1_counter_reset':mode.get('VTachyCounterData.Reset.VT1EpsdTotal', '0'),
                        'vf_counter_reset':mode.get('VTachyCounterData.Reset.VFEpsdTotal', '0'),

                        ####### test results
                        # RA
                        'ra_test_sense':mode.get('ManualIntrinsicResult.RAMsmt.Msmt', '0'),
                        'ra_test_threshold':mode.get('InterPaceThreshResult.RAMsmt.Amplitude', '0'),
                        'ra_test_pulsewidth':mode.get('InterPaceThreshResult.RAMsmt.PulseWidth', '0'),
                        'ra_test_impedance':mode.get('ManualLeadImpedData.RAMsmt.Msmt', '0'),
                        # RV
                        'rv_test_sense':mode.get('ManualIntrinsicResult.RVMsmt.Msmt', '0'),
                        'rv_test_threshold':mode.get('InterPaceThreshResult.RVMsmt.Amplitude', '0'),
                        'rv_test_pulsewidth':mode.get('InterPaceThreshResult.RVMsmt.PulseWidth', '0'),
                        'rv_test_impedance':mode.get('ManualLeadImpedData.RVMsmt.Msmt', '0'),
                        'hv_test_impedance':mode.get('ShockImpedanceLastMeas', '0'),
                        # LV
                        'lv_test_sense':mode.get('', '0'),
                        'lv_test_impedance':mode.get('ManualLeadImpedData.LVMsmt.Msmt', '0'),
                        'lv_test_threshold':mode.get('InterPaceThreshResult.LVMsmt.Amplitude', '0'),                       
                        'lv_test_pulsewidth':mode.get('InterPaceThreshResult.LVMsmt.PulseWidth', '0'),

                        ######  Settings
                        'mode':mode.get('BdyNormBradyMode', '-'),
                        'lowrate':mode.get('NormParams.LRLIntvl', '0'),
                        'max_tracking':mode.get('NormParams.MTRIntvl', '0'),
                        'max_sensor_rate':mode.get('', '0'),
                        'paced_AV_delay':mode.get('BdyNormAVDelayMax', '0'),
                        'sensed_AV_delay':mode.get('BdyNormSensedAVDelayMax', '0'),
                        'ra_amplitude':mode.get('BdyNormAAmplitude', '0'),
                        'ra_pulsewidth':mode.get('BdyNormAPulseWidth', '0'),
                        'ra_pace_polarity':mode.get('PaceVectorsParam.RA', '-'),
                        'ra_sense_polarity':mode.get('SenseVectorsParam.RA', '-'),
                        'ra_sensitivity':mode.get('CardiacSensingParams.BdyNormRASensitivity', '-'),
                        'rv_amplitude':mode.get('BdyNormVAmplitude', '0'),
                        'rv_pulsewidth':mode.get('BdyNormVPulseWidth', '0'),
                        'rv_sensitivity':mode.get('CardiacSensingParams.BdyNormRVSensitivity', '-'),
                        'rv_pace_polarity':mode.get('PaceVectorsParam.RV', '-'),
                        'rv_sense_polarity':mode.get('SenseVectorsParam.RV', '-'),
                        'lv_amplitude':mode.get('InterPaceThreshResult.LVMsmt.Amplitude', '0'),
                        'lv_pulsewidth':mode.get('', '0'),
                        'lv_polarity':mode.get('PaceVectorsParam.LV', '-'),
                        'LV Pulse Configuration': mode.get('', '-'),

                        ##### Battery
                        'batt_voltage':mode.get('', '0'),# not found currently in bnk file
                        'batt_remaining':mode.get('', '-'), # not found currently in bnk file
                        'batt_status':mode.get('BatteryStatus.BatteryPhase', '-'),
                        'batt_chrge_time':mode.get('CapformChargeTime', '0')}
        return self.bsc_Dict