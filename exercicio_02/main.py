import math

# Dados do problema
amplitude_cm = 15  # Amplitude em centímetros
frequencia = 20     # Frequência em Hz
c = 331 % 10       # Valor de c

# Conversão da amplitude para metros
amplitude_m = amplitude_cm / 100  # 1 metro = 100 centímetros

# Frequência angular (em radianos por segundo)
omega = 2 * math.pi * frequencia

# Tempo em que queremos calcular a aceleração
t = 10  # segundos

# Equação do deslocamento
deslocamento = amplitude_m * math.cos(omega * t - c)

# Equação da aceleração
aceleracao = -amplitude_m * omega**2 * math.cos(omega * t - c)

# Imprime os resultados
print("Equação do deslocamento (x(t)): x =", deslocamento, "metros")
print("Equação da aceleração (a(t)): a =", aceleracao, "metros por segundo quadrado")
