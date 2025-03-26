from bot import bot
import pytest


@bot.message_handler(commands=["start"])
def welcome_message(message):
    print(message)
    print("Текст сообщения: \n" + message.text)
    bot.send_message(message.from_user.id, text=f"Здравствуй, {message.from_user.first_name}!")


@bot.message_handler(commands=["pytest"])
def launch_tests(message):
    """
    Запуск тестов, бот просит передать конфигурации
    :param message:
    :return:
    """
    msg = bot.send_message(message.from_user.id, text=f"Напишите параметры для запуска тестов, например ‘-v -m api’. По умолчанию pytest запускается с параметром --html=report.html")
    bot.register_next_step_handler(msg, start_tests_with_params)


def start_tests_with_params(message):
    options = (lambda message: message.text.split(" ") if message.text.replace(" ", "") != "" else [])(message)
    options.extend(["--html=report.html"])
    print(options)
    retcode = pytest.main(options)
    # retcode = pytest.main(message.text + " --html=report.html")
    bot.send_document(message.from_user.id, open("./report.html", "rb"), caption="Результаты тестов")
