import requests

# --- MODUL 1 & 2: GET REQUEST & DATA VALIDATION (MURNI PYTHON) ---
def test_get_post_and_validate_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    response = requests.get(url)
    
    # 1. Validasi status wajib 200 OK
    assert response.status_code == 200
    
    # 2. Ubah response menjadi object JSON Python (Dictionary)
    response_json = response.json()
    print(f"\n[GET] Isi JSON Server: {response_json}")
    
    # 3. Validasi isi field spesifik di dalam JSON-nya le!
    assert response_json["userId"] == 1
    assert response_json["id"] == 1
    assert "sunt aut facere" in response_json["title"]


# --- MODUL 3: POST REQUEST (KIRIM DATA BARU MURNI PYTHON) ---
def test_create_new_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Data JSON mentah yang mau kita kirim (Payload)
    payload = {
        "title": "Belajar API Automation",
        "body": "Hari ini gw berhasil naklukin API pake Playwright Python",
        "userId": 99
    }
    
    # Tembak pake method POST, kirim payload-nya di parameter 'json'
    response = requests.post(url, json=payload)
    
    print(f"\n[POST] Status Code: {response.status_code}")
    print(f"[POST] Data Baru yang Berhasil Dibuat: {response.text}")
    
    # 🌟 Validasi: Kalau berhasil membuat data baru, HTTP Status-nya wajib 201 (Created)
    assert response.status_code == 201
    
    # Validasi kalau data yang dibalikin sama dengan yang kita kirim
    response_json = response.json()
    assert response_json["title"] == "Belajar API Automation"
    assert response_json["userId"] == 99
    assert "id" in response_json  # Server otomatis bikin ID unik (misal: 101)
    
# --- MODUL 4: PUT REQUEST (UPDATE DATA ELEMEN) ---
def test_update_existing_post():
    # Target artikel yang mau diubah (ID: 1)
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    # Payload data baru yang mau ditimpa ke server
    updated_payload = {
        "id": 1,
        "title": "Title Ini Sudah Gw Ubah Le",
        "body": "Konten baru hasil revisi automation",
        "userId": 1
    }
    
    # Kirim pake method PUT
    response = requests.put(url, json=updated_payload)
    
    print(f"\n[PUT] Status Code: {response.status_code}")
    print(f"[PUT] Respon Hasil Update: {response.text}")
    
    # Validasi asersi
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["title"] == "Title Ini Sudah Gw Ubah Le"


# --- MODUL 5: DELETE REQUEST (HAPUS DATA ELEMEN) ---
def test_delete_existing_post():
    # Target artikel yang mau dimusnahkan (ID: 1)
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    # Kirim pake method DELETE (tidak butuh payload body)
    response = requests.delete(url)
    
    print(f"\n[DELETE] Status Code: {response.status_code}")
    
    # Validasi asersi: JSONPlaceholder membalas 200 jika sukses menghapus
    assert response.status_code == 200