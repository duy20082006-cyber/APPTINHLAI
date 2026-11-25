
import streamlit as st

# ==============================
# CẤU HÌNH TRANG WEB
# ==============================
st.set_page_config(
    page_title="Công cụ tính lãi đơn và lãi kép",
    page_icon="💰",
    layout="centered"
)

# ==============================
# TIÊU ĐỀ ỨNG DỤNG
# ==============================
st.title("💰 CÔNG CỤ TÍNH LÃI ĐƠN VÀ LÃI KÉP")

st.write(
    "Ứng dụng giúp khách hàng tính toán và so sánh "
    "số tiền nhận được theo phương pháp lãi đơn và lãi kép."
)

st.divider()

# ==============================
# NHẬP DỮ LIỆU
# ==============================
st.subheader("📌 Nhập thông tin khoản tiền gửi")

C = st.number_input(
    "Số tiền gốc (đồng)",
    min_value=0,
    value=100_000_000,
    step=10_000_000,
    format="%d"
)

i_percent = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    value=1.0,
    step=0.1
)

n = st.number_input(
    "Thời gian gửi (năm)",
    min_value=0,
    value=3,
    step=1
)

# Chuyển lãi suất từ phần trăm sang số thập phân
i = i_percent / 100

st.divider()

# ==============================
# TÍNH TOÁN
# ==============================
st.subheader("📊 Kết quả tính toán")

if st.button("TÍNH TOÁN", type="primary", use_container_width=True):

    # Tính lãi đơn
    An = C * (1 + i * n)

    # Tính lãi kép
    Bn = C * ((1 + i) ** n)

    # Tính tiền lãi
    lai_don = An - C
    lai_kep = Bn - C

    # Hiển thị kết quả
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="💵 Số tiền theo lãi đơn",
            value=f"{An:,.0f} đồng",
            delta=f"Lãi nhận được: {lai_don:,.0f} đồng"
        )

    with col2:
        st.metric(
            label="💰 Số tiền theo lãi kép",
            value=f"{Bn:,.0f} đồng",
            delta=f"Lãi nhận được: {lai_kep:,.0f} đồng"
        )

    st.divider()

    # So sánh hai phương pháp
    chenh_lech = Bn - An

    st.subheader("📈 So sánh kết quả")

    st.write(
        f"Số tiền chênh lệch giữa lãi kép và lãi đơn: "
        f"**{chenh_lech:,.0f} đồng**"
    )

    if Bn > An:
        st.success(
            "Lãi kép mang lại số tiền cao hơn lãi đơn."
        )
    elif Bn < An:
        st.info(
            "Lãi đơn mang lại số tiền cao hơn lãi kép."
        )
    else:
        st.info("Hai phương pháp cho kết quả bằng nhau.")

    # Bảng kết quả
    st.subheader("📋 Bảng tổng hợp")

    data = {
        "Nội dung": [
            "Tiền gốc",
            "Tiền lãi",
            "Tổng số tiền nhận được"
        ],
        "Lãi đơn": [
            f"{C:,.0f} đồng",
            f"{lai_don:,.0f} đồng",
            f"{An:,.0f} đồng"
        ],
        "Lãi kép": [
            f"{C:,.0f} đồng",
            f"{lai_kep:,.0f} đồng",
            f"{Bn:,.0f} đồng"
        ]
    }

    st.table(data)

    st.caption(
        "Lưu ý: Giả định lãi suất không đổi và được tính theo năm, "
        "lãi kép nhập gốc một lần mỗi năm."
    )
