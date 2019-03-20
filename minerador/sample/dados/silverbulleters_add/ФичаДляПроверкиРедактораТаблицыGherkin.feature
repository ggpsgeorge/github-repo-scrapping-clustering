﻿# language: ru

@IgnoreOnCIMainBuild

Функционал: Проверить редактор таблиц. Служебная фича.
 

Контекст: 
	Дано Я запускаю сценарий открытия TestClient или подключаю уже существующий
 
 
Сценарий: Проверка редактора таблиц.
	Когда В панели разделов я выбираю "Основная"
	И     В панели функций я выбираю "Справочник1"
	Тогда открылось окно "Справочник1"
	И     я нажимаю на кнопку "Создать"
	Тогда открылось окно "Справочник1 (создание)"
	И     в ТЧ "ТабличнаяЧасть1" я нажимаю на кнопку "Добавить"
	И     в таблице "ТабличнаяЧасть1" в поле "Реквизит строка" я ввожу текст 
		|'Стр1'|
		|'Стр2'|
	И     В форме "Справочник1 (создание)" в ТЧ "ТабличнаяЧасть1" я завершаю редактирование строки
	И     в ТЧ "ТабличнаяЧасть1" я нажимаю на кнопку "Добавить"
	И     в таблице "ТабличнаяЧасть1" в поле "Реквизит строка" я ввожу текст 
		|'Стр3'|
		|'Стр4'|
	И     В форме "Справочник1 (создание)" в ТЧ "ТабличнаяЧасть1" я завершаю редактирование строки
	И     в ТЧ "ТабличнаяЧасть1" я нажимаю на кнопку "Добавить"
	И     в таблице "ТабличнаяЧасть1" в поле "Реквизит строка" я ввожу текст 
		|'Стр5'|
		|'Стр6'|
	И     В форме "Справочник1 (создание)" в ТЧ "ТабличнаяЧасть1" я завершаю редактирование строки
	
	И     таблица "ТабличнаяЧасть1" стала равной:
		| 'Реквизит строка' |
		| 'Стр1\nСтр2'      |
		| 'Стр3\nСтр4'      |
		| 'Стр5\nСтр6'      |
	И     в поле с именем "Наименование" я ввожу текст "Проверка редактора таблиц."
	И     я нажимаю на кнопку "Записать и закрыть"

	
	
