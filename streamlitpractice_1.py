import streamlit as st
st.title("Lean Application")

cri_annual_sal = 50000
cri_year_work = 5

annual_sal = st.number_input("Please enter your annual salary:")
year_work = st.number_input("Please enter your work year:")

need_sal = cri_annual_sal - annual_sal
need_year = cri_year_work - year_work

if st.button("Submit"):
    if annual_sal >= cri_annual_sal:
        if year_work >= cri_year_work:
            st.write("Congratulation, your application has accepted")
        else:
            st.write(f"Sorry, your application has rejected. The thing you need improve is the work of year, still need {need_year:.1f} years.")

    else:
        if year_work >= cri_year_work:
            st.write(f'Sorry, your application has rejected. The thing you need improve is the annual salary, still need {need_sal:,.2f} yuan.')
        else:
            st.write(f"Sorry, your application has rejected. The thing you need improve is the annual salary and the work of year, still need {need_sal:,.2f} yuan and {need_year:.1f} years.")
