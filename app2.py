import streamlit as st

st.title("Calculadora de Leyes de los Gases")

ley = st.selectbox("Selecciona la ley que deseas usar", ["Ley de Boyle", "Ley de Charles", "Ley de Gay-Lussac"])

st.markdown("### Ingresa los valores conocidos. Deja vacío el que quieres calcular.")

if ley == "Ley de Boyle":
    st.latex("P_1 \\cdot V_1 = P_2 \\cdot V_2")
    
    P1 = st.number_input("Presión inicial (P1) [atm]", value=None, step=0.1, format="%.3f")
    V1 = st.number_input("Volumen inicial (V1) [L]", value=None, step=0.1, format="%.3f")
    P2 = st.number_input("Presión final (P2) [atm]", value=None, step=0.1, format="%.3f")
    V2 = st.number_input("Volumen final (V2) [L]", value=None, step=0.1, format="%.3f")

    if st.button("Calcular"):
        try:
            if P1 is None:
                P1 = (P2 * V2) / V1
                st.success(f"P1 = {P1:.3f} atm")
            elif V1 is None:
                V1 = (P2 * V2) / P1
                st.success(f"V1 = {V1:.3f} L")
            elif P2 is None:
                P2 = (P1 * V1) / V2
                st.success(f"P2 = {P2:.3f} atm")
            elif V2 is None:
                V2 = (P1 * V1) / P2
                st.success(f"V2 = {V2:.3f} L")
            else:
                st.warning("Deja uno de los campos vacío para calcularlo.")
        except:
            st.error("Verifica que los valores ingresados sean válidos y que no dividas entre cero.")

elif ley == "Ley de Charles":
    st.latex("\\frac{V_1}{T_1} = \\frac{V_2}{T_2}")
    
    V1 = st.number_input("Volumen inicial (V1) [L]", value=None, step=0.1, format="%.3f")
    T1 = st.number_input("Temperatura inicial (T1) [K]", value=None, step=0.1, format="%.3f")
    V2 = st.number_input("Volumen final (V2) [L]", value=None, step=0.1, format="%.3f")
    T2 = st.number_input("Temperatura final (T2) [K]", value=None, step=0.1, format="%.3f")

    if st.button("Calcular"):
        try:
            if V1 is None:
                V1 = (V2 * T1) / T2
                st.success(f"V1 = {V1:.3f} L")
            elif T1 is None:
                T1 = (V1 * T2) / V2
                st.success(f"T1 = {T1:.3f} K")
            elif V2 is None:
                V2 = (V1 * T2) / T1
                st.success(f"V2 = {V2:.3f} L")
            elif T2 is None:
                T2 = (V2 * T1) / V1
                st.success(f"T2 = {T2:.3f} K")
            else:
                st.warning("Deja uno de los campos vacío para calcularlo.")
        except:
            st.error("Verifica los valores y asegúrate de no dividir entre cero.")

elif ley == "Ley de Gay-Lussac":
    st.latex("\\frac{P_1}{T_1} = \\frac{P_2}{T_2}")
    
    P1 = st.number_input("Presión inicial (P1) [atm]", value=None, step=0.1, format="%.3f")
    T1 = st.number_input("Temperatura inicial (T1) [K]", value=None, step=0.1, format="%.3f")
    P2 = st.number_input("Presión final (P2) [atm]", value=None, step=0.1, format="%.3f")
    T2 = st.number_input("Temperatura final (T2) [K]", value=None, step=0.1, format="%.3f")

    if st.button("Calcular"):
        try:
            if P1 is None:
                P1 = (P2 * T1) / T2
                st.success(f"P1 = {P1:.3f} atm")
            elif T1 is None:
                T1 = (P1 * T2) / P2
                st.success(f"T1 = {T1:.3f} K")
            elif P2 is None:
                P2 = (P1 * T2) / T1
                st.success(f"P2 = {P2:.3f} atm")
            elif T2 is None:
                T2 = (P2 * T1) / P1
                st.success(f"T2 = {T2:.3f} K")
            else:
                st.warning("Deja uno de los campos vacío para calcularlo.")
        except:
            st.error("Verifica los valores y asegúrate de no dividir entre cero.")
