import streamlit as st

from parse import parse_with_ollama
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape"):
    st.write("scraping the website")

    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM content", cleaned_content, height=500)

    print(result)

if "dom_content" in st.session_state:
    parse_description = st.text_area("What u want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)