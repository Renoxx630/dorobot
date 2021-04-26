# Импортируем необходимые классы.

from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from log_tok import TOKEN
import random


reply_keyboard1 = [['cube6', 'cube6_cube6'],
                   ['cube20', 'back']]
markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=False)
reply_keyboard2 = [['tell_about_sweet', 'back']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)
reply_keyboard3 = [['A'],
                   ['B'],
                   ['C'],
                   ['back']]
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=False)

# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.


def info(update):
    update.message.reply_text('Привет. Я - бот, а точнее проект моих разработчиков.'
                              ' Со мной ты можешь провести время и узнать о сладостях.\n'
                              'А ещё я знаю многое о сладостях. И у моих разработчиков есть '
                              'специальный сайт о конфетах.\n'
                              'Мои создатели будут рады вашей помощи.\n'
                              'Для того, чтобы узнать, что я могу, напиши: /help')


def help(update):
    update.message.reply_text('Вот, что я могу:\n'
                              '    /sweets - узнать про сладости\n'
                              '    /facts - интересные факты\n'
                              '    /info - немного о боте\n'
                              '    /dice - кинуть кубики\n'
                              '    /help - список команд\n'
                              '    /tell_about_sweet - рассказать мне сладости\n'
                              '    /notes - вывести заметки(указывает номера заметок)\n'
                              '    /new_note <заметка> - сделать новую заметку\n'
                              '    /delete_note <номер заметки> - удалить\n'
                              '    /cake_time <время> - таймер запекания ваших кексиков!\n'
                              '    /cake_facts <сладость> - факт о сладости\n'
                              '    /test -  запустить тест, который подготовили для вас разработчики\n'
                              'На данный момент это всё, что могу. Но вы можете помочь моим разработчикам:\n'
                              '    /ideas <ваша идея> - предложите идею для развития бота.')


def test(update):
    f = open('question.txt', 'r', encoding='utf-8')
    stroki = f.readlines()
    f.close()
    f = open('answers.txt', 'r', encoding='utf-8')
    ans = f.readlines()
    f.close()
    if len(ans[0]) < 10:
        i = len(ans[0]) - 1
        question = stroki[i]
        f = open('variants.txt', 'r', encoding='utf-8')
        var = f.readlines()
        f.close()
        v = var[i].split('; ')
        var_a = v[0]
        var_b = v[1]
        var_c = v[2]
        update.message.reply_text(f'{question}\n'
                                  f'\n'
                                  f'{var_a}'
                                  f'{var_b}'
                                  f'{var_c}',
                                  reply_markup=markup3)
    else:
        right_ans = ['c', 'b', 'b', 'b', 'b', 'a', 'c', 'a', 'a', 'b']
        f = open('answers.txt', 'r', encoding='utf-8')
        answer = f.readlines()
        f.close()
        balls = 0
        for i in range(len(answer)):
            if right_ans[i] == answer[i]:
                balls += 1
        update.message.reply_text(f'Вы набрали {balls} из 10 баллов.')
        f = open('answers.txt', 'w', encoding='utf-8')
        f.write('')
        f.close()


def A(update):
    f = open('answers.txt', 'a', encoding='utf-8')
    f.write('a')
    f.close()
    test(update)


def B(update):
    f = open('answers.txt', 'a', encoding='utf-8')
    f.write('b')
    f.close()
    test(update)


def C(update):
    f = open('answers.txt', 'a', encoding='utf-8')
    f.write('c')
    f.close()
    test(update)


def facts(update):
    f = open('facts.txt', 'r', encoding='utf-8')
    facts = f.readlines()
    f.close()
    fact = facts[random.randint(0, len(facts) - 1)]
    update.message.reply_text(fact)


def ideas(update, context):
    f = open('ideas.txt', 'a', encoding='utf-8')
    if len(context.args) != 0:
        idea = ' '.join(context.args)
        f.write(idea + '\n')
        update.message.reply_text('Спасибо за ваши идеи!')
    else:
        update.message.reply_text('Если хотите предложить идеи для бота,'
                                  ' то напишите: /ideas <ваша идея>')
    f.close()


def notes(update):
    f = open('notes.txt', 'r', encoding='utf-8')
    notes = f.readlines()
    for i in range(len(notes)):
        text = f'{i + 1}. {notes[i]}'
        update.message.reply_text(text)
    f.close()


