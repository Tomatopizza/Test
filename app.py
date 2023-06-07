import streamlit as st
import openai
openai.api_key = "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"
# openai를 이용하려면 key를 발급받아야함. 돈 든다고 함.
st.write("Hello World!")
st.title("Hello WOrld!")

with st.form("form"):
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("Submit")

if submit:
    st.write(user_input)
    gpt_prompt = [] #리스트 형태로 저장. 명령어를 계속 추가해주기 우해
    gpt_prompt.append({ #시스템의 역할
        "role": "system",
        "content": "Respond my questions in 5 nouns",

    })

    gpt_prompt.append({ #사용자 역할 한마디로 위의 프롬프트에서 입력한 것.
        "role": "user",
        "content": user_input,

    })
    with st.spinner("Waiting for ChatGPT..."):#그냥 별건 아니고 로딩창
        prompt = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=gpt_prompt)

    st.markdown(prompt["choices"][0]["message"]["content"])
    # prompt = prompt["choices"][0]["message"]["content"] 
    # st.caption(prompt) #이게 태그처럼 하나 하나 묶어주는 것.


    #DALL-E 그림 그리는 놈 한테 넣어줄 것임.
    # result = openai.Image.create(
    #     prompt=prompt,
    #     size="1024x1024")
    # st.image(result["data"][0]["url"])