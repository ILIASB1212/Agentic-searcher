from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain.agents import AgentType,initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain_groq import ChatGroq
from exception.EXCEPTION import AppException
from LOGGER.log import logging
from config import setup_environment
import streamlit as st
import os

setup_environment()


# archiv api setup
arxiv_api=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=400)
arxiv=ArxivQueryRun(api_wrapper=arxiv_api)

# wikipedia api setup
wikip_api=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=400)
wiki=WikipediaQueryRun(api_wrapper=wikip_api)

# internet search api setup
search=DuckDuckGoSearchRun(name="search")

st.title("langchain search ")

st.sidebar.title("settings")
input_api_key=st.sidebar.text_input("groq API key",type="password")
# default message showed to user Iin the first reload of page
if "messages" not in st.session_state:
    try:
        st.session_state["messages"]=[
            {"role":"assisstant","content":"hi i can search the internet for you with 3 agents how can i help you "}
        ]
    except AppException as e:
        logging.info(e)
        st.write(e)
#
for msg in st.session_state.messages: 
        with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
#
if prompt:=st.chat_input(placeholder="what is the news today"):
    logging.info(f'user asked for \n{prompt}')
    try:
        st.session_state.messages.append({"role": "user", "content": prompt})
        #
        with st.chat_message("user"):
            st.write(prompt)
        # add llm
        llm=ChatGroq(api_key=input_api_key, model="llama-3.3-70b-versatile",streaming=True)
        #
        tools=[search,arxiv,wiki]
        search_angine = initialize_agent(tools,llm,agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,handle_parsing_errors=True
    ) # t add context/memory ro convesation)
        with st.chat_message("assistant"):
            st_callback=StreamlitCallbackHandler(st.container(),expand_new_thoughts=True)
            response=search_angine.run(st.session_state.messages,callbacks=[st_callback])
            st.session_state.messages.append({"role":"assistant","content":response})
            st.write(response)
            logging.info(f"user recived answer {response}")
    except AppException as e:
        logging.info(e)
        st.write(e)