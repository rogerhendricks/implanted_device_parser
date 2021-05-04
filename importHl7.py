# class hl7():
#     def __init__(self, *args, **kwargs):
#         self.hl7Dict = {}
#     def getHl7(self, fileName):
#         with open(fileName) as hl7File:
#             hl7File =  hl7File.read()
#             h = HL7Message(hl7File)
#             mshDict = {}
#             pidDict = {}
#             obxList = h.obx
#             obxDict = {}
#             hl7Dict = {}
#             for obxdata in range(len(obxList)):
#                 key = obxList[obxdata].observation_identifier[1]
#                 value  = obxList[obxdata].observation_value[0]
#                 obxDict[str(key)] = str(value)
#             #return obxDict

#             # adding PID and MSH seperately as they do not change and are required as a valid hl7 message
#             pidDict['MDC_ATTR_PT_NAME_GIVEN'] = str(h.pid.patient_name[0][1])
#             pidDict['MDC_ATTR_PT_NAME_FAMILY'] = str(h.pid.patient_name[0][0])

#             mshDict['SEND_DATE'] = str(h.msh[7])
#             mshDict['SENDING_FACILITY'] = str(h.msh[4])
#             mshDict['RECEIVING_FACILITY'] = str(h.msh[6])

#             self.hl7Dict = dict(**pidDict,**mshDict, **obxDict)
#             return self.hl7Dict
#             #print(self.hl7Dict)
