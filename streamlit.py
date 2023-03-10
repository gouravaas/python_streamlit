import streamlit as st
st.title("Welcome To BMI Calculator")
weight = st.number_input("\nEnter The Weight In(KG :)")
status = st.radio("\nSelect Your Height Format :",('CM','Meter',"Feet"))
if status=="CM":
    height = st.number_input('\nCenteMeter :')
    try:
        bmi = weight/((height/100)**2)
    except:
        st.text("\nEnter Some value of Height :")
elif status=="Meter":
    height = st.number_input("\nMeter :")
    try:
        bmi = weight/(height**2)
    except:
        st.text("\nEnter Some Value of Height :")
else:
    height = st.number_input("\nFeet :")
    try:
        bmi = weight/(((height/3.28))**2)
    except:
        st.text("\nEnter Some value of Height :")
if st.button("Calculator BMI"):
    st.text("\nYour BMI Index Is {}.".format(bmi))
    if bmi<16:
        st.error("\nYou Are Extermely UnderWeight.")
    elif bmi>=16 and bmi<18.5:
        st.warning("\nYou Are UnderWeight.")
    elif bmi>=18.5 and bmi<25:
        st.success("\nHealthy.")
    elif bmi>=25 and bmi<30:
        st.warning("\nOverWeight.")
    elif bmi>=30:
        st.error("\n.Extermely UnderWeight")
