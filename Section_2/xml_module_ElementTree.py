import xml.etree.ElementTree as xml

def createXml(filename):
    root = xml.Element('zAppointments')
    appt = xml.Element('appointment')
    root.append(appt)

    #Add appointment children
    begin = xml.SubElement(appt, 'begin')
    begin.text = "1181251680"

    uid = xml.SubElement(appt, "uid")
    uid.text = "040000008200E000"

    alarmTime = xml.SubElement(appt, "alarmTime")
    alarmTime.text = "1181572063"

    state = xml.SubElement(appt, "state")

    location = xml.SubElement(appt, "location")

    duration = xml.SubElement(appt, "duration")
    duration.text = "1800"

    subject = xml.SubElement(appt, "subject")

    tree = xml.ElementTree(root)
    with open(filename, 'wb') as fh:
        tree.write(fh)

if __name__ == '__main__':
    createXml('appt.xml')
