#kode program metodefuzzy tsukamoto menggunakan skfuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from matplotlib import pyplot as plt


# Varibel
kelembapan = ctrl.Antecedent(np.arange(0, 100.01, 0.5), 'kelembapan')
ketebalan = ctrl.Antecedent(np.arange(0, 100.01, 0.5), 'ketebalan')
umur = ctrl.Antecedent(np.arange(0, 100.01, 0.5), 'umur')
kelayakan = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'kelayakan')

# Membership function
kelembapan['basah'] = fuzz.trapmf(kelembapan.universe,[0,0,40,45])
kelembapan['lembab'] = fuzz.trimf(kelembapan.universe,[40,55,70])
kelembapan['kering'] = fuzz.trapmf(kelembapan.universe,[65,75,100,100])

ketebalan['tipis'] = fuzz.trapmf(ketebalan.universe,[0,0,40,45])
ketebalan['sedang'] = fuzz.trimf(ketebalan.universe,[40,55,70])
ketebalan['tebal'] = fuzz.trapmf(ketebalan.universe,[65,75,100,100])

umur['muda'] = fuzz.trapmf(umur.universe,[0,0,40,45])
umur['menengah'] = fuzz.trimf(umur.universe,[40,55,70])
umur['tua'] = fuzz.trapmf(umur.universe,[65,75,100,100])


kelayakan['tidak_layak'] = fuzz.trapmf(kelayakan.universe,[0,0,0.3,0.55])
kelayakan['layak'] = fuzz.trapmf(kelayakan.universe,[0.45,0.7,1,1])

kelembapan.view()
ketebalan.view()
umur.view()
kelayakan.view()

#Aturan
rule1 = ctrl.Rule(kelembapan['basah'] & ketebalan['tipis'] & umur['muda'], kelayakan['tidak_layak'])
rule2 = ctrl.Rule(kelembapan['basah'] & ketebalan['tipis'] & umur['menengah'], kelayakan['tidak_layak'])
rule3 = ctrl.Rule(kelembapan['basah'] & ketebalan['tipis'] & umur['tua'], kelayakan['tidak_layak'])
rule4 = ctrl.Rule(kelembapan['basah'] & ketebalan['sedang'] & umur['muda'], kelayakan['tidak_layak'])
rule5 = ctrl.Rule(kelembapan['basah'] & ketebalan['sedang'] & umur['menengah'], kelayakan['tidak_layak'])
rule6 = ctrl.Rule(kelembapan['basah'] & ketebalan['sedang'] & umur['tua'], kelayakan['tidak_layak'])
rule7 = ctrl.Rule(kelembapan['basah'] & ketebalan['tebal'] & umur['muda'], kelayakan['tidak_layak'])
rule8 = ctrl.Rule(kelembapan['basah'] & ketebalan['tebal'] & umur['menengah'], kelayakan['tidak_layak'])
rule9 = ctrl.Rule(kelembapan['basah'] & ketebalan['tebal'] & umur['tua'], kelayakan['tidak_layak'])
  
rule10 = ctrl.Rule(kelembapan['lembab'] & ketebalan['tipis'] & umur['muda'], kelayakan['tidak_layak'])
rule11 = ctrl.Rule(kelembapan['lembab'] & ketebalan['tipis'] & umur['menengah'], kelayakan['tidak_layak'])
rule12 = ctrl.Rule(kelembapan['lembab'] & ketebalan['tipis'] & umur['tua'], kelayakan['tidak_layak'])
rule13 = ctrl.Rule(kelembapan['lembab'] & ketebalan['sedang'] & umur['muda'], kelayakan['tidak_layak'])
rule14 = ctrl.Rule(kelembapan['lembab'] & ketebalan['sedang'] & umur['menengah'], kelayakan['tidak_layak'])
rule15 = ctrl.Rule(kelembapan['lembab'] & ketebalan['sedang'] & umur['tua'], kelayakan['tidak_layak'])
rule16 = ctrl.Rule(kelembapan['lembab'] & ketebalan['tebal'] & umur['muda'], kelayakan['tidak_layak'])
rule17 = ctrl.Rule(kelembapan['lembab'] & ketebalan['tebal'] & umur['menengah'], kelayakan['tidak_layak'])
rule18 = ctrl.Rule(kelembapan['lembab'] & ketebalan['tebal'] & umur['tua'], kelayakan['tidak_layak'])

rule19 = ctrl.Rule(kelembapan['kering'] & ketebalan['tipis'] & umur['muda'], kelayakan['tidak_layak'])
rule20 = ctrl.Rule(kelembapan['kering'] & ketebalan['tipis'] & umur['menengah'], kelayakan['tidak_layak'])
rule21 = ctrl.Rule(kelembapan['kering'] & ketebalan['tipis'] & umur['tua'], kelayakan['layak'])
rule22 = ctrl.Rule(kelembapan['kering'] & ketebalan['sedang'] & umur['muda'], kelayakan['tidak_layak'])
rule23 = ctrl.Rule(kelembapan['kering'] & ketebalan['sedang'] & umur['menengah'], kelayakan['layak'])
rule24 = ctrl.Rule(kelembapan['kering'] & ketebalan['sedang'] & umur['tua'], kelayakan['layak'])
rule25 = ctrl.Rule(kelembapan['kering'] & ketebalan['tebal'] & umur['muda'], kelayakan['tidak_layak'])
rule26 = ctrl.Rule(kelembapan['kering'] & ketebalan['tebal'] & umur['menengah'], kelayakan['layak'])
rule27 = ctrl.Rule(kelembapan['kering'] & ketebalan['tebal'] & umur['tua'], kelayakan['layak'])

kelayakan_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, 
     rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, 
     rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27])

hasil_kelayakan = ctrl.ControlSystemSimulation(kelayakan_ctrl)

hasil_kelayakan.input['kelembapan'] = 72
hasil_kelayakan.input['ketebalan'] = 81
hasil_kelayakan.input['umur'] = 80

hasil_kelayakan.compute()

print(hasil_kelayakan.output['kelayakan'])

kelayakan.view(sim=hasil_kelayakan)

plt.show()