""" import requests
from trivia.models import Question, Answer


def populate_database():
    response = requests.get("https://opentdb.com/api.php?amount=10")
    trivia_questions = response.json()["results"]

    for question in trivia_questions:
        q = Question.objects.create(
            category=question["category"], question=question["question"]
        )
    Answer.objects.create(
        question=q, answer=question["correct_answer"], is_correct=True
    )
    for answer in question["incorrect_answers"]:
        Answer.objects.create(question=q, answer=answer, is_correct=False)


 questions = [q.question for q in Question.objects.all()] 


populate_database() """
