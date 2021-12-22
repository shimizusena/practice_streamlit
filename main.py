import streamlit as st
import time

st.title("Streamlit　超入門")

st.write("プレグレスバーの表示")

"Start!!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Interaction {i+1} ")
    bar.progress(i+1)
    time.sleep(0.1)

"Done!!!"


left_column,right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

# df = pd.DataFrame({
#     "1列目" : [1,2,3,4],
#     "2列目" : [10,20,30,40]
# })

# st.write(df.style.highlight_max(axis=0))




# text = st.text_input("あなたの趣味を教えて下さい")
# conditions = st.slider("あなたの調子はどれくらいですか?",0,100,50)

# "あなたの趣味は",text,"です"
# "あなたの調子は",conditions,"です"
# if st.checkbox("Show Image"):
#     img = Image.open("プリン.jpg")
#     st.image(img,caption="プリンちゃん",use_column_width=True)



# df = pd.DataFrame(
#     np.random.rand(100,2)/[100,100]+ [34.4235,135.2934],
#     columns=["lat","lon"]
# )

# st.map(df)