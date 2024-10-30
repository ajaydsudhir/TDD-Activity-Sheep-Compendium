# Import TestClient to simulate API requests
from fastapi.testclient import TestClient

# Import the FastAPI app instance from the controller module
from main import app

# Create a TestClient instance for the FastAPI app
client = TestClient(app)


# Define a test function for reading a specific sheep
def test_read_sheep():
    # Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected data
    assert response.json() == {
        # Expected JSON structure
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

# Define a test function for adding a new sheep
def test_add_sheep():
    # TODO: Prepare the new sheep data in a dictionary format
    new_sheep = {
        "id": 7,
        "name": "Lessie",
        "breed": "Suffolk",
        "sex": "ram"
    }

    # TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
    #  Arguments should be your endpoint and new sheep data.
    response = client.post("/sheep", json=new_sheep)

    # TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # TODO: Assert that the response JSON matches the new sheep data
    sheep_added = response.json()
    assert sheep_added["id"] == new_sheep["id"]
    assert sheep_added["name"] == new_sheep["name"]
    assert sheep_added["breed"] == new_sheep["breed"]
    assert sheep_added["sex"] == new_sheep["sex"]

    # TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    #  include an assert statement to see if the new sheep data can be retrieved.
    sheep_added_id = new_sheep["id"]
    response = client.get(f"/sheep/{sheep_added_id}")
    assert response.status_code == 200

# Define a test function for deleting a new sheep
def test_delete_sheep():
    response = client.delete("/sheep/1")
    assert response.status_code == 200

    response = client.get("/sheep/1")
    assert response.status_code == 404

def test_update_sheep():
    updated_sheep = {
        "id": 2,
        "name": "Blondie Updated",
        "breed": "Polypay",
        "sex": "ewe"
    }
    response = client.put("/sheep/2", json=updated_sheep)
    assert response.status_code == 200
    assert response.json()["name"] == updated_sheep["name"]

    response = client.get("/sheep/2")
    assert response.status_code == 200
    assert response.json()["name"] == updated_sheep["name"]

def test_read_all_sheep():
    response = client.get("/sheep")
    assert response.status_code == 200
    sheep_list = response.json()
    assert isinstance(sheep_list, list)
    assert len(sheep_list) > 0