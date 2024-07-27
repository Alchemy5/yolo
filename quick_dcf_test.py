growth_rate = 3.6855580182064696/100
discount_rate = 0.057818362470047215
terminal_growth_rate = 1.84/100
initial_cash_flow = 2884000000.0

cash_flows = []
discounted_cash_flows = []

years = 10
for year in range(1, years + 1):
    next_cash_flow = initial_cash_flow * ((1 + growth_rate) ** year)
    cash_flows.append(next_cash_flow)

print(cash_flows)

for year in range(1, years + 1):
    discounted_cash_flow = cash_flows[year - 1] / ((1 + discount_rate) ** year)
    discounted_cash_flows.append(discounted_cash_flow)

print(discounted_cash_flows)

terminal_value = cash_flows[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)

print(terminal_value)

discounted_terminal_value = terminal_value / ((1 + discount_rate) ** years)

total_value = sum(discounted_cash_flows) + discounted_terminal_value

print(total_value / 721790976)
