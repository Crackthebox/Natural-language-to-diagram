import streamlit as st

import streamlit.components.v1 as components

import ollama


# --- CONFIGURATION ---

st.set_page_config(layout="wide", page_title="NL to Diagram Pipeline", page_icon="📊")


# --- INITIALIZE SESSION STATE ---

if "draft_code" not in st.session_state:

    # The default LSEG diagram for testing (Box 2)

    default_lseg = """graph TD

    User([User])

    Orch[Orchestrator]

    AppHist[Append History]

    Hist[(Conversation History)]

    Guard[Azure Guardrails]

    Blocked([Request Blocked])

    Class[Intent Classifier]

    Sent[Sentiment Analysis Tool]

    Summ[Summarization Tool]

    Draw[Drawing Tool]

    RespForm[Response Formatter]

    UserResp([User Response])


    User -->|sends-query| Orch

    Orch -->|forward-query| AppHist

    AppHist -.->|fetch-history| Hist

    AppHist -->|enriched-query| Guard

    Guard -.->|policy violation| Blocked

    Guard -->|approved| Class

    Class -->|sentiment-intent| Sent

    Class -->|summarization-intent| Summ

    Class -->|drawing-intent| Draw

    Sent -->|result| RespForm

    Summ -->|result| RespForm

    Draw -->|result| RespForm

    Hist -.->|store interaction| RespForm

    RespForm -->|formatted-response| UserResp


    style User fill:#4A629B,color:#fff

    style Orch fill:#4A86E8,color:#fff

    style AppHist fill:#4A86E8,color:#fff

    style Hist fill:#4A629B,color:#fff

    style Guard fill:#D99C3B,color:#fff

    style Blocked fill:#596168,color:#fff

    style Class fill:#34A853,color:#fff

    style Sent fill:#BA3B3B,color:#fff

    style Summ fill:#BA3B3B,color:#fff

    style Draw fill:#BA3B3B,color:#fff

    style RespForm fill:#4A86E8,color:#fff

    style UserResp fill:#4A629B,color:#fff"""

   

    st.session_state.draft_code = default_lseg

    st.session_state.confirmed_code = default_lseg

    st.session_state.visual_code = ""


# --- FUNCTIONS ---

def extract_mermaid(text):
    """
    Extrage codul Mermaid și aplică reguli de auto-corecție pentru 
    sintaxa invalidă generată frecvent de modelele mici (1.5B).
    """
    clean_code = ""

    # 1. Extracție din blocuri de cod (backticks)
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            p = part.strip()
            # Eliminăm prefixul "mermaid" dacă există
            if p.lower().startswith("mermaid"):
                p = p[7:].strip()
            if p.lower().startswith("graph") or p.lower().startswith("flowchart"):
                clean_code = p
                break

    # 2. Extracție bazată pe cuvinte cheie (dacă nu există backticks)
    if not clean_code:
        start_keywords = ["graph TD", "graph LR", "flowchart TD", "flowchart LR"]
        start_pos = -1
        for kw in start_keywords:
            if kw in text:
                start_pos = text.find(kw)
                break
        
        if start_pos != -1:
            lines = text[start_pos:].split('\n')
            collected_lines = []
            code_markers = ['-', '>', '[', '(', '{', '}', 'style', 'classDef', 'subgraph', 'end', '%%']
            
            for line in lines:
                stripped = line.strip()
                if not stripped or any(marker in stripped for marker in code_markers):
                    collected_lines.append(line)
                else:
                    if len(stripped.split()) > 7: # Chat-ul AI-ului de final
                        break
                    collected_lines.append(line)
            clean_code = "\n".join(collected_lines).strip()
        else:
            clean_code = text.strip()

    # --- 3. AUTO-REPAIR LOGIC (Bonus Points Feature) ---
    
    # Corectăm săgețile invalide (cea mai comună eroare: -> în loc de -->)
    # Folosim un loop pentru a prinde cazurile repetate
    clean_code = clean_code.replace(" -> ", " --> ")
    clean_code = clean_code.replace(" ->>", " --> ")
    clean_code = clean_code.replace(" - > ", " --> ")
    
    # Schimbăm comentariile stil Python (#) în stil Mermaid (%%)
    lines = clean_code.split('\n')
    repaired_lines = []
    for line in lines:
        if line.strip().startswith("#"):
            repaired_lines.append(line.replace("#", "%%", 1))
        else:
            # Forțăm textul negru dacă AI-ul a pus color:#fff
            repaired_lines.append(line.replace("color:#fff", "color:#000"))
    
    clean_code = "\n".join(repaired_lines)

    return clean_code

def render_diagram(code: str):

    """Forces Streamlit to render the visual picture using the official Mermaid JS engine."""

    components.html(

        f"""

        <script type="module">

            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

            // We added the 'flowchart' configuration here to increase spacing!

            mermaid.initialize({{

                startOnLoad: true,

                theme: 'default',

                flowchart: {{

                    nodeSpacing: 70,

                    rankSpacing: 100

                }}

            }});

        </script>

        <div class="mermaid" style="display: flex; justify-content: center;">

            {code}

        </div>

        """,

        height=700,

        scrolling=True

    )


# --- UI HEADER ---

