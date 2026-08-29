import seaborn as sns
def table(x,y):
    fig, ax = plt.subplots()
    sns.scatterplot(data=d, x="Age", y="bmi", hue="Risk_Level", palette="Set1", ax=ax)
    st.pyplot(fig)