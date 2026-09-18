import re
ESC=[r"\brefund\b",r"\bchargeback\b",r"\baccount hacked\b",r"\bsecurity\b",r"\bpersonal data\b",r"\blawsuit\b",r"\blegal\b",r"\bcomplaint\b",r"\bscam\b",r"\bfraud\b"]
T={
'battery_issue':'Thanks for reaching out. Please share your device model and iOS version, and let us know whether the battery drains during charging so we can narrow this down.',
'software_update':'Thanks for reaching out. Please share your device model and iOS version, plus what happens when you try the update.',
'app_issue':'Sorry you are running into this. Please tell us which app is affected, your device model, and iOS version.',
'account_access':'We can help troubleshoot this. Please do not post account credentials here; use the private support channel for account-specific help.',
'connectivity':'Please share the device model, iOS version, and whether the issue affects Wi-Fi, Bluetooth, or mobile connectivity.',
'device_hardware':'Please share the device model and describe what is happening with the hardware. Avoid posting personal information publicly.',
'storage_performance':'Please share your device model, iOS version, and available storage so we can narrow down the issue.',
'purchase_billing':'For billing or purchase issues, please use the private support channel and do not post payment details publicly.',
'feature_how_to':'I can help with that. Please tell me the feature and your device/iOS version so I can give the relevant steps.',
'other':'Thanks for reaching out. Please provide a little more detail about the issue and your device/app context so we can route it correctly.'}
def escalate(msg,sim,conf=1):
    reasons=[];t=str(msg).lower()
    if any(re.search(p,t) for p in ESC):reasons.append('sensitive financial/security/legal/complaint language')
    if sim<.25:reasons.append('low historical similarity')
    if conf<.35:reasons.append('low intent confidence')
    return bool(reasons),'; '.join(reasons) if reasons else 'sufficient grounding for routine handling'
def reply(msg,intent,evidence,api_key=None,model='gpt-4o-mini'):
    if not api_key or not evidence:return T.get(intent,T['other'])
    try:
        from openai import OpenAI
        c=OpenAI(api_key=api_key)
        ev='\n\n'.join(f"Customer: {x['customer_message']}\nSupport: {x['support_reply']}" for x in evidence)
        prompt=f"Intent: {intent}\nCustomer: {msg}\nHistorical examples:\n{ev}\nDraft a concise reply grounded only in these examples. Do not invent policies, refunds, links or actions. Do not request passwords or payment credentials."
        r=c.chat.completions.create(model=model,temperature=.2,max_tokens=180,messages=[{'role':'system','content':'You draft grounded customer support replies.'},{'role':'user','content':prompt}])
        return r.choices[0].message.content.strip()
    except Exception:return T.get(intent,T['other'])
