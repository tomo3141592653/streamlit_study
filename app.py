import streamlit as st
from sympy import factorint

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