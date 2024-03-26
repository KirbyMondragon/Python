def generate_list(today):
  """Genera una lista de días desde hoy hasta 30 días después."""

  days = []
  for i in range(1, 31):
    day = today + timedelta(days=i)
    days.append(f"{day.strftime('%A, %d de %B de %Y')}")
  return days


today = date.today()
days = generate_list(today)

# Resalta los fines de semana
for i in range(len(days)):
  if days[i].split(',')[0] in ('Sábado', 'Domingo'):
    days[i] = f"<span style='color:red'>{days[i]}</span>"

print(days)