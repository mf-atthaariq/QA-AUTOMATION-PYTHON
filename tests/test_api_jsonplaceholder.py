import json
import pytest
import requests
from jsonschema import validate
from utils.api_routes import ApiRoutes  # Memastikan satu pintu import

# --- GATEKEEPER SUITE: SCHEMA CONTRACT VALIDATION (TC1) ---
def test_json_schema_contract_validation():
    response = requests.get(ApiRoutes.get_post_by_id(1))
    assert response.status_code == 200
    
    with open("schemas/post_schema.json", "r") as schema_file:
        expected_schema = json.load(schema_file)
        
    response_json = response.json()
    validate(instance=response_json, schema=expected_schema)
    print("\n[SCHEMA] Contract Validation PASSED: Kontrak JSON Sesuai Spesifikasi Enterprise!")


# --- ENTERPRISE SUITE: TOKEN AUTH & CHAINING LIFECYCLE ---
def test_api_chaining_and_auth_lifecycle():
    # Skenario Industri: Token didapat dari secure endpoint login
    mock_bearer_token = "Bearer enterprise_secure_token_2026_le"
    
    # Standard header xUnit Pattern
    secure_headers = {
        "Authorization": mock_bearer_token,
        "Content-Type": "application/json"
    }

    # CHAIN 1: Create Resource (POST)
    new_payload = {
        "title": "Enterprise Automation Pattern",
        "body": "Adopting C# discipline inside Python framework",
        "userId": 99
    }
    post_response = requests.post(ApiRoutes.POSTS, json=new_payload, headers=secure_headers)
    assert post_response.status_code == 201
    
    # Tangkap ID dinamis dari server untuk diestafetkan (Chaining)
    created_id = post_response.json()["id"]
    print(f"\n[CHAIN-POST] Resource created with dynamic ID: {created_id}")

    # CHAIN 2: Update Resource (PUT) menggunakan ID estafet tadi
    target_put_url = ApiRoutes.get_post_by_id(1)
    update_payload = {
        "id": 1,
        "title": "Title Ini Sudah Di-Mutasi Le",
        "body": f"Revisi menggunakan ID estafet {created_id}",
        "userId": 99
    }
    put_response = requests.put(target_put_url, json=update_payload, headers=secure_headers)
    assert put_response.status_code == 200
    assert put_response.json()["title"] == "Title Ini Sudah Di-Mutasi Le"
    print(f"[CHAIN-PUT] Mutation sync completed for target URL: {target_put_url}")

    # CHAIN 3: Destroy Resource (DELETE)
    delete_response = requests.delete(target_put_url, headers=secure_headers)
    assert delete_response.status_code == 200
    print(f"[CHAIN-DELETE] Destruction compliance verified for target URL: {target_put_url}")


# --- LOGICAL SUITE: INDEPENDENT CHECK ---
def test_get_post_and_validate_data():
    response = requests.get(ApiRoutes.get_post_by_id(1))
    assert response.status_code == 200
    
    response_json = response.json()
    assert response_json["userId"] == 1
    assert "sunt aut facere" in response_json["title"]


# --- DEFENSIVE SUITE: EXTERNAL DATA-DRIVEN TESTING (SoC) ---

# Helper function untuk membaca data eksternal (Penerapan SoC)
def load_negative_test_data():
    with open("data/api_negative_cases.json", "r") as file:
        return json.load(file)

@pytest.mark.parametrize("case", load_negative_test_data())
def test_api_negative_security_scenarios(case):
    """
    TC Fungsionalitas Negatif (SoC Pattern): Memvalidasi ketangguhan API.
    Note: Di industri nyata, expected_status adalah 400/401. 
    Namun karena menggunakan JSONPlaceholder Mock API, server merespon dengan 404 Not Found.
    """
    print(f"\n[RUNNING SCENARIO] -> {case['scenario']}")
    
    response = requests.post(
        ApiRoutes.POSTS, 
        json=case['payload'], 
        headers=case['headers']
    )
    
    # Validasi asersi status code
    assert response.status_code == case['expected_status'], \
        f"Gagal pada {case['scenario']}! Harusnya {case['expected_status']} tapi dapet {response.status_code}"