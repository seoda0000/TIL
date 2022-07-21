s_cost, cost, price = map(int, input().split())

if price-cost <= 0:
  n = -1
else: 
  n = s_cost//(price-cost) + 1
print(n)