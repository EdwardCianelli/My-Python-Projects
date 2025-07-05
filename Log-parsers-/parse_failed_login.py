from Evtx.Evtx import Evtx
import xml.etree.ElementTree as ET

# Path to the EVTX log file we're working with
log_file = r"D:\Python\EVTX-ATTACK-SAMPLES-master\Credential Access\CA_4624_4625_LogonType2_LogonProc_chrome.evtx"

# Open the log file using python-evtx
with Evtx(log_file) as evtx:
    for record in evtx.records():
        try:
            # Parse the XML content of the log entry
            xml_content = record.xml()
            root = ET.fromstring(xml_content)

            # Get the event ID for this record
            event_id_element = root.find(".//{*}EventID")
            if event_id_element is None:
                continue

            # We're only interested in failed logon attempts (4625)
            if event_id_element.text != "4625":
                continue

            # Pull out a few key pieces of information
            timestamp   = root.find(".//{*}TimeCreated").attrib.get("SystemTime", "Unknown")
            username    = root.find(".//{*}Data[@Name='TargetUserName']").text
            domain      = root.find(".//{*}Data[@Name='TargetDomainName']").text
            logon_type  = root.find(".//{*}Data[@Name='LogonType']").text
            process     = root.find(".//{*}Data[@Name='ProcessName']").text
            ip_address  = root.find(".//{*}Data[@Name='IpAddress']").text

            # Print it in a way that's easy to read
            print("\nFailed login detected:")
            print(f"  Event ID:     {event_id_element.text}")
            print(f"  Time:         {timestamp}")
            print(f"  User:         {domain}\\{username}")
            print(f"  Logon Type:   {logon_type}")
            print(f"  Process:      {process}")
            print(f"  Source IP:    {ip_address}")
            print("-" * 50)

        except Exception as e:
            print(f"Error reading log entry: {e}")
