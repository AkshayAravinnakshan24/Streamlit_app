import streamlit as st
from Test1 import Calculate_cost
import pandas as pd 


# Run Calculation
with st.form("my_form"):
   st.write("Inside the form")
   Maintainace_cost = st.number_input('Insert a number')
   Wear_Tear_cost=st.slider("Wear_Tear_cost")
   Include_maintainance = st.checkbox("Include maintainance?")

   # Every form must have a submit button.
   run = st.form_submit_button("Run Calculation")
   if run:
       stringtttt=Calculate_cost(Maintainace_cost,Wear_Tear_cost,Include_maintainance)
       st.write("Total Cost = ", str(stringtttt))

st.write("Outside the form")




with st.expander("See explanation"):
    df=pd.read_csv('C:\MAN_2023\edited_df.csv')
    
edited_df = st.experimental_data_editor(df) # 👈 An editable dataframe





# Save changes made
if st.button('Save changes'):
    edited_df.to_csv('C:\MAN_2023\edited_df.csv',index=False)
    st.write('Saved')

# Download edited data

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(edited_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='edited_df.csv',
    mime='text/csv',
)
