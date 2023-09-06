import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Cria as variáveis do problema

# Idade das aves
# Idade das aves
idade = ctrl.Antecedent(np.arange(0, 22, 1), 'idade')
idade['I1'] = fuzz.trapmf(idade.universe, [0, 2, 4, 8])
idade['I2'] = fuzz.trapmf(idade.universe, [7, 10, 13, 15])
idade['I3'] = fuzz.trapmf(idade.universe, [14, 16, 19, 22]) 

# Temperatura do ar
temperatura = ctrl.Antecedent(np.arange(20, 36, 1), 'temperatura')
temperatura['T1'] = fuzz.trapmf(temperatura.universe, [20, 22, 24, 26])
temperatura['T2'] = fuzz.trapmf(temperatura.universe, [25, 25, 28.5, 28.5])
temperatura['T3'] = fuzz.trapmf(temperatura.universe, [28, 28, 30, 30])
temperatura['T4'] = fuzz.trapmf(temperatura.universe, [29, 29, 33, 33])
temperatura['T5'] = fuzz.trapmf(temperatura.universe, [32, 32, 35, 36])

# Umidade relativa do ar
umidade = ctrl.Antecedent(np.arange(20, 100, 1), 'umidade')
umidade['UR1'] = fuzz.trapmf(umidade.universe, [20, 30, 40, 58])
umidade['UR2'] = fuzz.trapmf(umidade.universe, [55, 65, 70, 75])
umidade['UR3'] = fuzz.trapmf(umidade.universe, [70, 80, 90, 100])


# Variáveis de saída
CR = ctrl.Consequent(np.arange(0, 1500, 1), 'CR')


GP = ctrl.Consequent(np.arange(0, 1000, 1), 'GP')


CA = ctrl.Consequent(np.arange(0, 20, 1), 'CA')

# CR
# CR
CR['CR1'] = fuzz.trimf(CR.universe, [80, 100, 180])
CR['CR2'] = fuzz.trimf(CR.universe, [80, 180, 190])
CR['CR3'] = fuzz.trimf(CR.universe, [180, 180, 250])
CR['CR4'] = fuzz.trimf(CR.universe, [190, 330, 380])
CR['CR5'] = fuzz.trimf(CR.universe, [270, 340, 380])
CR['CR6'] = fuzz.trimf(CR.universe, [380, 380, 450])
CR['CR7'] = fuzz.trimf(CR.universe, [390, 550, 600])
CR['CR8'] = fuzz.trimf(CR.universe, [490, 660, 760])
CR['CR9'] = fuzz.trimf(CR.universe, [700, 820, 1000])

# GP
GP['GP1'] = fuzz.trimf(GP.universe, [100, 100, 120.5])
GP['GP2'] = fuzz.trimf(GP.universe, [100, 150, 170])
GP['GP3'] = fuzz.trimf(GP.universe, [130, 170, 200])
GP['GP4'] = fuzz.trimf(GP.universe, [170, 200, 210])
GP['GP5'] = fuzz.trimf(GP.universe, [200, 250, 300])
GP['GP6'] = fuzz.trimf(GP.universe, [250, 310, 360])
GP['GP7'] = fuzz.trimf(GP.universe, [330, 370, 415])
GP['GP8'] = fuzz.trimf(GP.universe, [370, 415, 450])
GP['GP9'] = fuzz.trimf(GP.universe, [415, 430, 455])
GP['GP10'] = fuzz.trimf(GP.universe, [450, 510, 580])
GP['GP11'] = fuzz.trimf(GP.universe, [510, 600, 700])

# CA
CA['CA1'] = fuzz.trimf(CA.universe, [6.3, 8.2, 11.3])
CA['CA2'] = fuzz.trimf(CA.universe, [10, 11.5, 12.85])
CA['CA3'] = fuzz.trimf(CA.universe, [11.5, 12, 13])
CA['CA4'] = fuzz.trimf(CA.universe, [12.85, 14, 15])
CA['CA5'] = fuzz.trimf(CA.universe, [13.8, 14.85, 15.3])
CA['CA6'] = fuzz.trimf(CA.universe, [15, 15.25, 16])




