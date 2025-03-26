import streamlit as st

def converter(category,value,from_unit,to_unit):
 try:
    if value is None or value==0:
        raise ValueError("Please enter a valid number greater than zero.")
    if from_unit==to_unit:
        raise ValueError("The selected units are the same. Please choose different units.")
    if category=="Length":
        if from_unit=="kilometers" and to_unit=="meters":
            return value*1000
        elif from_unit=="meters" and to_unit=="kilometers":
            return value/1000


    elif category =="Weight":
        if from_unit=="kilograms" and to_unit=="grams":
            return value*1000
        elif from_unit=="grams" and to_unit=="kilograms":
            return value/1000

        
    elif category =="Time":
        if from_unit=="hours" and to_unit=="minutes":
            return value*60
        elif from_unit=="minutes" and to_unit=="hours":
            return value/60
        elif from_unit=="minutes" and to_unit=="seconds":
            return value*60
        elif from_unit=="seconds" and to_unit=="minutes":
            return value/60
        elif from_unit=="hours" and to_unit=="seconds":
            return value*3600
        elif from_unit=="seconds" and to_unit=="hours":
            return value/3600
 except ValueError as e:
    st.error(f"⚠️ {e}")
    return None
 except Exception as e:
     st.error("⚠️ An unexpected error occurred! Please try again.")
     return None




def main():
    st.title("Unit converter app") 
    st.subheader("Welcome to our app 👋")   
    unit_from, unit_to = None, None 
    category=st.segmented_control("Select a category",["Length","Weight","Time"], selection_mode="single")  
    if category=="Length":
        unit_from=st.selectbox("Select the length's unit you want to convert from",["kilometers","meters"], placeholder="Choose an option",index=None,)
        unit_to=st.selectbox("Select a length's unit you want to convert into",["kilometers","meters"], placeholder="Choose an option",index=None,)
    elif category=="Weight":
        unit_from=st.selectbox("Select the weight's unit you want to convert from",["kilograms","grams"], placeholder="Choose an option",index=None,)
        unit_to=st.selectbox("Select a weight's unit you want to convert into",["kilograms","grams"], placeholder="Choose an option",index=None,)
    elif category=="Time":
        unit_from=st.selectbox("Select the time's unit you want to convert from",["hours","minutes","seconds"], placeholder="Choose an option",index=None,)
        unit_to=st.selectbox("Select a time's unit you want to convert into",["hours","minutes","seconds"], placeholder="Choose an option",index=None,)
    value=st.number_input("Enter a value to be converted", min_value=0.0)
    if st.button("Convert"):
       if not unit_from or not unit_to:
           st.error("⚠️ Please select both 'From' and 'To' units before converting.") 
       else:   
         result=converter(category,value,unit_from,unit_to)
         if result is not None:
            st.success(f"✅ The converted value is: **{result}**")

    
        
main()                       