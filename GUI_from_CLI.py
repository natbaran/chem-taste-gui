import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

# Dictionary of molecules with taste and SMILES representation
taste_dictionary = {
    'glucose': {'taste': 'sweet', 'smiles': 'C(C1C(C(C(C(O1)O)O)O)O)O'},
    'fructose': {'taste': 'sweet', 'smiles': 'C(C1C(C(C(C(O1)O)O)O)O)O'},
    'aspartame': {'taste': 'sweet', 'smiles': 'CC(C(=O)O)N[C@@H](C(=O)O)C1=CC(=C(C=C1)O)C2=CC(=C(C=C2)O)C(=O)O'},
    'caffeine': {'taste': 'bitter', 'smiles': 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C'},
    'sodium chloride': {'taste': 'salty', 'smiles': 'Cl[Na]'},
    'citric acid': {'taste': 'sour', 'smiles': 'C(C(=O)O)C(C(=O)O)C(C(=O)O)O'},
    'lactic acid': {'taste': 'sour', 'smiles': 'CC(C(=O)O)O'},
    'vanillin': {'taste': 'sweet', 'smiles': 'C1=CC(=C(C=C1O)O)C(=O)O'},
    'menthol': {'taste': 'minty', 'smiles': 'CC(C)C1=CC2=C(C=C1O)C(=O)O2'},
    'gingerol': {'taste': 'spicy', 'smiles': 'CC(C(=O)O)C1=CC(=C(C=C1O)O)C(=O)O'},
    'capsaicin': {'taste': 'spicy', 'smiles': 'CC(C(=O)O)C1=CC(=C(C=C1O)O)C(=O)O'},
    'monosodium glutamate': {'taste': 'umami', 'smiles': 'C(C(=O)O)C(C(=O)O)C(C(=O)O)O'}
}


# Function to generate 2D molecular image from SMILES
def create_smiles_image(smiles):
    mol = Chem.MolFromSmiles(smiles)
    image = Draw.MolToImage(mol)
    return image

# -------------------------
# Streamlit GUI
# -------------------------
st.title("🧪 ChemTaste GUI")
st.write("Predict the taste of a molecule and visualize it!")

# Dropdown for molecule selection
chosen_molecule = st.selectbox("Choose a molecule:", list(taste_dictionary.keys()))

if st.button("Predict Taste"):
    smiles = taste_dictionary[chosen_molecule]['smiles']
    taste = taste_dictionary[chosen_molecule]['taste']

    # Display predicted taste
    st.success(f"The predicted taste of **{chosen_molecule}** is: **{taste}**")
    
    # Display 2D molecular image centered using columns
    img = create_smiles_image(smiles)
    col1, col2, col3 = st.columns([1,2,1])   # column ratios: left, center, right
    with col2:
        st.image(img, caption=f"2D structure of {chosen_molecule}", width=280)


