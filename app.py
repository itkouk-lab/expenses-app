import streamlit as st

st.title("💸 Καταχώριση Δαπανών")

date = st.date_input("Ημερομηνία")
category = st.text_input("Κατηγορία")
amount = st.number_input("Ποσό", min_value=0.0, step=0.5)
description = st.text_area("Περιγραφή")

if st.button("Καταχώριση"):
    st.success("Η δαπάνη καταχωρήθηκε!")

from supabase import create_client

url = "https://wimodtqnvupohnhgtsts.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndpbW9kdHFudnVwb2huaGd0c3RzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjUxMjQ2MzEsImV4cCI6MjA4MDcwMDYzMX0.SIrsiKVAr6XX7Y31pnVAQuatt5CB0C1SmF3eSGoq56Q"
supabase = create_client(url, key)

if st.button("Καταχώριση"):
    data = {
        "date": str(date),
        "category": category,
        "amount": amount,
        "description": description
    }
    supabase.table("expenses").insert(data).execute()
    st.success("Η δαπάνη αποθηκεύτηκε στο Supabase!")

st.subheader("📋 Όλες οι δαπάνες")
expenses = supabase.table("expenses").select("*").execute()
st.dataframe(expenses.data)