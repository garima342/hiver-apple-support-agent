import re
INTENTS=["battery_issue","software_update","app_issue","account_access","connectivity","device_hardware","storage_performance","purchase_billing","feature_how_to","other"]
PATTERNS={
"battery_issue":[r"\bbattery\b",r"\bcharging\b",r"\bcharger\b",r"\bcharge\b",r"\bdrain\b",r"\bpower\b"],
"software_update":[r"\bios\b",r"\bupdate\b",r"\bupdated\b",r"\bupgrade\b",r"\bverification\b"],
"app_issue":[r"\bapp\b",r"\bapps\b",r"\bcrash\b",r"\bcrashing\b",r"\bfreeze\b",r"\bfreezing\b"],
"account_access":[r"\bapple id\b",r"\bicloud\b",r"\blog.?in\b",r"\bpassword\b",r"\baccount\b"],
"connectivity":[r"\bwifi\b",r"\bwi-fi\b",r"\bbluetooth\b",r"\bnetwork\b",r"\binternet\b",r"\bdisconnect\b",r"\bsignal\b"],
"device_hardware":[r"\bscreen\b",r"\bdisplay\b",r"\bcamera\b",r"\bspeaker\b",r"\bmicrophone\b",r"\bhardware\b",r"\bbroken\b",r"\bdamaged\b"],
"storage_performance":[r"\bstorage\b",r"\bspace\b",r"\bmemory\b",r"\bslow\b",r"\bsluggish\b"],
"purchase_billing":[r"\bpayment\b",r"\bcharged\b",r"\bpurchase\b",r"\bbought\b",r"\brefund\b",r"\bbilling\b",r"\bprice\b"],
"feature_how_to":[r"\bhow do i\b",r"\bhow can i\b",r"\bhow to\b",r"\bcan i\b",r"\bwhere do i\b",r"\bhow does\b"]}
def weak_intent(text):
    t=str(text or '').lower()
    for intent in INTENTS[:-1]:
        if any(re.search(p,t) for p in PATTERNS[intent]): return intent
    return 'other'
