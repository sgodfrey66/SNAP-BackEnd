from .factories import UserFactory, UserProfileFactory


def test_user_factory():
    user = UserFactory()
    assert user is not None
    assert user.profile is not None
