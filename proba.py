# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 16:33:22 2025

@author: pranjikl
"""

import streamlit as st
from PIL import Image
import os

# Postavljanje stranice
st.set_page_config(
    page_title="MuraDrava-FFS Izvještaj",
    page_icon="🌊",
    layout="wide"
)

def main():
    st.title("🌊 MuraDrava-FFS Izvještaj")
    
    # Putanja do PNG datoteke
    image_path = "muradrava_report.png"  # Promijenite naziv datoteke prema potrebi
    
    # Provjeri postoji li datoteka
    if os.path.exists(image_path):
        # Učitaj i prikaži sliku
        image = Image.open(image_path)
        st.image(image, use_container_width=True)
        
        # Opcija za download
        with open(image_path, "rb") as file:
            btn = st.download_button(
                label="📥 Preuzmi izvještaj",
                data=file,
                file_name="MuraDrava_izvjestaj.png",
                mime="image/png"
            )
    else:
        st.error(f"❌ Datoteka '{image_path}' nije pronađena.")
        st.info("💡 Molimo stavite PNG datoteku u isti direktorij kao ovu skriptu i nazovite je 'muradrava_report.png'")
        
        # Upload opcija
        st.subheader("📤 Ili uploadajte PNG datoteku:")
        uploaded_file = st.file_uploader(
            "Odaberite PNG datoteku",
            type=['png', 'jpg', 'jpeg'],
            help="Podržani formati: PNG, JPG, JPEG"
        )
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=True)
            
            # Opcija za download uploaded slike
            st.download_button(
                label="📥 Preuzmi sliku",
                data=uploaded_file.getvalue(),
                file_name=f"extracted_{uploaded_file.name}",
                mime=f"image/{uploaded_file.name.split('.')[-1]}"
            )

# Sidebar informacije
st.sidebar.markdown("### ℹ️ Kako koristiti")
st.sidebar.markdown("""
1. **Stavite PNG datoteku** u isti direktorij kao ovu skriptu
2. **Nazovite je** `muradrava_report.png`
3. **Pokrenite aplikaciju** - slika će se automatski prikazati

**Ili:**
- Koristite upload opciju za bilo koju PNG/JPG datoteku
""")

st.sidebar.markdown("---")
st.sidebar.markdown("📧 Za pomoć kontaktirajte admin")

if __name__ == "__main__":
    main()
