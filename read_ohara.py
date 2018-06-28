# -*- coding: utf-8 -*-
"""
Parse the ohara downloaded catalog (csv format), and create a new cleaned up
data frame with glass type and sellmeier coeffs for all glass types.  Output 
in csv and pickled formats

Ohara download version 20171130

Hover code found here: 
https://stackoverflow.com/questions/7908636/
possible-to-make-labels-appear-when-hovering-over-a-point-in-matplotlib

"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#ohara has 140 glasses
df = pd.read_csv('OHARA_20171130_6.csv', header=[0, 1])

#glass names are in column 1
glass = df[df.columns[1]].values
for i in range(len(glass)):
    glass[i] = glass[i].replace(" ","")  #make consitent with no spaces
         
          
#Index at sodium d-line (Nd) is in column 16
nd = df[df.columns[16]].values

columns = ['Nd', 'A1', 'A2', 'A3', 'B1', 'B2', 'B3']

# Create a new data frame with just the glass type, Nd, and sellmeiers.
# Todo: maybe add other properties. 
# best format - pickled df, json, hdf5, yml?

df_sell = pd.DataFrame(index=glass,columns=columns)

df_sell = df_sell.fillna(0)
abbe = df[df.columns[26]].values
A1 = df[df.columns[60]].values
A2 = df[df.columns[61]].values
A3 = df[df.columns[62]].values
B1 = df[df.columns[63]].values
B2 = df[df.columns[64]].values
B3 = df[df.columns[65]].values
       
   
df_sell['Glass'] = glass
df_sell['Abbe'] = abbe      
df_sell['Nd'] = nd
df_sell['A1'] = A1
df_sell['A2'] = A2
df_sell['A3'] = A3
df_sell['B1'] = B1
df_sell['B2'] = B2
df_sell['B3'] = B3       
        

#plot 
fig,ax = plt.subplots()
plt.title('Index vs. Abbe Number for Ohara Glass')
plt.ylabel('Refractive Index (Nd)')
plt.xlabel('Abbe Number')
plt.gca().invert_xaxis()

sc = plt.scatter(abbe, nd)
                 
annot = ax.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):

    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}, {}".format(" ".join([glass[n] for n in ind["ind"]]), 
                           " ".join(str([nd[n] for n in ind["ind"]])))
    annot.set_text(text)
    #annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)
     

#later add schott glasses too 
#schottdf = pd.read_csv('schott-optical-glass-06032017.csv')  #utf-8 error



# Reference:  index, glass types

#0 S-FPL51
#1 S-FPL53
#2 S-FPL55
#3 S-FPM2
#4 S-FPM3
#5 S-FSL5
#6 S-BSL7
#7 S-BSM2
#8 S-BSM4
#9 S-BSM10
#10 S-BSM14
#11 S-BSM15
#12 S-BSM16
#13 S-BSM18
#14 S-BSM22
#15 S-BSM25
#16 S-BSM28
#17 S-BSM71
#18 S-BSM81
#19 S-NSL3
#20 S-NSL5
#21 S-NSL36
#22 S-BAL2
#23 S-BAL3
#24 S-BAL12
#25 S-BAL14
#26 S-BAL35
#27 S-BAL41
#28 S-BAL42
#29 S-BAM4
#30 S-BAM12
#31 S-BAH10
#32 S-BAH11
#33 S-BAH27
#34 S-BAH28
#35 S-BAH32
#36 S-PHM52
#37 S-PHM53
#38 S-TIL1
#39 S-TIL2
#40 S-TIL6
#41 S-TIL25
#42 S-TIL26
#43 S-TIL27
#44 S-TIM1
#45 S-TIM2
#46 S-TIM5
#47 S-TIM8
#48 S-TIM22
#49 S-TIM25
#50 S-TIM27
#51 S-TIM28
#52 S-TIM35
#53 S-TIM39
#54 S-TIH1
#55 S-TIH3
#56 S-TIH4
#57 S-TIH6
#58 S-TIH10
#59 S-TIH11
#60 S-TIH13
#61 S-TIH14
#62 S-TIH18
#63 S-TIH23
#64 S-TIH53
#65 S-TIH53W
#66 S-TIH57
#67 S-LAL7
#68 S-LAL8
#69 S-LAL9
#70 S-LAL10
#71 S-LAL12
#72 S-LAL13
#73 S-LAL14
#74 S-LAL18
#75 S-LAL19
#76 S-LAL20
#77 S-LAL54
#78 S-LAL54Q
#79 S-LAL58
#80 S-LAL59
#81 S-LAL61
#82 S-LAM2
#83 S-LAM3
#84 S-LAM7
#85 S-LAM52
#86 S-LAM54
#87 S-LAM55
#88 S-LAM58
#89 S-LAM59
#90 S-LAM60
#91 S-LAM61
#92 S-LAM66
#93 S-LAM73
#94 S-LAH51
#95 S-LAH52
#96 S-LAH52Q
#97 S-LAH53
#98 S-LAH53V
#99 S-LAH55V
#100 S-LAH55VS
#101 S-LAH58
#102 S-LAH59
#103 S-LAH60
#104 S-LAH60V
#105 S-LAH63
#106 S-LAH63Q
#107 S-LAH64
#108 S-LAH65V
#109 S-LAH65VS
#110 S-LAH66
#111 S-LAH71
#112 S-LAH79
#113 S-LAH88
#114 S-LAH89
#115 S-LAH92
#116 S-LAH93
#117 S-LAH95
#118 S-LAH96
#119 S-LAH97
#120 S-YGH51
#121 S-FTM16
#122 S-NBM51
#123 S-NBH5
#124 S-NBH8
#125 S-NBH51
#126 S-NBH52
#127 S-NBH52V
#128 S-NBH53
#129 S-NBH53V
#130 S-NBH55
#131 S-NBH56
#132 S-NBH57
#133 S-NPH1
#134 S-NPH1W
#135 S-NPH2
#136 S-NPH3
#137 S-NPH4
#138 S-NPH5
#139 S-NPH53             
                       
                                         
# Parsed raw columns from csv ------------------------------------------                       
                       
#0 ('Unnamed: 0_level_0', 'Unnamed: 0_level_1')
#1 ('Unnamed: 1_level_0', 'Glass ')
#2 ('Unnamed: 2_level_0', 'Code(d)')
#3 ('Unnamed: 3_level_0', 'Code(e)')
#4 ('REFRACTIVE INDICES', 'n2325')
#5 ('Unnamed: 5_level_0', 'n1970')
#6 ('Unnamed: 6_level_0', 'n1530')
#7 ('Unnamed: 7_level_0', 'n1129')
#8 ('REFRACTIVE INDICES', 'nt')
#9 ('Unnamed: 9_level_0', 'ns')
#10 ('Unnamed: 10_level_0', "nA'")
#11 ('Unnamed: 11_level_0', 'nr')
#12 ('REFRACTIVE INDICES', 'nC')
#13 ('Unnamed: 13_level_0', "nC'")
#14 ('Unnamed: 14_level_0', 'nHe-Ne')
#15 ('Unnamed: 15_level_0', 'nD')
#16 ('REFRACTIVE INDICES', 'nd')
#17 ('Unnamed: 17_level_0', 'ne')
#18 ('Unnamed: 18_level_0', 'nF')
#19 ('Unnamed: 19_level_0', "nF'")
#20 ('REFRACTIVE INDICES', 'nHe-Cd')
#21 ('Unnamed: 21_level_0', 'ng')
#22 ('Unnamed: 22_level_0', 'nh')
#23 ('Unnamed: 23_level_0', 'ni')
#24 ('ABBE', '?d')
#25 ('Unnamed: 25_level_0', '?e')
#26 ('ABBE', '?d').1
#27 ('Unnamed: 27_level_0', '?e')
#28 ('DISPERSIONS', 'nF-nC')
#29 ('Unnamed: 29_level_0', 'nF-nC')
#30 ('Unnamed: 30_level_0', "nF'-nC'")
#31 ('PARTIAL DISPERSIONS', 'nC-nt')
#32 ('Unnamed: 32_level_0', "nC-nA'")
#33 ('Unnamed: 33_level_0', 'nd-nC')
#34 ('Unnamed: 34_level_0', 'ne-nC')
#35 ('Unnamed: 35_level_0', 'ng-nd')
#36 ('Unnamed: 36_level_0', 'ng-nF')
#37 ('PARTIAL DISPERSIONS', 'nh-ng')
#38 ('Unnamed: 38_level_0', 'ni-ng')
#39 ('Unnamed: 39_level_0', "nC'-nt")
#40 ('Unnamed: 40_level_0', "ne-nC'")
#41 ('Unnamed: 41_level_0', "nF'-ne")
#42 ('Unnamed: 42_level_0', "ni-nF'")
#43 ('RELATIVE PARTIAL DISPERSIONS', '?C,t')
#44 ('Unnamed: 44_level_0', "?C,A'")
#45 ('Unnamed: 45_level_0', '?d,C')
#46 ('Unnamed: 46_level_0', '?e,C')
#47 ('Unnamed: 47_level_0', '?g,d')
#48 ('Unnamed: 48_level_0', '?g,F')
#49 ('RELATIVE PARTIAL DISPERSIONS', '?h,g')
#50 ('Unnamed: 50_level_0', '?i,g')
#51 ('Unnamed: 51_level_0', "?'C',t")
#52 ('Unnamed: 52_level_0', "?'e,C'")
#53 ('Unnamed: 53_level_0', "?'F',e")
#54 ('Unnamed: 54_level_0', "?'i,F'")
#55 ('Deviation of Relative Partial Dispesions', '??C,t')
#56 ('Unnamed: 56_level_0', "??C,A'")
#57 ('Unnamed: 57_level_0', '??g,d')
#58 ('Unnamed: 58_level_0', '??g,F')
#59 ('Unnamed: 59_level_0', '??i,g')
#60 ('CONSTANTS  OF DISPERSION FORMULA (Sellmeier)', 'A1')
#61 ('Unnamed: 61_level_0', 'A2')
#62 ('Unnamed: 62_level_0', 'A3')
#63 ('Unnamed: 63_level_0', 'B1')
#64 ('Unnamed: 64_level_0', 'B2')
#65 ('Unnamed: 65_level_0', 'B3')
#66 ('CONSTANTS  OF DISPERSION FORMULA (Cauchy)', 'A0')
#67 ('Unnamed: 67_level_0', 'A1')
#68 ('Unnamed: 68_level_0', 'A2')
#69 ('Unnamed: 69_level_0', 'A3')
#70 ('Unnamed: 70_level_0', 'A4')
#71 ('Unnamed: 71_level_0', 'A5')
#72 ('COLORING', '?80')
#73 ('Unnamed: 73_level_0', '(?70)')
#74 ('Unnamed: 74_level_0', '?5')
#75 ('INTERNAL  TRANSMISSION COLORING', '?0.80')
#76 ('Unnamed: 76_level_0', '?0.05')
#77 ('CCI', 'B')
#78 ('Unnamed: 78_level_0', 'G')
#79 ('Unnamed: 79_level_0', 'R')
#80 ('INTERNAL  TRANSMISSION  (?/10mm Thick) ', '280')
#81 ('Unnamed: 81_level_0', '290')
#82 ('Unnamed: 82_level_0', '300')
#83 ('Unnamed: 83_level_0', '310')
#84 ('Unnamed: 84_level_0', '320')
#85 ('Unnamed: 85_level_0', '330')
#86 ('Unnamed: 86_level_0', '340')
#87 ('Unnamed: 87_level_0', '350')
#88 ('Unnamed: 88_level_0', '360')
#89 ('INTERNAL  TRANSMISSION  (?/10mm Thick) ', '370')
#90 ('Unnamed: 90_level_0', '380')
#91 ('Unnamed: 91_level_0', '390')
#92 ('Unnamed: 92_level_0', '400')
#93 ('Unnamed: 93_level_0', '420')
#94 ('Unnamed: 94_level_0', '440')
#95 ('Unnamed: 95_level_0', '460')
#96 ('Unnamed: 96_level_0', '480')
#97 ('INTERNAL  TRANSMISSION  (?/10mm Thick) ', '500')
#98 ('Unnamed: 98_level_0', '550')
#99 ('Unnamed: 99_level_0', '600')
#100 ('Unnamed: 100_level_0', '650')
#101 ('Unnamed: 101_level_0', '700')
#102 ('Unnamed: 102_level_0', '800')
#103 ('Unnamed: 103_level_0', '900')
#104 ('Unnamed: 104_level_0', '1000')
#105 ('INTERNAL  TRANSMISSION  (?/10mm Thick) ', '1200')
#106 ('Unnamed: 106_level_0', '1400')
#107 ('Unnamed: 107_level_0', '1600')
#108 ('Unnamed: 108_level_0', '1800')
#109 ('Unnamed: 109_level_0', '2000')
#110 ('Unnamed: 110_level_0', '2200')
#111 ('Unnamed: 111_level_0', '2400')
#112 ('dn/dT  relative   (10-6 / ?)', 't(-40~-20)')
#113 ('Unnamed: 113_level_0', 't(-20~0)')
#114 ('Unnamed: 114_level_0', 't(0~20)')
#115 ('Unnamed: 115_level_0', 't(20~40)')
#116 ('Unnamed: 116_level_0', 't(40~60)')
#117 ('Unnamed: 117_level_0', 't(60~80)')
#118 ('dn/dT  relative   (10-6 / ?)', "C'(-40~-20)")
#119 ('Unnamed: 119_level_0', "C'(-20~0)")
#120 ('Unnamed: 120_level_0', "C'(0~20)")
#121 ('Unnamed: 121_level_0', "C'(20~40)")
#122 ('Unnamed: 122_level_0', "C'(40~60)")
#123 ('Unnamed: 123_level_0', "C'(60~80)")
#124 ('dn/dT  relative   (10-6 / ?)', 'He-Ne(-40~-20)')
#125 ('Unnamed: 125_level_0', 'He-Ne(20~0)')
#126 ('Unnamed: 126_level_0', 'He-Ne(0~20)')
#127 ('Unnamed: 127_level_0', 'He-Ne(20~40)')
#128 ('Unnamed: 128_level_0', 'He-Ne(40~60)')
#129 ('Unnamed: 129_level_0', 'He-Ne(60~80)')
#130 ('dn/dT  relative   (10-6 / ?)', 'D(-40~-20)')
#131 ('Unnamed: 131_level_0', 'D(-20~0)')
#132 ('Unnamed: 132_level_0', 'D(0~20)')
#133 ('Unnamed: 133_level_0', 'D(20~40)')
#134 ('Unnamed: 134_level_0', 'D(40~60)')
#135 ('Unnamed: 135_level_0', 'D(60~80)')
#136 ('dn/dT  relative   (10-6 / ?)', 'e(-40~-20)')
#137 ('Unnamed: 137_level_0', 'e(-20~0)')
#138 ('Unnamed: 138_level_0', 'e(0~20)')
#139 ('Unnamed: 139_level_0', 'e(20~40)')
#140 ('Unnamed: 140_level_0', 'e(40~60)')
#141 ('Unnamed: 141_level_0', 'e(60~80)')
#142 ('dn/dT  relative   (10-6 / ?)', "F'(-40~-20)")
#143 ('Unnamed: 143_level_0', "F'(-20~0)")
#144 ('Unnamed: 144_level_0', "F'(0~20)")
#145 ('Unnamed: 145_level_0', "F'(20~40)")
#146 ('Unnamed: 146_level_0', "F'(40~60)")
#147 ('Unnamed: 147_level_0', "F'(60~80)")
#148 ('dn/dT  relative   (10-6 / ?)', 'g(-40~-20)')
#149 ('Unnamed: 149_level_0', 'g(-20~0)')
#150 ('Unnamed: 150_level_0', 'g(0~20)')
#151 ('Unnamed: 151_level_0', 'g(20~40)')
#152 ('Unnamed: 152_level_0', 'g(40~60)')
#153 ('Unnamed: 153_level_0', 'g(60~80)')
#154 ('Constants of dn/dT', ' D0')
#155 ('Unnamed: 155_level_0', ' D1')
#156 ('Unnamed: 156_level_0', ' D2')
#157 ('Unnamed: 157_level_0', ' E0')
#158 ('Unnamed: 158_level_0', ' E1')
#159 ('Unnamed: 159_level_0', '?TK')
#160 ('Thermal Properties', 'StP(?)')
#161 ('Unnamed: 161_level_0', 'AP(?)')
#162 ('Unnamed: 162_level_0', 'Tg(?)')
#163 ('Unnamed: 163_level_0', 'At(?)')
#164 ('Unnamed: 164_level_0', 'SP(?)')
#165 ('CTE?(10-7/?)', '(-30~+70)')
#166 ('Unnamed: 166_level_0', '(100~300)')
#167 ('Conductivity', 'k(W/m?K)')
#168 ('Mechanical  Properties', "Young's (E) ")
#169 ('Unnamed: 169_level_0', 'Rigidity (G)')
#170 ('Unnamed: 170_level_0', "Poisson's(?)")
#171 ('Unnamed: 171_level_0', 'Knoop (Hk)')
#172 ('Unnamed: 172_level_0', 'Group')
#173 ('Unnamed: 173_level_0', 'Abrasion(Aa)')
#174 ('Unnamed: 174_level_0', '?')
#175 ('Chemical  Properties', 'RW(P)')
#176 ('Unnamed: 176_level_0', 'RA(P)')
#177 ('Unnamed: 177_level_0', 'W(S)max')
#178 ('Unnamed: 178_level_0', 'W(S)min')
#179 ('Unnamed: 179_level_0', 'SR')
#180 ('Unnamed: 180_level_0', 'PR')
#181 ('Bubble Grp', 'B')
#182 ('Spec. Gravity', 'd')