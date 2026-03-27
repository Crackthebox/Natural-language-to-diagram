# 📊 NeuroArchitect: AI-Driven Diagram Engine
**Creat de: Surei Ștefan** | *Proiect dezvoltat pentru QuantChallenge 2026*

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-black?style=for-the-badge&logo=ollama&logoColor=white)
![Mermaid](https://img.shields.io/badge/Mermaid-ff69b4?style=for-the-badge&logo=mermaid&logoColor=white)

---

## 🏠 1. Home: Prezentare Proiect

**NeuroArchitect** este o soluție inovatoare care transformă limbajul natural în diagrame tehnice de înaltă precizie. Proiectul rezolvă problema documentației manuale cronofage, permițând arhitecților de sistem și dezvoltatorilor să genereze vizualizări profesionale prin simple descrieri textuale.

### ✨ Caracteristici Principale
* **🤖 AI Local (Privacy First):** Rulează integral pe modelul `qwen2.5-coder:1.5b` via Ollama. Datele tale nu părăsesc niciodată mașina locală.
* **🎨 Enterprise Styling:** Culori predefinite pentru standarde industriale (inspirat de LSEG):
    * 🟠 **Security:** Guardrails și Censors (#D99C3B).
    * 🟢 **Logic:** Routere și Clasificatori (#34A853).
    * 🔴 **Tools:** Servicii active și unelte (#BA3B3B).
    * 🔵 **Data:** Baze de date și utilizatori (#4A629B).
* **⚙️ Pipeline de Control:** Generare AI ➡️ Editare Live ➡️ Sintaxă Robustă ➡️ Randare Canvas.

---

## ⚙️ 2. Configurare Mediu și Instalare

Copiați și rulați următoarele comenzi în terminal pentru a configura și porni aplicația într-un singur flux:

```bash
# Instalează modelul AI, clonează proiectul, instalează librăriile și pornește aplicația
ollama pull qwen2.5-coder:1.5b
git clone [https://github.com/stefansurei/neuroarchitect.git](https://github.com/stefansurei/neuroarchitect.git)
cd neuroarchitect
pip install streamlit ollama
streamlit run graphic.py

Dezvoltat de Surei Stefan