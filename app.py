from helper.libraries import st, pd
from helper.functions import display_summary


def app():
    try:
        summary_df = pd.read_csv("./datasets/summarized_dataframe_sshleifer_distilbart-cnn-12-6.csv")
        classification_df = pd.read_csv("./datasets/classification_distilbert-base-uncased-finetuned-sst-2-english.csv")

        # index = [str(i) for i in range(df.shape[0])]
        # df["index"] = index
        # df = df.set_index('index')
    except NameError:
        print("Some problem with file...")

    st.sidebar.title("Menu")
    company = st.sidebar.selectbox("Choose Company", list(summary_df.loc[:, "Company"].unique()))
    year = st.sidebar.selectbox("Choose Year", list(summary_df.loc[:, "Year"].unique()))

    which_summary = st.sidebar.selectbox("See Summary For", ["Everything", "Section-wise"])

    st.markdown("<h1 style='text-align: center;'>Financial Dashboard</h1>", unsafe_allow_html=True)

    if which_summary == "Everything":
        display_summary(summary_df, classification_df, summary_df.columns[2:], company, year)
    else:
        options = st.multiselect('Which Section(s) you wanna see?', summary_df.columns[2:], "Risk Factor")
        display_summary(summary_df, classification_df, options, company, year)


if __name__ == '__main__':
    app()
