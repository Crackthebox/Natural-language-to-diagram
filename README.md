# Natural-language-to-diagram
A project for an lseg event that is supposed to turn natural language into diagrams that represent ai models

📊 NeuroArchitect: De la Limbaj Natural la Diagramă

Creat de: Surei Ștefan (sau link-ul tău de GitHub)

    "Vizualizarea ideilor complexe nu ar trebui să fie o barieră, ci un reflex."

NeuroArchitect este un instrument interactiv dezvoltat în cadrul QuantChallenge 2026, conceput să elimine efortul manual de a desena diagrame tehnice. Folosind puterea modelelor LLM locale (via Ollama) și flexibilitatea Mermaid.js, aplicația transformă descrierile textuale simple în arhitecturi vizuale profesionale, riguros structurate și estetic plăcute.
✨ Caracteristici Principale

    🤖 Generare Bazată pe AI: Scrie un prompt simplu (ex: "Un sistem bancar cu un gateway și un filtru de securitate") și urmărește cum AI-ul construiește logica în locul tău.

    🛠️ Pipeline în 4 Pași:

        AI Generator: Motorul de gândire (Qwen 2.5 Coder).

        Code Editor: Flexibilitate totală pentru ajustări manuale.

        Syntax View: Validare instantanee a codului Mermaid.

        Rendered Canvas: Export vizual cu auto-layout inteligent.

    🎨 Stilizare Inteligentă (LSEG Inspired): Algoritmul aplică automat o paletă de culori profesională:

        🟠 Security/Guardrails pentru siguranță.

        🟢 Classifiers/Routers pentru decizii.

        🔴 Action Tools pentru procesare.

        🔵 Data/Users pentru fluxul informațional.

    📐 Geometrie Dinamică: Noduri rotunjite, margini accentuate și săgeți colorate care urmăresc fluxul logic pentru o lizibilitate maximă.

🚀 Tehnologii Utilizate

    Python & Streamlit: Pentru o interfață web fluidă și reactivă.

    Ollama (Qwen 2.5 Coder): Procesare LLM locală pentru confidențialitate și viteză.

    Mermaid.js: Motorul de randare pentru diagrame vectoriale de înaltă calitate.

    Regex & String Processing: Un extractor customizat care elimină "zgomotul" din răspunsurile AI pentru a livra cod pur.

📖 Exemple de Utilizare

Proiectul este versatil și poate interpreta:

    Arhitecturi Cloud/AI (Node-uri de securitate, API Call-uri, Gateways).

    Fluxuri de Decizie (Itinerarii de călătorie, algoritmi logici).

    Arhitecturi Deep Learning (Structuri de Transformer, rețele neurale).

    Diagrame de Relații (Family trees sau ierarhii organizaționale).

⚙️ Instalare și Pornire

    Asigură-te că ai Ollama instalat și modelul descărcat:
    Bash

    ollama pull qwen2.5-coder:1.5b

    Instalează dependențele:
    Bash

    pip install streamlit ollama

    Rulează aplicația:
    Bash

    streamlit run graphic.py

👨‍💻 Contribuții

Acest proiect a fost dezvoltat cu pasiune pentru arhitectura de sistem și AI. Dacă ai idei de îmbunătățire, deschide un Issue sau un Pull Request!