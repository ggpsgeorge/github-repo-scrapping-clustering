﻿# language: ru

@IgnoreOnWeb

Функционал: Проверка создания fixtures
	Как Разработчик
	Я Хочу чтобы чтобы я мог создавать fixtures по макетам
 

	Сценарий: Создание fixtures

	
	Когда в метаданных есть Справочник "Справочник1"
	И я удаляю все элементы Справочника "Справочник1"
	И в базе нет элементов Справочника "Справочник1"
	И я создал fixture справочника по макету "Макет"
	Тогда В базе появился хотя бы один элемент справочника "Справочник1"
	

