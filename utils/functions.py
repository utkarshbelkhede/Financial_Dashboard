from utils.libraries import st, re


#set_of_words = set(words.words())


def display_summary(summary_df, classification_df, topic_extraction_df, columns, company, year, show_topics, show_score):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3 style='text-align: left;'>Company</h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: left;color: #665A48;'>" + str(company) + "</h5>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h3 style='text-align: right;'>Year</h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: right;color: #665A48;'>" + str(year) + "</h5>", unsafe_allow_html=True)

    for col in columns:
        st.markdown("<h4 style='text-align: left; color: #9F8772;'>" + str(col) + "</h4>", unsafe_allow_html=True)

        summary_result = summary_df[(summary_df['Company'] == company) & (summary_df['Year'] == year)]

        topic_extraction_result = topic_extraction_df[
            (topic_extraction_df['Company'] == company) & (topic_extraction_df['Year'] == year)]

        text = summary_result.loc[summary_result.index[0], col]

        topics = eval(topic_extraction_result.loc[topic_extraction_result.index[0], col])

        for topic in topics:
            if not bool(re.search(r'\d', topic[1])):

                if not show_score:
                    replace_with = '<span style="background: #EAEA7F; border-radius: 0.33rem; padding: 1.5px ;">'+ str(topic[1]) +'</span>'
                else:
                    replace_with = '<span style="background: #EAEA7F; border-radius: 0.33rem; padding: 1.5px ;">' + str(topic[1]) + '<span style="font-size:12px; padding-left: 8px; padding-right: 8px; opacity:0.5">' + str(round(topic[0], 1)) + '</span></span>'

                #st.write(str(topic[1]))
                #st.write(re.sub(str(topic[1]), replace_with, text))
                #if not any(chr.isdigit() for chr in str(topic[1])):
                    #text = re.sub(str(topic[1]), replace_with, text)

                #st.write(text)
                #text_score = re.sub(str(topic[1]), replace_with, text)

        if show_topics:
            st.markdown("<p style='text-align: justify;'>" + text + "</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='text-align: justify;'>" + summary_result.loc[summary_result.index[0], col] + "</p>",
                        unsafe_allow_html=True)

        classification_df = classification_df[
            (classification_df['Company'] == company) & (classification_df['Year'] == year)]
        sentiment = eval(classification_df.loc[classification_df.index[0], col])

        col1, col2 = st.columns(2)

        with col1:
            if sentiment['label'] == 'POSITIVE':
                st.markdown(
                    "<p style='width:100px ;background-color:  #1C6758; border: 0px; border-radius: 4px; box-sizing: border-box; color: #FFFFFF; font-size: 14px; line-height: 1.15; padding: 12px;text-align: center;'>" +
                    sentiment['label'] + "</p>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<p style='width:100px ;background-color:  #AE431E; border: 0px; border-radius: 4px; box-sizing: border-box; color: #FFFFFF; font-size: 14px; line-height: 1.15; padding: 12px;text-align: center;'>" +
                    sentiment['label'] + "</p>",
                    unsafe_allow_html=True
                )

        with col2:
            st.markdown("<h5 style='text-align: right;'>" + '%.4f' % sentiment['score'] + " % </h5>",
                        unsafe_allow_html=True)
