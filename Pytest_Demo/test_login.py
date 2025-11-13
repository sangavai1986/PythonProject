import pytest

@pytest.fixture(params=["a","b"])
def demo_fixture(request):
    print(request.param)


def testlogin(demo_fixture):
    print("Login successful")

@pytest.mark.parametrize("username,password",[("user1","pass1"),("user2","pass2")])
def test_loginwith(username,password):
    print(f"Login with{username} and password {password}")

# @pytest.mark.regression
# def testlogoff():
#     print("Logoff success")
#
# @pytest.mark.skip
# def testcalc():
#     assert 2+2 ==4
#
# @pytest.mark.xfail
# def testcalc1():
#     assert 3+2 == 4