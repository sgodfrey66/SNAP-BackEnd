import pytest


def test_signup_page_is_showing_a_form(client):
  response = client.get("/health/")
  assert response.status_code == 200
