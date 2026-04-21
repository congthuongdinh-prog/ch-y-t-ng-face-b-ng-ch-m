import streamlit as st
import webbrowser
import subprocess
import os

st.set_page_config(page_title="Tự động mở Facebook", page_icon="🌐")

st.title("Tự động mở Facebook bằng Google Chrome 🌐")
st.markdown("""
Chương trình này giúp bạn mở Facebook bằng trình duyệt Chrome, **giữ nguyên phiên đăng nhập (đã lưu tên và mật khẩu)**.
""")

st.subheader("Tùy chọn 1: Mở như một Tab bình thường (Khuyên dùng)")
st.write("Cách này rất an toàn, không bị lỗi ngay cả khi bạn đang mở sẵn Chrome.")

if st.button("Mở Facebook (Cách 1)", type="primary"):
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
    ]
    
    opened = False
    for path in chrome_paths:
        if os.path.exists(path):
            try:
                subprocess.Popen([path, "https://www.facebook.com"])
                st.success("✅ Đã mở Facebook thành công!")
                opened = True
                break
            except Exception as e:
                st.error(f"Lỗi khi mở: {e}")
    
    if not opened:
        st.warning("⚠️ Không tìm thấy Chrome, đang mở bằng trình duyệt mặc định...")
        webbrowser.open("https://www.facebook.com")

st.divider()

st.subheader("Tùy chọn 2: Mở bằng Selenium (Dành cho tự động hóa)")
st.write("Cách này dùng để chạy bot tự động. **Lưu ý:** Bạn phải đóng TẤT CẢ các cửa sổ Chrome hiện tại trước khi bấm nút này, nếu không sẽ bị lỗi.")

if st.button("Mở Facebook bằng Selenium (Cách 2)"):
    st.info("Đang khởi động Selenium...")
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
        
        # Đường dẫn tới thư mục User Data của Chrome
        user_data_dir = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")
        
        options = Options()
        options.add_argument(f"user-data-dir={user_data_dir}")
        options.add_argument("profile-directory=Default") # Có thể thay 'Default' bằng 'Profile 1', v.v.
        
        # Tự động tải ChromeDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get("https://www.facebook.com")
        st.success("✅ Đã mở Facebook bằng Selenium với profile của bạn!")
        
    except ImportError:
        st.error("⚠️ Bạn chưa cài đặt thư viện cần thiết. Hãy chạy lệnh: `pip install selenium webdriver-manager`")
    except Exception as e:
        if "user data directory is already in use" in str(e).lower():
            st.error("❌ Lỗi: Bạn phải đóng TẤT CẢ các cửa sổ Chrome đang mở trước khi chạy lệnh này.")
        else:
            st.error(f"❌ Lỗi: {e}")
