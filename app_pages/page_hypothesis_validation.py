import streamlit as st


def hypothesis_and_validation():
    st.write('#### Project Hypothesis and Validation')
    st.success(
        '''
        * We initially suspected that the 2 most important features would be the **year** and the **Kms driven**.  \n
        * The correlation study showed that in fact the two most important features would be the 
        **ex showroom price** and the **year**. 
        * Based on experience and studies conducted with people regarding what they are looking for when 
        buying a used bike, we decided to leave the KMs driven input there as well (as a third input) for 
        prediction, as it turns out it is a really important feature to look out for in real life.
        '''
    )