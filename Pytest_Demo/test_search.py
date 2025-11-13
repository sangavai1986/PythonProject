import pytest
@pytest.mark.parametrize("username",["user1","user2","user3"])
def test_search(username):
    print(f"Searching user {username}")
