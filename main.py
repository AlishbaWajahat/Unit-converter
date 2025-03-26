import streamlit as st

def converter(category,value,from_unit,to_unit):
    if category=="Length":
        if from_unit=="kilometers" and to_unit=="meters":
            return value*1000
        elif from_unit=="meters" and to_unit=="kilometers":
            return value/1000
        else:
         raise ValueError("unsupported value")
    elif category =="Weight":
        if from_unit=="kilograms" and to_unit=="grams":
            return value*1000
        elif from_unit=="grams" and to_unit=="kilograms":
            return value/1000
        else:
         raise ValueError("unsupported value")
        
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
        else:
         raise ValueError("unsupported value")



def main():
    st.title("Unit converter app") 
    st.subheader("Welcome to our app 👋")    
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
    value=st.number_input("Enter a value to be converted")
    if st.button("Convert"):
        result=converter(category,value,unit_from,unit_to)
        st.write(f"The converted value is:" , result)
    
        
main()            