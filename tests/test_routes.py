def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Foozie",
        "description": "The fuzziest planet"
    }

def test_no_planet_data(client):
    response = client.get("/planets/509")
    response_body = response.get_json()
    assert response.status_code == 404



def test_get_one_planet_fixtures(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Foozie",
        "description": "The fuzziest planet"
    }