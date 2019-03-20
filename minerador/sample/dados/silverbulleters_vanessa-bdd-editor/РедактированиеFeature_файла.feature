﻿#encoding: utf-8
#language: ru

Функционал: Редактирование feature-файла                                                                                                                  
	Как пользователь BDD-Editor                                                                                                                           
	Я хочу редактировать feature-файл в разных режимах                                                                                                    
	Чтобы было быстро редактировать feature-файл                                                                                                          
	
Контекст:
    Дано Я запускаю сценарий открытия TestClient или подключаю уже существующий 

Сценарий:
   Когда В панели разделов я выбираю "Обработки"
    И     Я нажимаю кнопку командного интерфейса "BDDEditor"
    Тогда открылось окно "Обработка требований: BDDEditor*"
    Когда В открытой форме я перехожу к закладке с заголовком "Сбор требований"
    И     В открытой форме в поле с заголовком "Структура хранения требований" я ввожу текст "D:\Rep\Hissin\Features"
    И     В открытой форме я нажимаю на кнопку с заголовком "Обновить из временного каталога"
    Тогда В открытой форме в ТЧ "ТЗСбораТребований" заполняется список фача-файлов из временного каталога    
	И     таблица формы с именем "ТЗСбораТребований" стала равной:
		| 'Функционал'                    | 'Комментарий создания' | 'Компонент' | 'Количество сценариев' | 'Цель (Чтобы) Ожидаемый конечный результат' | 'feature-файл'                                                     | 'Роль (Как)'         | 'Описание функционала (Я хочу)'                 |
		| 'Создание фича-файла по кнопке' | ''                     | ''          | '1'                    | 'не создавать вручную фича-файлы'           | 'D:\Rep\Hissin\Features\Drafts\СозданиеФича_файлаПоКнопке.feature' | 'системный аналитик' | 'автоматическое создание фича-файла по шаблону' |
	Когда 	В форме "Обработка требований: BDDEditor*" в таблице "ТЗСбораТребований" я перехожу к строке:
		| 'Функционал'                    | 'Комментарий создания' | 'Компонент' | 'Количество сценариев' | 'Цель (Чтобы) Ожидаемый конечный результат' | 'feature-файл'                                                     | 'Роль (Как)'         | 'Описание функционала (Я хочу)'                 |
		| 'Создание фича-файла по кнопке' | ''                     | ''          | '1'                    | 'не создавать вручную фича-файлы'           | 'D:\Rep\Hissin\Features\Drafts\СозданиеФича_файлаПоКнопке.feature' | 'системный аналитик' | 'автоматическое создание фича-файла по шаблону' |
	И Нажимаю гиперссылку на feature-файл в ТЧ "ТЗСбораТребований" в поле с заголовком "feature-файл"
	#В форме "Обработка требований: BDDEditor*" в ТЧ "ТЗСбораТребований" я выбираю текущую строку
	Тогда 	  открылось окно "Редактор feature-файла: BDDEditor*"
	И     Я нажимаю кнопку командного интерфейса "Редактор feature-файла: BDDEditor*"	
