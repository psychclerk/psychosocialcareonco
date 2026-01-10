"""
Psycho-Oncology Training Manual for Psychiatry Residents (India)
A Streamlit application for interactive learning
"""

import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Psycho-Oncology Training Manual",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .chapter-header {
        background: linear-gradient(135deg, #2d5a87 0%, #3d7ab8 100%);
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
        color: white;
    }
    
    .learning-objectives {
        background: #f0f7ff;
        border-left: 4px solid #2d5a87;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    
    .key-concept {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    
    .clinical-tip {
        background: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    
    .case-study {
        background: #e7f1ff;
        border-left: 4px solid #007bff;
        padding: 1.5rem;
        border-radius: 0 8px 8px 0;
        margin: 1.5rem 0;
    }
    
    .review-question {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    
    .summary-box {
        background: #e2e3e5;
        border-left: 4px solid #6c757d;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    
    .nav-button {
        width: 100%;
        text-align: left;
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        border-radius: 8px;
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .nav-button:hover {
        background: #e9ecef;
        border-color: #2d5a87;
    }
    
    .nav-button.active {
        background: #2d5a87;
        color: white;
        border-color: #2d5a87;
    }
    
    .tool-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
    }
    
    .tool-table th, .tool-table td {
        border: 1px solid #dee2e6;
        padding: 0.75rem;
        text-align: left;
    }
    
    .tool-table th {
        background: #2d5a87;
        color: white;
    }
    
    .tool-table tr:nth-child(even) {
        background: #f8f9fa;
    }
    
    div.stButton > button {
        background: #2d5a87;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        transition: all 0.3s;
    }
    
    div.stButton > button:hover {
        background: #1e3a5f;
        color: white;
    }
    
    .sidebar-section {
        margin-bottom: 1.5rem;
    }
    
    .quick-reference {
        background: #f1f3f4;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for navigation
if 'current_section' not in st.session_state:
    st.session_state.current_section = "1.1"
if 'expanded_cases' not in st.session_state:
    st.session_state.expanded_cases = []

# Navigation data structure
navigation_data = {
    "Section I: Foundations of Psycho-Oncology": {
        "1.1": "Introduction to Psycho-Oncology",
        "1.2": "Epidemiology of Cancer in India",
        "1.3": "Biopsychosocial Model in Oncology"
    },
    "Section II: Psychological Reactions": {
        "2.1": "Psychological Responses to Cancer Diagnosis",
        "2.2": "Adjustment Disorders in Cancer Patients",
        "2.3": "Anxiety Disorders in Oncology",
        "2.4": "Depression in Cancer",
        "2.5": "Delirium and Neuropsychiatric Syndromes"
    },
    "Section III: Assessment": {
        "3.1": "Psychiatric Assessment of the Cancer Patient",
        "3.2": "Screening Tools in Psycho-Oncology",
        "3.3": "Communication Skills in Oncology Settings"
    },
    "Section IV: Psychopharmacology": {
        "4.1": "Principles of Psychopharmacology in Oncology"
    },
    "Section V: Psychological Interventions": {
        "5.1": "Supportive Psychotherapy in Oncology"
    },
    "Section VI: Palliative Care": {
        "6.1": "Depression vs Demoralization in Advanced Cancer",
        "6.2": "Grief, Bereavement, and Complicated Grief"
    },
    "Quick Reference": {
        "REF1": "Screening Tools Summary",
        "REF2": "SPIKES Protocol",
        "REF3": "Emergency Resources"
    }
}

def render_header():
    """Render the main header"""
    st.markdown("""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 2.5rem;">🏥 Training Manual in Psycho-Oncology</h1>
        <h3 style="margin: 0.5rem 0 0 0; font-weight: normal;">For Psychiatry Residents in India</h3>
        <p style="margin: 1rem 0 0 0; opacity: 0.9;">A comprehensive guide to psychological care in cancer patients</p>
    </div>
    """, unsafe_allow_html=True)

def render_section_header(section_number, section_title):
    """Render section headers"""
    st.markdown(f"""
    <div class="chapter-header">
        <h2 style="margin: 0;">Section {section_number}: {section_title}</h2>
    </div>
    """, unsafe_allow_html=True)

def render_learning_objectives(objectives):
    """Render learning objectives section"""
    st.markdown('<div class="learning-objectives">', unsafe_allow_html=True)
    st.markdown("**🎯 Learning Objectives**")
    st.markdown("<ul>", unsafe_allow_html=True)
    for obj in objectives:
        st.markdown(f"<li>{obj}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_key_concept(content):
    """Render key concept box"""
    st.markdown('<div class="key-concept">', unsafe_allow_html=True)
    st.markdown("**💡 Key Concept**")
    st.markdown(content, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_clinical_tip(content):
    """Render clinical tip box"""
    st.markdown('<div class="clinical-tip">', unsafe_allow_html=True)
    st.markdown("**🩺 Clinical Tip**")
    st.markdown(content, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_warning(content):
    """Render warning box"""
    st.markdown('<div class="warning-box">', unsafe_allow_html=True)
    st.markdown("**⚠️ Warning**")
    st.markdown(content, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_case_study(case_number, title, content):
    """Render case study with expand/collapse"""
    case_key = f"case_{case_number}"
    
    with st.expander(f"📋 Case Study {case_number}: {title}", expanded=(case_key in st.session_state.expanded_cases)):
        st.markdown(f"""
        <div class="case-study">
            <h4 style="margin-top: 0; color: #007bff;">Case Study {case_number}: {title}</h4>
            {content}
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Toggle Details", key=f"toggle_{case_key}"):
            if case_key in st.session_state.expanded_cases:
                st.session_state.expanded_cases.remove(case_key)
            else:
                st.session_state.expanded_cases.append(case_key)

def render_review_questions(questions):
    """Render review questions"""
    st.markdown("### 📝 Review Questions")
    for i, question in enumerate(questions, 1):
        st.markdown(f"""
        <div class="review-question">
            <strong>{i}. {question}</strong>
        </div>
        """, unsafe_allow_html=True)

def render_summary(content):
    """Render chapter summary"""
    st.markdown('<div class="summary-box">', unsafe_allow_html=True)
    st.markdown("**📌 Chapter Summary**")
    st.markdown(content, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_table(data, caption=""):
    """Render a formatted table"""
    if caption:
        st.markdown(f"**{caption}**")
    df = pd.DataFrame(data)
    st.table(df)

def render_spiKES():
    """Render SPIKES protocol as a structured display"""
    spikes_data = {
        "Step": ["S", "P", "I", "K", "E", "S"],
        "Meaning": ["Setting up", "Perception", "Invitation", "Knowledge", "Emotions", "Strategy/Summary"],
        "Description": [
            "Arrange privacy, include family, sit down, establish rapport",
            "Assess what patient already knows about their condition",
            "Determine how much information patient wishes to receive",
            "Deliver information clearly and without jargon, in graduated manner",
            "Observe for emotional reactions and respond with empathy",
            "Outline treatment plan and next steps, provide summary"
        ],
        "Key Question": [
            "How should I arrange the conversation?",
            "What does the patient already know?",
            "How much does the patient want to know?",
            "How should I deliver the information?",
            "How should I respond to feelings?",
            "What are the next steps?"
        ]
    }
    render_table(spikes_data, "SPIKES Protocol for Breaking Bad News")

def render_screening_tools_summary():
    """Render screening tools summary table"""
    tools_data = {
        "Tool": ["Distress Thermometer", "PHQ-9", "GAD-7", "HADS"],
        "Items": ["1 + problem list", "9", "7", "14"],
        "Admin Time": ["1-2 minutes", "2-3 minutes", "2 minutes", "3-5 minutes"],
        "Cutoff": ["≥4", "5/10/15", "5/10/15", "≥8 per subscale"],
        "Key Use": [
            "Brief distress screening",
            "Depression screening",
            "Anxiety screening",
            "Depression/anxiety in medical patients"
        ]
    }
    render_table(tools_data, "Commonly Used Screening Tools")

def render_emergency_resources():
    """Render emergency resources"""
    st.markdown("""
    <div class="quick-reference">
        <h4 style="margin-top: 0;">🚨 Emergency Resources</h4>
        <table class="tool-table">
            <tr>
                <th>Resource</th>
                <th>Contact</th>
                <th>Description</th>
            </tr>
            <tr>
                <td>iCALL</td>
                <td>9152987821</td>
                <td>Mental health helpline</td>
            </tr>
            <tr>
                <td>Vandrevala Foundation</td>
                <td>1860-2662-345 or 1800-2333-330</td>
                <td>24/7 mental health support</td>
            </tr>
            <tr>
                <td>Snehi</td>
                <td>044-24640050</td>
                <td>Psychological support</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

def render_chapter_1_1():
    """Chapter 1.1: Introduction to Psycho-Oncology"""
    render_learning_objectives([
        "Define psycho-oncology and describe its scope and evolution",
        "Explain the role of the psycho-oncologist within the multidisciplinary oncology team",
        "Compare global and Indian perspectives on psycho-oncology practice"
    ])
    
    st.markdown("""
    ## 1.1 Definition, Scope, and Evolution
    
    Psycho-oncology is a specialized interdisciplinary field that addresses the psychological, social, behavioral, and ethical dimensions of cancer care. The discipline emerged from the recognition that cancer, as a disease, extends far beyond its biological manifestations to profoundly affect the psychological well-being of patients, their families, and even the healthcare professionals who care for them.
    """)
    
    st.markdown("### The Scope of Psycho-Oncology")
    
    scope_data = {
        "Domain": ["Psychological Responses", "Psychosocial Factors", "Psychological Interventions"],
        "Description": [
            "Study of emotional and cognitive responses to cancer at all stages of the disease trajectory",
            "Investigation of factors that may influence cancer incidence, progression, and outcomes",
            "Development and implementation of interventions to improve quality of life and clinical outcomes"
        ]
    }
    render_table(scope_data)
    
    st.markdown("""
    The evolution of psycho-oncology as a formal discipline can be traced to several key developments. In the mid-twentieth century, pioneering work by Elizabeth Kübler-Ross transformed understanding of death and dying, introducing the influential model of five stages of grief. The formal establishment of the International Psycho-Oncology Society (IPOS) in 1984 marked a milestone in the field's institutional development.
    """)
    
    render_key_concept("""
    **Key Historical Milestones:**
    
    - **1970s**: Kübler-Ross's work on death and dying
    - **1984**: Establishment of International Psycho-Oncology Society (IPOS)
    - **1990s-2000s**: Integration of psychosocial care into oncology guidelines
    - **Present**: Growing recognition in India with dedicated departments at major cancer centers
    """)
    
    st.markdown("### 1.2 Role of the Psycho-Oncologist")
    
    st.markdown("""
    The psycho-oncologist occupies a unique position within the oncology team, bringing specialized expertise in the assessment and management of psychological disorders while maintaining sensitivity to the medical context of cancer care.
    """)
    
    st.markdown("**Clinical services provided by psycho-oncologists include:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - Assessment and treatment of psychiatric disorders (depression, anxiety, delirium, adjustment disorders)
        - Management of psychological aspects of pain, fatigue, nausea, and other physical symptoms
        - Consultation to oncology teams regarding treatment decision-making
        """)
    
    with col2:
        st.markdown("""
        - Capacity assessments
        - Management of treatment refusal
        - Education and training of oncology staff
        - Research and quality improvement activities
        """)
    
    render_clinical_tip("""
    **Indian Context:** Psycho-oncology departments have been established at major cancer centers including:
    - Tata Memorial Hospital, Mumbai
    - AIIMS, New Delhi
    - Cancer Institute (WIA), Chennai
    """)
    
    st.markdown("### 1.3 Global and Indian Perspectives")
    
    st.markdown("""
    The global landscape of psycho-oncology reflects both shared challenges and significant disparities in resources and implementation. High-income countries have generally made substantial progress in integrating psychosocial care into standard oncology practice.
    """)
    
    india_stats = {
        "Metric": [
            "Estimated annual new cancer cases",
            "Common cancers in men",
            "Common cancers in women",
            "Prevalence of depression in advanced cancer",
            "Prevalence of anxiety in cancer patients"
        ],
        "Value": [
            "~1.4 million",
            "Head and neck, lung, GI cancers",
            "Breast, cervical, gynecological cancers",
            "15-30%",
            "20-25%"
        ]
    }
    render_table(india_stats, "Key Cancer Statistics in India")
    
    render_warning("""
    **Challenges for Psycho-Oncology in India:**
    
    - Fragmented cancer care system
    - Disparities between urban and rural access
    - Significant public-private sector differences
    - Cultural factors (stigma, family dynamics, traditional healing)
    - Limited resources outside major urban centers
    """)
    
    render_summary("""
    Psycho-oncology is an interdisciplinary field addressing the psychological, social, and behavioral dimensions of cancer care. The psycho-oncologist plays a unique role in assessing and treating psychiatric disorders while integrating medical knowledge with psychological expertise. India faces significant challenges in cancer care delivery, requiring culturally adapted approaches to psycho-oncology practice.
    """)
    
    render_review_questions([
        "What are the three primary domains of psycho-oncology?",
        "How does the role of the psycho-oncologist differ from that of a general psychiatrist?",
        "What are the main challenges for psycho-oncology practice in India?"
    ])

def render_chapter_1_2():
    """Chapter 1.2: Epidemiology of Cancer in India"""
    render_learning_objectives([
        "Describe the epidemiology of common cancers in India",
        "Explain how sociocultural determinants influence cancer presentation",
        "Discuss the psychological burden of cancer in Indian patients"
    ])
    
    st.markdown("## 1.2 Epidemiology of Cancer in India")
    
    st.markdown("""
    India faces a significant and growing cancer burden that presents unique challenges for healthcare systems and mental health professionals. The epidemiology of cancer in India differs in important ways from that observed in Western countries.
    """)
    
    st.markdown("### Common Cancers by Gender")
    
    cancer_data = {
        "Gender": ["Men", "Women"],
        "Most Common Cancers": [
            "Head and neck cancers, lung cancer, gastrointestinal cancers",
            "Breast cancer, cervical cancer, gynecological cancers"
        ],
        "Key Risk Factors": [
            "Tobacco use, diet, H. pylori infection",
            "Reproductive factors, HPV infection, lifestyle changes"
        ]
    }
    render_table(cancer_data)
    
    render_clinical_tip("""
    **Regional Variations:**
    
    - **North India**: Higher rates of tobacco-related cancers
    - **South India**: Higher rates of breast cancer
    - **Northeast India**: Higher rates of esophageal and lung cancer
    - **Urban areas**: Increasing breast cancer rates
    - **Rural areas**: Higher rates of cervical cancer
    """)
    
    st.markdown("### 1.2.1 Sociocultural Determinants of Cancer Presentation")
    
    st.markdown("""
    The presentation of cancer in Indian patients is profoundly shaped by sociocultural factors that influence help-seeking behavior, symptom interpretation, treatment decisions, and psychological response.
    """)
    
    sociocultural_data = {
        "Factor": [
            "Health Literacy",
            "Stigma",
            "Family Structures",
            "Religious Beliefs",
            "Traditional Healing"
        ],
        "Impact": [
            "Limited knowledge delays presentation",
            "Cancer perceived as divine punishment or moral failing",
            "Extended family central to healthcare decisions",
            "Provide resources and challenges for coping",
            "Ayurveda, Siddha consulted alongside oncologists"
        ]
    }
    render_table(sociocultural_data, "Key Sociocultural Factors")
    
    render_case_study(
        "1.2.1",
        "Delayed Presentation Due to Traditional Beliefs",
        """
        **Patient:** 55-year-old farmer from Bihar
        
        **Presentation:** 6-month history of oral ulcer treated by traditional healers
        
        **Outcome:** Diagnosed with oral cavity cancer after failing to improve
        
        **Factors:** Belief that illness was "bad karma" requiring spiritual healing
        
        **Lesson:** Cultural beliefs can significantly delay presentation and treatment
        """
    )
    
    st.markdown("### 1.2.2 Psychological Burden of Cancer in Indian Patients")
    
    burden_data = {
        "Condition": ["Depression", "Anxiety Disorders", "Adjustment Disorders", "Significant Distress"],
        "Prevalence": ["15-30%", "20-25%", "20-35%", "50%+"],
        "Notes": [
            "Higher in advanced disease",
            "Includes procedural and health anxiety",
            "Most common psychiatric diagnosis",
            "Subthreshold distress requiring attention"
        ]
    }
    render_table(burden_data, "Psychological Morbidity in Indian Cancer Patients")
    
    render_key_concept("""
    **Risk Factors for Psychological Morbidity:**
    
    1. Advanced disease stage
    2. Uncontrolled pain
    3. Poor performance status
    4. Lack of social support
    5. Financial toxicity
    6. Late presentation
    """)
    
    render_summary("""
    India faces a growing cancer burden with distinct epidemiological patterns. Sociocultural factors including stigma, family dynamics, and traditional healing practices significantly influence cancer presentation and care. Psychological morbidity is substantial, with depression, anxiety, and adjustment disorders being the most common presentations.
    """)
    
    render_review_questions([
        "How does the epidemiology of cancer in India differ from Western countries?",
        "What sociocultural factors influence cancer presentation in Indian patients?",
        "What is the approximate prevalence of depression in Indian cancer patients?"
    ])

def render_chapter_1_3():
    """Chapter 1.3: Biopsychosocial Model in Oncology"""
    render_learning_objectives([
        "Explain the biopsychosocial model as applied to oncology",
        "Discuss how family systems operate in the Indian collectivist culture",
        "Describe the role of illness narratives and meaning-making in cancer adaptation"
    ])
    
    st.markdown("## 1.3 Biopsychosocial Model in Oncology")
    
    st.markdown("""
    The biopsychosocial model, articulated by George Engel in 1977, provides a comprehensive framework for understanding cancer that transcends purely biological explanations to encompass the full range of human experience.
    """)
    
    render_learning_objectives([
        "Explain the biopsychosocial model as applied to oncology",
        "Discuss how family systems operate in the Indian collectivist culture",
        "Describe the role of illness narratives and meaning-making in cancer adaptation"
    ])
    
    st.markdown("### Dimensions of the Biopsychosocial Model")
    
    dimensions_data = {
        "Dimension": ["Biological", "Psychological", "Social", "Spiritual/Existential"],
        "Key Considerations": [
            "Disease stage, treatment side effects, biological mechanisms",
            "Cognitive appraisals, emotional responses, coping styles",
            "Family relationships, social support, socioeconomic factors",
            "Meaning-making, religious beliefs, death anxiety"
        ]
    }
    render_table(dimensions_data)
    
    render_key_concept("""
    **Biological Dimension:**
    
    - Disease stage determines prognosis and treatment options
    - Treatment side effects (fatigue, pain, nausea, cognitive changes) have psychological consequences
    - Certain cancers (pancreatic, lung) show stronger associations with depression
    """)
    
    st.markdown("### 1.3.1 Family Systems and Collectivist Culture")
    
    st.markdown("""
    The family constitutes the primary unit of care in Indian society, and cancer is appropriately understood as a family diagnosis rather than an individual illness.
    """)
    
    st.markdown("**Family Roles in Cancer Care:**")
    
    family_data = {
        "Role": ["Practical Support", "Emotional Support", "Financial Support", "Decision-Making"],
        "Examples": [
            "Accompanying to appointments, managing medications, transportation",
            "Listening, comforting, encouraging",
            "Pooling resources, managing medical expenses",
            "Participating in treatment decisions"
        ]
    }
    render_table(family_data)
    
    render_clinical_tip("""
    **Cultural Consideration:**
    
    The family unit in India may include not only immediate relatives but also in-laws, clan elders, or community leaders whose opinions carry significant weight. Identifying key stakeholders is essential for effective communication.
    """)
    
    st.markdown("### 1.3.2 Illness Narratives and Meaning-Making")
    
    st.markdown("""
    Cancer disrupts the life narrative that individuals construct to make sense of their experiences and identity. Patients develop an "illness narrative" that helps them understand what is happening and what it means.
    """)
    
    narrative_data = {
        "Pattern": ["Restitution", "Chaos", "Quest"],
        "Description": [
            "Emphasize recovery and return to normal life",
            "Portray illness as overwhelming and incomprehensible",
            "Frame cancer as a journey leading to growth or insight"
        ]
    }
    render_table(narrative_data, "Common Narrative Patterns")
    
    render_key_concept("""
    **Indian Context:**
    
    Illness narratives are shaped by religious and philosophical traditions:
    
    - **Hindu concepts of karma**: Current suffering as consequence of past actions
    - **Divine will**: Illness as spiritual test
    - **Buddhist perspectives**: Impermanence and detachment
    
    These frameworks may provide comfort or generate distress depending on interpretation.
    """)
    
    render_summary("""
    The biopsychosocial model provides a comprehensive framework for understanding cancer that encompasses biological, psychological, social, and spiritual dimensions. In Indian culture, family systems play a central role in cancer care, with collectivist values shaping decision-making and support. Illness narratives help patients integrate cancer into their life story, with meaning-making influenced by religious and cultural frameworks.
    """)
    
    render_review_questions([
        "What are the four dimensions of the biopsychosocial model?",
        "How does the collectivist nature of Indian families influence cancer care?",
        "What are the three common narrative patterns in illness narratives?"
    ])

def render_chapter_2_1():
    """Chapter 2.1: Psychological Responses to Cancer Diagnosis"""
    render_learning_objectives([
        "Describe common emotional responses to cancer diagnosis",
        "Explain cultural variations in the expression of distress",
        "Differentiate normal from pathological responses to diagnosis"
    ])
    
    st.markdown("## 2.1 Psychological Responses to Cancer Diagnosis")
    
    st.markdown("""
    The diagnosis of cancer typically precipitates a crisis that triggers intense emotional responses. While these responses are highly variable across individuals, certain emotional reactions are sufficiently common to be considered characteristic.
    """)
    
    emotional_data = {
        "Response": ["Shock", "Denial", "Anger", "Fear", "Guilt"],
        "Clinical Features": [
            "Numbness, disbelief, sense of unreality, impaired processing",
            "Protective mechanism allowing gradual absorption of reality",
            "May be directed at cancer, healthcare system, family, or fate",
            "Pervasive; may concern disease, treatment, death, social consequences",
            "Self-blame for past behaviors, perceived moral failings, burden on family"
        ]
    }
    render_table(emotional_data, "Common Emotional Responses to Diagnosis")
    
    st.markdown("### 2.1.1 Cultural Expressions of Distress")
    
    st.markdown("""
    The expression of psychological distress is profoundly shaped by cultural norms. Indian culture, with its emphasis on emotional restraint, family privacy, and collective over individual expression, shapes how cancer-related distress is manifested.
    """)
    
    render_key_concept("""
    **Cultural Patterns in Distress Expression:**
    
    1. **Emotional restraint**: Cultural value of "sthithi" may lead to minimization
    2. **Somatization**: Body as culturally sanctioned medium for distress
    3. **Gender modulation**: Emotional expression may be more accepted from women
    4. **Religious expression**: Prayer, rituals, spiritual consultation
    """)
    
    st.markdown("### 2.1.2 Normal vs Pathological Responses")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Normal Response Characteristics:**")
        st.markdown("""
        - Intense but time-limited emotions
        - Gradual diminution over weeks to months
        - Maintenance of engagement with treatment
        - Ability to make use of support
        """)
    
    with col2:
        st.markdown("**Pathological Response Red Flags:**")
        st.markdown("""
        - Persistent inability to function
        - Meets criteria for psychiatric disorder
        - Expressed thoughts of self-harm or suicide
        - Self-neglect or treatment refusal
        """)
    
    render_case_study(
        "2.1.1",
        "Typical Initial Response",
        """
        **Patient:** 48-year-old businessman with newly diagnosed lung cancer
        
        **Response:** Intense shock and disbelief on first visit, unable to recall information given during consultation. Returned with wife 1 week later in better emotional state, with questions about treatment options.
        
        **Assessment:** Normal acute response to diagnosis
        
        **Management:** Supportive follow-up, clear communication, family involvement
        """
    )
    
    render_summary("""
    Cancer diagnosis triggers characteristic emotional responses including shock, denial, anger, fear, and guilt. Cultural norms shape how distress is expressed, with Indian patients often demonstrating emotional restraint and somatization. Normal responses are time-limited and improve with supportive care, while pathological responses require specific intervention.
    """)
    
    render_review_questions([
        "Describe the five common emotional responses to cancer diagnosis.",
        "How does Indian culture influence the expression of psychological distress?",
        "What are the red flags that suggest a normal response has become pathological?"
    ])

def render_chapter_2_2():
    """Chapter 2.2: Adjustment Disorders in Cancer Patients"""
    render_learning_objectives([
        "Describe the diagnostic criteria for adjustment disorders",
        "Identify common clinical presentations in cancer patients",
        "Outline evidence-based management strategies"
    ])
    
    st.markdown("## 2.2 Adjustment Disorders in Cancer Patients")
    
    st.markdown("""
    Adjustment disorders represent one of the most common psychiatric diagnoses in cancer populations, reflecting the significant psychological stress inherent in cancer diagnosis and treatment.
    """)
    
    render_learning_objectives([
        "Describe the diagnostic criteria for adjustment disorders",
        "Identify common clinical presentations in cancer patients",
        "Outline evidence-based management strategies"
    ])
    
    st.markdown("### 2.2.1 Diagnostic Criteria")
    
    st.markdown("""
    Adjustment disorders are characterized by emotional or behavioral symptoms in response to an identifiable stressor that develop within three months of the stressor's onset.
    """)
    
    subtypes_data = {
        "Subtype": [
            "With depressed mood",
            "With anxiety",
            "With mixed anxiety and depressed mood",
            "With disturbance of conduct"
        ],
        "Features": [
            "Sadness, tearfulness, feelings of hopelessness",
            "Nervousness, worry, jitteriness",
            "Both depressive and anxiety symptoms",
            "Behavioral problems, violation of norms"
        ]
    }
    render_table(subtypes_data, "DSM-5 Subtypes of Adjustment Disorder")
    
    render_key_concept("""
    **Diagnostic Criteria Requirements:**
    
    1. Identifiable stressor (cancer diagnosis, treatment, complications)
    2. Symptoms develop within 3 months of stressor onset
    3. Clinically significant distress or impairment
    4. Symptoms not persisting >6 months after stressor ends
    
    **Prevalence:** 15-35% of cancer patients
    """)
    
    st.markdown("### 2.2.2 Clinical Presentation")
    
    st.markdown("**With Depressed Mood:**")
    st.markdown("""
    - Persistent low mood and tearfulness
    - Pessimism about treatment outcomes
    - Sleep disturbance and appetite changes
    - Social withdrawal
    """)
    
    st.markdown("**With Anxiety:**")
    st.markdown("""
    - Excessive worry about prognosis and treatment
    - Somatic symptoms of anxiety (palpitations, sweating)
    - Reassurance-seeking behaviors
    - Sleep disturbance
    """)
    
    render_case_study(
        "2.2.1",
        "Adjustment Disorder with Depressed Mood",
        """
        **Patient:** 52-year-old school teacher with oral cavity cancer
        
        **Situation:** Post-surgical resection with significant facial disfigurement and speech difficulty
        
        **Symptoms:** Withdrawn, missed appointments, stated "there is no point in continuing"
        
        **Treatment:**
        - Supportive psychotherapy (8 sessions)
        - Grief work related to losses
        - Cognitive restructuring of catastrophic beliefs
        - Family involvement (wife joined sessions)
        
        **Outcome:** Returned to part-time teaching, mood improved substantially
        """
    )
    
    st.markdown("### 2.2.3 Management Strategies")
    
    management_data = {
        "Intervention": ["Supportive Psychotherapy", "Psychoeducation", "CBT Techniques", "Pharmacotherapy"],
        "Description": [
            "Therapeutic alliance, emotional validation, coping enhancement",
            "Understanding normal responses, expected course, treatment options",
            "Cognitive restructuring, behavioral activation, relaxation",
            "SSRIs/SNRIs for severe symptoms; benzodiazepines for acute anxiety"
        ]
    }
    render_table(management_data, "Management Components")
    
    render_clinical_tip("""
    **Stepped Care Approach:**
    
    1. **Mild**: Supportive counseling and psychoeducation
    2. **Moderate**: Structured psychotherapy (CBT, supportive therapy)
    3. **Severe**: Combination of psychotherapy and pharmacotherapy
    """)
    
    render_summary("""
    Adjustment disorders are characterized by emotional or behavioral symptoms in response to cancer-related stressors that cause significant distress or impairment. Clinical presentations vary and may include depressed mood, anxiety, or behavioral disturbances. Management involves supportive psychotherapy, psychoeducation, and potentially pharmacotherapy.
    """)
    
    render_review_questions([
        "What are the DSM-5 subtypes of adjustment disorder?",
        "How does adjustment disorder with depressed mood typically present in cancer patients?",
        "What are the key components of management for adjustment disorders?"
    ])

def render_chapter_2_3():
    """Chapter 2.3: Anxiety Disorders in Oncology"""
    render_learning_objectives([
        "Describe the spectrum of anxiety in cancer patients",
        "Identify specific anxiety disorders commonly encountered",
        "Implement evidence-based treatment approaches"
    ])
    
    st.markdown("## 2.3 Anxiety Disorders in Oncology")
    
    st.markdown("""
    Anxiety is among the most common psychological responses to cancer, occurring across the disease trajectory from diagnosis through survivorship or end-of-life care.
    """)
    
    render_learning_objectives([
        "Describe the spectrum of anxiety in cancer patients",
        "Identify specific anxiety disorders commonly encountered",
        "Implement evidence-based treatment approaches"
    ])
    
    st.markdown("### 2.3.1 Cancer-Related Anxiety")
    
    sources_data = {
        "Source": ["Disease-related", "Treatment-related", "Existential", "Social", "Practical/Financial"],
        "Examples": [
            "Fear of progression, recurrence, metastasis, death",
            "Worry about efficacy, side effects, procedural experiences",
            "Concerns about mortality, meaning, human existence",
            "Impact on relationships, work, social roles",
            "Treatment costs, employment impact, caregiving burden"
        ]
    }
    render_table(sources_data, "Sources of Cancer-Related Anxiety")
    
    render_key_concept("""
    **Fear of Cancer Recurrence:**
    
    - Most prevalent concern among cancer survivors (20-70%)
    - Associated with: younger age, greater symptom burden, lower quality of life
    - May persist for years after treatment completion
    - Interventions: CBT, mindfulness, meaning-making therapies
    """)
    
    st.markdown("### 2.3.2 Specific Anxiety Disorders")
    
    st.markdown("**Panic Disorder:**")
    st.markdown("""
    Cancer patients may experience spontaneous panic attacks triggered by physical sensations interpreted catastrophically or occurring de novo due to physiological stress.
    """)
    
    st.markdown("**Specific Phobias:**")
    phobias_data = {
        "Phobia": ["Needle Phobia", "Blood/Injury Fear", "Claustrophobia", "Dental Phobia"],
        "Relevance": ["Chemotherapy, blood draws", "Surgical procedures", "MRI scans", "Dental work for head/neck cancer"]
    }
    render_table(phobias_data)
    
    render_case_study(
        "2.3.1",
        "Panic Disorder with Agoraphobia",
        """
        **Patient:** 45-year-old housewife undergoing chemotherapy
        
        **Presentation:** Panic attack during second infusion, developed anticipatory anxiety
        
        **Symptoms:** Palpitations, breathlessness, dizziness, fear of dying
        
        **Course:** Avoided social situations, considered refusing treatment
        
        **Treatment:**
        - Psychoeducation about panic
        - Cognitive restructuring
        - Graduated exposure to chemotherapy setting
        - Relaxation techniques
        - Sertraline 50mg daily
        
        **Outcome:** Completed remaining chemotherapy with minimal distress
        """
    )
    
    st.markdown("### 2.3.3 Management Approaches")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Psychological Interventions:**")
        st.markdown("""
        - Cognitive-behavioral therapy
        - Exposure-based treatment for phobias
        - Relaxation training
        - Mindfulness-based interventions
        """)
    
    with col2:
        st.markdown("**Pharmacological Interventions:**")
        st.markdown("""
        - SSRIs as first-line for anxiety disorders
        - Benzodiazepines for acute symptom relief (short-term)
        - Careful consideration of drug interactions
        """)
    
    render_summary("""
    Anxiety in cancer patients encompasses a spectrum from adaptive responses to pathological anxiety disorders. Common presentations include generalized anxiety, panic disorder, specific phobias related to medical procedures, and illness anxiety. Management combines psychological interventions (particularly CBT) and pharmacotherapy (SSRIs, short-term benzodiazepines).
    """)
    
    render_review_questions([
        "What are the major sources of anxiety for cancer patients?",
        "How does panic disorder present in cancer patients?",
        "What are the key components of anxiety management in oncology?"
    ])

def render_chapter_2_4():
    """Chapter 2.4: Depression in Cancer"""
    render_learning_objectives([
        "Describe the diagnostic challenges in assessing depression in cancer patients",
        "Differentiate depression from cancer-related somatic symptoms",
        "Conduct suicide risk assessment in oncology patients"
    ])
    
    st.markdown("## 2.4 Depression in Cancer")
    
    st.markdown("""
    Depression is one of the most common and debilitating psychiatric complications of cancer, affecting an estimated 15 to 30 percent of patients.
    """)
    
    render_learning_objectives([
        "Describe the diagnostic challenges in assessing depression in cancer patients",
        "Differentiate depression from cancer-related somatic symptoms",
        "Conduct suicide risk assessment in oncology patients"
    ])
    
    st.markdown("### 2.4.1 Diagnostic Challenges")
    
    st.markdown("""
    The diagnosis of depression in cancer patients presents significant challenges that can lead to under-recognition and under-treatment.
    """)
    
    challenges_data = {
        "Challenge": ["Symptom Overlap", "Somatic Presentation", "Cultural Factors", "Attribution Bias"],
        "Description": [
            "Fatigue, sleep disturbance, appetite change common to both",
            "Indian patients often express distress somatically",
            "Emotional restraint may minimize reported suffering",
            "Clinicians may attribute symptoms to cancer rather than depression"
        ]
    }
    render_table(challenges_data, "Diagnostic Challenges")
    
    render_key_concept("""
    **Strategies for Improved Diagnosis:**
    
    1. **Emphasize psychological symptoms**: mood, anhedonia, guilt, worthlessness, hopelessness, suicidal ideation
    2. **Consider symptom timing**: predating cancer or disproportionate to disease stage
    3. **Use collateral information**: family perspective on baseline functioning
    4. **Screen systematically**: use validated tools
    """)
    
    st.markdown("### 2.4.2 Differentiating Depression from Cancer-Related Somatic Symptoms")
    
    st.markdown("**Symptoms Suggestive of Depression:**")
    
    diff_data = {
        "Symptom": ["Sleep Disturbance", "Appetite Change", "Fatigue", "Cognitive Complaints"],
        "Depressive Features": [
            "Early morning awakening (2+ hours before desired time)",
            "Significant decrease with weight loss not explained by cancer",
            "Overwhelming exhaustion not relieved by rest, impairing all domains",
            "Subjective complaints disproportionate to objective findings"
        ]
    }
    render_table(diff_data, "Differentiating Features")
    
    st.markdown("### 2.4.3 Suicide Risk Assessment")
    
    st.markdown("""
    Cancer patients face elevated suicide risk (2-3 times general population). Systematic assessment is essential.
    """)
    
    risk_factors_data = {
        "Category": ["Psychiatric", "Medical", "Social", "Demographic"],
        "Factors": [
            "Depression, prior suicide attempt",
            "Advanced disease, uncontrolled pain, functional decline",
            "Social isolation, inadequate support",
            "Male gender, older age"
        ]
    }
    render_table(risk_factors_data, "Suicide Risk Factors")
    
    render_warning("""
    **Assessment Components:**
    
    1. Frequency, duration, and intensity of suicidal ideation
    2. Presence of plans for how suicide would be accomplished
    3. Access to means
    4. Any intent to act on ideation
    5. Protective factors and reasons for living
    6. History of prior suicide attempts
    """)
    
    render_case_study(
        "2.4.1",
        "Depression with Passive Suicidal Ideation",
        """
        **Patient:** 58-year-old businessman with metastatic lung cancer
        
        **Presentation:** Referred after stating "I don't want to live like this anymore"
        
        **History:** 6-week progressive mood decline, poor prognosis, smoking-related guilt
        
        **Assessment:** Major depressive disorder, passive suicidal ideation, no plan/intent
        
        **Treatment:**
        - Supportive psychotherapy
        - Cognitive therapy for guilt and all-or-nothing thinking
        - Sertraline initiated
        - Safety planning with family
        
        **Outcome:** Mood improved gradually, engaged with family, died peacefully 3 months later
        """
    )
    
    render_summary("""
    Depression diagnosis in cancer patients is complicated by symptom overlap with cancer and treatment effects. Psychological symptoms such as guilt, worthlessness, and suicidal ideation are particularly valuable for diagnosis. Suicide risk is elevated in cancer patients and requires systematic assessment. Management combines psychotherapy and pharmacotherapy.
    """)
    
    render_review_questions([
        "What are the main diagnostic challenges in assessing depression in cancer patients?",
        "How would you differentiate depressive fatigue from cancer-related fatigue?",
        "What are the key components of suicide risk assessment in oncology patients?"
    ])

def render_chapter_2_5():
    """Chapter 2.5: Delirium and Neuropsychiatric Syndromes"""
    render_learning_objectives([
        "Describe the clinical features and causes of delirium in cancer patients",
        "Identify neuropsychiatric complications of cancer and its treatment",
        "Outline management approaches for delirium"
    ])
    
    st.markdown("## 2.5 Delirium and Neuropsychiatric Syndromes")
    
    st.markdown("""
    Delirium is the most common neuropsychiatric complication of advanced cancer, affecting an estimated 25 to 40 percent of hospitalized cancer patients and up to 85 percent in the terminal phase.
    """)
    
    render_learning_objectives([
        "Describe the clinical features and causes of delirium in cancer patients",
        "Identify neuropsychiatric complications of cancer and its treatment",
        "Outline management approaches for delirium"
    ])
    
    st.markdown("### 2.5.1 Delirium in Advanced Cancer")
    
    st.markdown("**Clinical Features:**")
    
    features_data = {
        "Domain": ["Core", "Cognitive", "Psychomotor", "Circadian"],
        "Features": [
            "Disturbance in attention and awareness",
            "Disorientation, memory impairment, language disturbance, perceptual disturbances",
            "Hyperactive (agitation), hypoactive (lethargy), or mixed",
            "Symptoms fluctuate throughout the day"
        ]
    }
    render_table(features_data)
    
    st.markdown("**Causes in Cancer Patients (typically multifactorial):**")
    causes = [
        "Medications (opioids, benzodiazepines, anticholinergics, corticosteroids)",
        "Metabolic disturbances (electrolyte abnormalities, hepatic/renal failure)",
        "Infection",
        "Hypoxia",
        "Dehydration and nutritional deficiencies",
        "Brain metastases or leptomeningeal disease"
    ]
    for cause in causes:
        st.markdown(f"- {cause}")
    
    render_key_concept("""
    **Delirium Subtypes:**
    
    1. **Hyperactive**: Agitation, restlessness, hallucinations, attempts to remove devices
    2. **Hypoactive**: Reduced motor activity, lethargy, decreased responsiveness (more common, often under-recognized)
    3. **Mixed**: Fluctuations between hyperactive and hypoactive states
    """)
    
    st.markdown("### 2.5.2 Brain Metastases and Paraneoplastic Syndromes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Brain Metastases:**")
        st.markdown("""
        - Occur in 20-40% of cancer patients
        - Higher rates in lung, breast, melanoma
        - Psychiatric symptoms: personality change, emotional lability, depression, psychosis, cognitive impairment
        - Any new psychiatric symptom warrants neurological evaluation
        """)
    
    with col2:
        st.markdown("**Paraneoplastic Syndromes:**")
        st.markdown("""
        - Remote effects of cancer via immune mechanisms
        - Can affect any part of nervous system
        - Psychiatric presentations: psychosis, depression, cognitive impairment
        - May precede cancer diagnosis
        """)
    
    st.markdown("### 2.5.3 Chemotherapy-Related Cognitive Impairment")
    
    st.markdown("""
    Cognitive impairment associated with cancer and its treatments ("chemo brain") affects an estimated 15 to 75 percent of cancer patients.
    """)
    
    chemo_features = {
        "Domain": ["Attention", "Processing Speed", "Working Memory", "Executive Function"],
        "Deficit": ["Concentration difficulties", "Slowed thinking", "Memory problems", "Planning/organization difficulties"]
    }
    render_table(chemo_features, "Cognitive Domains Affected")
    
    st.markdown("**Contributing Factors:**")
    factors = [
        "Direct neurotoxic effects of chemotherapy",
        "Hormonal therapies (particularly breast cancer)",
        "Radiation therapy to the brain",
        "Fatigue, sleep disturbance, depression, anxiety",
        "Supportive medications (benzodiazepines, opioids)"
    ]
    for factor in factors:
        st.markdown(f"- {factor}")
    
    render_clinical_tip("""
    **Management of Cognitive Impairment:**
    
    1. Address modifiable contributing factors
    2. Cognitive rehabilitation strategies
    3. External memory aids and compensatory strategies
    4. Lifestyle interventions (exercise, stress management)
    5. Psychostimulants for persistent, functionally significant impairment
    """)
    
    render_summary("""
    Delirium is the most common neuropsychiatric complication in advanced cancer, presenting with attention deficits, cognitive impairment, and psychomotor changes. Causes are typically multifactorial. Brain metastases and paraneoplastic syndromes can also produce psychiatric symptoms. Chemotherapy-related cognitive impairment affects many patients and requires multimodal management.
    """)
    
    render_review_questions([
        "What are the core clinical features of delirium?",
        "List the common causes of delirium in cancer patients.",
        "What is the difference between hyperactive and hypoactive delirium?"
    ])

def render_chapter_3_1():
    """Chapter 3.1: Psychiatric Assessment of the Cancer Patient"""
    render_learning_objectives([
        "Adapt psychiatric history-taking to the medical context",
        "Perform mental status examination in cancer patients",
        "Conduct capacity assessment"
    ])
    
    st.markdown("## 3.1 Psychiatric Assessment of the Cancer Patient")
    
    st.markdown("""
    Psychiatric assessment of the cancer patient requires adaptation of standard psychiatric history-taking to accommodate the medical context.
    """)
    
    render_learning_objectives([
        "Adapt psychiatric history-taking to the medical context",
        "Perform mental status examination in cancer patients",
        "Conduct capacity assessment"
    ])
    
    st.markdown("### 3.1.1 History Taking in Medically Ill Patients")
    
    st.markdown("**Essential Components:**")
    
    history_data = {
        "Component": ["Current Medical Situation", "History of Present Illness", "Past Psychiatric History", "Family Psychiatric History", "Social History", "Medication Review"],
        "Considerations": [
            "Type and stage of cancer, current treatment, prognosis",
            "Onset, duration, course of symptoms, relationship to medical events",
            "Prior episodes, treatment, outcomes",
            "Psychiatric conditions in family members, family dynamics",
            "Living situation, support network, occupation, cultural/religious background",
            "Psychiatric side effects, drug interactions"
        ]
    }
    render_table(history_data)
    
    st.markdown("**Medication Review Priorities:**")
    meds = [
        "Corticosteroids (mood elevation, depression, psychosis)",
        "Anti-emetics (5-HT3 antagonists and depression)",
        "Analgesics (opioid effects)",
        "Sedatives (benzodiazepine effects)"
    ]
    for med in meds:
        st.markdown(f"- {med}")
    
    st.markdown("### 3.1.2 Mental Status Examination Adaptations")
    
    mse_data = {
        "Domain": ["Appearance", "Behavior", "Mood/Affect", "Thought Content", "Thought Process", "Cognition", "Insight/Judgment"],
        "Assessment Focus": [
            "Signs of illness, nutritional status, self-care, physical stigmata",
            "Agitation, retardation, engagement with examiner",
            "Emotional state, range, reactivity, appropriateness",
            "Suicidal ideation, homicidal ideation, delusions, preoccupations",
            "Organization, coherence, rate",
            "Consciousness, attention, orientation, memory, higher functions",
            "Understanding of psychiatric condition, decision-making capacity"
        ]
    }
    render_table(mse_data, "Mental Status Examination Adaptations")
    
    st.markdown("### 3.1.3 Capacity and Competence Assessment")
    
    st.markdown("""
    Decision-making capacity is a central concern in psycho-oncology. Capacity is decision-specific, time-specific, and can fluctuate.
    """)
    
    render_key_concept("""
    **Abilities Required for Capacity:**
    
    1. **Understanding** - Ability to comprehend information relevant to the decision
    2. **Appreciation** - Ability to recognize how information applies to one's own situation
    3. **Reasoning** - Ability to weigh options in a logical manner
    4. **Communication** - Ability to communicate a choice
    
    **Clinical Considerations:**
    - Cognitive impairment from metastases, metabolic disturbances, or medications
    - Psychiatric disorders impairing reasoning (severe depression, psychosis)
    - Emotional stress affecting judgment
    - These factors do not automatically render a patient incapable
    """)
    
    render_summary("""
    Psychiatric assessment of cancer patients requires comprehensive history-taking adapted to the medical context, including detailed medication review. Mental status examination should attend to features specific to the cancer population. Capacity assessment examines understanding, appreciation, reasoning, and communication abilities.
    """)
    
    render_review_questions([
        "What components are essential in the history of a cancer patient with psychiatric symptoms?",
        "How does the mental status examination differ for cancer patients?",
        "What four abilities are required for decision-making capacity?"
    ])

def render_chapter_3_2():
    """Chapter 3.2: Screening Tools in Psycho-Oncology"""
    render_learning_objectives([
        "Describe commonly used screening tools in psycho-oncology",
        "Select appropriate screening tools for different clinical situations",
        "Interpret screening tool results appropriately"
    ])
    
    st.markdown("## 3.2 Screening Tools in Psycho-Oncology")
    
    render_learning_objectives([
        "Describe commonly used screening tools in psycho-oncology",
        "Select appropriate screening tools for different clinical situations",
        "Interpret screening tool results appropriately"
    ])
    
    st.markdown("### 3.2.1 Distress Thermometer")
    
    st.markdown("""
    The Distress Thermometer (DT) is a simple visual analog scale (0-10) for identifying cancer patients experiencing clinically significant distress.
    """)
    
    dt_features = {
        "Feature": ["Format", "Administration Time", "Cutoff", "Companion Tool"],
        "Value": ["Visual analog scale (0-10)", "~1 minute", "≥4", "Problem list"]
    }
    render_table(dt_features, "Distress Thermometer Features")
    
    st.markdown("**Problem List Domains:**")
    domains = [
        "Practical problems",
        "Family problems", 
        "Emotional problems",
        "Spiritual/religious concerns",
        "Physical problems"
    ]
    for domain in domains:
        st.markdown(f"- {domain}")
    
    render_clinical_tip("""
    **Limitations of DT:**
    
    - Single global measure, cannot distinguish types of distress
    - Screening tool, not diagnostic
    - Cultural factors may influence responses (under-reporting due to emotional restraint)
    """)
    
    st.markdown("### 3.2.2 PHQ-9, GAD-7, and HADS")
    
    render_screening_tools_summary()
    
    st.markdown("""
    **PHQ-9 (Patient Health Questionnaire-9):**
    - Assesses depressive symptoms over preceding two weeks
    - Items correspond to DSM criteria for major depression
    - Good sensitivity and specificity in medical populations
    - Limitation: Somatic items may be confounded by cancer symptoms
    
    **GAD-7 (Generalized Anxiety Disorder-7):**
    - Assesses anxiety symptoms over preceding two weeks
    - Developed for GAD but reasonable for other anxiety disorders
    - Brief and well-validated
    
    **HADS (Hospital Anxiety and Depression Scale):**
    - Designed specifically for medical populations
    - Excludes somatic symptoms to reduce confounding
    - Particularly useful for cancer populations
    - Hindi and other Indian language versions available
    """)
    
    st.markdown("### 3.2.3 Tools Validated in Indian Populations")
    
    st.markdown("""
    While many screening tools have been developed in Western populations, their applicability to Indian settings requires local validation.
    """)
    
    india_validation = {
        "Tool": ["PHQ-9", "HADS", "WHODAS 2.0"],
        "Status": ["Validated in primary care", "Used in Indian cancer populations", "Validated in Indian settings"],
        "Languages": ["Hindi and other Indian languages", "Hindi", "Multiple Indian languages"]
    }
    render_table(india_validation, "Tools Validated in Indian Populations")
    
    render_summary("""
    Several validated screening tools are available for psycho-oncology, including the Distress Thermometer, PHQ-9, GAD-7, and HADS. The HADS is particularly useful in cancer populations due to exclusion of somatic symptoms. Several tools have been validated in Indian populations.
    """)
    
    render_review_questions([
        "What is the cutoff score for the Distress Thermometer?",
        "Why is the HADS particularly useful for cancer populations?",
        "What are the limitations of the PHQ-9 in cancer patients?"
    ])

def render_chapter_3_3():
    """Chapter 3.3: Communication Skills in Oncology Settings"""
    render_learning_objectives([
        "Apply the SPIKES protocol for breaking bad news",
        "Navigate issues of collusion and nondisclosure",
        "Adapt communication to the Indian cultural context"
    ])
    
    st.markdown("## 3.3 Communication Skills in Oncology Settings")
    
    st.markdown("""
    Breaking bad news is one of the most challenging communication tasks in oncology. The SPIKES protocol provides a structured framework.
    """)
    
    render_learning_objectives([
        "Apply the SPIKES protocol for breaking bad news",
        "Navigate issues of collusion and nondisclosure",
        "Adapt communication to the Indian cultural context"
    ])
    
    render_spiKES()
    
    st.markdown("**Cultural Adaptations for India:**")
    adaptations = [
        "Clarify patient preferences regarding family involvement",
        "Some patients prefer family involvement in discussions",
        "Provide family members advance warning when appropriate",
        "Address practical concerns including costs and logistics"
    ]
    for adaptation in adaptations:
        st.markdown(f"- {adaptation}")
    
    st.markdown("### 3.3.1 Handling Collusion and Nondisclosure")
    
    st.markdown("""
    Collusion—agreement between family members and healthcare providers to withhold information from the patient—represents a significant challenge in Indian oncology settings.
    """)
    
    render_key_concept("""
    **Rationale for Nondisclosure in Indian Contexts:**
    
    - Protecting patient from emotional distress
    - Belief that knowing the diagnosis will devastate the patient
    - Cultural values of family protection and respect for elders
    - Concerns about taking away hope
    """)
    
    st.markdown("**Approaches to Managing Collusion:**")
    approaches = [
        "Acknowledge family's loving intentions",
        "Explore patient's likely preferences",
        "Consider graduated disclosure approach",
        "Respect patient autonomy while acknowledging cultural realities",
        "Conduct private conversation with patient to assess preferences"
    ]
    for approach in approaches:
        st.markdown(f"- {approach}")
    
    render_clinical_tip("""
    **Graduated Disclosure Approach:**
    
    1. Acknowledge seriousness without immediate full disclosure
    2. Provide information as patient indicates readiness
    3. Allow patient to guide depth of information desired
    4. Work with families to develop disclosure plans
    5. Provide ongoing support throughout the process
    """)
    
    render_summary("""
    The SPIKES protocol provides a structured approach to breaking bad news, with adaptations needed for the Indian cultural context. Collusion and nondisclosure are common challenges that require sensitivity, acknowledgment of family's loving intentions, and graduated approaches that respect patient autonomy.
    """)
    
    render_review_questions([
        "What does each letter in the SPIKES acronym stand for?",
        "What are common reasons for nondisclosure in Indian families?",
        "How would you approach a family that requests you not disclose a cancer diagnosis to their loved one?"
    ])

def render_chapter_4_1():
    """Chapter 4.1: Principles of Psychopharmacology in Oncology"""
    render_learning_objectives([
        "Describe principles of drug-drug interactions in cancer patients",
        "Consider organ dysfunction in medication selection",
        "Adapt route of administration to patient needs"
    ])
    
    st.markdown("## 4.1 Principles of Psychopharmacology in Oncology")
    
    render_learning_objectives([
        "Describe principles of drug-drug interactions in cancer patients",
        "Consider organ dysfunction in medication selection",
        "Adapt route of administration to patient needs"
    ])
    
    st.markdown("### 4.1.1 Drug-Drug Interactions")
    
    st.markdown("""
    Psychopharmacology in cancer patients requires careful attention to drug-drug interactions that may affect efficacy or safety.
    """)
    
    interaction_types = {
        "Type": ["Pharmacokinetic", "Pharmacodynamic"],
        "Description": [
            "Effects on absorption, distribution, metabolism, excretion",
            "Additive or antagonistic effects"
        ],
        "Example": [
            "CYP450 interactions affecting drug levels",
            "CNS depression from combining sedatives"
        ]
    }
    render_table(interaction_types, "Types of Drug Interactions")
    
    render_key_concept("""
    **Key Pharmacokinetic Interactions:**
    
    - CYP2D6 inhibitors (fluoxetine, paroxetine) can reduce tamoxifen efficacy
    - Sertraline and citalopram have less significant CYP interactions
    - Many chemotherapeutic agents and psychotropics share metabolic pathways
    
    **Key Pharmacodynamic Interactions:**
    
    - Additive CNS depression with combined sedatives
    - Serotonin syndrome risk with serotonergic psychotropics + ondansetron, tramadol, linezolid
    """)
    
    st.markdown("### 4.1.2 Organ Dysfunction Considerations")
    
    st.markdown("""
    Organ dysfunction is common in cancer patients and significantly affects pharmacokinetics.
    """)
    
    organ_data = {
        "Dysfunction": ["Hepatic", "Renal", "Bone Marrow Suppression"],
        "Impact": [
            "Most psychotropics undergo hepatic metabolism; clearance reduced",
            "Lithium renally excreted, requires dose adjustment; gabapentin/pregabalin need reduction",
            "Mirtazapine can cause neutropenia; clozapine carries hematologic risks"
        ],
        "Management": [
            "Start at lower doses, titrate cautiously",
            "Careful dose adjustment and monitoring",
            "Weigh risks against benefits"
        ]
    }
    render_table(organ_data)
    
    st.markdown("### 4.1.3 Route of Administration Issues")
    
    st.markdown("""
    Cancer patients may have impaired ability to take oral medications due to nausea, vomiting, dysphagia, or gastrointestinal obstruction.
    """)
    
    route_data = {
        "Route": ["Intravenous", "Intramuscular", "Sublingual/Buccal", "Rectal"],
        "Available Medications": [
            "Haloperidol, olanzapine, aripiprazole, lorazepam, midazolam",
            "Haloperidol, olanzapine, aripiprazole, benzodiazepines",
            "Lorazepam, buprenorphine, olanzapine",
            "Diazepam (gel)"
        ],
        "Considerations": [
            "Rapid onset; requires IV access",
            "May be painful; absorption varies",
            "Bypasses first-pass metabolism",
            "Absorption variable"
        ]
    }
    render_table(route_data, "Alternative Routes of Administration")
    
    render_clinical_tip("""
    **Clinical Pearls:**
    
    - Lorazepam is preferred for IM/IV due to reliable absorption
    - Olanzapine can be given sublingually for rapid effect
    - Haloperidol remains first-line for delirium when QTc allows
    - Always consider potential interactions with chemotherapy agents
    """)
    
    render_summary("""
    Psychopharmacology in cancer patients requires attention to drug-drug interactions (both pharmacokinetic and pharmacodynamic), organ dysfunction (hepatic and renal), and route of administration issues. Choice of psychotropic medications must consider these factors along with cancer treatments the patient is receiving.
    """)
    
    render_review_questions([
        "What type of interaction can occur when fluoxetine is given with tamoxifen?",
        "Which psychotropic drug requires the most careful dose adjustment in renal impairment?",
        "What are the alternative routes of administration for psychotropic medications?"
    ])

def render_chapter_5_1():
    """Chapter 5.1: Supportive Psychotherapy in Oncology"""
    render_learning_objectives([
        "Describe principles of supportive psychotherapy in oncology",
        "Apply specific techniques used in supportive therapy",
        "Recognize when supportive therapy is indicated"
    ])
    
    st.markdown("## 5.1 Supportive Psychotherapy in Oncology")
    
    st.markdown("""
    Supportive psychotherapy is the most widely used psychotherapeutic approach for cancer patients, focusing on strengthening the therapeutic relationship, reducing symptoms, improving coping, and enhancing quality of life.
    """)
    
    render_learning_objectives([
        "Describe principles of supportive psychotherapy in oncology",
        "Apply specific techniques used in supportive therapy",
        "Recognize when supportive therapy is indicated"
    ])
    
    st.markdown("### 5.1.1 Principles of Supportive Therapy")
    
    principles_data = {
        "Principle": ["Therapeutic Alliance", "Emotional Support", "Coping Enhancement", "Present Focus", "Active/Directive Role"],
        "Description": [
            "Maintaining strong, collaborative relationship",
            "Providing validation and empathy",
            "Strengthening adaptive coping resources",
            "Addressing current functioning rather than past experiences",
            "Offering encouragement, advice, and practical assistance"
        ]
    }
    render_table(principles_data)
    
    st.markdown("### 5.1.2 Specific Techniques")
    
    techniques = [
        "**Active listening and validation:** Communicating understanding and acceptance",
        "**Exploration of feelings:** Helping patients identify and express emotions",
        "**Psychoeducation:** Providing information about normal responses and coping strategies",
        "**Problem-solving assistance:** Helping define problems and generate solutions",
        "**Cognitive techniques:** Gently challenging maladaptive thought patterns"
    ]
    for technique in techniques:
        st.markdown(f"- {technique}")
    
    render_key_concept("""
    **Clinical Indications:**
    
    - Adjustment disorders
    - Mild to moderate distress
    - Patients with limited time/energy
    - When the primary challenges are situational rather than characterological
    
    **Session Structure:**
    
    - Time-limited (typically 6-12 sessions)
    - Focused on concrete goals identified collaboratively
    - Frequency adjusted to patient needs
    """)
    
    render_case_study(
        "5.1.1",
        "Supportive Therapy in Action",
        """
        **Patient:** 65-year-old woman with metastatic breast cancer
        
        **Presenting Problem:** Distress related to impending dependency, worry about burdening family
        
        **Supportive Therapy Approach:**
        - Active listening and validation of her fears
        - Exploration of her feelings about loss of independence
        - Cognitive work on reframing dependence as allowing family to give
        - Problem-solving practical concerns
        - Involvement of family in selected sessions
        
        **Outcome:** Reduced distress, improved family communication, greater peace about prognosis
        """
    )
    
    render_summary("""
    Supportive psychotherapy is the cornerstone of psycho-oncology treatment, focusing on the therapeutic relationship, emotional support, coping enhancement, and present-focused problem-solving. Techniques include active listening, validation, psychoeducation, and cognitive interventions. This approach is appropriate for most cancer patients with psychological distress.
    """)
    
    render_review_questions([
        "What are the core principles of supportive psychotherapy?",
        "What techniques are used in supportive therapy?",
        "When is supportive therapy particularly indicated?"
    ])

def render_chapter_6_1():
    """Chapter 6.1: Depression vs Demoralization in Advanced Cancer"""
    render_learning_objectives([
        "Differentiate depression from demoralization in advanced cancer",
        "Describe assessment and management of desire for death",
        "Address existential distress in terminal illness"
    ])
    
    st.markdown("## 6.1 Depression vs Demoralization in Advanced Cancer")
    
    render_learning_objectives([
        "Differentiate depression from demoralization in advanced cancer",
        "Describe assessment and management of desire for death",
        "Address existential distress in terminal illness"
    ])
    
    st.markdown("""
    The distinction between depression and demoralization is particularly important in advanced cancer, as they may require different treatment approaches.
    """)
    
    comparison_data = {
        "Feature": ["Core Symptoms", "Guilt", "Pleasure Capacity", "Hopelessness", "Treatment Response"],
        "Depression": [
            "Pervasive low mood, anhedonia",
            "Excessive, inappropriate",
            "Anhedonia (loss)",
            "About self and future",
            "Antidepressants effective"
        ],
        "Demoralization": [
            "Helplessness, loss of confidence",
            "May be present but not primary",
            "Often preserved",
            "About situation being intolerable",
            "Better response to existential therapies"
        ]
    }
    render_table(comparison_data, "Depression vs Demoralization")
    
    st.markdown("**Demoralization Components:**")
    components = [
        "**Helplessness:** Sense of being unable to influence one's situation",
        "**Hopelessness:** Belief that things will not improve",
        "**Entrapment:** Feeling of having no way out",
        "**Shame/guilt:** Related to perceived failure",
        "**Existential distress:** Questioning meaning of life and suffering"
    ]
    for component in components:
        st.markdown(f"- {component}")
    
    render_case_study(
        "6.1.1",
        "Demoralization vs Depression",
        """
        **Patient:** 68-year-old retired school principal with metastatic ovarian cancer
        
        **Presentation:** Referred for "depression," withdrawn, expressed desire to die
        
        **Assessment Findings:**
        - Not pervasive depressed mood
        - Capacity for pleasure retained (enjoyed grandchildren visits)
        - Core distress: loss of purpose and meaning
        - Felt "useless" and "a burden"
        
        **Diagnosis:** Demoralization rather than major depression
        
        **Treatment:**
        - Meaning-making work
        - Reframing dependence as opportunity for family to give
        - Dignity therapy for legacy creation
        - No antidepressants needed
        
        **Outcome:** Found renewed meaning, died peacefully "at peace"
        """
    )
    
    st.markdown("### 6.1.1 Desire for Death")
    
    st.markdown("""
    Desire for death in cancer patients ranges from passive death wishes to serious suicidal ideation.
    """)
    
    assessment_components = [
        "1. **Explore the desire:** 'What do you mean when you say you want to die?'",
        "2. **Assess contributing factors:** Uncontrolled symptoms, depression, existential distress",
        "3. **Evaluate risk:** Presence of plan, means, intent, past attempts",
        "4. **Identify protective factors:** Reasons for living, family support, religious beliefs"
    ]
    for component in assessment_components:
        st.markdown(component)
    
    render_clinical_tip("""
    **Management of Desire for Death:**
    
    - Treat reversible causes (pain, depression, delirium)
    - Provide symptomatic relief and palliative sedation if needed
    - Existential and spiritual support
    - Honest discussion about fears and concerns
    - Maintain hope for comfort even when cure is not possible
    """)
    
    render_summary("""
    Depression and demoralization are distinct syndromes that require different treatment approaches. Depression responds to antidepressants while demoralization responds better to existential therapies. Desire for death requires careful assessment of contributing factors and risk. Existential distress in terminal cancer involves confrontation with fundamental questions about meaning and mortality.
    """)
    
    render_review_questions([
        "How does demoralization differ from depression in advanced cancer?",
        "What are the key components of desire for death assessment?",
        "What existential concerns are common in terminal cancer?"
    ])

def render_chapter_6_2():
    """Chapter 6.2: Grief, Bereavement, and Complicated Grief"""
    render_learning_objectives([
        "Describe the course of normal grief",
        "Identify features of complicated grief",
        "Understand cultural mourning practices in India"
    ])
    
    st.markdown("## 6.2 Grief, Bereavement, and Complicated Grief")
    
    st.markdown("""
    Grief is a natural response to loss, and the death of a loved one to cancer is one of the most profound losses a person can experience.
    """)
    
    render_learning_objectives([
        "Describe the course of normal grief",
        "Identify features of complicated grief",
        "Understand cultural mourning practices in India"
    ])
    
    st.markdown("### 6.2.1 Normal vs Pathological Grief")
    
    st.markdown("**Normal Grief Features:**")
    
    phases_data = {
        "Phase": ["Acute Grief", "Transition", "Integration"],
        "Duration": ["Weeks to months", "Months to years", "Ongoing"],
        "Characteristics": [
            "Intense emotional pain, yearning, preoccupation, functional impairment",
            "Gradual diminution of pain, integration of loss",
            "Ability to move forward while maintaining connection to deceased"
        ]
    }
    render_table(phases_data)
    
    st.markdown("**Symptoms of Normal Grief:**")
    symptoms = [
        "Waves of grief triggered by reminders",
        "Physical symptoms (sleep disturbance, appetite change, fatigue)",
        "Cognitive difficulties (concentration, decision-making)",
        "Social withdrawal"
    ]
    for symptom in symptoms:
        st.markdown(f"- {symptom}")
    
    st.markdown("**Complicated Grief (Prolonged Grief Disorder):**")
    complicated = [
        "Persistent, severe grief not showing expected improvement",
        "Duration beyond expected norms (typically 6-12 months)",
        "Symptoms: persistent yearning, preoccupation, difficulty accepting death, bitterness, inability to envision future"
    ]
    for item in complicated:
        st.markdown(f"- {item}")
    
    render_key_concept("""
    **Risk Factors for Complicated Grief:**
    
    - Sudden or violent death
    - Ambivalent or dependent relationship
    - Multiple recent losses
    - History of depression or anxiety
    - Inadequate social support
    - Traumatic aspects of dying process
    - Parents losing children, spouses losing partners, suicide bereavement
    """)
    
    st.markdown("### 6.2.2 Cultural Mourning Practices in India")
    
    st.markdown("""
    India is characterized by extraordinary cultural and religious diversity, and mourning practices vary correspondingly across communities.
    """)
    
    practices_data = {
        "Tradition": ["Hindu", "Muslim", "Christian"],
        "Death Understanding": [
            "Transition (mrityu), soul continues journey",
            "Return to God",
            "Varies by denomination"
        ],
        "Key Practices": [
            "Cremation, 10-13 day impurity period, annual ancestor rites (shraddha)",
            "Prompt burial, washing (ghusl), shrouding (kafan), 40-day mourning (iddah)",
            "Wake services, funeral liturgies, memorial services"
        ]
    }
    render_table(practices_data, "Cultural Mourning Practices")
    
    render_clinical_tip("""
    **Psychological Significance of Rituals:**
    
    - Structured opportunities for expression of grief
    - Concrete actions for bereaved to perform
    - Community support through visits, meals, shared mourning
    - Collective rather than individual experience
    
    **Potential Challenges:**
    
    - Collective mourning may overshadow individual grief
    - Expectations of emotional restraint may discourage expression
    - Widows may face particular social vulnerabilities
    """)
    
    render_summary("""
    Normal grief progresses from acute grief through transition to integration. Complicated grief persists beyond expected norms and causes significant impairment. Indian cultural and religious traditions provide structured rituals for mourning that serve important psychological functions, though attention to individual needs within cultural frameworks remains important.
    """)
    
    render_review_questions([
        "What are the phases of normal grief?",
        "What are the risk factors for complicated grief?",
        "What psychological functions do cultural mourning rituals serve?"
    ])

def render_quick_reference():
    """Render quick reference materials"""
    st.markdown("""
    <div class="chapter-header">
        <h2 style="margin: 0;">📚 Quick Reference Materials</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Screening Tools Summary")
    render_screening_tools_summary()
    
    st.markdown("---")
    
    st.markdown("## SPIKES Protocol")
    render_spiKES()
    
    st.markdown("---")
    
    st.markdown("## Emergency Resources")
    render_emergency_resources()
    
    st.markdown("---")
    
    st.markdown("## Key Psychotropic Medications")
    
    meds_data = {
        "Class": ["SSRIs", "SNRIs", "Benzodiazepines", "Antipsychotics"],
        "Common Agents": [
            "Sertraline, citalopram, escitalopram",
            "Venlafaxine, duloxetine",
            "Lorazepam, clonazepam",
            "Haloperidol, olanzapine, quetiapine"
        ],
        "Key Considerations": [
            "First-line for depression/anxiety; fewer drug interactions",
            "Useful for neuropathic pain + depression",
            "Short-term for acute anxiety; risk of falls, delirium",
            "Delirium management; antiemetic properties"
        ]
    }
    render_table(meds_data, "Key Psychotropic Medications in Oncology")

def main():
    """Main application function"""
    
    # Sidebar navigation
    st.sidebar.markdown("""
    <div class="main-header" style="padding: 1rem; margin-bottom: 1rem;">
        <h3 style="margin: 0; font-size: 1.2rem;">📖 Navigation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Create navigation sections
    for section_title, chapters in navigation_data.items():
        st.sidebar.markdown(f"**{section_title}**")
        
        for chapter_id, chapter_title in chapters.items():
            # Create button-like navigation
            button_key = f"nav_{chapter_id}"
            if st.sidebar.button(
                f"   {chapter_id}: {chapter_title}",
                key=button_key,
                help=f"Go to {chapter_title}"
            ):
                st.session_state.current_section = chapter_id
        
        st.sidebar.markdown("---")
    
    # Add search functionality
    st.sidebar.markdown("### 🔍 Search")
    search_query = st.sidebar.text_input("Search topics...", placeholder="e.g., depression, delirium...")
    
    if search_query:
        st.sidebar.markdown(f"**Results for '{search_query}':**")
        st.sidebar.info("Search functionality would filter content here. For now, use navigation to find specific topics.")
    
    # Main content area
    render_header()
    
    # Route to appropriate chapter
    current_section = st.session_state.current_section
    
    section_map = {
        "1.1": render_chapter_1_1,
        "1.2": render_chapter_1_2,
        "1.3": render_chapter_1_3,
        "2.1": render_chapter_2_1,
        "2.2": render_chapter_2_2,
        "2.3": render_chapter_2_3,
        "2.4": render_chapter_2_4,
        "2.5": render_chapter_2_5,
        "3.1": render_chapter_3_1,
        "3.2": render_chapter_3_2,
        "3.3": render_chapter_3_3,
        "4.1": render_chapter_4_1,
        "5.1": render_chapter_5_1,
        "6.1": render_chapter_6_1,
        "6.2": render_chapter_6_2,
        "REF1": render_quick_reference,
        "REF2": render_quick_reference,
        "REF3": render_quick_reference
    }
    
    if current_section in section_map:
        section_map[current_section]()
    else:
        render_chapter_1_1()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 8px;">
        <p style="margin: 0; color: #6c757d;">
            <strong>Training Manual in Psycho-Oncology for Psychiatry Residents (India)</strong><br>
            © 2024 | For educational purposes only
        </p>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #6c757d;">
            This manual should be used in conjunction with supervised clinical training and current evidence-based guidelines.
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
