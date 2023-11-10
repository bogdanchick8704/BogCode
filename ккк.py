import random

def run_test():
    questions = {
        "Как называется столица Франции?": "Париж",
        "Какое растение символизирует Ирландию?": "Трилистник",
        "Какой цвет имеет внешний слой кожи банана?": "Желтый"
    }

    while True:
        # Перемешиваем вопросы
        shuffled_questions = list(questions.keys())
        random.shuffle(shuffled_questions)

        # Проходимся по каждому вопросу
        for question in shuffled_questions:
            answer = input(question + " ")

            if answer.lower() != questions[question].lower():
                print("Неправильный ответ. Попробуйте еще раз.\n")
                break
        else:
            print("Молодец! Вы ответили на все вопросы верно.")
            break

run_test()

