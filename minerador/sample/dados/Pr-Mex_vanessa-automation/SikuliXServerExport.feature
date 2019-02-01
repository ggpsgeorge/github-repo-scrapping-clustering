# language: ru

@IgnoreOnCIMainBuild
@ExportScenarios



Функциональность: Служебные сценарии для проверки работы SikuliX сервера


Сценарий: Я устанавливаю настройки SikuliX сервера
	И я перехожу к закладке "Сервис"
	И я перехожу к закладке "Автоинструкции"
	
	И я устанавливаю флаг 'Использовать SikuliX сервер'
	И Я запоминаю значение выражения 'Объект.КаталогИнструментов + "\tools\Sikuli"' в переменную "КаталогСкриптовSikuliX"
	И в поле с именем "КаталогиСкриптовSikuliX" ввожу значение переменной "КаталогСкриптовSikuliX"
	
	И я перехожу к закладке "Сервис"
	И я перехожу к закладке "Основные"
	И Я запоминаю значение выражения 'Объект.КаталогИнструментов + "\tools\Sikuli\pict"' в переменную "КаталогПроекта"
	И в поле с именем "КаталогПроекта" ввожу значение переменной "КаталогПроекта"
