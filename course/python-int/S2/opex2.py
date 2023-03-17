segundosTotais = int(input("Por favor, entre com o número de segundos que deseja converter:"))

segundos = segundosTotais % 60
minutosTotais = segundosTotais // 60
minutos = minutosTotais % 60
horasTotais = minutosTotais // 60
horas = horasTotais % 24
diasTotais = horasTotais // 24

print(diasTotais, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.") 