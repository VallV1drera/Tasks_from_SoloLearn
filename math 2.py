import matplotlib.pyplot as plt

# Значения критериев 𝑓1 и 𝑓2
crit1 = [4.7, 6.5, 2.7, 3.2, 2.8, 1.6, 2.2, 5.8, 3.2, 6.0, 1.4, 4.5, 2.4, 5.7]
crit2 = [4.5, 2.2, 3.8, 1.8, 2.1, 4.8, 4.7, 5.9, 7.4, 5.0, 3.0, 2.1, 6.7, 3.8]

# Сортировка решений по каждому критерию
sorted_crit1 = sorted(crit1)
sorted_crit2 = sorted(crit2)

# Массив для хранения недоминируемых вариантов решений
non_dominated = []

# Пошаговое определение недоминируемых вариантов
for i in range(len(sorted_crit1)):
    is_dominated = False
    for j in range(len(sorted_crit2)):
        if crit1[j] < sorted_crit1[i] and crit2[j] < sorted_crit2[i]:
            is_dominated = True  # если нашли хотя бы одно доминирующее решение, то текущее решение доминируется
            break
    if not is_dominated:
        non_dominated.append((sorted_crit1[i], sorted_crit2[i]))

# Разделение недоминируемых вариантов по критериям
non_dominated_crit1 = [x[0] for x in non_dominated]
non_dominated_crit2 = [x[1] for x in non_dominated]

# Построение критериальной плоскости с недоминируемыми вариантами
plt.scatter(crit1, crit2, color='b', label='Альтернативы')
plt.scatter(non_dominated_crit1, non_dominated_crit2, color='r', label='Недоминируемые варианты')
plt.xlabel('Критерий 𝑓1')
plt.ylabel('Критерий 𝑓2')
plt.title('Недоминируемые варианты решений')
plt.legend()
plt.show()