rule1 = ctrl.Rule(idade['I1'] & temperatura['T1'] & umidade['UR1'], (CR['CR1'], GP['GP1'], CA['CA1']))
rule2 = ctrl.Rule(idade['I1'] & temperatura['T1'] & umidade['UR2'], (CR['CR2'], GP['GP2'], CA['CA2']))
rule3 = ctrl.Rule(idade['I1'] & temperatura['T1'] & umidade['UR3'], (CR['CR3'], GP['GP3'], CA['CA3']))
rule4 = ctrl.Rule(idade['I1'] & temperatura['T2'] & umidade['UR1'], (CR['CR4'], GP['GP4'], CA['CA4']))
rule5 = ctrl.Rule(idade['I1'] & temperatura['T2'] & umidade['UR2'], (CR['CR1'], GP['GP1'], CA['CA2']))
rule6 = ctrl.Rule(idade['I1'] & temperatura['T2'] & umidade['UR3'], (CR['CR2'], GP['GP1'], CA['CA2']))
rule7 = ctrl.Rule(idade['I1'] & temperatura['T3'] & umidade['UR1'], (CR['CR2'], GP['GP4'], CA['CA1']))
rule8 = ctrl.Rule(idade['I1'] & temperatura['T3'] & umidade['UR2'], (CR['CR2'], GP['GP1'], CA['CA2']))
rule9 = ctrl.Rule(idade['I1'] & temperatura['T3'] & umidade['UR3'], (CR['CR3'], GP['GP3'], CA['CA2']))
rule10 = ctrl.Rule(idade['I1'] & temperatura['T4'] & umidade['UR1'], (CR['CR1'], GP['GP2'], CA['CA1']))
rule11 = ctrl.Rule(idade['I1'] & temperatura['T4'] & umidade['UR2'], (CR['CR1'], GP['GP1'], CA['CA2']))
rule12 = ctrl.Rule(idade['I1'] & temperatura['T4'] & umidade['UR3'], (CR['CR2'], GP['GP2'], CA['CA2']))
rule13 = ctrl.Rule(idade['I1'] & temperatura['T5'] & umidade['UR1'], (CR['CR2'], GP['GP2'], CA['CA2']))
rule14 = ctrl.Rule(idade['I1'] & temperatura['T5'] & umidade['UR2'], (CR['CR2'], GP['GP2'], CA['CA2']))
rule15 = ctrl.Rule(idade['I1'] & temperatura['T5'] & umidade['UR3'], (CR['CR2'], GP['GP2'], CA['CA2']))
rule16 = ctrl.Rule(idade['I2'] & temperatura['T1'] & umidade['UR1'], (CR['CR4'], GP['GP4'], CA['CA3']))
rule17 = ctrl.Rule(idade['I2'] & temperatura['T1'] & umidade['UR2'], (CR['CR5'], GP['GP5'], CA['CA5']))
rule18 = ctrl.Rule(idade['I2'] & temperatura['T1'] & umidade['UR3'], (CR['CR4'], GP['GP4'], CA['CA2']))
rule19 = ctrl.Rule(idade['I2'] & temperatura['T2'] & umidade['UR1'], (CR['CR4'], GP['GP4'], CA['CA4']))
rule20 = ctrl.Rule(idade['I2'] & temperatura['T2'] & umidade['UR2'], (CR['CR4'], GP['GP5'], CA['CA3']))
rule21 = ctrl.Rule(idade['I2'] & temperatura['T2'] & umidade['UR3'], (CR['CR4'], GP['GP5'], CA['CA3']))
rule22 = ctrl.Rule(idade['I2'] & temperatura['T3'] & umidade['UR1'], (CR['CR4'], GP['GP5'], CA['CA3']))
rule23 = ctrl.Rule(idade['I2'] & temperatura['T3'] & umidade['UR2'], (CR['CR4'], GP['GP5'], CA['CA4']))
rule24 = ctrl.Rule(idade['I2'] & temperatura['T3'] & umidade['UR3'], (CR['CR7'], GP['GP7'], CA['CA4']))
rule25 = ctrl.Rule(idade['I2'] & temperatura['T4'] & umidade['UR1'], (CR['CR6'], GP['GP6'], CA['CA4']))
rule26 = ctrl.Rule(idade['I2'] & temperatura['T4'] & umidade['UR2'], (CR['CR5'], GP['GP6'], CA['CA2']))
rule27 = ctrl.Rule(idade['I2'] & temperatura['T4'] & umidade['UR3'], (CR['CR5'], GP['GP5'], CA['CA5']))
rule28 = ctrl.Rule(idade['I2'] & temperatura['T5'] & umidade['UR1'], (CR['CR4'], GP['GP4'], CA['CA5']))
rule29 = ctrl.Rule(idade['I2'] & temperatura['T5'] & umidade['UR2'], (CR['CR3'], GP['GP4'], CA['CA5']))
rule30 = ctrl.Rule(idade['I2'] & temperatura['T5'] & umidade['UR3'], (CR['CR3'], GP['GP4'], CA['CA5']))
rule31 = ctrl.Rule(idade['I3'] & temperatura['T1'] & umidade['UR1'], (CR['CR7'], GP['GP8'], CA['CA5']))
rule32 = ctrl.Rule(idade['I3'] & temperatura['T1'] & umidade['UR2'], (CR['CR8'], GP['GP8'], CA['CA6']))
rule33 = ctrl.Rule(idade['I3'] & temperatura['T1'] & umidade['UR3'], (CR['CR8'], GP['GP8'], CA['CA6']))
rule34 = ctrl.Rule(idade['I3'] & temperatura['T2'] & umidade['UR1'], (CR['CR7'], GP['GP7'], CA['CA5']))
rule35 = ctrl.Rule(idade['I3'] & temperatura['T2'] & umidade['UR2'], (CR['CR5'], GP['GP6'], CA['CA5']))
rule36 = ctrl.Rule(idade['I3'] & temperatura['T2'] & umidade['UR3'], (CR['CR9'], GP['GP11'], CA['CA5']))
rule37 = ctrl.Rule(idade['I3'] & temperatura['T3'] & umidade['UR1'], (CR['CR8'], GP['GP9'], CA['CA5']))
rule38 = ctrl.Rule(idade['I3'] & temperatura['T3'] & umidade['UR2'], (CR['CR9'], GP['GP6'], CA['CA5']))
rule39 = ctrl.Rule(idade['I3'] & temperatura['T3'] & umidade['UR3'], (CR['CR8'], GP['GP6'], CA['CA5']))
rule40 = ctrl.Rule(idade['I3'] & temperatura['T4'] & umidade['UR1'], (CR['CR8'], GP['GP10'], CA['CA6']))
rule41 = ctrl.Rule(idade['I3'] & temperatura['T4'] & umidade['UR2'], (CR['CR8'], GP['GP8'], CA['CA6']))
rule42 = ctrl.Rule(idade['I3'] & temperatura['T4'] & umidade['UR3'], (CR['CR7'], GP['GP7'], CA['CA6']))
rule43 = ctrl.Rule(idade['I3'] & temperatura['T5'] & umidade['UR1'], (CR['CR7'], GP['GP7'], CA['CA6']))
rule44 = ctrl.Rule(idade['I3'] & temperatura['T5'] & umidade['UR2'], (CR['CR7'], GP['GP6'], CA['CA6']))
rule45 = ctrl.Rule(idade['I3'] & temperatura['T5'] & umidade['UR3'], (CR['CR6'], GP['GP6'], CA['CA6']))







# Adicionando regras ao sistema e criando a simulação
system = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
    rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17,
    rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25,
    rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33,
    rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41,
    rule42, rule43, rule44, rule45
])


sim = ctrl.ControlSystemSimulation(system)

# Entrada de dados pelo usuário
try:
    idade_user = float(input("Digite a idade das aves (0 a 22 dias): "))
    temperatura_user = float(input("Digite a temperatura do ar (20 a 36°C): "))
    umidade_user = float(input("Digite a umidade relativa do ar (20 a 100%): "))
    
    sim.input['idade'] = idade_user
    sim.input['temperatura'] = temperatura_user
    sim.input['umidade'] = umidade_user
except ValueError:
    print("Valor inserido não é válido. Por favor, insira um número.")
    exit()

# Computar a inferência
sim.compute()


print(f"Consumo de Ração (CR): {sim.output['CR']}")
print(f"Ganho de Peso (GP): {sim.output['GP']}")
print(f"Conversão Alimentar (CA):{sim.output['CA']}")

variables = [idade, temperatura, umidade, CR, GP, CA]

for var in variables:
    var.view(sim=sim)


plt.show()