import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('posities_A5.csv')

# Eerst snelheid bereken voor alle punten door dx en dt te maken voor allebei de lijsten.
dt = [0]
dpos1 = [0]
dpos2 = [0]
npdt = np.diff(df['tijd'])
nppos1 = np.diff(df['positie1'])
nppos2 = np.diff(df['positie2'])
ldt = npdt.tolist()
lpos1 = nppos1.tolist()
lpos2 = nppos2.tolist()
dt.extend(ldt)
dpos1.extend(lpos1)
dpos2.extend(lpos2)
df['dt'] = dt
df['dpos1'] = dpos1
df['dpos2'] = dpos2

df['v1'] = df['dpos1'] / df['dt']
df['v2'] = df['dpos2'] / df['dt']

# Dan a berekenen door dv te maken voor allebei de lijsten
dv1 = [0]
dv2 = [0]
npv1 = np.diff(df['v1'])
npv2 = np.diff(df['v2'])
lv1 = npv1.tolist()
lv2 = npv2.tolist()
dv1.extend(lv1)
dv2.extend(lv2)
df['dv1'] = dv1
df['dv2'] = dv2
    # omdat de eerste v waardes NaN zijn worden ze gezien als 0
    #  dus is dv in rij 1 gelijk aan v
v1 = df.at[1, 'v1']
v2 = df.at[1, 'v2']
df.at[1, 'dv1'] = v1
df.at[1, 'dv2'] = v2

df['a1'] = df['dv1'] / df['dt']
df['a2'] = df['dv2'] / df['dt']

# Nieuw dataframe aanmaken om op te slaan.
# Zo hoeven de reken colommen niet mee in het bestand.
# Aanroeprij voor python wordt ook opgeslagen.
df2 = pd.DataFrame()
df2['tijd'] = df['tijd']
df2['pos_1'] = df['positie1']
df2['v_1'] = df['v1']
df2['a_1'] = df['a1']
df2['pos_2'] = df['positie2']
df2['v_2'] = df['v2']
df2['a_2'] = df['a2']

df2.to_csv('p_v_a_team_A5.csv')

# Plot de snelheid en versnelling van beide posities.
plt.figure(1)

plt.subplot(121)
plt.plot(df.tijd, df.v1)

plt.title("v/t diagram")
plt.xlabel("tijd(s)")
plt.ylabel("snelheid(m/s)")

plt.subplot(122)
plt.plot(df.tijd, df.a1)

plt.title("a/t diagram")
plt.xlabel("tijd(s)")
plt.ylabel("versnelling(m/s^2)")

plt.tight_layout()
plt.savefig('pos1.png')

plt.figure(2)

plt.subplot(221)
plt.plot(df.tijd, df.v2)

plt.title("v/t diagram")
plt.xlabel("tijd(s)")
plt.ylabel("snelheid(m/s)")

plt.subplot(222)
plt.plot(df.tijd, df.a2)

plt.title("a/t diagram")
plt.xlabel("tijd(s)")
plt.ylabel("versnelling(m/s^2)")

plt.tight_layout()
plt.title("Grafieken positie 2")
plt.savefig('pos2.png')
