from helper.libraries import st


def display_summary(summary_df, classification_df, columns, company, year):
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
