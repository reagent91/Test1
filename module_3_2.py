def send_email(message, recipient, *, sender= "universsity.help@gmail.com"):
    domens = ".com", ".ru", ".net"
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if any(item in "@" for item in recipient and sender) and recipient.endswith(domens) and sender.endswith(domens) :
        if sender == "universsity.help@gmail.com":
            print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, "на адрес", recipient)

    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')