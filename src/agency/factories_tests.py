from .factories import AgencyFactory


def test_agency_factory():
    agency = AgencyFactory(users=2)

    members = agency.user_profiles.all()
    assert len(members) == 2
    assert members[0].user.username == 'Agency0-user0'
    assert members[1].user.username == 'Agency0-user1'
