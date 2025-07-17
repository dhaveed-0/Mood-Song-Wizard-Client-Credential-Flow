import pytest
from project import (
    recommend_song,
    get_user_mood,
    display_recommendation,
    handle_user_feedback,
)


def test_get_user_mood(monkeypatch):
    user_responses = iter(["1234", "I am happy"])  # simulated user responses
    monkeypatch.setattr("builtins.input", lambda _: next(user_responses))
    assert get_user_mood() == "i am happy"


# This tests the structure of the return value of 'recommend_song(mood)' function...
# ...since it return a random track each time.
def test_recommend_song():
    test_result = recommend_song("happy")  # mood == "happy"
    assert isinstance(test_result, list)  # test that the result is a list
    assert len(test_result) == 3  # test that the list contains 3 items
    assert all(isinstance(i, str) for i in test_result)
    # makes sure that each item in list is a string


def test_display_recommendation():
    # this has the same test as 'recommend_song()'...
    # since the return value of the function is the same as 'recommend_song()'
    test_result = display_recommendation("happy")  # mood == "happy"
    assert isinstance(test_result, list)  # test that the result is a list
    assert len(test_result) == 3  # test that the list contains 3 items
    assert all(isinstance(i, str) for i in test_result)
    # makes sure that each item in list is a string


def test_handle_user_feedback_1(monkeypatch):
    # This will simulate the user saying 'Yes', then 'No'
    inputs = iter(["Yes", "No"])
    # Mock input()
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # Mock display_recommendation() to do nothing
    monkeypatch.setattr("project.display_recommendation", lambda mood: None)
    # Mock recommend_song() just in case
    monkeypatch.setattr(
        "project.recommend_song",
        lambda mood: [
            "The Happy Song",
            "Imogen Heap",
            "https://open.spotify.com/artist/6Xb4ezwoAQC4516kI89nWz",
        ],
    )
    # Catch sys.exit
    with pytest.raises(SystemExit) as exit_message:
        # positional arguments: mood and last_recommendation
        handle_user_feedback(
            "happy",
            [
                "The Happy Song",
                "Imogen Heap",
                "https://open.spotify.com/artist/6Xb4ezwoAQC4516kI89nWz",
            ],
        )
    # Assert exit message
    assert "Thank you for listening. Come back soon! 👋" in str(exit_message.value)


def test_handle_user_feedback_2(monkeypatch):
    # This will simulate the user saying 'No', 'No', 'No'
    inputs = iter(["No", "No", "No"])
    # Mock input()
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # Mock display_recommendation() to do nothing
    monkeypatch.setattr("project.display_recommendation", lambda mood: None)
    # Mock recommend_song() just in case
    monkeypatch.setattr(
        "project.recommend_song",
        lambda mood: [
            "The Happy Song",
            "Imogen Heap",
            "https://open.spotify.com/artist/6Xb4ezwoAQC4516kI89nWz",
        ],
    )
    # Catch sys.exit
    with pytest.raises(SystemExit) as exit_message:
        # positional arguments: mood and last_recommendation
        handle_user_feedback(
            "happy",
            [
                "The Happy Song",
                "Imogen Heap",
                "https://open.spotify.com/artist/6Xb4ezwoAQC4516kI89nWz",
            ],
        )
    # Assert exit message
    assert "We are sorry we couldn't find what you were looking for 😔" in str(
        exit_message.value
    )
