import pytest
from src.API.api_interface import app
from src.core.ohce import Ohce

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_greet(client, monkeypatch):
    # Simuler le comportement de Ohce.greet()
    monkeypatch.setattr('core.ohce.Ohce.greet', lambda self: "Bonjour")
    
    response = client.get('/greet?lang=fr')
    assert response.status_code == 200
    assert response.json == {"greeting": "Bonjour"}

def test_api_echo(client, monkeypatch):
    # Simuler le comportement de Ohce.echo()
    test_text = "kayak"
    monkeypatch.setattr('core.ohce.Ohce.echo', lambda self, text: f"{text} (Bien dit!)")
    
    response = client.post('/echo', json={"text": test_text})
    assert response.status_code == 200
    assert response.json == {"echo": f"{test_text} (Bien dit!)"}

def test_api_farewell(client, monkeypatch):
    # Simuler le comportement de Ohce.farewell()
    monkeypatch.setattr('core.ohce.Ohce.farewell', lambda self: "Au revoir")
    
    response = client.get('/farewell?lang=fr')
    assert response.status_code == 200
    assert response.json == {"farewell": "Au revoir"}
