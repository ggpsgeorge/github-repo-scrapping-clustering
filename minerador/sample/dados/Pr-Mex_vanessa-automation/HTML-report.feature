# language: ru

@IgnoreOn82Builds
@IgnoreOnOFBuilds
@IgnoreOnWeb



Функционал: Проверка формирования отчета HTML

Как разработчик
Я хочу чтобы корректно формировался отчет HTML
Чтобы я мог видеть результат работы сценариев

Контекст: 
	Дано Я запускаю сценарий открытия TestClient или подключаю уже существующий
	
	
Сценарий: Проверка отчета HTML
	Когда Я открываю VanessaAutomation в режиме TestClient
	И В поле с именем "КаталогФичСлужебный" я указываю путь к служебной фиче "ФичаДляПроверкиОтчетаHTML"
	И     В открытой форме я перехожу к закладке с заголовком "Сервис"
	И     В открытой форме я изменяю флаг "Создавать HTML инструкцию"
	И     В открытой форме в поле "Консольная команда создания скриншотов" я ввожу команду для IrfanView 
	И     в поле каталог отчета HTML я указываю путь к относительному каталогу "tools\HTML"
	И Я нажимаю на кнопку перезагрузить сценарии в Vanessa-Automation TestClient
	И Я нажимаю на кнопку выполнить сценарии в Vanessa-Automation TestClient
	И в каталоге HTML появился 1 файл html
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "я выполняю простой шаг контекста"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" есть строка "Другой текст первого шага"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" есть строка "Другой текст второго шага Параметр2 и Параметр1"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "И этот шаг должен быть проигнориорован в автоинструкции"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "<b>004</b>. И я выполняю ещё простой шаг"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "<b>004</b>.И я выполняю ещё простой шаг"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "Когда я выполняю простой шаг в группе один"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "Когда я выполняю простой шаг в группе два"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" есть строка "И группа шагов один"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "И группа шагов два"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" есть строка "И группа другой текст"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "И группа шагов три"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "И группа шагов четыре"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "Когда я выполняю простой шаг в группе пять"
	И в Файле инструкции "Instr_Тестовая фича, проверяющая генерацию отчета HTML.HTML" нет строки  "Когда я выполняю простой шаг в группе шесть"
