import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
rng=np.random.default_rng(7)
n=40*104
v=rng.lognormal(np.log(1150),0.28,n)
idx=rng.choice(n,90,replace=False); v[idx]*=rng.uniform(1.8,2.4,90)   # semanas festivas
z=rng.choice(n,120,replace=False); v[z]=0                              # quiebres de stock
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.edgecolor":"#52514e","axes.labelcolor":"#0b0b0b","xtick.color":"#52514e","ytick.color":"#52514e"})
fig,ax=plt.subplots(1,2,figsize=(10,3.9),gridspec_kw={"width_ratios":[1.35,1]})
a=ax[0]
a.hist(v,bins=60,color="#2a78d6",edgecolor="#fcfcfb",linewidth=0.8)
q1,q3=np.percentile(v[v>0],[25,75]); lim=q3+1.5*(q3-q1)
a.axvline(lim,color="#52514e",ls="--",lw=1.2)
a.text(lim+60,470,"Q3 + 1,5·IQR\n≈ "+f"{lim:,.0f}".replace(",",".")+" u.",color="#0b0b0b",fontsize=9)
a.text(-60,135,"Venta = 0\n(quiebres\nde stock)",fontsize=9,color="#0b0b0b",va="bottom")
a.set_xlim(-100,4000); a.set_ylim(0,530); a.set_xlabel("Unidades vendidas por tienda y semana"); a.set_ylabel("Frecuencia (semanas)")
a.set_title("(a) Distribución de las ventas semanales",loc="left",fontsize=10.5)
b=ax[1]
vars_=["Precio","Promoción activa","Unidades vendidas","Temperatura","Tráfico en tienda"]
miss=[0.4,2.1,3.0,11.5,18.7]
b.barh(vars_,miss,color="#2a78d6",height=0.6)
for i,m in enumerate(miss): b.text(m+0.4,i,f"{m:.1f} %".replace(".",","),va="center",fontsize=9,color="#0b0b0b")
b.set_xlim(0,23); b.set_xlabel("Registros faltantes (%)")
b.set_title("(b) Datos faltantes por variable",loc="left",fontsize=10.5)
for x in ax:
    x.spines[["top","right"]].set_visible(False); x.grid(axis="x" if x is b else "y",color="#e6e5e1",lw=0.8); x.set_axisbelow(True)
fig.tight_layout(); fig.savefig("figura2.png",dpi=200,facecolor="white")
print(lim)
