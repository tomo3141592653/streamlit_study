import streamlit as st
from sympy import factorint
import io 

# Streamlit アプリのタイトル
st.title('素因数分解計算機')

# ユーザーから数値を入力してもらう
number = st.number_input('数値を入力してください', min_value=1, step=1, format='%d')

# 素因数分解ボタン
if st.button('素因数分解'):
    # SymPy の factorint 関数を使用して素因数分解
    factors = factorint(number)

    # 結果を表示するための文字列を生成
    result = ', '.join([f'{factor}^{exponent}' if exponent > 1 else str(factor) for factor, exponent in factors.items()])

    # 結果を表示
    st.write(f'{number} の素因数分解: {result}')


# ファイルアップロードセクション
uploaded_file = st.file_uploader("数字のリストが含まれるテキストファイルをアップロードしてください (.txt)")

if uploaded_file is not None:
    # ファイルの内容を読み込む
    content = uploaded_file.getvalue().decode("utf-8")
    numbers = content.splitlines()

    # 処理結果を保存するための文字列IO
    result_io = io.StringIO()

    # ファイルから読み取った各行に対して処理
    for number in numbers:
        number = int(number)
        factors = factorint(number)
        result = ', '.join([f'{factor}^{exponent}' if exponent > 1 else str(factor) for factor, exponent in factors.items()])
        result_io.write(f'{number} の素因数分解: {result}\n')
    
    # ユーザーにダウンロードリンクを提供
    st.download_button(
        label="結果をダウンロード",
        data=result_io.getvalue(),
        file_name="factorization_results.txt",
        mime="text/plain"
    )