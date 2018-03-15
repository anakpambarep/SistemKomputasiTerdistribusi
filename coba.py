#author : erdiansahlan@student.ub.ac.id

import json

json.dumps({'Suhu': 24, 'Kelembapan': '15%', 'Kadar O2': '30mg'}, sort_keys=True, indent=4)
data = json.loads()