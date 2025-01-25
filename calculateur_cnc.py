import streamlit as st
import math

st.title("Calculateur CNC - RPM et Vitesse d'avance")

# Input parameters with sliders
D = st.slider("Diamètre de l'outil (D) en mm", min_value=1.0, max_value=20.0, value=3.0, step=0.1)
Nd = st.slider("Nombre de dents (Nd)", min_value=1, max_value=6, value=2, step=1)
Vc = st.slider("Vitesse de coupe (Vc) en m/min", min_value=50.0, max_value=500.0, value=200.0, step=10.0)
fz = st.slider(
    "Avance par dent (fz) en mm/dent",
    min_value=0.020,
    max_value=0.200,
    value=0.050,
    step=0.001,
    format="%.3f"  # Force display to 3 decimal places
)

# Calculations for initial results
RPM = (Vc * 1000) / (math.pi * D)  # Convert Vc from m/min to mm/min
Vf = fz * Nd * RPM

with st.container():
    st.subheader("Résultats initiaux")
    st.markdown(f"""
    - **Vitesse de rotation (RPM)** : `{RPM:.2f}` tr/min  
    - **Vitesse d'avance (Vf)** : `{Vf:.2f}` mm/min  
    """)

# Divider for visual separation
st.divider()

# Sliders for adjusting RPM and Vf
st.subheader("Réglage interactif des paramètres")
adjusted_RPM = st.slider(
    "Réglez la vitesse de rotation (RPM)",
    min_value=100.0,
    max_value=30000.0,
    value=float(RPM),
    step=100.0
)
adjusted_Vf = st.slider(
    "Réglez la vitesse d'avance (Vf) en mm/min",
    min_value=10.0,
    max_value=10000.0,
    value=float(Vf),
    step=10.0
)

# Recalculate fz and Vc based on the adjusted parameters
adjusted_fz = adjusted_Vf / (Nd * adjusted_RPM) if adjusted_RPM > 0 else 0
adjusted_Vc = (adjusted_RPM * math.pi * D) / 1000  # Convert back to m/min

with st.container():
    st.subheader("Résultats réajustés")
    st.markdown(f"""
    - **Nouvelle vitesse de rotation (RPM)** : `{adjusted_RPM:.2f}` tr/min  
    - **Nouvelle vitesse d'avance (Vf)** : `{adjusted_Vf:.2f}` mm/min  
    - **Avance par dent recalculée (fz)** : `{adjusted_fz:.3f}` mm/dent  
    - **Nouvelle vitesse de coupe (Vc)** : `{adjusted_Vc:.2f}` m/min  
    """)
