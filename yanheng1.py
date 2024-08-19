'''我的主页'''
import streamlit as st
from PIL import Image
import base64
import wordcloud
import datetime
page = st.sidebar.radio('以文为鉴',['专区','我的笔记','文字美化','小词典'])
now = datetime.datetime.now()
def page_1():
    '''专区'''
    with open('陈致逸,HOYO-MiX - 不再年轻的村庄(轻策夜间) The Fading Stories (Qingce Night.mp3','rb')as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3', start_time=0)

    tab1,tab2,tab3= st.tabs(["余华","莫言","刘慈欣"])
    with tab1: 
        bar_ag('生死.png')
        page_bg('活着.jpeg')
        #st.balloons()
        st.title("现代文学史·余华篇")
        st.write('----')
        
        a = ":black[余华是一位中国当代著名的作家，以其深刻的现实主义风格和对人性深刻的洞察而闻名。他的作品常常探讨生活中的苦难、人性的复杂性以及社会变迁对个人的影响。余华的一些著名作品包括《活着》、《许三观卖血记》和《兄弟》等，这些作品不仅在中国国内广受欢迎，也在国际上获得了极高的评价]"
        st.subheader(a)
        go = st.selectbox(' ', ['《在细雨中呼喊》', '《许三观卖血记》','【余华的“中式恐怖”与“暴力美学”】','《活着》'])
        if go == '【余华的“中式恐怖”与“暴力美学”】':
            st.link_button('点击此处，快快看罢（喜', 'https://www.bilibili.com/video/BV1fJ4m187V6?vd_source=6c8f95fc83fd6c5105c26790746cff10')
        elif go == '《在细雨中呼喊》':
            st.link_button('点击此处，快快看罢（喜','https://www.bilibili.com/video/BV1qH4y1X7sr/?spm_id_from=333.337.search-card.all.click' )
        elif go == '《许三观卖血记》':
            st.link_button('点击此处，快快看罢（喜','https://www.bilibili.com/video/BV1Z14y1m7Fw/?spm_id_from=333.788' )
        elif go == '《活着》':
            st.link_button('点击此处，快快看罢（喜','https://www.bilibili.com/video/BV1Jm4y1D7PL/?spm_id_from=333.337.search-card.all.click' )

    with tab2:
        if st.tabs == tab2:
            bar_bg('生死.png')
            page_bg('生死.png')
        #st.balloons()
        st.title("现代文学史·莫言篇")
        st.write('----')
        st.subheader("莫言的作品深受魔幻现实主义的影响，代表作包括《红高粱家族》、《檀香刑》、《丰乳肥臀》等")
        st.subheader('他的创作风格独特，语言犀利，想象狂放，叙事磅礴，深受读者喜爱,2012年，莫言因其“用魔幻现实主义将民间故事、历史和现代融为一体”的卓越成就，荣获诺贝尔文学奖')
        go = st.selectbox(' ', ['《生死疲劳》'])
        if go == '《生死疲劳》':
            st.link_button('点击此处，快快看罢（喜', 'https://www.bilibili.com/video/BV1vY4y157BE/?spm_id_from=333.337.search-card.all.click')

    with tab3:
        st.title("中国科幻界扛把子·刘慈欣篇")
        st.write('----')
        st.subheader("刘慈欣从上世纪九十年代开始发表科幻作品，曾于1999年至2006年连续八年获得中国科幻最高奖“银河奖”。他的代表作包括长篇小说《三体》、《超新星纪元》和《球状闪电》，以及中篇小说《流浪地球》和《乡村教师》等")
        st.subheader('刘慈欣的作品以其宏伟大气、想象绚丽而著称，常常包含对现实的反思和科学启蒙的主题，他的创作风格融合了奇幻与现实，通过构建宏伟的科幻世界来探讨人类命运和宇宙奥秘')
        go = st.selectbox(' ', ['超新星纪元','综合','三体','流浪地球'])
        if go == '超新星纪元':
            st.link_button('点击此处，快快看罢（喜', 'https://www.bilibili.com/video/BV1tJ4m1W7sH/?spm_id_from=333.999.0.0')
        if go == '综合':
            st.link_button('点击此处，快快看罢（喜', 'https://www.bilibili.com/video/BV17L4y1e7tr/?spm_id_from=333.337.search-card.all.click')    
        if go == '三体':
            st.link_button('点击此处，快快看罢（喜', ' https://www.bilibili.com/video/BV1HV4y1E7Mm/?spm_id_from=333.337.search-card.all.click')
        if go == '流浪地球':
            st.link_button('点击此处，快快看罢（喜', ' https://www.bilibili.com/video/BV1HP4y167hG/?spm_id_from=333.337.search-card.all.click')


   # st.subheader("余华是一位中国当代著名的作家，以其深刻的现实主义风格和对人性深刻的洞察而闻名。他的作品常常探讨生活中的苦难、人性的复杂性以及社会变迁对个人的影响。余华的一些著名作品包括《活着》、《许三观卖血记》和《兄弟》等，这些作品不仅在中国国内广受欢迎，也在国际上获得了极高的评价")
   # st.write("【看不到时代的方向，就会感到生命毫无意义】")
   # st.link_button('', 'https://www.bilibili.com/video/BV1qH4y1X7sr/?spm_id_from=333.337.search-card.all.click')
   # st.write("【余华的“中式恐怖”与“暴力美学”】")
    #st.link_button('点击此处，快快看罢（喜', 'https://www.bilibili.com/video/BV1fJ4m187V6?vd_source=6c8f95fc83fd6c5105c26790746cff10')
   # st.write("【许三观卖血记】")
   # st.link_button('点击此处，快快看罢（喜', 'https://www.bilibili.com/video/BV1Z14y1m7Fw/?spm_id_from=333.788')

    
