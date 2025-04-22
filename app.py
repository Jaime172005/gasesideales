import streamlit as st
st.image("images 1.jpg")
R = 0.0821  # Constante de los gases ideales en L·atm/mol·K

st.title("Calculadora de la Ecuación de los Gases Ideales")
st.markdown("**Ecuación:** PV = nRT")

opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

if opcion == "Presión (P)":
    volumen = st.number_input("Volumen (L)", min_value=0.01)
    temperatura = st.number_input("Temperatura (K)", min_value=0.01)
    moles = st.number_input("Número de moles (mol)", min_value=0.01)
    if st.button("Calcular Presión"):
        presion = (moles * R * temperatura) / volumen
        st.success(f"Presión = {presion:.3f} atm")

elif opcion == "Volumen (V)":
    presion = st.number_input("Presión (atm)", min_value=0.01)
    temperatura = st.number_input("Temperatura (K)", min_value=0.01)
    moles = st.number_input("Número de moles (mol)", min_value=0.01)
    if st.button("Calcular Volumen"):
        volumen = (moles * R * temperatura) / presion
        st.success(f"Volumen = {volumen:.3f} L")

elif opcion == "Temperatura (T)":
    presion = st.number_input("Presión (atm)", min_value=0.01)
    volumen = st.number_input("Volumen (L)", min_value=0.01)
    moles = st.number_input("Número de moles (mol)", min_value=0.01)
    if st.button("Calcular Temperatura"):
        temperatura = (presion * volumen) / (moles * R)
        st.success(f"Temperatura = {temperatura:.3f} K")

elif opcion == "Número de moles (n)":
    presion = st.number_input("Presión (atm)", min_value=0.01)
    volumen = st.number_input("Volumen (L)", min_value=0.01)
    temperatura = st.number_input("Temperatura (K)", min_value=0.01)
    if st.button("Calcular número de moles"):
        moles = (presion * volumen) / (R * temperatura)
        st.success(f"Número de moles = {moles:.3f} mol")
