﻿#language: ru

@IgnoreOnCIMainBuild
@tree


Функциональность: Тест

Контекст: 
	Дано Я запускаю сценарий открытия TestClient или подключаю уже существующий

Сценарий: Тест 
			
	И В командном интерфейсе я выбираю 'Основная' 'Справочник1'
	Тогда открылось окно 'Справочник1'
	И я нажимаю на кнопку с именем 'ФормаСоздать'

	И в таблице "ТабличнаяЧасть1" я нажимаю на кнопку с именем 'ТабличнаяЧасть1Добавить'
	И в таблице "ТабличнаяЧасть1" я активизирую поле с именем "ТабличнаяЧасть1РеквизитСтрока"
	И в таблице "ТабличнаяЧасть1" в поле 'Реквизит строка' я ввожу текст '1|1'
	И в таблице "ТабличнаяЧасть1" я завершаю редактирование строки
	И     в поле с именем "Наименование" я ввожу текст "1|1"
	И     я нажимаю на кнопку "Записать и закрыть"

	