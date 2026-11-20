from pathlib import Path as P
import json, hashlib, soundfile as sf,numpy as np
from PIL import Image
read=lambda p:json.loads(P(p).read_text()); scenes=read('content/scenes.json');audio={a['id']:a for a in read('content/audio-manifest.json')};blocks=read('content/blocks.json');sources={s['id'] for s in read('content/sources.json')};catalogue=read('content/coverage.json');errors=[];todo=[]
for e in catalogue:
 if not any(e['id'] in s['eventIds'] for s in scenes):todo.append(e['id']+' : scène, image et narration à produire')
for s in scenes:
 for route,seq in s['nextSceneRules'].items():
  if s['sceneId'] not in seq:errors.append(s['sceneId']+' inaccessible '+route)
 for k in s['sourceIds']:
  if k not in sources:errors.append('référence '+k)
 for k in s['narrativeBlocks']:
  a=audio.get(k)
  if not a or k not in s['audioRefs'] or not P(a['path']).is_file():errors.append('MP3 absent : '+k);continue
  if a['scene']!=s['sceneId'] or a['sha256']!=hashlib.sha256(blocks[k].encode()).hexdigest() or blocks[k]!=a['texte']:errors.append('variante ou empreinte : '+k)
  try:
   data,rate=sf.read(a['path']);assert sf.info(a['path']).subtype=='MPEG_LAYER_III' and len(data)>0 and abs(len(data)/rate-a['duree'])<.03 and np.max(np.abs(data))>.005 and P(a['path']).stat().st_size==a['poids']
  except Exception:errors.append('décodage/durée : '+k)
 for p in s['imageRefs']:
  try:
   with Image.open(p) as img:assert img.format=='JPEG';img.verify()
  except Exception:errors.append('illustration : '+p)
 for c in s['choices']:
  if c['destination'] not in {x['sceneId'] for x in scenes}|{'route','fin','retry'}:errors.append('destination '+c['id'])
 if not any(not c['preconditions'] and c['destination']!='retry' for c in s['choices']):errors.append('sortie inconditionnelle absente '+s['sceneId'])
if set(blocks)!={x for s in scenes for x in s['narrativeBlocks']}:errors.append('bloc sans scène')
print(json.dumps(dict(erreursPilote=errors,manquesCampagne=todo),ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
