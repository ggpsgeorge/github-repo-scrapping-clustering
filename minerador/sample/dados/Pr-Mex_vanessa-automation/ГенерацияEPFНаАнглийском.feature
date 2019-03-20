﻿# language: ru

@IgnoreOn82Builds
@IgnoreOnOFBuilds
@IgnoreOnWeb

Функционал: Проверка создания EPF из фичи на английском языке
	Как Разработчик
	Я Хочу чтобы чтобы у меня была возможность на основании фичи генерировать epf файлы с английскими снипетами
 

Контекст: 
	Дано Я запускаю сценарий открытия TestClient или подключаю уже существующий
	
//https://github.com/Pr-Mex/vanessa-automation/issues/140	
Сценарий: Генерация EPF на английском простая
	И Я запоминаю значение выражения 'Ванесса.Объект.КаталогИнструментов + "/features/Support/Templates/step_definitions/ФичаДляПроверкиГенерацииEPFАнглийский.epf"' в переменную "СлужебныйФайл"
	Если Файл "$СлужебныйФайл$" существует тогда
		Тогда я удаляю файл "$СлужебныйФайл$"
		
	Когда Я открываю VanessaAutomation в режиме TestClient
	Когда В поле с именем "КаталогФичСлужебный" я указываю путь к служебной фиче "ФичаДляПроверкиГенерацииEPFАнглийский"
	И Я нажимаю на кнопку перезагрузить сценарии в Vanessa-Automation TestClient
	И я перехожу к закладке "Генератор EPF"
	И я изменяю флаг 'Генерировать управляемую форму'
	И я нажимаю на кнопку 'Создать и обновить шаблоны обработок'
	Затем я жду, что в сообщениях пользователю будет подстрока "Создание epf по фичам закончено." в течение 30 секунд
	И я перехожу к закладке "Запуск сценариев"
	И Я нажимаю на кнопку перезагрузить сценарии в Vanessa-Automation TestClient
	
	И в таблице "ДеревоТестов" я перехожу к первой строке:
	И в таблице "ДеревоТестов" я разворачиваю текущую строку
	И в таблице "ДеревоТестов" я разворачиваю строку:
		| 'Наименование'    |
		| 'Test feature en' |
	И в таблице "ДеревоТестов" я разворачиваю строку:
		| 'Наименование'     |
		| 'Test scenario en' |
	
	И в таблице "ДеревоТестов" я перехожу к строке:
		| 'Наименование'         |
		| 'And I am your father' |
	И в таблице "ДеревоТестов" я активизирую поле с именем "ДеревоТестовАдресСнипета"
	И в таблице текущее поле заполнено

Сценарий: Удаление служебного файла (Генерация EPF на английском простая)
	И Я запоминаю значение выражения 'Ванесса.Объект.КаталогИнструментов + "/features/Support/Templates/step_definitions/ФичаДляПроверкиГенерацииEPFАнглийский.epf"' в переменную "СлужебныйФайл"
	Если Файл "$СлужебныйФайл$" существует тогда
		Тогда я удаляю файл "$СлужебныйФайл$"
