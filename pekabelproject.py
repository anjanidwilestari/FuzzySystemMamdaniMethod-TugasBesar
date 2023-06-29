import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import cv2

# Generate universe variables
#   * kelembapan, ketebalan, umur memiliki range [0-100]
#   * Kelayakan has a range of [0, 1] in units of percentage points
def layak(value):
    x_kelembapan = np.arange( 0, 100.01, 0.5), 'kelembapan'
    x_ketebalan = np.arange( 0, 100.01, 0.5), 'ketebalan'
    x_umur  = np.arange(0, 100.01, 0.5), 'umur'
    x_kelayakan=np.arange(0, 1.01, 0.01), 'kelayakan'

    # Generate fuzzy membership functions
    kelembapan_lo = fuzz.trimf(x_kelembapan, [0,40,45])
    kelembapan_md = fuzz.trimf(x_kelembapan, [40,55,70])
    kelembapan_hi = fuzz.trimf(x_kelembapan, [65,75,100])
    ketebalan_lo = fuzz.trimf(x_ketebalan, [0,40,45])
    ketebalan_md = fuzz.trimf(x_ketebalan, [40,55,70])
    ketebalan_hi = fuzz.trimf(x_ketebalan, [65,75,100])
    umur_lo = fuzz.trimf(x_umur, [0,40,45])
    umur_md = fuzz.trimf(x_umur, [40,55,70])
    umur_hi = fuzz.trimf(x_umur, [65,75,100])
    kelayakan_lo= fuzz.trimf(x_kelayakan, [0,0.3,0.55])
    kelayakan_hi= fuzz.trimf(x_kelayakan, [0.45,0.7,1])



    kelembapan_level_lo = fuzz.interp_membership(x_kelembapan, kelembapan_lo, kelembapan)
    kelembapan_level_md = fuzz.interp_membership(x_kelembapan, kelembapan_md, kelembapan)
    kelembapan_level_hi = fuzz.interp_membership(x_kelembapan, kelembapan_hi, kelembapan)

    ketebalan_level_lo = fuzz.interp_membership(x_ketebalan, ketebalan_lo, ketebalan)
    ketebalan_level_md = fuzz.interp_membership(x_ketebalan, ketebalan_md, ketebalan)
    ketebalan_level_hi = fuzz.interp_membership(x_ketebalan, ketebalan_hi, ketebalan)
    
    umur_level_lo = fuzz.interp_membership(x_umur, umur_lo, umur)
    umur_level_md = fuzz.interp_membership(x_umur, umur_md, umur)
    umur_level_hi = fuzz.interp_membership(x_umur, umur_hi, umur)
    
    kelayakan_level_lo = fuzz.interp_membership(x_kelayakan, kelayakan_lo, kelayakan)
    kelayakan_level_hi = fuzz.interp_membership(x_kelayakan, kelayakan_hi, kelayakan)

    # Now we take our rules and apply them. Rule 1 concerns bad food OR service.
    rule1 = np.fmin(kelembapan_level_lo & ketebalan_level_lo & umur_level_lo, kelayakan_level_lo)
    rule2 = ctrl.Rule(kelembapan_level_lo & ketebalan_level_lo & umur_level_md, kelayakan_level_lo)
    rule3 = ctrl.Rule(kelembapan_level_lo & ketebalan_level_lo & umur_level_hi, kelayakan_level_lo)
    rule4 = ctrl.Rule(kelembapan_level_lo & ketebalan_level_md & umur_level_lo, kelayakan_level_lo)
    rule5 = ctrl.Rule(kelembapan_level_lo & ketebalan_level_md & umur_level_md, kelayakan_level_lo)
    rule6 = ctrl.Rule(kelembapan_level_lo & ketebalan_level_md & umur_level_hi, kelayakan_level_lo)
    rule7 = ctrl.Rule(kelembapan_level_lo & ketebalan_level_hi & umur_level_lo, kelayakan_level_lo)
    rule8 = ctrl.Rule(kelembapan_level_lo & ketebalan_level_hi & umur_level_md, kelayakan_level_lo)
    rule9 = ctrl.Rule(kelembapan_level_lo & ketebalan_level_hi & umur_level_hi, kelayakan_level_lo)
    
    rule10 = Rule(kelembapan_level_md & ketebalan_level_lo & umur_level_lo, kelayakan_level_lo)
    rule11 = ctrl.Rule(kelembapan_level_md & ketebalan_level_lo & umur_level_md, kelayakan_level_lo)
    rule12 = ctrl.Rule(kelembapan_level_md & ketebalan_level_lo & umur_level_hi, kelayakan_level_lo)
    rule13 = ctrl.Rule(kelembapan_level_md & ketebalan_level_md & umur_level_lo, kelayakan_level_lo)
    rule14 = ctrl.Rule(kelembapan_level_md & ketebalan_level_md & umur_level_md, kelayakan_level_lo)
    rule15 = ctrl.Rule(kelembapan_level_md & ketebalan_level_md & umur_level_hi, kelayakan_level_lo)
    rule16 = ctrl.Rule(kelembapan_level_md & ketebalan_level_hi & umur_level_lo, kelayakan_level_lo)
    rule17 = ctrl.Rule(kelembapan_level_md & ketebalan_level_hi & umur_level_md, kelayakan_level_lo)
    rule18 = ctrl.Rule(kelembapan_level_md & ketebalan_level_hi & umur_level_hi, kelayakan_level_lo)

    rule19 = ctrl.Rule(kelembapan_level_hi & ketebalan_level_lo & umur_level_lo, kelayakan_level_lo)
    rule20 = ctrl.Rule(kelembapan_level_hi & ketebalan_level_lo & umur_level_md, kelayakan_level_lo)
    rule21 = ctrl.Rule(kelembapan_level_hi & ketebalan_level_lo & umur_level_hi, kelayakan_level_hi)
    rule22 = ctrl.Rule(kelembapan_level_hi & ketebalan_level_md & umur_level_lo, kelayakan_level_lo)
    rule23 = ctrl.Rule(kelembapan_level_hi & ketebalan_level_md & umur_level_md, kelayakan_level_lo)
    rule24 = ctrl.Rule(kelembapan_level_hi & ketebalan_level_md & umur_level_hi, kelayakan_level_hi)
    rule25 = ctrl.Rule(kelembapan_level_hi & ketebalan_level_hi & umur_level_lo, kelayakan_level_lo)
    rule26 = ctrl.Rule(kelembapan_level_hi & ketebalan_level_hi & umur_level_md, kelayakan_level_hi)
    rule27 = ctrl.Rule(kelembapan_level_hi & ketebalan_level_hi & umur_level_hi, kelayakan_level_hi)

    # Now we apply this by clipping the top off the corresponding output
    # membership function with `np.fmin`
    layak_activation_lo = np.fmin(rule1,rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
                                  rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
                                  rule22, rule25, kelayakan_lo)  # removed entirely to 0

    # For rule 2 we connect acceptable service to medium tipping
    layak_activation_hi = np.fmin(rule21, rule23, rule24, rule26, rule27, kelayakan_hi)

    
    layak0 = np.zeros_like(x_kelayakan)
    # Aggregate all three output membership functions together
    aggregated = np.fmin(layak_activation_lo,layak_activation_hi)

    # Calculate defuzzified result
    kelayakan = fuzz.defuzz(x_kelayakan, aggregated, 'centroid')
    layak_activation = fuzz.interp_membership(x_kelayakan, aggregated, kelayakan)  # for plot
    # Visualize this
    # Visualize these universes and membership functions
    fig, (ax0, ax1, ax2,ax3, ax4) = plt.subplots(nrows=4, figsize=(8, 9))

    ax0.plot(x_kelembapan, kelembapan_lo, 'b', linewidth=1.5, label='Basah')
    ax0.plot(x_kelembapan, kelembapan_md, 'g', linewidth=1.5, label='Lembab')
    ax0.plot(x_kelembapan, kelembapan_hi, 'r', linewidth=1.5, label='Kering')
    ax0.set_title('Kelembapan')
    ax0.legend()

    ax1.plot(x_ketebalan, ketebalan_lo, 'b', linewidth=1.5, label='Poor')
    ax1.plot(x_ketebalan, ketebalan_md, 'g', linewidth=1.5, label='Acceptable')
    ax1.plot(x_ketebalan, ketebalan_hi, 'r', linewidth=1.5, label='Amazing')
    ax1.set_title('Ketebalan')
    ax1.legend()

    ax2.plot(x_umur, umur_lo, 'b', linewidth=1.5, label='Low')
    ax2.plot(x_umur, umur_md, 'g', linewidth=1.5, label='Medium')
    ax2.plot(x_umur, umur_hi, 'r', linewidth=1.5, label='High')
    ax2.set_title('Umur')
    ax2.legend()

    ax3.plot(x_kelayakan, kelayakan_lo, 'b', linewidth=1.5, label='Low')
    ax3.plot(x_kelayakan, kelayakan_hi, 'g', linewidth=1.5, label='Medium')
    ax3.set_title('Kelayakan')
    ax3.legend()
    
    
    ax4.plot(x_kelayakan, kelayakan_lo, 'b', linewidth=0.5, linestyle='--', )
    ax4.plot(x_kelayakan, kelayakan_hi, 'r', linewidth=0.5, linestyle='--')
    ax4.fill_between(x_kelayakan, layak0, aggregated, facecolor='Orange', alpha=0.7)
    ax4.plot([kelayakan, kelayakan], [0, layak_activation], 'k', linewidth=1.5, alpha=0.9)
    ax4.set_title('Aggregated membership and result (line)')
    ax4.legend()
    
    # Turn off top/right axes
    for ax in (ax0, ax1, ax2, ax3):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
    
    plt.show()
    
    return layak
