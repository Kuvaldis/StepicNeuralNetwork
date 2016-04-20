import numpy as np

examples = np.array([[1, 1.0, 0.3], [1, 0.4, 0.5], [1, 0.7, 0.8]])
targets = [1, 1, 0]
ws = np.array([0, 0, 0])

perfect = True
for i, e in enumerate(examples):
	target = targets[i]
	predict = 1 if ws.dot(e.T) > 0 else 0
	if predict != target:
		perfect = False
		if predict == 0:
			ws = ws + e
		elif predict == 1:
			ws = ws - e
output = ",".join(map(str, ws))			
print(output)