import xml.etree.ElementTree as ET
import datetime

class bioImport():

    def __init__(self, *args, **kwargs):
        self.biodevdata = {}
        self.biosessdata = {}
        self.biobatdata = {}
        self.biocapdata = {}
        self.biorvdata = {}
        self.biobradydata = {}
        self.biolist = []
        self.bio_f_dict = {}
        self.bioradata = {}
        self.biohvdata = {}
        self.bioptdata = {}
        self.biolvdata = {}
        self.biodtdata = {}
        self.biostatdata = {}
        self.bioatdata = {}
        self.biocrtdata = {}
        self.biotachydata = {}
        self.biovt2data = {}
        self.biovfdata = {}
        self.bioatafdata = {}
        self.biosvtdata = {}
        self.bio_ra_sense_set_data = {}
        self.bio_ra_pace_set_data = {}
        self.bio_rv_sense_set_data = {}
        self.bio_rv_pace_set_data = {}
        self.biolvsetdata = {}

        self.bioepisodedata = {}
        self.bioepisodelist = []
        self.bioleaddata = {}
        self.bioleadlist = []

    def getBioDevData(self, fileName):
        parser = ET.XMLParser(encoding="UTF-8")
        tree = ET.parse(fileName, parser=parser)

        root = tree.getroot()
        #bioData = {}


        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="DEV"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biodevdata[keys] = values
        except:
            self.biodevdata = {}


        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="SESS"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biosessdata[keys] = values
        except:
            self.biosessdata = {}

        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="MSMT"]/section[@name="BATTERY"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                           self. biobatdata[keys] = values
        except:
            self.biobatdata = {}
        # Cap reformation and charge time
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="MSMT"]/section[@name="CAP"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biocapdata[keys] = values
        except:
            self.biocapdata = {}

        # RV test measurements
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="MSMT"]/section[@name="LEADCHNL_RV"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biorvdata[keys] = values
        except:
            self.biorvdata = {}
        # LV test measurements
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="MSMT"]/section[@name="LEADHVCHNL"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biohvdata[keys] = values
        except:
            self.biohvdata = {}
        
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="BRADY"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biobradydata[keys] = values
        except:
            self.biobradydata = {}

        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="AT"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.bioatdata[keys] = values
        except:
            self.bioatdata = {}

        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="TACHYTHERAPY"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biotachydata[keys] = values
        except:
            self.biotachydata = {}
        

        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="CRT"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biocrtdata[keys] = values
        except:
            self.biocrtdata = {}        
        # RA test measurements
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="MSMT"]/section[@name="LEADCHNL_RA"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.bioradata[keys] = values
        except:
            self.bioradata = {}
        
        # LV test measurements
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="MSMT"]/section[@name="LEADCHNL_LV"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biolvdata[keys] = values
        except:
            self.biolvdata = {}

        # Patient data
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="ATTR"]/section[@name="PT"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.bioptdata[keys] = values
        except:
                self.bioptdata = {}
        
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="BIO"]/section[@name="REQUEST"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biodtdata[keys] = values
        except:
                self.biodtdata = {}

        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="STAT"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biostatdata[keys] = values
                    
        except:
            self.biostatdata = {}

        # getting episodes
        try:
            for child in root.iter("dataset"):
                for x in child.findall('.//section[@name="STAT"]/section[@name="EPISODE"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.bioepisodedata[keys] = values
                    self.bioepisodelist.append(self.bioepisodedata.copy()) # gets a copy for each loop and appends it to list without .copy method it only appends last loop 
            #print(self.bioepisodelist)        
    
        except:
            self.bioepisodelist = ()

        # RA  sense settings
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="SET"]/section[@name="LEADCHNL_RA"]/section[@name="SENSING"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.bio_ra_sense_set_data[keys] = values
        except:
            self.bio_ra_sense_set_data = {}

        # RA pace settings
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="SET"]/section[@name="LEADCHNL_RA"]/section[@name="PACING"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.bio_ra_pace_set_data[keys] = values
        except:
            self.bio_ra_pace_set_data = {}

        # RV  sensing settings
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="SET"]/section[@name="LEADCHNL_RV"]/section[@name="SENSING"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.bio_rv_sense_set_data[keys] = values
        except:
            self.bio_rv_sense_set_data = {}

        # RV  pace settings
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="SET"]/section[@name="LEADCHNL_RV"]/section[@name="PACING"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.bio_rv_pace_set_data[keys] = values
        except:
            self.bio_rv_pace_set_data = {}

        # LV  settings
        try:
            for child in root.iter("dataset"):
                for x in child.find('.//section[@name="SET"]/section[@name="LEADCHNL_LV"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.biolvsetdata[keys] = values
        except:
            self.biolvsetdata = {}
        
        # Leads
        try:
            for child in root.iter("dataset"):
                for x in child.findall('.//section[@name="LEAD"]'):
                    for a in x.iter('value'):
                        values = a.text
                        keys = a.get('name')
                        for i in keys:
                            self.bioleaddata[keys] = values
                    self.bioleadlist.append(self.bioleaddata.copy()) # gets a copy for each loop and appends it to list without .copy method it only appends last loop 
            print(self.bioleadlist)        
    
        except:
            self.bioleadlist = ()

            
        self.biolist.append(self.biobradydata)  #0
        self.biolist.append(self.biorvdata)  #1 RV test results
        self.biolist.append(self.biocapdata)  #2
        self.biolist.append(self.biosessdata)  #3
        self.biolist.append(self.biodevdata)  #4
        self.biolist.append(self.biobatdata)  #5
        self.biolist.append(self.bioradata)  #6 RA test results
        self.biolist.append(self.biohvdata)  #7 HV test results
        self.biolist.append(self.bioptdata)  #8
        self.biolist.append(self.biolvdata)  #9 LV test results
        self.biolist.append(self.biodtdata) #10
        self.biolist.append(self.biostatdata) #11
        self.biolist.append(self.bioatdata) #12
        self.biolist.append(self.biocrtdata) #13
        self.biolist.append(self.biotachydata) #14
        self.biolist.append(self.bioepisodelist) #15
        self.biolist.append(self.bio_ra_sense_set_data) #16 RA sense settings
        self.biolist.append(self.bio_ra_pace_set_data) #17 RA pace settings
        self.biolist.append(self.bio_rv_sense_set_data) #18 RV sense  settings
        self.biolist.append(self.bio_rv_pace_set_data) # 19 RV pace settings
        self.biolist.append(self.biolvsetdata) #20 LV settings
        self.biolist.append(self.bioleadlist) #21 Lead data


    def mode(self):
        mode = self.biolist
    
        self.bio_dict = {
        'name_given':mode[8].get('NAME_GIVEN', 'Not Given'),
        'name_family':mode[8].get('NAME_FAMILY', 'Not Given'),
        'client_id':mode[8].get('ID', '-'),
        'followup_physician':'-',
        'sess_date': datetime.datetime.strptime(mode[10].get('DATE'), "%Y%m%dT%H%M%S%z").replace(tzinfo=None),
        'dev_implant_date': datetime.datetime.strptime(mode[4].get('IMPLANT_DT'), "%Y%m%dT%H%M%S").strftime("%d-%m-%Y"),
        'type':mode[4].get('TYPE', '-'), # CIED device type
        'model': mode[4].get('MODEL', '-'), # device model name
        'device_name':mode[4].get('MODEL','-'),
        'serial': mode[4].get('SERIAL', '-'), # device serial number
        'mfg':mode[4].get('MFG', 'Biotronik'), # manufacturer

        ###### diagnostics

        'ra_percent_paced': mode[11].get('RA_PERCENT_PACED', '0'), # ra pacing percentage
        'rv_percent_paced': mode[11].get('RV_PERCENT_PACED', '0'), # rv pacing percentage
        'lv_percent_paced': mode[11].get('LV_PERCENT_PACED', '0'), # LV pacing percentage
        'biv_percent_paced': mode[11].get('PERCENT_PACED', '0'),


        ##### arrhythmia log is 15
        # 'biv_percent_paced': mode[13].get('PERCENT_PACED', '0'), # biventricular pacing percentage
        'at_burden': mode[12].get('BURDEN_PERCENT', '0'), #at/af burden in pecentage form
        # 'total_pac_count'
        # 'total_pvc_count'
        
        

       
        #ra
        'ra_test_sense': mode[6].get('INTR_AMPL_MEAN', '0'), # ra sensing
        'ra_test_threshold':mode[6].get('AMPLITUDE', '0'), # ra voltage threshold
        'ra_test_pulsewidth':mode[6].get('PULSEWIDTH', '0'), # ra pacing pulse width
        'ra_test_impedance': mode[6].get('VALUE', '0'), 
        #rv
        'rv_test_sense': mode[1].get('INTR_AMPL_MEAN', '0'), # rv sensing
        'rv_test_threshold':mode[1].get('AMPLITUDE', '0'), # rv voltage threshold
        'rv_test_pulsewidth':mode[1].get('PULSEWIDTH', '0'), # rv pacing pulse width
        'rv_test_impedance': mode[1].get('VALUE', '0'), # rv impedance measurement
        'hv_test_impedance':mode[7].get('IMPEDANCE', '0'),  # hv impedance measurement
        #lv
        'lv_test_sense': mode[9].get('INTR_AMPL_MEAN', '0'), # lv sensing
        'lv_test_impedance':mode[9].get('VALUE', '0'), # lv impedance measurement
        'lv_test_threshold':mode[9].get('AMPLITUDE', '0'), # lv voltage threshold
        'lv_test_pulsewidth':mode[9].get('PULSEWIDTH', '0'), # lv pacing pulse width
        

        #### Settings : RA sensing is 16, RA pace is 17, RV sense is 18, RV pace is 19
        'mode': mode[0].get('MODE', '-'), 
        'lowrate': mode[0].get('LOWRATE', '0'),
        'max_tracking_rate': mode[0].get('MAX_TRACKING_RATE', '0'),
        'max_sensor_rate':mode[0].get('MAX_SENSOR_RATE', '0'),
        'paced_AV_delay':mode[0].get('SAV_DELAY_LOW', '0'),
        'sensed_AV_delay':mode[0].get('PAV_DELAY_LOW', ''),
        'ra_amplitude':mode[17].get('AMPLITUDE', '0'),
        'ra_pulsewidth':mode[17].get('PULSEWIDTH', '0'),
        'ra_pace_polarity':mode[17].get('POLARITY', '-'), # ra pacing polarity
        'ra_sense_polarity':mode[16].get('POLARITY', '-'), # ra sensing polarity
        'ra_sensitivity':mode[16].get('SENSITIVITY', '0'),
        'rv_amplitude':mode[19].get('AMPLITUDE', '0'),
        'rv_pulsewidth':mode[19].get('PULSEWIDTH', '0'),
        'rv_sensitivity':mode[18].get('SENSITIVITY', '0'),
        'rv_pace_polarity':mode[19].get('POLARITY', '-'), # rv pacing polarity
        'rv_sense_polarity':mode[18].get('POLARITY', '-'),
        'lv_amplitude':mode[9].get('lv_amplitude', '-'), # these are the measurements for LV
        'lv_pulsewidth':'-',
        'lv_polarity':mode[9].get('POLARITY', '-'),
        'LV Pulse Configuration': '-',

        ##### Battery 5 and 2
        'batt_voltage' : mode[5].get('VOLTAGE', '0'), 
        'batt_remaining' : mode[5].get('REMAINING_PERCENTAGE', '-'), # remaining battery percentage
        'batt_status' : mode[5].get('STATUS', '-'),
        'batt_chrge_time' : mode[2].get('CHARGE_TIME', '0'),
        }

        leadIndex = 0
        for leads in mode[21]:
            for k, v in leads.items():               
                print(k +"_"+str(leadIndex),  v)
                self.bio_dict[k.lower() +"_"+str(leadIndex)] = v
            leadIndex +=1
            
        if mode[4].get('TYPE') == "ICD" or "CRT_D" and mode[15]:
            # AT/AF is 0, SVT is 1, VF is 2, VT1 is 3, NSVT is 4, VT2 is 5
            # AT/AF & SVT Episodes
            self.bio_dict['ataf_total'] = mode[15][0].get('TOTAL_COUNT', '0')
            self.bio_dict['ataf_reset'] =  mode[15][0].get('RECENT_COUNT', '0')
            self.bio_dict['svt_total'] = mode[15][1].get('TOTAL_SVT', '0')
            self.bio_dict['svt_reset'] = mode[15][1].get('RECENT_SVT', '0')
            # VT & VF Episodes 
            self.bio_dict['nsvt_counter_life'] = mode[15][4].get('TOTAL_COUNT', '0')
            self.bio_dict['nsvt_counter_reset']= mode[15][4].get('RECENT_COUNT', '0')
            self.bio_dict['vt_counter_life'] = mode[15][3].get('TOTAL_COUNT', '0')
            self.bio_dict['vt_counter_reset'] = mode[15][3].get('TOTAL_COUNT', '0')
            self.bio_dict['vf_counter_life'] = mode[15][2].get('TOTAL_COUNT', '0')
            self.bio_dict['vf_counter_reset'] = mode[15][2].get('RECENT_COUNT', '0')
            self.bio_dict['vt2_counter_reset'] = mode[15][5].get('RECENT_COUNT', '0')
            self.bio_dict['vt2_counter_reset'] = mode[15][5].get('TOTAL_COUNT', '0')
        return self.bio_dict

        