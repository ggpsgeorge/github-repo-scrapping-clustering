﻿# language: ru

@IgnoreOn82Builds
@IgnoreOnOFBuilds



Функционал: Проверка кнопки открытия элемента формы

Как разработчик 
Я хочу чтобы у меня была возможность открывать элемент формы кнопкой с двумя квадратиками
Чтобы у меня актоматически генерировались шаги Gherkin без программирования

Контекст: 
	Дано Я запускаю сценарий открытия TestClient или подключаю уже существующий


Сценарий: Проверка открытия элемента формы

	Когда В панели разделов я выбираю "Основная"
	И     В панели функций я выбираю "Справочник1"
	И     открылось окно "Справочник1"
	И     В открытой форме я нажимаю на кнопку с заголовком "Создать"
	Тогда открылось окно "Справочник1 (создание)"
	И     В открытой форме в поле с именем "Наименование" я ввожу текст "Тест"
	И     В открытой форме я нажимаю кнопку выбора у поля с заголовком "Реквизит2"
	Тогда открылось окно "Справочник2"
	И     В форме "Справочник2" в таблице "Список" я перехожу к строке:
	| 'Наименование'      |
	| 'ТестовыйЭлемент21' |
	И     В форме "Справочник2" в ТЧ "Список" я выбираю текущую строку
	
	И     В открытой форме я нажимаю кнопку выбора у поля с именем "Реквизит4"
	Тогда открылось окно "Справочник2"
	И     В форме "Справочник2" в таблице "Список" я перехожу к строке:
	| 'Наименование'      |
	| 'ТестовыйЭлемент21' |
	И     В форме "Справочник2" в ТЧ "Список" я выбираю текущую строку
	
	Тогда открылось окно "Справочник1 (создание) *"
	И     В открытой форме я нажимаю на кнопку с заголовком "Записать и закрыть"
