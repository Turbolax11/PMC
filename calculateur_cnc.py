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

# Adjust RPM or Vf and recalculate
st.subheader("Réajustement des paramètres")
adjust_option = st.radio(
    "Quel paramètre souhaitez-vous ajuster ?",
    ("Ajuster la vitesse de rotation (RPM)", "Ajuster la vitesse d'avance (Vf)")
)

if adjust_option == "Ajuster la vitesse de rotation (RPM)":
    new_RPM = st.slider("Nouvelle vitesse de rotation (RPM)", min_value=100.0, max_value=50000.0, value=RPM, step=100.0)
    new_fz = Vf / (Nd * new_RPM)
    new_Vc = (new_RPM * math.pi * D) / 1000  # Convert back to m/min

    with st.container():
        st.subheader("Résultats réajustés (RPM ajusté)")
        st.markdown(f"""
        - **Nouvelle vitesse de rotation (RPM)** : `{new_RPM:.2f}` tr/min  
        - **Avance par dent recalculée (fz)** : `{new_fz:.3f}` mm/dent  
        - **Nouvelle vitesse de coupe (Vc)** : `{new_Vc:.2f}` m/min  
        """)

elif adjust_option == "Ajuster la vitesse d'avance (Vf)":
    new_Vf = st.slider("Nouvelle vitesse d'avance (Vf) en mm/min", min_value=10.0, max_value=10000.0, value=Vf, step=10.0)
    new_fz = new_Vf / (Nd * RPM)
    new_Vc = (RPM * math.pi * D) / 1000  # Convert back to m/min

    with st.container():
        st.subheader("Résultats réajustés (Vf ajusté)")
        st.markdown(f"""
        - **Nouvelle vitesse d'avance (Vf)** : `{new_Vf:.2f}` mm/min  
        - **Avance par dent recalculée (fz)** : `{new_fz:.3f}` mm/dent  
        - **Vitesse de coupe (Vc)** : `{new_Vc:.2f}` m/min  
        """)
