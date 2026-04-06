"""
Unit tests for Python Application
Uses pytest for testing
"""

import pytest
from app import app

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestHome:
    """Test home endpoint"""
    
    def test_home_status_code(self, client):
        """Test home returns 200"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_response(self, client):
        """Test home returns correct data"""
        response = client.get('/')
        data = response.get_json()
        assert 'message' in data
        assert data['status'] == 'success'

class TestHealth:
    """Test health endpoint"""
    
    def test_health_status_code(self, client):
        """Test health returns 200"""
        response = client.get('/health')
        assert response.status_code == 200
    
    def test_health_response(self, client):
        """Test health returns healthy status"""
        response = client.get('/health')
        data = response.get_json()
        assert data['status'] == 'healthy'

class TestGreet:
    """Test greet endpoint"""
    
    def test_greet_success(self, client):
        """Test greet with valid data"""
        response = client.post('/api/greet', 
            json={'name': 'Alice'},
            content_type='application/json'
        )
        assert response.status_code == 200
        data = response.get_json()
        assert 'Hello, Alice!' in data['message']
    
    def test_greet_missing_name(self, client):
        """Test greet without name"""
        response = client.post('/api/greet',
            json={},
            content_type='application/json'
        )
        assert response.status_code == 400
        data = response.get_json()
        assert data['status'] == 'error'

class TestInfo:
    """Test info endpoint"""
    
    def test_info_status_code(self, client):
        """Test info returns 200"""
        response = client.get('/api/info')
        assert response.status_code == 200
    
    def test_info_response(self, client):
        """Test info returns application data"""
        response = client.get('/api/info')
        data = response.get_json()
        assert 'name' in data
        assert 'version' in data

class TestNotFound:
    """Test 404 handling"""
    
    def test_404_not_found(self, client):
        """Test non-existent endpoint"""
        response = client.get('/nonexistent')
        assert response.status_code == 404

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