st.title("📊 Architecture Diagram Generator")

st.markdown("QuantChallenge 2026 - Interactive Pipeline")


# --- TOP ROW: AI vs MANUAL ---

col1, col2 = st.columns(2)


with col1:

    st.subheader("1. AI Generator")

    default_prompt = "I want an orchestrator tool that receives a user query append history applies azure guardrails and then decides to which component to use from a sentiment ; summarizations; or drawing tools I want the tools to be in red and the classificator in green"

   

    user_input = st.text_area("Describe your architecture:", value=default_prompt, height=200)

   

    # BUTTON 1

    if st.button("🤖 1. Generate Code with AI", type="primary", use_container_width=True):

        system_instruction = """You are an expert Enterprise AI Architecture Compiler. Convert the user's natural language description into a perfectly valid Mermaid.js flowchart (graph TD).


        CRITICAL LOGIC RULES:

        1. ONLY output raw mermaid code. No markdown formatting, no explanations.

        2. Deduce missing logical steps. If a "censor", "guardrail", "moderation", or "filter" is mentioned, YOU MUST automatically create a dashed-line branch (`-.->`) that leads to a "Request Blocked" terminal node.

        3. Include descriptive edge labels where logical (e.g., `A -->|sends query| B`).


        SHAPE RULES:

        - Users, Endpoints, and Terminal states: `([Text])`

        - Databases or Memory: `[(Text)]`

        - Processes, Tools, and Classifiers: `[Text]`


        MANDATORY COLOR PALETTE (Apply at the end using 'style NodeName fill:#HEX,color:#fff'):

        - Users & Databases: #4A629B (Dark Blue)

        - Orchestrators & Main Pipelines: #4A86E8 (Light Blue)

        - Guardrails, Censors, & Security: #D99C3B (Orange)

        - Classifiers, Routers, & Decisions: #34A853 (Green)

        - Action Tools (Sentiment, Logic, Code, Drawing): #BA3B3B (Red)

        - Blocked/Denied Terminal States: #596168 (Gray)
        

        EXAMPLE OUTPUT:

        graph TD

            U([User]) -->|input| Orch[Orchestrator]

            Orch --> Censor[Nudity Censor]

            Censor -.->|violation| Block([Request Blocked])

            Censor -->|clean| Class[Intent Classifier]

            Class -->|code intent| CodeTool[Code Tool]

            Class -->|logic intent| LogicTool[Logic Tool]

           

            style U fill:#4A629B,color:#fff

            style Orch fill:#4A86E8,color:#fff

            style Censor fill:#D99C3B,color:#fff

            style Block fill:#596168,color:#fff

            style Class fill:#34A853,color:#fff

            style CodeTool fill:#BA3B3B,color:#fff

            style LogicTool fill:#BA3B3B,color:#fff


            ALWAYS append this exact line at the very end of your code to style uncolored nodes:

        classDef default fill:#ffffff,stroke:#000000,stroke-width:2px,rx:10px,ry:10px

        """


        with st.expander("🧠 Live Thinking Process...", expanded=True):

            thinking_box = st.empty()

            raw_output = ""

            try:

                stream = ollama.chat(model='qwen2.5-coder:1.5b', messages=[

                    {'role': 'system', 'content': system_instruction},

                    {'role': 'user', 'content': user_input}

                ], stream=True)

               

                for chunk in stream:

                    raw_output += chunk['message']['content']

                    thinking_box.markdown(raw_output + "▌")

                thinking_box.markdown(raw_output)

               

                clean_code = extract_mermaid(raw_output)

                if clean_code:

                    # AI updates BOTH the editable draft and the syntax view instantly!

                    st.session_state.draft_code = clean_code

                    st.session_state.confirmed_code = clean_code

                    st.rerun()

                else:

                    st.error("Failed to generate valid Mermaid syntax.")

            except Exception as e:

                st.error(f"Error: {e}")


with col2:

    st.subheader("2. Code Editor")

    st.markdown("Edit the code manually if needed.")

   

    # Binding key="draft_code" holds the text here

    st.text_area("Mermaid Code:", height=222, key="draft_code", label_visibility="collapsed")

   

    # BUTTON 2: NEW! Pushes manual edits down to Box 3

    if st.button("🔄 2. Update Syntax View", type="secondary", use_container_width=True):

        st.session_state.confirmed_code = st.session_state.draft_code


st.divider()


# --- MIDDLE ROW: FORMATTED CODE ---

st.subheader("3. Code Syntax View")

st.markdown("This is the finalized syntax ready for rendering.")


# Displays whatever was pushed by the AI or Button 2

st.code(st.session_state.confirmed_code, language="mermaid")


# BUTTON 3

if st.button("🎨 3. Render Visual Diagram", type="primary"):

    # Pushes the confirmed code down to the visual canvas

    st.session_state.visual_code = st.session_state.confirmed_code


st.divider()


# --- BOTTOM ROW: VISUAL CANVAS ---

st.subheader("4. Rendered Diagram Canvas")


if st.session_state.visual_code:

    clean_final = extract_mermaid(st.session_state.visual_code)

    render_diagram(clean_final)

else:

    st.info("Click the 'Render Visual Diagram' button above to draw the flowchart here.") 