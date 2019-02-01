﻿# language: ru

@IgnoreOn82Builds
@IgnoreOnOFBuilds
@tree



Функционал: Переход к строке таблицы по значнию переменных Контекст и КонтекстСохраняемый

Как разработчик 
Я хочу чтобы у меня была возможность перейти к строке используюя значения переменных
Чтобы использовать это в сових сценариях

Контекст: 
	Дано Я запускаю сценарий открытия TestClient или подключаю уже существующий


	
	
Сценарий: Переход к строке таблицы по значнию переменных Контекст и КонтекстСохраняемый

	И     В командном интерфейсе я выбираю "Основная" "Справочник1"
	Тогда открылось окно "Справочник1"
	И     я нажимаю на кнопку "Создать"
	Тогда открылось окно "Справочник1 (создание)"
	И     в таблице "ТабличнаяЧасть1" я нажимаю на кнопку "Добавить"
	И     в таблице "ТабличнаяЧасть1" я активизирую поле "Реквизит строка"
	И     в таблице "ТабличнаяЧасть1" в поле "Реквизит строка" я ввожу текст "Строка1"
	И     в таблице "ТабличнаяЧасть1" я завершаю редактирование строки
	И     в таблице "ТабличнаяЧасть1" я нажимаю на кнопку "Добавить"
	И     в таблице "ТабличнаяЧасть1" я активизирую поле "Реквизит строка"
	И     в таблице "ТабличнаяЧасть1" в поле "Реквизит строка" я ввожу текст "Строка2"
	И     в таблице "ТабличнаяЧасть1" я завершаю редактирование строки
	И     в таблице "ТабличнаяЧасть1" я нажимаю на кнопку "Добавить"
	И     в таблице "ТабличнаяЧасть1" я активизирую поле "Реквизит строка"
	И     в таблице "ТабличнаяЧасть1" в поле "Реквизит строка" я ввожу текст "Строка3"
	И     в таблице "ТабличнаяЧасть1" я завершаю редактирование строки
	И     в таблице "ТабличнаяЧасть1" я нажимаю на кнопку "Добавить"
	И     в таблице "ТабличнаяЧасть1" я активизирую поле "Реквизит строка"
	И     в таблице "ТабличнаяЧасть1" в поле "Реквизит строка" я ввожу текст "$Строка4$"
	И     в таблице "ТабличнаяЧасть1" я завершаю редактирование строки
	
	И Я запоминаю значение выражения '"Строка2"' в переменную "ЗначениеДляСтроки2"
	И Я запоминаю значение выражения '"Строка3"' в переменную "ЗначениеДляСтроки3" глобально
	
	И     в таблице "ТабличнаяЧасть1" я перехожу к строке:
		| 'Реквизит строка'      |
		| '$ЗначениеДляСтроки2$' |

	И     в таблице "ТабличнаяЧасть1" я перехожу к строке:
		| 'Реквизит строка'        |
		| '$$ЗначениеДляСтроки3$$' |

	И     в таблице "ТабличнаяЧасть1" я перехожу к строке:
		| 'Реквизит строка'        |
		| '$$$Строка4$$$' |