def page_2():
    page_ag('8.png')
    """我的笔记"""
    st.write(":sunglasses:点击此处，上传图片:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=['png','gpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5 = st.tabs(["原图","改色1","改色2","改色3","改色4",])
        with tab1:
            st.image(img)
        with tab2:
            st.image(image_change(img, 0, 2, 1))
        with tab3:
            st.image(image_change(img, 1, 0, 2))
        with tab4:
            st.image(image_change(img, 1, 1, 0))
        with tab5:
            st.image(image_change(img, 2, 1, 0))
    st.write("-------------------------")
    st.write('笔记（写点什么吧）')
    with open('leave_messages.txt','r', encoding='utf-8')as f:
        messages_list = f.read().split('\n')
        for i in range(len(messages_list)):
            messages_list[i] = messages_list[i].split('#')
        for i in messages_list:
            if i[1] == '记录':
                with st.chat_message('👨‍🦰👆👇'):
                     st.write(i[1],':',i[2])
            elif i[1] == '反思':
                with st.chat_message('👨‍🦱👆👇'):
                    st.write(i[1],':',i[2])
    name = st.selectbox('写个...', ['记录', '反思'])
    new_message = st.text_input('想说的话...')
    if st.button('笔记'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    
    st.write(now)
def ciyun(str):
    font = "anna.ttf"
    w= wordcloud.WordCloud(width=600, height=400, font_path=font, max_words=50).generate(str)
    w.to_file("ciyun.png")
    img = Image.open("ciyun.png")
    return img
        
def page_3():
    """个性化文字处理"""
    uploaded_file = st.file_uploader("上传txt文件")
    if uploaded_file is not None:
        str_data = uploaded_file.read().decode("utf-8")
        st.image(ciyun(str_data))
    else:
        pass
    
    
def page_4():
    page_ag('文城.jpeg')
    """神奇小词典"""
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])

def image_change(img, rc, gc, bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r, g, b)
    return img
    
def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last},base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )   
def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def bar_ag(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_ag(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

bar_ag('生死.png')

    
if page == '专区':
    page_1()
elif page == '我的笔记':
    page_2()
elif page == '浏览记录':
    page_3()
elif page == '社区分享':
    page_4()

