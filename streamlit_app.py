import streamlit as st

# -----------------------------------
# App Configuration
# -----------------------------------
st.set_page_config(
    page_title="Psychosocial Aspects of Cancer Care",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        color: #1E3A8A;
        padding-bottom: 1rem;
        border-bottom: 2px solid #E5E7EB;
    }
    .sub-header {
        color: #374151;
        margin-top: 2rem !important;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #E5E7EB;
    }
    .highlight-box {
        background-color: #F3F4F6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3B82F6;
        margin: 1rem 0;
    }
    .nursing-box {
        background-color: #F0F9FF;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #0EA5E9;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #FEF3C7;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #F59E0B;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Header Section
# -----------------------------------
st.title("🏥 Psychosocial Aspects of Cancer Care")
st.markdown("### A Comprehensive Guide for Oncology Nurses")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("📋 Chapter Navigation")
    sections = st.radio(
        "Go to section:",
        ["Introduction", "Psychological Responses", "Psychosocial Challenges", 
         "Social Sphere", "Therapeutic Communication", "Self-Care", "Assessment"]
    )
    
    st.divider()
    
    st.header("📞 Resources")
    st.write("**Patient Relation Services:** Ext. ")
    st.write("**Psychooncology service:** Ext. ")
    st.write("**Palliative care service:** Ext. ")

# -----------------------------------
# Main Content Sections
# -----------------------------------

if sections == "Introduction":
    st.markdown('<div class="main-header"><h2>Introduction</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        Welcome, oncology nurses. You are at the heart of cancer care, witnessing not just the 
        physical trajectory of disease, but the profound human experience that accompanies it.
        
        This guide is designed to frame and deepen your understanding of the psychological and 
        social dimensions of cancer. Our goal is to equip you with insights and frameworks that 
        can enhance your already vital therapeutic presence.
        """)
    
    #with col2:
    #    st.image("https://ifanglobal.com/2022/10/10/indian-nurses-a-force-to-reckon-with-on-the-global-map/", 
    #            caption="The Nurse as a Healing Environment", use_container_width=True)
    
    st.markdown('<div class="sub-header"><h3>Understanding the Psychosocial Landscape</h3></div>', unsafe_allow_html=True)
    
    st.markdown("""
    Psychosocial care recognizes that a patient is **more than a diagnosis**. It encompasses:
    
    - **Psychological**: Emotional, cognitive, and behavioral factors
    - **Social**: Relationships, roles, financial, and cultural factors
    
    **The Biopsychosocial Model**: Cancer affects the mind and society, which in turn affect biology. 
    Stress, isolation, or depression can influence pain perception, treatment adherence, and immune function.
    """)
    
    st.markdown('<div>', unsafe_allow_html=True)
    st.markdown("**Key Takeaway**: Your holistic care directly addresses the interplay between biological, psychological, and social factors.")
    st.markdown('</div>', unsafe_allow_html=True)

elif sections == "Psychological Responses":
    st.markdown('<div class="main-header"><h2>Psychological Responses to Cancer</h2></div>', unsafe_allow_html=True)
    
    st.markdown("""
    Responses are highly individual but often follow a **non-linear pattern**. 
    These are **normal reactions to an abnormal situation**.
    """)
    
    # Create tabs for different responses
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Shock & Disbelief", "Anxiety & Fear", "Sadness & Grief", "Anger", "Hope"
    ])
    
    with tab1:
        st.markdown("### Initial Shock & Disbelief")
        st.markdown("*'This can\\'t be happening.'*")
        st.markdown("**Manifestations**: Numbness, automatic pilot, detachment")
        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown("**Nursing Implications**:")
        st.markdown("""
        - Provide clear, simple information repeatedly
        - Be a calm, grounding presence
        - Use short sentences and check understanding
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Anxiety & Fear")
        st.markdown("*Fear of pain, death, treatment side effects, loss of identity*")
        st.markdown("**Manifestations**: Restlessness, insomnia, constant questioning, hypervigilance")
        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown("**Nursing Implications**:")
        st.markdown("""
        - Normalize these fears
        - Provide concrete information about what to expect
        - Teach simple breathing techniques (4-7-8 breathing)
        - Offer distractions when appropriate
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### Sadness & Grief")
        st.markdown("*Grieving for lost health, future plans, or physical changes*")
        st.markdown("**Different from clinical depression**, but on a continuum")
        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown("**Nursing Implications**:")
        st.markdown("""
        - Allow space for tears without immediately jumping to cheer up
        - Use empathetic statements: *"This is so much to cope with"*
        - Assess for clinical depression (PHQ-2/9 when appropriate)
        - Connect with support groups
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### Anger")
        st.markdown("*A response to helplessness or perceived injustice*")
        st.markdown("**Manifestations**: Irritability, blaming others, withdrawal")
        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown("**Nursing Implications**:")
        st.markdown("""
        - Do not take it personally
        - See anger as an expression of underlying distress
        - Respond with curiosity: *"You seem really frustrated. Tell me more..."*
        - Set boundaries while maintaining empathy
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab5:
        st.markdown("### Hope")
        st.markdown("*An essential survival tool*")
        st.markdown("**Evolves over time**: Cure → Remission → Good days → Peace → Legacy")
        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown("**CRITICAL**: Never strip away hope. Help **reframe** it to match the current reality.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("**Ask**: *'What is most important to you right now?'*")

elif sections == "Psychosocial Challenges":
    st.markdown('<div class="main-header"><h2>Key Psychosocial Challenges Across the Trajectory</h2></div>', unsafe_allow_html=True)
    
    timeline = st.selectbox(
        "Select treatment phase:",
        ["During Active Treatment", "End of Treatment/Survivorship", "Advanced/Palliative Stages", "End of Life"]
    )
    
    if timeline == "During Active Treatment":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Focus Areas**:")
            st.markdown("""
            - Coping with side effects (fatigue, nausea)
            - Managing treatment adherence
            - Dealing with uncertainty
            - **Profound body image distress**
            """)
        with col2:
            st.markdown("**Your Role**:")
            st.markdown("""
            - Proactively address side effects
            - Normalize body image concerns
            - Offer resources (wigs, scarves, patient visitors)
            - Validate the difficulty
            """)
    
    elif timeline == "End of Treatment/Survivorship":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Common Experiences**:")
            st.markdown("""
            - 'Scanxiety' before follow-ups
            - Fear of recurrence
            - Loss of safety net (regular visits)
            - Challenges returning to 'normal'
            """)
        with col2:
            st.markdown("**Your Role**:")
            st.markdown("""
            - Validate these feelings
            - Prepare patients for transition
            - Discuss clear follow-up plans
            - Connect with survivorship programs
            """)
    
    elif timeline == "Advanced/Palliative Stages":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Key Issues**:")
            st.markdown("""
            - Confronting mortality
            - Existential distress (meaning, purpose)
            - Complex symptom management
            - Changing goals of care
            """)
        with col2:
            st.markdown("**Your Role**:")
            st.markdown("""
            - Shift focus to quality of life
            - Aggressive symptom control
            - Skilled communication about goals
            - Be comfortable with silence
            """)
    
    else:  # End of Life
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Focus Areas**:")
            st.markdown("""
            - Legacy and closure
            - Spiritual peace
            - Family support
            - Dignity conservation
            """)
        with col2:
            st.markdown("**Your Role**:")
            st.markdown("""
            - Facilitate difficult conversations
            - Honor cultural/spiritual practices
            - Provide unwavering compassionate care
            - Support the entire family system
            """)

elif sections == "Social Sphere":
    st.markdown('<div class="main-header"><h2>The Social Sphere: When the World Shrinks and Stress Expands</h2></div>', unsafe_allow_html=True)
    
    st.markdown("### Family Dynamics")
    st.markdown("Cancer is a **family diagnosis**. Roles shift dramatically.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Common Patterns**:")
        st.markdown("""
        - Overprotectiveness vs. abandonment
        - Caregiver burnout
        - Role reversal (child becomes caregiver)
        - Communication breakdowns
        """)
    
    with col2:
        st.markdown("**Your Role**:")
        st.markdown("""
        - Include family in teaching when appropriate
        - Assess caregiver burnout (ask directly!)
        - Refer to family counseling/support groups
        - Create 'family meetings' when needed
        """)
    
    st.divider()
    
    st.markdown("### Economic Toxicity")
    st.markdown("The crushing financial burden of treatment, travel, and lost wages.")
    
    st.markdown('<div>', unsafe_allow_html=True)
    st.markdown("**Sample Screening Question**:")
    st.markdown('*"Many people find the costs of treatment stressful. Would you like to speak with someone who can help?"*')
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("**Resources to Have Ready**:")
    st.markdown("""
    - Social work contacts
    - Financial counseling
    - Patient assistance programs
    - Transportation services
    """)
    
    st.divider()
    
    st.markdown("### Cultural Considerations")
    
    cultural_factors = st.multiselect(
        "Cultural factors to explore:",
        ["Illness causation beliefs", "Decision-making style", "Truth-telling preferences", 
         "Spiritual practices", "Family roles", "Communication norms", "Dietary restrictions"]
    )
    
    if cultural_factors:
        st.markdown("**Suggested Questions**:")
        for factor in cultural_factors:
            if factor == "Illness causation beliefs":
                st.write("- *'What do you believe is causing your illness?'*")
            elif factor == "Decision-making style":
                st.write("- *'How does your family prefer to make medical decisions?'*")
            elif factor == "Truth-telling preferences":
                st.write("- *'How would you like to receive information about your condition?'*")
            elif factor == "Spiritual practices":
                st.write("- *'Are there spiritual practices that are important to you during treatment?'*")

elif sections == "Therapeutic Communication":
    st.markdown('<div class="main-header"><h2>Your Most Powerful Tool: Therapeutic Communication</h2></div>', unsafe_allow_html=True)
    
    st.markdown("### Communication Skills Practice")
    
    scenario = st.selectbox(
        "Choose a patient scenario:",
        ["Patient expressing fear of dying", 
         "Patient angry about treatment delays",
         "Family member overwhelmed with caregiving",
         "Patient questioning 'Why me?'",
         "Patient crying about hair loss"]
    )
    
    st.markdown("**Patient Statement**:")
    if scenario == "Patient expressing fear of dying":
        st.write("*\"I'm so scared I'm going to die. I can't sleep thinking about it.\"*")
    elif scenario == "Patient angry about treatment delays":
        st.write("*\"This is ridiculous! I've been waiting 2 hours! Don't you people care?\"*")
    elif scenario == "Family member overwhelmed with caregiving":
        st.write("*\"I don't know how much longer I can do this. I'm exhausted and I'm failing at everything.\"*")
    elif scenario == "Patient questioning 'Why me?'":
        st.write("*\"Why is this happening to me? What did I do to deserve this?\"*")
    elif scenario == "Patient crying about hair loss":
        st.write("*\"I look like a monster. I can't even recognize myself in the mirror anymore.\"*")
    
    st.markdown("**Your Response Options**:")
    
    if scenario == "Patient expressing fear of dying":
        option = st.radio(
            "Select the most therapeutic response:",
            [
                "Don't worry, our doctors are the best.",
                "That sounds incredibly difficult. Tell me more about what scares you most.",
                "You need to think positively.",
                "Let me get you something for sleep."
            ]
        )
        if option == "That sounds incredibly difficult. Tell me more about what scares you most.":
            st.success("✅ Excellent! This validates emotion and invites sharing.")
        elif option:
            st.warning("Try again - look for the response that validates feelings first.")
    elif scenario == "Patient angry about treatment delays":
        option = st.radio(
            "Select the most therapeutic response:",
            [
                "Sir, please calm down. We're doing our best.",
                "I can hear how frustrated you are. This wait must be really difficult.",
                "Everyone has to wait their turn.",
                "I'll see what I can do to speed things up."
            ]
        )
        if option == "I can hear how frustrated you are. This wait must be really difficult.":
            st.success("✅ Excellent! This validates emotion and invites sharing.")
        elif option:
            st.warning("Try again - look for the response that validates feelings first.")
    elif scenario == "Family member overwhelmed with caregiving":
        option = st.radio(
            "Select the most therapeutic response:",
            [
                "Don't say that, you're doing a great job.",
                "Being a caregiver is incredibly challenging. Tell me more about what's hardest right now.",
                "Everyone feels this way sometimes.",
                "Maybe you should consider hiring more help."
            ]
        )
        if option == "Being a caregiver is incredibly challenging. Tell me more about what's hardest right now.":
            st.success("✅ Excellent! This validates emotion and invites sharing.")
        elif option:
            st.warning("Try again - look for the response that validates feelings first.")
    elif scenario == "Patient questioning 'Why me?'":
        option = st.radio(
            "Select the most therapeutic response:",
            [
                "Cancer is random - it can happen to anyone.",
                "That's a question many people ask. What thoughts or feelings come up when you wonder 'why me'?",
                "Try not to dwell on questions without answers.",
                "Everything happens for a reason.",
                "Let's focus on the treatment plan instead."
            ]
        )
        if option == "That's a question many people ask. What thoughts or feelings come up when you wonder 'why me'?":
            st.success("✅ Excellent! This validates emotion and invites sharing.")
        elif option:
            st.warning("Try again - look for the response that validates feelings first.")
    elif scenario == "Patient crying about hair loss":
        option = st.radio(
            "Select the most therapeutic response:",
            [
                "Don't worry, it will grow back after treatment.",
                "Losing your hair must be really difficult. Tell me more about how this is affecting you.",
                "It's just hair - what matters is that you're getting better.",
                "Many patients use wigs or scarves. Would you like to see some options?",
                "You're still beautiful, even without hair."
            ]
        )
        if option == "Losing your hair must be really difficult. Tell me more about how this is affecting you.":
            st.success("✅ Excellent! This validates emotion and invites sharing.")
        elif option:
            st.warning("Try again - look for the response that validates feelings first.")        
    
    st.divider()
    
    st.markdown("### Communication Techniques")
    
    techniques = [
        ("Active Listening", "Give full attention. Listen for feelings, not just facts."),
        ("Empathetic Statements", "\"That sounds incredibly difficult.\" \"I can see how worried you are.\""),
        ("Open-Ended Questions", "\"How are you coping with all this?\" vs. \"Are you okay?\""),
        ("Responding to Emotion", "Identify the feeling and validate it."),
        ("Silence", "Allow pauses for patients to gather thoughts.")
    ]
    
    for technique, description in techniques:
        with st.expander(f"📌 {technique}"):
            st.write(description)
            if technique == "Empathetic Statements":
                st.markdown("**Examples**:")
                st.write("- \"This must be so overwhelming for you.\"")
                st.write("- \"I hear how frustrating this is.\"")
                st.write("- \"It makes sense you'd feel that way.\"")

elif sections == "Self-Care":
    st.markdown('<div class="main-header"><h2>Boundaries and Self-Care: The Sustenance of the Caregiver</h2></div>', unsafe_allow_html=True)
    
    st.markdown("You cannot pour from an empty cup. Witnessing suffering daily leads to:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Compassion Fatigue**")
        st.markdown("Gradual lessening of compassion over time")
    with col2:
        st.markdown("**Burnout**")
        st.markdown("Physical, emotional, mental exhaustion")
    with col3:
        st.markdown("**Vicarious Trauma**")
        st.markdown("Negative transformation from others' trauma")
    
    st.divider()
    
    st.markdown("### Self-Assessment Checklist")
    
    burnout_signs = st.multiselect(
        "Which signs have you experienced recently?",
        [
            "Cynicism about work", "Dread of coming to work", "Emotional numbness",
            "Physical exhaustion", "Irritability with patients/colleagues",
            "Feeling ineffective", "Difficulty concentrating", "Frequent headaches/stomach issues"
        ]
    )
    
    if burnout_signs:
        st.warning(f"You selected {len(burnout_signs)} signs. Consider discussing with a supervisor or accessing wellness resources.")
    
    st.divider()
    
    st.markdown("### Self-Care Strategies")
    
    strategy_type = st.radio(
        "Focus area:",
        ["At Work", "During Transition", "Team Support"]
    )
    
    if strategy_type == "At Work":
        st.markdown("""
        - Take real breaks (leave the unit)
        - Debrief difficult cases with colleagues
        - Use deep breathing between patients
        - Stay hydrated and snack regularly
        """)
    elif strategy_type == "During Transition":
        st.markdown("""
        - Create a ritual to end your shift
        - Change out of scrubs before leaving
        - Listen to music/podcasts during commute
        - Practice mindfulness during travel
        """)
    elif strategy_type == "Team Support":
        st.markdown("""
        - Create a culture of checking in
        - Normalize saying 'This case was hard for me'
        - Celebrate small wins together
        - Organize team wellness activities
        """)
    
    st.markdown('<div>', unsafe_allow_html=True)
    st.markdown("**Remember**: Self-care is not selfish. It's a **professional requirement** for sustainable oncology nursing.")
    st.markdown('</div>', unsafe_allow_html=True)

elif sections == "Assessment":
    st.markdown('<div class="main-header"><h2>Learning Assessment</h2></div>', unsafe_allow_html=True)
    
    st.markdown("### 📝 Post-Session Learning Evaluation")
    
    st.markdown("""
    Please complete this brief assessment to help us understand what you've learned 
    and how we can improve future sessions.
    """)
    
    # Placeholder for Google Form link
    #form_link = st.text_input(
    #    "Enter Google Form Assessment Link:",
    #    placeholder="https://docs.google.com/forms/d/...",
    #    value=""
    #)
    
    #if form_link:
    #    st.success(f"✅ Link saved: {form_link}")
    #    if st.button("Open Assessment Form"):
    #        st.markdown(f'<meta http-equiv="refresh" content="0; url={form_link}">', unsafe_allow_html=True)
    #        st.write(f"Opening: {form_link}")
    #else:
    #    st.info("👆 Please enter the Google Form link above to access the assessment.")
    
    st.divider()
    
    st.markdown("### Quick Knowledge Check")
    
    q1 = st.radio(
        "1. Which statement about hope in cancer care is most accurate?",
        [
            "Nurses should maintain hope for cure at all times",
            "Hope should be reframed to match current reality",
            "Hope is only relevant in early-stage cancer",
            "Discussing hope gives false reassurance"
        ]
    )
    
    q2 = st.multiselect(
        "2. Which are appropriate therapeutic responses to anger? (Select all that apply)",
        [
            "Take it personally and defend the healthcare team",
            "See anger as expression of underlying distress",
            "Respond with curiosity about the source",
            "Set boundaries while maintaining empathy"
        ]
    )
    
    q3 = st.radio(
        "3. What is 'economic toxicity'?",
        [
            "Side effects of chemotherapy",
            "The financial burden of cancer treatment",
            "Toxic work environments",
            "Psychological distress from diagnosis"
        ]
    )
    
    if st.button("Check Answers"):
        score = 0
        if q1 == "Hope should be reframed to match current reality":
            score += 1
        if set(q2) == {"See anger as expression of underlying distress", "Respond with curiosity about the source", "Set boundaries while maintaining empathy"}:
            score += 1
        if q3 == "The financial burden of cancer treatment":
            score += 1
        
        st.success(f"**Score: {score}/3**")
        if score == 3:
            st.balloons()
            st.markdown("🎉 Excellent understanding of key concepts!")

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Session Developed By:**")
    st.markdown("Psychooncology Service, Dept. of Psychiatry, Pramukhswami Medical College, Bhaikaka University, Karamsad")
with col2:
    st.markdown("**For Support:**")
    st.markdown("Hospital Extension: 02692-228201")
