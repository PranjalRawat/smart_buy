import json
with open('mobile_and_accessories.json') as f:
		data = json.load(f)

for i in range(10):
    print(data[i]['title'],'--',data[i]['original_price'],'--',data[i]['discounted_price'],'--',data[i]['availability'])
