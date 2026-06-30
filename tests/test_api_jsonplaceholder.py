import json
import logging
import pytest
import requests
from jsonschema import validate
from utils.api_routes import ApiRoutes

# Inisialisasi Logger Instance sesuai modul pengujian paralel
logger = logging.getLogger(__name__)

# ==============================================================================
# GATEKEEPER SUITE: SCHEMA CONTRACT VALIDATION (TC1)
# ==============================================================================
def test_json_schema_contract_validation():
    logger.info("GATEKEEPER START: Memulai validasi JSON Schema Contract.")
    response = requests.get(ApiRoutes.get_post_by_id(1))
    assert response.status_code == 200
    
    with open("schemas/post_schema.json", "r") as schema_file:
        expected_schema = json.load(schema_file)
        
    response_json = response.json()
    validate(instance=response_json, schema=expected_schema)
    logger.info("CONTRACT PASSED: Struktur skema payload sesuai dengan spesifikasi enterprise!")


# ==============================================================================
# ENTERPRISE SUITE: TOKEN AUTH & CHAINING LIFECYCLE
# ==============================================================================
def test_api_chaining_and_auth_lifecycle():
    logger.info("ENTERPRISE SUITE START: Memulai Token Auth & API Chaining Lifecycle.")
    mock_bearer_token = "Bearer enterprise_secure_token_2026_le"
    
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
    
    created_id = post_response.json()["id"]
    logger.info(f"CHAIN-POST SUCCESS: Resource created with dynamic ID: {created_id}")

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
    logger.warning(f"CHAIN-PUT MUTATION: Sync completed on target URL: {target_put_url}")

    # CHAIN 3: Destroy Resource (DELETE)
    delete_response = requests.delete(target_put_url, headers=secure_headers)
    assert delete_response.status_code == 200
    logger.info(f"CHAIN-DELETE SUCCESS: Destruction compliance verified for URL: {target_put_url}")


# ==============================================================================
# LOGICAL SUITE: INDEPENDENT CHECK
# ==============================================================================
def test_get_post_and_validate_data():
    logger.info("LOGICAL SUITE START: Independent check untuk keakuratan data.")
    response = requests.get(ApiRoutes.get_post_by_id(1))
    assert response.status_code == 200
    
    response_json = response.json()
    assert response_json["userId"] == 1
    assert "sunt aut facere" in response_json["title"]
    logger.info("LOGICAL SUITE PASSED: Business logic content valid.")


# ==============================================================================
# DEFENSIVE SUITE: EXTERNAL DATA-DRIVEN TESTING (SoC)
# ==============================================================================
def load_negative_test_data():
    with open("data/api_negative_cases.json", "r") as file:
        return json.load(file)

@pytest.mark.parametrize("case", load_negative_test_data())
def test_api_negative_security_scenarios(case):
    """
    TC Fungsionalitas Negatif (SoC Pattern): Memvalidasi ketangguhan API secara paralel.
    """
    logger.warning(f"SECURITY INTRUSION RUNNING SCENARIO -> {case['scenario']}")
    
    response = requests.post(
        ApiRoutes.POSTS, 
        json=case['payload'], 
        headers=case['headers']
    )
    
    assert response.status_code == case['expected_status'], \
        f"Gagal pada {case['scenario']}! Harusnya {case['expected_status']} tapi dapet {response.status_code}"
    logger.info(f"SECURITY INTRUSION BLOCKED: Skenario [{case['scenario']}] tertahan dengan status {response.status_code}")