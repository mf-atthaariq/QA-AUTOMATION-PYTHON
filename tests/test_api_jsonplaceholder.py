import pytest

# --- MODUL 1 & 2: GET REQUEST & DATA VALIDATION ---
def test_get_post_and_validate_data(playwright):
    api_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    
    response = api_context.get("/posts/1")
    assert response.status == 200
    
    # 🌟 BARU: Ubah response teks menjadi object JSON Python (Dictionary)
    response_json = response.json()
    
    # Cetak biar lo bisa liat strukturnya di terminal
    print(f"\n[GET] Isi JSON Server: {response_json}")
    
    # Validasi isi field spesifik di dalam JSON-nya le!
    assert response_json["userId"] == 1
    assert response_json["id"] == 1
    assert "sunt aut facere" in response_json["title"] # Memastikan kata ini ada di title
    
    api_context.dispose()


# --- MODUL 3: POST REQUEST (KIRIM DATA BARU) ---
def test_create_new_post(playwright):
    api_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    
    # Data JSON mentah yang mau kita kirim (Payload)
    payload = {
        "title": "Belajar API Automation",
        "body": "Hari ini gw berhasil naklukin API pake Playwright Python",
        "userId": 99
    }
    
    # Tembak pake method POST, kirim payload-nya di parameter 'data'
    response = api_context.post("/posts", data=payload)
    
    print(f"\n[POST] Status Code: {response.status}")
    print(f"[POST] Data Baru yang Berhasil Dibuat: {response.text()}")
    
    # 🌟 Validasi: Kalau berhasil membuat data baru, HTTP Status-nya wajib 201 (Created)
    assert response.status == 201
    
    # Validasi kalau data yang dibalikin sama dengan yang kita kirim
    response_json = response.json()
    assert response_json["title"] == "Belajar API Automation"
    assert response_json["userId"] == 99
    assert "id" in response_json # Server biasanya otomatis bikinin ID unik (misal: 101)
    
    api_context.dispose()