def new_note(update, context):
    f = open('notes.txt', 'a', encoding='utf-8')
    if len(context.args) != 0:
        note = ' '.join(context.args)
        f.write(note + '\n')
        update.message.reply_text('Новая заметка добавлена')
    else:
        update.message.reply_text('Если хотите оставить новую заметку,'
                                  ' то напишите: /new_note <заметка>')
    f.close()


def delete_note(update, context):
    try:
        if len(context.args) != 0:
            f = open('notes.txt', 'r', encoding='utf-8')
            all_notes = f.readlines()
            f.close()
            f = open('notes.txt', 'w', encoding='utf-8')
            due = int(context.args[0])
            if due > 0 and due <= len(all_notes):
                for i in range(len(all_notes)):
                    if i + 1 != due:
                        f.write(all_notes[i])
                update.message.reply_text('Заметка удалена.')
            else:
                update.message.reply_text('Нет такого номера')
            f.close()
        else:
            update.message.reply_text('Если хотите предложить идеи для бота,'
                                      ' то напишите: /ideas <ваша идея>')
    except (IndexError, ValueError):
        update.message.reply_text('Использование: /delete_note <номер заметки>')
        update.message.reply_text('Номер заметки можно узнать с помощью команды: /notes')


def remove_job_if_exists(name, context):
    # def remove_job_if_exists(name, context):
    """Удаляем задачу по имени.
    Возвращаем True если задача была успешно удалена."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def cake_time(update, context):
    """Добавляем задачу в очередь"""
    chat_id = update.message.chat_id
    try:
        # args[0] должен содержать значение аргумента
        # (секунды таймера)
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text(
                'Извини, я не умею возвращаться в прошлое')
            return

        # Добавляем задачу в очередь
        # и останавливаем предыдущую (если она была)
        job_removed = remove_job_if_exists(
            str(chat_id),
            context
        )
        context.job_queue.run_once(
            task,
            due * 60,
            context=chat_id,
            name=str(chat_id)
        )
        text = f'Твои сладости приготовятся через {due} минут!'
        if job_removed:
            text += ' Старая задача удалена.'
        # Присылаем сообщение о том, что всё получилось.
        update.message.reply_text(text)

    except (IndexError, ValueError):
        update.message.reply_text('Использование: /cake_time <минуты>')


def cake_facts(update, context):
    sweet_dict = {'безе': 'По легенде, безе изобрели в праздничный вечер, когда в результате интриг соперника повар\n'
                          ' одного маркиза лишился всех продуктов. У него остались лишь яйца и сахар,\n'
                          ' с которыми он смело пофантазировал.',
                  'мармелад': 'Цепочкой из мишек Харибо, выпущенных за один год,\n'
                              ' можно будет четыре раза обернуть нашу планету',
                  'шоколад': 'Какао быстрее помогает восстановиться после занятий спортом за счёт\n'
                             ' высокого содержания белка и углеводов в напитке.',
                  'вафли': 'Само название десерта происходит от немецкого слова waffel – «сота, ячейка» - позже\n '
                           'видозмененного в waffle. Клеточки-ячейки удерживают начинку, не позволяя ей растечься.',
                  'зефир': 'Зефир имеет лекарственные свойства – если у вас болит горло,\n'
                           ' то можно выпить горячего чая со сладостью и смягчить боль.',
                  'маршмеллоу': 'Маршмеллоу не портится из-за перемены температур. Эти пастилки замерзают '
                                'в холодильнике \n'
                                'и плавятся на солнце, но в обоих случаях остаются съедобными.',
                  'марципан': 'В средние века марципан продавали аптекари. Они рекомендовали его как лекарство\n '
                              'для лечения телесных и душевных расстройств. В аптеках использовалось также\n'
                              ' специальное латинское название лекарства Marci panis. В те времена марципан \n'
                              'было изысканным блюдом, доступным только богатым.'
                  }
    try:
        sweets = context.args[0]
        if sweets == 'безе' or sweets == 'меренги':
            update.message.reply_text(sweet_dict['безе'])
        if sweets == 'мармелад':
            update.message.reply_text(sweet_dict['мармелад'])
        if sweets == 'шоколад':
            update.message.reply_text(sweet_dict['шоколад'])
        if sweets == 'вафли':
            update.message.reply_text(sweet_dict['вафли'])
        if sweets == 'зефир':
            update.message.reply_text(sweet_dict['зефир'])
        if sweets == 'маршмеллоу':
            update.message.reply_text(sweet_dict['маршмеллоу'])
        if sweets == 'марципан':
            update.message.reply_text(sweet_dict['марципан'])
        else:
            update.message.reply_text('Я не знаю интересного факта об этой сладости')
    except (IndexError, ValueError):
        update.message.reply_text('Использование: /sweetness <название>')


def task(context):
    """Выводит сообщение"""
    job = context.job
    context.bot.send_message(job.context, text='Вернулся!')


def echo(update):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text(F'Я получил сообщение {update.message.text}')


def sweets(update, context):
    sweetness = ['безе', 'зефир', 'шоколад', 'мармелад', 'суфле', 'помадка', 'вафли', 'карамель', 'меренги', 'мусс',
                 'пастила', 'маршмерллоу', 'грильяж', 'нуга', 'марципан', 'рахат-лукум']
    try:
        if len(context.args) != 0:
            f = open('new_sweets.txt', 'r', encoding='utf-8')
            sweeet = f.readlines()
            f.close()
            name = {}
            if len(sweeet) > 0:
                for i in sweeet:
                    x = i.split(':: ')
                    name[x[0]] = x[1]
            due = context.args[0]
            if due in sweetness:
                if due == 'безе':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'зефир':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'шоколад':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'мармелад':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'суфле':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'помадка':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'вафли':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'меренги':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'мусс':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'пастила':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'маршмерллоу':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'грильяж':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'нуга':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'марципан':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
                elif due == 'рахат-лукум':
                    update.message.reply_text('Держи:')
                    update.message.reply_text('ссылка')
            if due in name:
                update.message.reply_text('Вот, что я знаю об этой сладости:\n'
                                          + ' '.join(name[due]))
            else:
                update.message.reply_text('Прости, я пока не знаю такого вида сладости')
                update.message.reply_text('Но ты можешь рассказать мне о ней.', reply_markup=markup2)

        else:
            update.message.reply_text('Вот сладости, про которые написанона специальном сайте:'
                                      + ', '.join(sweetness))
            f = open('new_sweets.txt', 'r', encoding='utf-8')
            sweeet = f.readlines()
            f.close()
            if len(sweeet) > 0:
                name = []
                for i in sweeet:
                    x = i.split(': ')
                    name.append(x[0])
                update.message.reply_text('А это сладости, о которых я узнал от пользователей:'
                                          + ', '.join(name))

    except (IndexError, ValueError):
        update.message.reply_text('Использование: /sweetness <название>')


def dice(update):
    update.message.reply_text(
        "Что кинуть?",
        reply_markup=markup1
    )


def cube6(update):
    update.message.reply_text(str(random.randint(1, 6)))


def tell_about_sweet(update, context):
    f = open('new_sweets.txt', 'a', encoding='utf-8')
    if len(context.args) != 0:
        f.write(f'{context.args[0]}:: {context.args[1:]}')
        update.message.reply_text('Спасибо!')
    else:
        update.message.reply_text('Если хотите рассказатьо сладости,'
                                  ' то напишите: /tell_about_sweet <название сладости> <информация о сладости>')
    f.close()


def cube6_cube6(update):
    update.message.reply_text(str(random.randint(1, 6)) + ' ' + str(random.randint(1, 6)))


def cube20(update):
    update.message.reply_text(str(random.randint(1, 20)))


def close_keyboard(update):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )
    f = open('answers.txt', 'w', encoding='utf-8')
    f.write('')
    f.close()


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("facts", facts))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("ideas", ideas))
    dp.add_handler(CommandHandler("cake_time", cake_time))
    dp.add_handler(CommandHandler("sweets", sweets))
    dp.add_handler(CommandHandler("dice", dice))
    dp.add_handler(CommandHandler("cube6", cube6))
    dp.add_handler(CommandHandler("cube6_cube6", cube6_cube6))
    dp.add_handler(CommandHandler("cube20", cube20))
    dp.add_handler(CommandHandler("notes", notes))
    dp.add_handler(CommandHandler("new_note", new_note))
    dp.add_handler(CommandHandler("delete_note", delete_note))
    dp.add_handler(CommandHandler("tell_about_sweet", tell_about_sweet))
    dp.add_handler(CommandHandler("back", close_keyboard))
    dp.add_handler(CommandHandler("cake_facts", cake_facts))
    dp.add_handler(CommandHandler("test", test))
    dp.add_handler(CommandHandler("A", A))
    dp.add_handler(CommandHandler("B", B))
    dp.add_handler(CommandHandler("C", C))
    text_handler = MessageHandler(Filters.text, echo)

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(text_handler)
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
