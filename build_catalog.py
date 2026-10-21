"""Build the public link catalog from the private offline collection; no images copied."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
source=HERE.parent/'!PINOUTS'/'manifest.json'
rows=json.loads(source.read_text(encoding='utf-8'))
labels={'01_Boards':'Boards','02_Sensors':'Sensors','03_Displays_and_LEDs':'Displays & LEDs','04_Communication_and_GPS':'Communication & GPS','05_Motor_Drivers_and_Relays':'Motors & relays','06_Clocks_Storage_and_Logic':'Clocks, storage & logic','07_Inputs_and_Controls':'Inputs & controls','08_Power_Modules':'Power modules'}
official={'Arduino UNO R3':'https://content.arduino.cc/assets/A000066-full-pinout.pdf','Arduino Mega 2560':'https://docs.arduino.cc/resources/pinouts/A000067-full-pinout.pdf','Arduino Nano classic':'https://docs.arduino.cc/resources/pinouts/A000005-full-pinout.pdf'}
out=[]
for r in rows:
    if not r.get('files'):continue
    cat=r['category'].split('/')[0]
    item={'name':r['name'],'category':labels[cat],'group':r['category'].split('/')[-1].replace('_',' ') if '/' in r['category'] else labels[cat], 'source':r['source'],'publisher':'Components101' if 'components101' in r['source'] else 'Last Minute Engineers','diagrams':[{'label':f['label'],'url':f['url'],'kind':f['kind']} for f in r['files']]}
    if r['name'] in official:item['official']=official[r['name']]
    out.append(item)
out.sort(key=lambda x:(list(labels.values()).index(x['category']),x['name'].casefold()))
(HERE/'catalog.js').write_text('const catalog = '+json.dumps(out,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
(HERE/'catalog.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(out)} entries; {sum(len(x["diagrams"]) for x in out)} diagram links; no local paths or copied images.')
